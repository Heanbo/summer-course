import requests


def get_user_name(user_id):
    """Fetch a user's name from an API."""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    if response.status_code == 200:
        return response.json().get("name")
    return None
