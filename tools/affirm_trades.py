from typing import List, Dict
from langchain_core.tools import tool # type: ignore

@tool
def affirm_trades(trades: List[Dict]) -> List[Dict]:
    """
    Updates the matching status of each trade in the provided list to 'Affirmed'.

    Parameters:
        trades (List[Dict]): A list of trade records to be updated.

    Returns:
        List[Dict]: The modified trade records with 'matching_status' set to 'Affirmed'.
    """
    for trade in trades:
        trade["matching_status"] = "Affirmed"
    return trades