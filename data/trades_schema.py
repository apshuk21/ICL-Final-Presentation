from pydantic import BaseModel, Field # type: ignore
from typing import Literal, List

class TradesSchema(BaseModel):
    """
    Represents the structure of an individual trade, including parties involved,
    instrument details, monetary values, and matching status.
    """
    id: str = Field(description="This is the unique identifier of the trade")
    party: str = Field(description="This is the party involved in this trade")
    counter_party: str = Field(description="This is the counter party involved in this trade")
    trade_date: str = Field(description="This is the trade date of this trade")
    matching_status: Literal["Matched", "Unmatched", "Stale", "Active", "Affirmed"]
    instrument: str = Field(description="This is the instrument used in this trade")
    notional_amount: float = Field(description="This is the notional amount of this trade")
    currency: str = Field(description="This is the currency used in this trade")

class TradesResponse(BaseModel):
    """
    Represents the structured output containing a list of matched or filtered trades.
    This model wraps multiple TradesSchema objects under the `result` field.
    """
    result: List[TradesSchema]