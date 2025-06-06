signup_response = requests.post("https://api.example.com/signup", json={
    "name": "Jane Doe",
    "email": "jane@example.com",
    "password": "secure123"
})
signup_data = signup_response.json()
email = signup_data["email"]

enrich_response = requests.get(f"https://api.example.com/enrichment?email={email}", headers={
    "Authorization": "Bearer bearerkey"
})
enrich_data = enrich_response.json()

requests.post("https://api.example.com/users", json={
    "user_id": signup_data["id"],
    "company": enrich_data.get("company"),
    "title": enrich_data.get("title"),
    "linkedin": enrich_data.get("linkedin")
})
