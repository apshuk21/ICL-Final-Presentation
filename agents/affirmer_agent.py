from langgraph.graph import MessagesState # type: ignore
from langgraph.types import Command # type: ignore
from typing import Literal

def affirmer_agent(state: MessagesState) -> Command[Literal['supervisor_agent']]:
    print("-------------------Affirmer Agent--------------------")
    return Command(
        goto='supervisor_agent',
        update={
            **state
        }
    )