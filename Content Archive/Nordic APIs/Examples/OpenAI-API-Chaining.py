import requests
import openai
import json

openai.api_key = "sk-..."  # Your OpenAI API key

# Step 1: Sign up a new user (the info here simulates an external input)
signup_response = requests.post("https://api.example.com/signup", json={
    "name": "Jane Doe",
    "email": "jane@example.com",
    "password": "secure123"
}).json()

# Step 2: Ask GPT what to do next, based on the signup response
messages = [
    {
        "role": "system",
        "content": (
            "You are an API orchestration engine. Based on API responses you receive, "
            "decide what API should be called next, using structured JSON. "
            "Do not speculate - respond only using the data provided. Format:\n\n"
            "{\n"
            "  \"action\": \"next_api_to_call\",\n"
            "  \"payload\": { ...fields... }\n"
            "}\n\n"
            "If no further steps are needed, respond with { \"action\": \"complete\" }"
        )
    },
    {
        "role": "user",
        "content": f"Here is the response from the signup API:\n{json.dumps(signup_response)}"
    }
]

# Step 3: GPT determines the next step
decision_1 = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    temperature=0
)['choices'][0]['message']['content']

print("GPT Decision 1:\n", decision_1)

# Step 4: Parse GPT output and take action or alert that there's an issue during processing
try:
    decision_data = json.loads(decision_1)
except json.JSONDecodeError:
    print("Error - GPT response was not valid JSON. Cannot proceed.")
    exit(1)

action = decision_data.get("action")
payload = decision_data.get("payload", {})

if action == "call_enrichment_api":
    email = payload.get("email")
    enrich_response = requests.get(
        f"https://api.example.com/enrichment?email={email}",
        headers={"Authorization": "Bearer bearerkey"}
    )
    print("Enrichment Response:\n", enrich_response.json())

elif action == "call_verification_api":
    verify_response = requests.post(
        "https://api.example.com/verify",
        json=payload
    )
    print("Verification Response:\n", verify_response.json())

elif action == "complete":
    print("Workflow complete.")

else:
    print(f"Error - Unknown action '{action}'. Manual intervention required.")
