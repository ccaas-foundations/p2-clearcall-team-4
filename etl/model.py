from dataclasses import dataclass
import datetime
from typing import Optional
from uuid import UUID


@dataclass
class CallRecord:
    call_id: str
    call_date: datetime.date
    start_time: datetime
    end_time: datetime
    call_category: str
    ivr_contained: bool
    escalated: bool
    agent_id: Optional[str]
    duration_seconds: int
    ivr_path: list[str]

