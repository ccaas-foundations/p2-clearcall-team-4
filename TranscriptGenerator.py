import json
import random
import uuid
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime, timezone, timedelta

@dataclass
class CallTranscript:
    callId: str
    startTime: datetime
    endTime: datetime
    callCategory: str
    ivrContained: bool
    escalatedToAgent: bool
    agentId: Optional[str]
    ivrPath: List[str]

counter = 0
while counter < 5:
    generated_id = str(uuid.uuid4())

    # Generate random start time within today (UTC)
    start_time = datetime.now(tz=timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    start_time += timedelta(seconds=random.randint(0, 86399))

    # Generate duration (2–5 minutes)
    end_time = start_time + timedelta(seconds=random.randint(120, 300))

    start_time = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    call_category = random.choices(
        ["GENERAL", "SALES", "TECHNICAL", "BILLING"],
        weights=[10, 15, 35, 40],
        k=1
    )[0]

    ivr_contained = random.randint(1,100)
    if call_category == "SALES" or call_category =="TECHNICAL":
        ivr_contained= False
        escalated_to_agent = True
    elif ivr_contained<61:
        ivr_contained = True
        escalated_to_agent = False
    else:
        ivr_contained = False
        escalated_to_agent = True

    record = CallTranscript(
        callId=generated_id,
        startTime=start_time,
        endTime=end_time,
        callCategory=call_category,
        ivrContained=ivr_contained,
        escalatedToAgent=escalated_to_agent,
        agentId=None,
        ivrPath=["WELCOME", "BILLING", "ACCOUNT_LOOKUP", "RESOLVED"]
    )
    with open(f'transcripts/{generated_id}.json', 'w') as f:
        json.dump(record.__dict__, f, indent=4)
    counter+=1