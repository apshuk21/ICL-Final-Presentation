from datetime import datetime
from typing import List, Optional
from data.trades_schema import TradesSchema, TradesResponse
from langchain_core.tools import tool # type: ignore
import json
import os
import json

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the JSON file
json_path = os.path.join(current_dir, '..', 'data', 'trades.json')

@tool
def filter_trades(start_date: str, end_date: str, matching_status: Optional[str] = None) -> TradesResponse:
    """
    Filters a list of trade records based on a date range and optional matching status.

    Parameters:
        trades (List[Dict]): A list of trade dictionaries to filter.
        start_date (str): Start of the date range (YYYY-MM-DD).
        end_date (str): End of the date range (YYYY-MM-DD).
        matching_status (Optional[str]): Optional matching status to filter trades by.
                                         Valid values: 'Unmatched', 'Matched', 'Stale', 'Active', 'Affirmed'.

    Returns:
        List[Dict]: A list of trades that fall within the specified date range and match the optional status.
    """

    filtered = []
    trades = []

    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            trades = json.load(f)

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        for trade in trades:
            trade_date = datetime.strptime(trade["trade_date"], "%Y-%m-%d")
            if start <= trade_date <= end:
                if matching_status is None or trade["matching_status"] == matching_status:
                    filtered.append(trade)

    filtered = [TradesSchema.model_validate(trade) for trade in filtered]
    return TradesResponse(result=filtered)


if (__name__ == '__main__'):
    result = filter_trades('2025-06-21', '2025-07-07')
    print('##result', len(result))






