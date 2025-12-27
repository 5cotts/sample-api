"""
MCP SSE Client Module

This module provides functionality for sending MCP JSON-RPC requests via SSE.
"""

import json
from typing import Any, Dict, List, Optional

import httpx


class MCPSSEClient:
    """
    Client for interacting with MCP (Model Context Protocol) servers via SSE.

    This class provides methods to send JSON-RPC requests to MCP servers
    and handle Server-Sent Events (SSE) streaming responses.
    """

    def __init__(self, url: str, timeout: float = 30.0):
        """
        Initialize MCP SSE client.

        Args:
            url: MCP server URL (e.g., http://localhost:8000/mcp)
            timeout: Request timeout in seconds (default: 30.0)
        """
        self.url = url
        self.timeout = timeout
        self._request_id = 1

    def send_request(self, method: str, params: Optional[Dict[str, Any]] = None) -> str:
        """
        Send an MCP JSON-RPC request via SSE and return the raw response.

        Args:
            method: MCP method name (e.g., "tools/list", "tools/call")
            params: Method parameters (optional)

        Returns:
            Raw response body as a string (complete SSE stream content)

        Raises:
            httpx.HTTPError: If the HTTP request fails
        """
        # MCP JSON-RPC 2.0 request format
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "id": self._request_id,
        }
        self._request_id += 1

        if params:
            request["params"] = params

        # FastMCP uses POST with SSE response
        # Follow redirects automatically
        with httpx.stream(
            "POST",
            self.url,
            json=request,
            headers={"Accept": "text/event-stream"},
            timeout=self.timeout,
            follow_redirects=True,
        ) as response:
            response.raise_for_status()

            # Read raw response bytes directly, then decode to string
            # This preserves the exact response without any line processing
            raw_bytes = response.read()
            raw_response = raw_bytes.decode("utf-8")

        # Return raw response completely unedited
        return raw_response

    def parse_sse_response(self, raw_response: str) -> List[Dict[str, Any]]:
        """
        Parse raw SSE response string into structured data.

        Args:
            raw_response: Raw string returned by send_request()

        Returns:
            List of parsed JSON objects from the SSE stream. Each object represents
            a parsed "data:" line from the SSE stream. Event lines are included
            as dictionaries with an "event" key.
        """
        results: List[Dict[str, Any]] = []

        # Split by lines and process each line
        for line in raw_response.strip().split("\n"):
            if line.startswith("data: "):
                # Extract JSON from "data: " prefix
                json_str = line[6:]
                try:
                    parsed = json.loads(json_str)
                    results.append(parsed)
                except json.JSONDecodeError:
                    # Handle invalid JSON (still return raw line)
                    results.append({"raw": json_str})
            elif line.startswith("event: "):
                # Handle event lines
                event_type = line[7:]
                results.append({"event": event_type})

        return results
