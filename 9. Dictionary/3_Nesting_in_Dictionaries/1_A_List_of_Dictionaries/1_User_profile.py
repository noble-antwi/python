# Dictionary 1
user_profile_1 = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com",
    "is_active": True
}

# Dictionary 2
user_profile_2 = {
    "name": "Bob",
    "age": 30,
    "email": "bob@example.com",
    "is_active": True
}

# Dictionary 3
user_profile_3 = {
    "name": "Charlie",
    "age": 28,
    "email": "charlie@example.com",
    "is_active": False
}

# List of user profiles
user_profiles = [user_profile_1, user_profile_2, user_profile_3]
# Print each user profile
for profile in user_profiles:
    print(f"Name: {profile['name']}, Age: {profile['age']}, Email: {profile['email']}, Active: {profile['is_active']}")