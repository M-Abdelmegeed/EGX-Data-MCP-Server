from langchain.tools import BaseTool, StructuredTool, Tool, tool
from tradingview_ta import TA_Handler, Exchange, Interval
import os


@tool("stock_price_egx", return_direct=False)
def getStockPriceEGX(symbol:str) -> str:
    """Useful for when you need to find out the current price of a stock in EGX. You should input the stock ticker used on the tradingView API"""
    stock = TA_Handler(
        symbol=symbol,
        screener='egypt',
        exchange='EGX',
        interval=Interval.INTERVAL_1_DAY
    )
    return stock.get_analysis().indicators['close']

@tool("stock_data_egx", return_direct=False)
def getStockDataEGX(symbol:str) -> str:
    """Useful for when you need to find out stock technicals and statistics. You should input the stock ticker used on the tradingView API. Input only 4 letters"""
    stock = TA_Handler(
        symbol=symbol,
        screener='egypt',
        exchange='EGX',
        interval=Interval.INTERVAL_1_DAY
    )
    return stock.get_analysis().indicators

tools = [getStockDataEGX, getStockPriceEGX]