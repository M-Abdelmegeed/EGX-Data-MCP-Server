"""
Helper functions for the EGX MCP server.
This module contains utility functions for the Egyptian Exchange (EGX) stock tools.
"""

from typing import Dict, Any
from tradingview_ta import TA_Handler, Exchange, Interval

# Constants
EGX_EXCHANGE = 'EGX'
EGX_SCREENER = 'egypt'

def validate_symbol(symbol: str) -> bool:
    """
    Validate that a symbol is formatted correctly for EGX (4 letters).
    
    Args:
        symbol: The stock symbol to validate
        
    Returns:
        bool: True if the symbol is valid, False otherwise
    """
    if not symbol or not isinstance(symbol, str):
        return False
    
    # EGX symbols are typically 4 uppercase letters
    return len(symbol) == 4 and symbol.isalpha()

def format_indicators(indicators: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format technical indicators for better readability.
    
    Args:
        indicators: The raw indicators dictionary from TradingView
        
    Returns:
        dict: A formatted version of the indicators
    """
    # This could be expanded to format the data in a more readable way
    # or to filter out certain indicators
    return indicators

def get_stock_handler(symbol: str) -> TA_Handler:
    """
    Create a TradingView TA_Handler for a given EGX stock symbol.
    
    Args:
        symbol: The stock symbol to create a handler for
        
    Returns:
        TA_Handler: A handler for the specified stock
    """
    return TA_Handler(
        symbol=symbol,
        screener=EGX_SCREENER,
        exchange=EGX_EXCHANGE,
        interval=Interval.INTERVAL_1_DAY
    )