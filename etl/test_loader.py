from datetime import date, datetime

from model import CallRecord
from loader import CassandraLoader
from uuid import uuid4


record = CallRecord(
    call_id=uuid4(),
    call_date=date.today(),
    start_time=datetime.now(),
    end_time=datetime.now(),
    call_category="BILLING",
    ivr_contained=True,
    escalated_to_agent=False,
    agent_id=None,
    duration_seconds=0,
    ivr_path=["main_menu", "billing"]
)

loader = CassandraLoader("127.0.0.1", "clearcall")
loader.connect()
loader.load(record)
print("Test record inserted!")
loader.close()