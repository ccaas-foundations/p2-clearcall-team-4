import json
import random
import uuid
import os
import argparse
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

class TranscriptGenerator:
    def __init__(self,transcript_amount:int,transcript_directory:str):
        self.transcript_amount = transcript_amount
        self.transcript_directory = transcript_directory

    def generate_id(self):
        return str(uuid.uuid4())

    def generate_times(self):
        # Generate random start time within current month (UTC)
        start_time = datetime.now(tz=timezone.utc).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        start_time += timedelta(days=random.randint(0,28),seconds=random.randint(0, 86399))
        # Generate duration (2–10 minutes)
        end_time = start_time + timedelta(seconds=random.randint(120, 600))
        # Set time format
        start_time = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_time = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')

        return start_time,end_time

    def generate_call_category(self):
        return random.choices(
            ["GENERAL", "SALES", "TECHNICAL", "BILLING"],
            weights=[10, 15, 35, 40],
            k=1
        )[0]

    def generate_call_details(self,call_category:str):
        ivr_contained = random.randint(1,100)
        if call_category == "SALES" or call_category =="TECHNICAL":
            ivr_contained= False
            escalated_to_agent = True
            # Randomly determine Agent
            agent_id = f"agent-{random.randint(1, 5)}"
        elif ivr_contained<61:
            ivr_contained = True
            escalated_to_agent = False
            # Set agent id to null
            agent_id = None
        else:
            ivr_contained = False
            escalated_to_agent = True
            # Randomly determine Agent
            agent_id = f"agent-{random.randint(1, 5)}"
        return ivr_contained,escalated_to_agent,agent_id

    def generate_ivr_path(self,call_category:str,ivr_contained:list[str]):
        if call_category == "BILLING":
            if ivr_contained:
                return ["WELCOME", "BILLING", "ACCOUNT_LOOKUP", "RESOLVED"]
            return ["WELCOME", "BILLING", "ACCOUNT_LOOKUP", "UNRESOLVED"]

        if call_category == "TECHNICAL":
            if ivr_contained:
                return ["WELCOME", "TECH_SUPPORT", "DEVICE_TROUBLESHOOTING", "RESOLVED"]
            return ["WELCOME", "TECH_SUPPORT", "DEVICE_TROUBLESHOOTING", "UNRESOLVED"]

        if call_category == "SALES":
            if ivr_contained:
                return ["WELCOME", "SALES", "PRODUCT_INFO", "RESOLVED"]
            return ["WELCOME", "SALES", "PRODUCT_INFO", "UNRESOLVED"]

        if call_category == "GENERAL":
            if ivr_contained:
                return ["WELCOME", "GENERAL_INQUIRY", "FAQ", "RESOLVED"]
            return ["WELCOME", "GENERAL_INQUIRY", "FAQ", "UNRESOLVED"]

        return ["WELCOME", "UNKNOWN", "UNRESOLVED"]

    def build_transcript(self):

        generated_id = self.generate_id()
        start_time,end_time = self.generate_times()
        call_category = self.generate_call_category()
        ivr_contained,escalated_to_agent,agent_id = self.generate_call_details(call_category)
        ivr_path = self.generate_ivr_path(call_category,ivr_contained)

        return CallTranscript(
            callId=generated_id,
            startTime=start_time,
            endTime=end_time,
            callCategory=call_category,
            ivrContained=ivr_contained,
            escalatedToAgent=escalated_to_agent,
            agentId=str(agent_id),
            ivrPath=ivr_path
        )

    def write_transcript(self,transcript:CallTranscript):
        os.makedirs(self.transcript_directory, exist_ok=True)

        with open(f'{self.transcript_directory}/{transcript.callId}.json', 'w') as f:
            json.dump(transcript.__dict__, f, indent=4)

    def generate_transcripts(self):
        for _ in range(self.transcript_amount):
            transcript = self.build_transcript()
            self.write_transcript(transcript)


def parse_args():
    parser = argparse.ArgumentParser(description="Generate random call transcript JSON files.")
    parser.add_argument("-n",
                        "--num-transcripts",
                        type=int,
                        default=50,
                        help="Number of transcripts to generate (default: 50)"
                        )
    parser.add_argument("-o",
                        "--output-dir",
                        type=str,
                        default="transcripts",
                        help="Output directory for transcript files (default: transcripts)",
                        )
    return parser.parse_args()

def main():
    args = parse_args()

    generator = TranscriptGenerator(args.num_transcripts,args.output_dir)
    generator.generate_transcripts()

if __name__ == "__main__":
    main()