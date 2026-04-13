import json
import random
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta

@dataclass
class CallTranscript:
    callId: str
    startTime: str
    endTime: str
    callCategory: str
    ivrContained: bool
    escalatedToAgent: bool
    agentId: str | None
    ivrPath: list[str]

counter = 0
while counter < 5:
    # Generate uuid value for each file
    generated_id = str(uuid.uuid4())

    # Generate random start time within current month (UTC)
    start_time = datetime.now(tz=timezone.utc).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    start_time += timedelta(days=random.randint(0,28),seconds=random.randint(0, 86399))

    # Generate duration (2–10 minutes)
    end_time = start_time + timedelta(seconds=random.randint(120, 600))

    # Set time format
    start_time = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Randomly generate call_category
    call_category = random.choices(
        ["GENERAL", "SALES", "TECHNICAL", "BILLING"],
        weights=[10, 15, 35, 40],
        k=1
    )[0]

    # Determine if IVR is contained
    ivr_contained = random.randint(1,100)
    if call_category == "SALES" or call_category =="TECHNICAL":
        ivr_contained= False
        escalated_to_agent = True
        # Randomly determine Agent
        agent_id = random.randint(1,5)
    elif ivr_contained<61:
        ivr_contained = True
        escalated_to_agent = False
        # Set agent id to null
        agent_id = None
    else:
        ivr_contained = False
        escalated_to_agent = True
        # Randomly determine Agent
        agent_id = str(random.randint(1,5))



    # Create CallTranscript dataObject
    record = CallTranscript(
        callId=generated_id,
        startTime=start_time,
        endTime=end_time,
        callCategory=call_category,
        ivrContained=ivr_contained,
        escalatedToAgent=escalated_to_agent,
        agentId=str(agent_id),
        ivrPath=["WELCOME", "BILLING", "ACCOUNT_LOOKUP", "RESOLVED"]
    )
    # Write to new file in transcripts folder
    with open(f'transcripts/{generated_id}.json', 'w') as f:
        json.dump(record.__dict__, f, indent=4)

    counter+=1