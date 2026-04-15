from model import CallRecord
from datetime import datetime

class TranscriptTransformer:
    def transform_transcript(self,transcript: dict) -> CallRecord:
        start_dt = datetime.strptime(transcript["startTime"], '%Y-%m-%dT%H:%M:%SZ')
        end_dt = datetime.strptime(transcript["endTime"],'%Y-%m-%dT%H:%M:%SZ')

        duration = int((end_dt - start_dt).total_seconds())

        return CallRecord(
            call_id=transcript["callId"],
            call_date=start_dt.date(),
            start_time=start_dt,
            end_time=end_dt,
            call_category=transcript["callCategory"],
            ivr_contained=transcript["ivrContained"],
            escalated_to_agent=transcript["escalatedToAgent"],
            agent_id=transcript.get("agentId"),
            duration_seconds=duration,
            ivr_path=transcript["ivrPath"],
        )
