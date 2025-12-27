#!/usr/bin/env python3
"""
MCP SSE Client - Command-line tool to interact with MCP server via SSE

This script demonstrates how to use Server-Sent Events (SSE) to communicate
with the MCP server directly from the command line.
"""

import json
import sys

from src.mcp.sse_client import MCPSSEClient


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="MCP SSE Client - Interact with MCP server via SSE"
    )
    parser.add_argument(
        "--url",
        default="http://localhost:8000/mcp/",
        help="MCP server URL (default: http://localhost:8000/mcp/)",
    )
    parser.add_argument(
        "method",
        choices=["tools/list", "tools/call"],
        help="MCP method to call",
    )
    parser.add_argument(
        "--params",
        type=str,
        help="JSON parameters (for tools/call)",
    )

    args = parser.parse_args()

    params = None
    if args.params:
        try:
            params = json.loads(args.params)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in --params: {args.params}", file=sys.stderr)
            sys.exit(1)

    client = MCPSSEClient(args.url)
    response = client.send_request(args.method, params)

    # Print raw response
    if not response.strip():
        print("No response received")
    else:
        print(response)


if __name__ == "__main__":
    main()
