"""
Unit Tests for MCPSSEClient

These tests demonstrate how to test the MCP SSE client independently
of any API or interface implementation. Tests cover client initialization,
request sending (with mocked HTTP), and SSE response parsing.

Tests cover:
- Client initialization
- Request ID management
- send_request method (with mocked httpx)
- parse_sse_response method (pure function)
- Error handling
- Edge cases
"""

import json
import unittest
from unittest import mock
from unittest.mock import patch

from src.mcp.sse_client import MCPSSEClient


class TestMCPSSEClientInitialization(unittest.TestCase):
    """Tests for MCPSSEClient initialization."""

    def test_default_initialization(self):
        """Test client initialization with default timeout."""
        client = MCPSSEClient("http://localhost:8000/mcp/")
        self.assertEqual(client.url, "http://localhost:8000/mcp/")
        self.assertEqual(client.timeout, 30.0)
        self.assertEqual(client._request_id, 1)

    def test_custom_timeout(self):
        """Test client initialization with custom timeout."""
        client = MCPSSEClient("http://example.com/mcp/", timeout=60.0)
        self.assertEqual(client.url, "http://example.com/mcp/")
        self.assertEqual(client.timeout, 60.0)
        self.assertEqual(client._request_id, 1)

    def test_multiple_instances(self):
        """Test that multiple instances are independent."""
        client1 = MCPSSEClient("http://localhost:8000/mcp/")
        client2 = MCPSSEClient("http://localhost:8000/mcp/")
        self.assertIsNot(client1, client2)
        self.assertEqual(client1._request_id, client2._request_id)


class TestMCPSSEClientRequestID(unittest.TestCase):
    """Tests for request ID management."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = MCPSSEClient("http://localhost:8000/mcp/")

    def test_request_id_increments(self):
        """Test that request IDs increment with each request."""
        initial_id = self.client._request_id

        with patch("src.mcp.sse_client.httpx.stream") as mock_stream:
            mock_response = mock.Mock()
            mock_response.read.return_value = b""
            mock_response.raise_for_status = mock.Mock()
            mock_stream.return_value.__enter__.return_value = mock_response

            self.client.send_request("tools/list")

        self.assertEqual(self.client._request_id, initial_id + 1)

    def test_request_id_multiple_requests(self):
        """Test that request IDs increment correctly across multiple requests."""
        initial_id = self.client._request_id

        with patch("src.mcp.sse_client.httpx.stream") as mock_stream:
            mock_response = mock.Mock()
            mock_response.read.return_value = b""
            mock_response.raise_for_status = mock.Mock()
            mock_stream.return_value.__enter__.return_value = mock_response

            self.client.send_request("tools/list")
            self.client.send_request("tools/list")
            self.client.send_request("tools/list")

        self.assertEqual(self.client._request_id, initial_id + 3)


class TestMCPSSEClientSendRequest(unittest.TestCase):
    """Tests for send_request method."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = MCPSSEClient("http://localhost:8000/mcp/")

    @patch("src.mcp.sse_client.httpx.stream")
    def test_send_request_basic(self, mock_stream):
        """Test basic send_request functionality."""
        mock_response = mock.Mock()
        raw_response = (
            "data: "
            + json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"tools": []}})
            + "\n"
        )
        mock_response.read.return_value = raw_response.encode("utf-8")
        mock_response.raise_for_status = mock.Mock()
        mock_stream.return_value.__enter__.return_value = mock_response

        response = self.client.send_request("tools/list")

        self.assertIsInstance(response, str)
        self.assertIn("jsonrpc", response)
        self.assertIn("tools", response)

    @patch("src.mcp.sse_client.httpx.stream")
    def test_send_request_with_params(self, mock_stream):
        """Test send_request with parameters."""
        mock_response = mock.Mock()
        raw_response = (
            "data: "
            + json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"success": True}})
            + "\n"
        )
        mock_response.read.return_value = raw_response.encode("utf-8")
        mock_response.raise_for_status = mock.Mock()
        mock_stream.return_value.__enter__.return_value = mock_response

        params = {"name": "square", "arguments": {"number": 5}}
        response = self.client.send_request("tools/call", params=params)

        self.assertIsInstance(response, str)
        # Verify request was made with params
        call_args = mock_stream.call_args
        self.assertEqual(call_args[0][0], "POST")
        self.assertEqual(call_args[0][1], "http://localhost:8000/mcp/")
        request_json = call_args[1]["json"]
        self.assertIn("params", request_json)
        self.assertEqual(request_json["params"], params)

    @patch("src.mcp.sse_client.httpx.stream")
    def test_send_request_empty_response(self, mock_stream):
        """Test send_request with empty response."""
        mock_response = mock.Mock()
        mock_response.read.return_value = b""
        mock_response.raise_for_status = mock.Mock()
        mock_stream.return_value.__enter__.return_value = mock_response

        response = self.client.send_request("tools/list")

        self.assertEqual(response, "")

    @patch("src.mcp.sse_client.httpx.stream")
    def test_send_request_multi_line_response(self, mock_stream):
        """Test send_request with multi-line SSE response."""
        mock_response = mock.Mock()
        raw_response = (
            "\n".join(
                [
                    "event: message",
                    "data: "
                    + json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"tools": []}}),
                    "",
                    "data: "
                    + json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"done": True}}),
                ]
            )
            + "\n"
        )
        mock_response.read.return_value = raw_response.encode("utf-8")
        mock_response.raise_for_status = mock.Mock()
        mock_stream.return_value.__enter__.return_value = mock_response

        response = self.client.send_request("tools/list")

        self.assertIn("event: message", response)
        self.assertIn("tools", response)
        self.assertIn("done", response)

    @patch("src.mcp.sse_client.httpx.stream")
    def test_send_request_http_error(self, mock_stream):
        """Test send_request raises HTTPError on HTTP failure."""
        mock_response = mock.Mock()
        mock_response.raise_for_status.side_effect = Exception("HTTP 500")
        mock_stream.return_value.__enter__.return_value = mock_response

        with self.assertRaises(Exception):
            self.client.send_request("tools/list")

    @patch("src.mcp.sse_client.httpx.stream")
    def test_send_request_headers(self, mock_stream):
        """Test that send_request sets correct headers."""
        mock_response = mock.Mock()
        mock_response.read.return_value = b""
        mock_response.raise_for_status = mock.Mock()
        mock_stream.return_value.__enter__.return_value = mock_response

        self.client.send_request("tools/list")

        call_args = mock_stream.call_args
        headers = call_args[1]["headers"]
        self.assertEqual(headers["Accept"], "text/event-stream")

    @patch("src.mcp.sse_client.httpx.stream")
    def test_send_request_timeout(self, mock_stream):
        """Test that send_request uses client timeout."""
        mock_response = mock.Mock()
        mock_response.read.return_value = b""
        mock_response.raise_for_status = mock.Mock()
        mock_stream.return_value.__enter__.return_value = mock_response

        client = MCPSSEClient("http://localhost:8000/mcp/", timeout=60.0)
        client.send_request("tools/list")

        call_args = mock_stream.call_args
        self.assertEqual(call_args[1]["timeout"], 60.0)


class TestMCPSSEClientParseSSEResponse(unittest.TestCase):
    """Tests for parse_sse_response method (pure function)."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = MCPSSEClient("http://localhost:8000/mcp/")

    def test_parse_single_data_line(self):
        """Test parsing a single data line."""
        raw_response = (
            "data: "
            + json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"tools": []}})
            + "\n"
        )

        result = self.client.parse_sse_response(raw_response)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["jsonrpc"], "2.0")
        self.assertEqual(result[0]["id"], 1)
        self.assertIn("result", result[0])

    def test_parse_multiple_data_lines(self):
        """Test parsing multiple data lines."""
        raw_response = (
            "\n".join(
                [
                    "data: "
                    + json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"step": 1}}),
                    "data: "
                    + json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"step": 2}}),
                    "data: "
                    + json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"done": True}}),
                ]
            )
            + "\n"
        )

        result = self.client.parse_sse_response(raw_response)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["result"]["step"], 1)
        self.assertEqual(result[1]["result"]["step"], 2)
        self.assertTrue(result[2]["result"]["done"])

    def test_parse_with_event_lines(self):
        """Test parsing SSE response with event lines."""
        raw_response = (
            "\n".join(
                [
                    "event: message",
                    "data: "
                    + json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"tools": []}}),
                    "",
                    "data: "
                    + json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"done": True}}),
                ]
            )
            + "\n"
        )

        result = self.client.parse_sse_response(raw_response)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["event"], "message")
        self.assertIn("result", result[1])
        self.assertIn("result", result[2])

    def test_parse_empty_response(self):
        """Test parsing empty response."""
        result = self.client.parse_sse_response("")

        self.assertEqual(result, [])

    def test_parse_whitespace_only(self):
        """Test parsing response with only whitespace."""
        result = self.client.parse_sse_response("   \n\n   ")

        self.assertEqual(result, [])

    def test_parse_invalid_json(self):
        """Test parsing response with invalid JSON."""
        raw_response = "data: invalid json here\n"

        result = self.client.parse_sse_response(raw_response)

        self.assertEqual(len(result), 1)
        self.assertIn("raw", result[0])
        self.assertEqual(result[0]["raw"], "invalid json here")

    def test_parse_mixed_valid_invalid_json(self):
        """Test parsing response with both valid and invalid JSON."""
        raw_response = (
            "\n".join(
                [
                    "data: " + json.dumps({"valid": True}),
                    "data: invalid json",
                    "data: " + json.dumps({"also_valid": True}),
                ]
            )
            + "\n"
        )

        result = self.client.parse_sse_response(raw_response)

        self.assertEqual(len(result), 3)
        self.assertTrue(result[0]["valid"])
        self.assertIn("raw", result[1])
        self.assertTrue(result[2]["also_valid"])

    def test_parse_ignores_regular_lines(self):
        """Test that parse_sse_response ignores lines without data: or event: prefix."""
        raw_response = (
            "\n".join(
                [
                    "data: " + json.dumps({"jsonrpc": "2.0", "id": 1}),
                    "some regular line",
                    "another line",
                    "data: " + json.dumps({"jsonrpc": "2.0", "id": 2}),
                ]
            )
            + "\n"
        )

        result = self.client.parse_sse_response(raw_response)

        # Should only parse data: lines, ignoring regular lines
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[1]["id"], 2)

    def test_parse_preserves_json_structure(self):
        """Test that parsing preserves complex JSON structures."""
        complex_data = {
            "jsonrpc": "2.0",
            "id": 1,
            "result": {
                "content": [{"text": "Hello"}, {"text": "World"}],
                "metadata": {"count": 2, "nested": {"deep": "value"}},
            },
        }
        raw_response = "data: " + json.dumps(complex_data) + "\n"

        result = self.client.parse_sse_response(raw_response)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], complex_data)
        self.assertEqual(len(result[0]["result"]["content"]), 2)
        self.assertEqual(result[0]["result"]["metadata"]["nested"]["deep"], "value")

    def test_parse_multiple_events(self):
        """Test parsing multiple event lines."""
        raw_response = (
            "\n".join(
                [
                    "event: start",
                    "event: progress",
                    "event: complete",
                ]
            )
            + "\n"
        )

        result = self.client.parse_sse_response(raw_response)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["event"], "start")
        self.assertEqual(result[1]["event"], "progress")
        self.assertEqual(result[2]["event"], "complete")


if __name__ == "__main__":
    unittest.main()
