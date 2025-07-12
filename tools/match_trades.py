from typing import List, Dict
from langchain_core.tools import tool # type: ignore

@tool
def match_trades(trades: List[Dict]) -> List[Dict]:
    """
    Updates the matching status of each trade in the provided list to 'Matched'.

    Parameters:
        trades (List[Dict]): A list of trade records to be updated.

    Returns:
        List[Dict]: The modified trade records with 'matching_status' set to 'Matched'.
    """
    for trade in trades:
        trade["matching_status"] = "Matched"
    return trades