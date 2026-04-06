import random
import uuid
from datetime import datetime, timezone, timedelta

counter = 0
while counter < 5:
    generatedId = uuid.uuid4()
    startTime = datetime.now(tz=timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    random_seconds = random.randint(0, 86399)
    startTime = startTime + timedelta(seconds=random_seconds)
    random_seconds = random.randint(120, 300)
    endTime = startTime + timedelta(seconds=random_seconds)
    startTime = startTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    endTime = endTime.strftime('%Y-%m-%dT%H:%M:%SZ')

    callCategory = random.randint(1,100)
    ivrContainment = random.randint(1,100)
    if callCategory>90:
        callCategory = "GENERAL"
    elif callCategory>75:
        callCategory = "SALES"
    elif callCategory>40:
        callCategory = "TECHNICAL"
    else:
        callCategory = "BILLING"

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

    print(generatedId)
    scriptFile =open(f"./transcripts/{generatedId}.txt",'w')
    scriptFile.write(f"\n    \"callId\": \"{generatedId}\",\n    \"startTime\": \"{startTime}\",\n    \"endTime\": \"2026-03-17T09:44:35Z\",\n    \"callCategory\": \"{callCategory}\",\n    \"ivrContained\": {ivrContainment},\n    \"escalatedToAgent\": {escalatedToAgent},\n    \"agentId\": null,\n    \"ivrPath\": [\"WELCOME\", \"BILLING\",\"ACCOUNT_LOOKUP\", \"RESOLVED\"]\n")
    scriptFile.close()
    counter+=1