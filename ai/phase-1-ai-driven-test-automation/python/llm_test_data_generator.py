import json
import random

def generate_test_user_data(requirements: str) -> dict:
    # This function simulates an LLM generating data based on requirements.
    # In a real scenario, this would involve calling an LLM API (e.g., OpenAI, Gemini).

    print(f"Simulating LLM generating data for requirements: '{requirements}'")

    # Mock LLM output based on common user data requirements
    mock_data = {
        "valid_user": {
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "age": 30,
            "isActive": True
        },
        "invalid_email_user": {
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "invalid-email",
            "age": 25,
            "isActive": True
        },
        "minor_user": {
            "firstName": "Alice",
            "lastName": "Wonder",
            "email": "alice.wonder@example.com",
            "age": 16,
            "isActive": False
        }
    }

    # Simple logic to pick data based on keywords in requirements
    if "invalid email" in requirements.lower():
        return mock_data["invalid_email_user"]
    elif "minor" in requirements.lower():
        return mock_data["minor_user"]
    else:
        return mock_data["valid_user"]

def mock_save_user_to_db(user_data: dict) -> bool:
    # This simulates interacting with an "internal system" (e.g., a database API).
    print(f"Mock: Saving user to database: {user_data.get('email', 'N/A')}")
    if user_data.get('email') and '@' in user_data['email']:
        print("Mock: User saved successfully.")
        return True
    else:
        print("Mock: Failed to save user - invalid email.")
        return False

if __name__ == "__main__":
    print("--- LLM Test Data Generator ---")

    # Example 1: Generate a valid user
    req1 = "Generate data for a standard valid user"
    user1 = generate_test_user_data(req1)
    print(f"Generated user data: {json.dumps(user1, indent=2)}")
    mock_save_user_to_db(user1)
    print("-" * 30)

    # Example 2: Generate user with invalid email
    req2 = "Generate data for a user with an invalid email"
    user2 = generate_test_user_data(req2)
    print(f"Generated user data: {json.dumps(user2, indent=2)}")
    mock_save_user_to_db(user2)
    print("-" * 30)

    # Example 3: Generate a minor user
    req3 = "Generate data for a minor user (under 18)"
    user3 = generate_test_user_data(req3)
    print(f"Generated user data: {json.dumps(user3, indent=2)}")
    mock_save_user_to_db(user3)
    print("-" * 30)

    print("\n--- Using Developer AI Tools Conceptually ---")
    print("In a real scenario, developer AI tools like Copilot, Cursor, or Devin AI would assist directly in writing the above Python code, suggesting data structures, function implementations, and even generating docstrings or tests for this script.")
    print("For example, if you typed 'def generate_test_user_data(requirements: str) -> dict:' and paused, a tool like Copilot might suggest the entire mock_data dictionary and the if/elif logic based on common patterns.")
    print("Similarly, for 'def mock_save_user_to_db', the AI could suggest the database interaction logic.")
    print("-" * 30)

