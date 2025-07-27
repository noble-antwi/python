user_profile = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com",
    "skills": ["Python", "Linux", "Docker"],
    "certifications": ["AWS Certified Cloud Practitioner", "CompTIA Security+"],
    "is_active": True
}

user_profile["certifications"].append("Certified Kubernetes Administrator")
user_profile["skills"].append("Kubernetes")

for key, value in user_profile.items():
    if isinstance(value, list):
        print(f"{key.title()}: {', '.join(value)}")
    else:
        print(f"{key.title()}: {value}")