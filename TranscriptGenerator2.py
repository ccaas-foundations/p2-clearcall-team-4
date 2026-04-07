from datetime import datetime, timedelta, timezone
import json
import random
import uuid

counter = 0
while counter < 100:
    def SetCallCategory():
        return random.choices(
            ["BILLING", "TECHNICAL", "SALES", "GENERAL"],
            weights=[40,35,15,10],
            k=1
        )[0]

    AGENT_IDS = ["AGENT001", "AGENT002", "AGENT003", "AGENT004", "AGENT005"]

    def AssignAgentId(escalatedToAgent):
            if escalatedToAgent == "true":
                return random.choice(AGENT_IDS)
            else:
                return None


    def SetIvrCoontained(callCategory):
        ivrContainment = random.randint(1,100)
        if callCategory == "SALES" or callCategory =="TECHNICAL":
            ivrContainment="false"
            escalatedToAgent = "true"
        elif ivrContainment<61:
            ivrContainment = "true"
            escalatedToAgent = "false"
        else:
            ivrContainment = "false"
            escalatedToAgent = "true"
        return ivrContainment, escalatedToAgent


    startTime = datetime.now(tz=timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    random_seconds = random.randint(0, 86399)
    startTime = startTime + timedelta(seconds=random_seconds)
    random_seconds = random.randint(0, 300)
    endTime = startTime + timedelta(seconds=random_seconds)

    transcript = {
        "callId" : str(uuid.uuid4()),
        "startTime" : startTime,
        "endTime" : endTime,
        "callCategory": SetCallCategory(),
        "ivrContained" : SetIvrCoontained(SetCallCategory())[0],
        "esclatedToAgent" : False,
        "agentId": AssignAgentId(SetIvrCoontained(SetCallCategory())[1]),
        "ivrPath": ["WELCOME", "BILLING" , "ACCOUNT_LOOKUP", "RESOLVED"]
                }


    filename = f'transcript_{counter}.json'
    with open(filename, 'w') as f:
        json.dump(transcript, f, indent=4)
    
    counter += 1

# #startTime = datetime.now(tz=timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
# random_seconds = random.randint(0, 86399)
# startTime = startTime + timedelta(seconds=random_seconds)
# random_seconds = random.randint(0, 300)
# endTime = startTime + timedelta(seconds=random_seconds)


# ivrContainment = random.randint(1,100)
# if callCategory == "SALES" or callCategory =="TECHNICAL":
#     ivrContainment="false"
#     escalatedToAgent = "true"
# elif ivrContainment<61:
#     ivrContainment = "true"
#     escalatedToAgent = "false"
# else:
#     ivrContainment = "false"
#     escalatedToAgent = "true"

 






