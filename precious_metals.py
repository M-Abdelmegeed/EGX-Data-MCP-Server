import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_metal_price(symbol, currency="EGP"):
    """
    Get the current price of a precious metal using GoldAPI.io
    
    Args:
        symbol (str): The symbol for the metal (XAU for gold, XAG for silver)
        currency (str): The currency to get the price in (default: EGP)
    
    Returns:
        dict: The price data for the metal
    """
    api_key = os.getenv("GOLDAPI_KEY")
    if not api_key:
        return {"error": "GOLDAPI_KEY environment variable is not set"}
    
    url = f"https://www.goldapi.io/api/{symbol}/{currency}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def get_gold_price() -> str:
    """Get the current price of gold in EGP"""
    result = get_metal_price("XAU")
    if "error" in result:
        return f"Error fetching gold price: {result['error']}"
    return f"Gold price object: {result}"

def get_silver_price() -> str:
    """Get the current price of silver in EGP"""
    result = get_metal_price("XAG")
    if "error" in result:
        return f"Error fetching silver price: {result['error']}"
    return f"Silver price object: {result}"

# For testing purposes
# if __name__ == "__main__":
#     print(get_gold_price())
#     print(get_silver_price())
