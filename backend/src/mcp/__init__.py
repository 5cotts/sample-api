"""
MCP (Model Context Protocol) client module.

This module provides functionality for interacting with MCP servers.
"""

from .sse_client import MCPSSEClient

__all__ = ["MCPSSEClient"]
