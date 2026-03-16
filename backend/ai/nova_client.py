import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

MODEL_ID = "amazon.nova-lite-v1:0"

def analyze_security_event(iocs):

    prompt = f"""
You are a SOC security analyst.

Analyze the following indicators of compromise:

{iocs}

Provide:

1. Possible attack type
2. Severity (Low / Medium / High)
3. MITRE ATT&CK techniques involved
4. Recommended response actions
"""

    body = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 500,
            "temperature": 0.3
        }
    }

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())

    return result["results"][0]["outputText"]