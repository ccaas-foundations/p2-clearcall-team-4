import random

counter = 2
while counter < 1:
    generatedId = random.randint(0,100)
    print(generatedId)
    scriptFile =open(f"./transcripts/{generatedId}.txt",'w')
    scriptFile.write("{\n    \"callId\": \"a3f9c2e1-7b44-4d18-9f2c-1a2b3c4d5e6f\",\n    \"startTime\": \"2026-03-17T09:42:00Z\",\n    \"endTime\": \"2026-03-17T09:44:35Z\",\n    \"callCategory\": \"BILLING\",\n    \"ivrContained\": true,\n    \"escalatedToAgent\": false,\n    \"agentId\": null,\n    \"ivrPath\": [\"WELCOME\", \"BILLING\",\"ACCOUNT_LOOKUP\", \"RESOLVED\"]\n}")
    scriptFile.close()
    counter+=1