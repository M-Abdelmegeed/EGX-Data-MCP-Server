from typing import Any
import sys
import os
from mcp.server.fastmcp import FastMCP
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools import getStockPriceEGX, getStockDataEGX
from egx import validate_symbol, format_indicators
from precious_metals import get_gold_price, get_silver_price

# Initialize FastMCP server
mcp = FastMCP("egx_stock_tools", validate_schemas=False)

@mcp.tool()
def stock_price_egx(symbol: str) -> str:
    """Get the current price of a stock in EGX.
    
    Args:
        symbol: Stock ticker symbol (4 letters) used on the tradingView API
    """
    # Validate the symbol format
    if not validate_symbol(symbol):
        return f"Error: Invalid symbol format. Symbol should be 4 letters (received: {symbol})"
    
    try:
        return str(getStockPriceEGX(symbol))
    except Exception as e:
        return f"Error getting stock price: {str(e)}"

@mcp.tool()
def stock_data_egx(symbol: str) -> str:
    """Get stock technicals and statistics from EGX.
    
    Args:
        symbol: Stock ticker symbol (4 letters) used on the tradingView API
    """
    # Validate the symbol format
    if not validate_symbol(symbol):
        return f"Error: Invalid symbol format. Symbol should be 4 letters (received: {symbol})"
    
    try:
        indicators = getStockDataEGX(symbol)
        # Format the indicators for better readability
        if isinstance(indicators, dict):
            # Format indicators using the helper function
            formatted_indicators = format_indicators(indicators)
            formatted_data = "\n".join([f"{k}: {v}" for k, v in formatted_indicators.items()])
            return formatted_data
        return str(indicators)
    except Exception as e:
        return f"Error getting stock data: {str(e)}"

@mcp.tool()
def gold_price() -> str:
    """Get the current price of gold in EGP.
    """
    try:
        return get_gold_price()
    except Exception as e:
        return f"Error getting gold price: {str(e)}"

@mcp.tool()
def silver_price() -> str:
    """Get the current price of silver in EGP.
    """
    try:
        return get_silver_price()
    except Exception as e:
        return f"Error getting silver price: {str(e)}"

if __name__ == "__main__":
    print("Starting EGX Stock Tools MCP Server...")
    # Initialize and run the server
    mcp.run(transport='stdio')
