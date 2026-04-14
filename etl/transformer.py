from model import CallRecord
from datetime import datetime

def transform_transcript(transcript: dict) -> CallRecord:
    start_dt = datetime.strptime(transcript["startTime"], '%Y-%m-%dT%H:%M:%SZ')
    end_dt = datetime.strptime(transcript["endTime"],'%Y-%m-%dT%H:%M:%SZ')

    duration = int((end_dt - start_dt).total_seconds())

    if transcript["agentId"] is not None:
        agent = transcript["agentId"]
    else:
        agent = None

    return CallRecord(
        call_id=transcript["callId"],
        call_date=start_dt.date(),
        start_time=start_dt,
        end_time=end_dt,
        call_category=transcript["callCategory"],
        ivr_contained=transcript["ivrContained"],
        escalated_to_agent=transcript["escalatedToAgent"],
        agent_id=agent,
        duration_seconds=duration,
        ivr_path=transcript["ivrPath"],
    )

newTranscript = {
    "callId": "4aa23055-9b14-4cf6-bc2d-11d979e67814",
    "startTime": "2026-04-19T23:25:03Z",
    "endTime": "2026-04-19T23:30:00Z",
    "callCategory": "TECHNICAL",
    "ivrContained": False,
    "escalatedToAgent": True,
    "agentId": "4",
    "ivrPath": [
        "WELCOME",
        "BILLING",
        "ACCOUNT_LOOKUP",
        "RESOLVED"
    ]
}
print(transform_transcript(newTranscript))
