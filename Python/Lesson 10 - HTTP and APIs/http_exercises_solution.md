# HTTP and APIs Solutions

This file provides one possible solution set for [http_exercises.md](http_exercises.md).

- [HTTP and APIs Solutions](#http-and-apis-solutions)
  - [Hands-On #1 Solutions: Python `requests` Basics](#hands-on-1-solutions-python-requests-basics)
    - [Exercise 1: First GET Request](#exercise-1-first-get-request)
    - [Exercise 2: Read Response Metadata](#exercise-2-read-response-metadata)
    - [Exercise 3: Parse JSON Safely](#exercise-3-parse-json-safely)
    - [Exercise 4: Send Query Parameters](#exercise-4-send-query-parameters)
  - [Stretch (Optional) Solution](#stretch-optional-solution)
    - [Handle HTTP and Network Errors](#handle-http-and-network-errors)
  - [Hands-On #2 Solutions: Authentication with Python `requests`](#hands-on-2-solutions-authentication-with-python-requests)
    - [Exercise 1: Basic Authentication](#exercise-1-basic-authentication)
    - [Exercise 2: Bearer Token Header](#exercise-2-bearer-token-header)
    - [Exercise 3: API Key in Header and Query String](#exercise-3-api-key-in-header-and-query-string)
    - [Exercise 4: Session Cookies](#exercise-4-session-cookies)
  - [Stretch (Optional) Solution](#stretch-optional-solution-1)
    - [Auth Wrapper with Safe Secret Handling](#auth-wrapper-with-safe-secret-handling)


## Hands-On #1 Solutions: Python `requests` Basics

Use this base URL for hands-on #1:

```python
BASE_URL = "https://jsonplaceholder.typicode.com"
```

---

### Exercise 1: First GET Request

```python
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{BASE_URL}/posts/1")
print(response.status_code)
print(response.reason)
```

✅ *Check*: Should print `200` and `OK`.

---

### Exercise 2: Read Response Metadata

```python
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{BASE_URL}/posts/1")
content_type = response.headers.get("Content-Type", "<missing>")
elapsed_ms = int(response.elapsed.total_seconds() * 1000)

print(f"Content-Type: {content_type}")
print(f"Elapsed: {elapsed_ms} ms")
```

✅ *Check*: `Content-Type` should contain `application/json` and elapsed time should be numeric.

---

### Exercise 3: Parse JSON Safely

```python
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

response = requests.get(f"{BASE_URL}/posts/1")

try:
    data = response.json()
    print(f"userId: {data['userId']}")
    print(f"id: {data['id']}")
    print(f"title: {data['title']}")
except ValueError:
    print("Response body was not valid JSON")
```

✅ *Check*: Prints the 3 fields and handles JSON parsing errors safely.

---

### Exercise 4: Send Query Parameters

```python
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

params = {"postId": 1}
response = requests.get(f"{BASE_URL}/comments", params=params)
comments = response.json()

print(f"Comments returned: {len(comments)}")
if comments:
    print(f"First email: {comments[0]['email']}")
```

✅ *Check*: Non-zero comment count and a valid-looking email should be printed.

---

## Stretch (Optional) Solution

### Handle HTTP and Network Errors

```python
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch(url: str):
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        print(f"Success: {url} -> {response.status_code}")
        return response
    except requests.exceptions.Timeout:
        print(f"Timeout: request to {url} took too long")
    except requests.exceptions.HTTPError as err:
        status = err.response.status_code if err.response is not None else "unknown"
        print(f"HTTP error ({status}) for {url}")
    except requests.exceptions.RequestException as err:
        print(f"Request failed for {url}: {err}")


fetch(f"{BASE_URL}/posts/1")
fetch(f"{BASE_URL}/not-a-real-route")
```

✅ *Check*: Valid endpoint succeeds; invalid endpoint shows a friendly HTTP error.

---

## Hands-On #2 Solutions: Authentication with Python `requests`

Use this base URL for hands-on #2:

```python
BASE_URL = "https://httpbin.org"
```

---

### Exercise 1: Basic Authentication

```python
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://httpbin.org"

response = requests.get(
    f"{BASE_URL}/basic-auth/student/pass123",
    auth=HTTPBasicAuth("student", "pass123"),
)

print(response.status_code)
print(response.json())
```

✅ *Check*: Returns `200` and JSON with authentication success.

---

### Exercise 2: Bearer Token Header

```python
import requests

BASE_URL = "https://httpbin.org"

headers = {"Authorization": "Bearer abc123"}
response = requests.get(f"{BASE_URL}/bearer", headers=headers)

print(response.status_code)
print(response.json())
```

✅ *Check*: Response should indicate bearer auth succeeded.

---

### Exercise 3: API Key in Header and Query String

```python
import requests

BASE_URL = "https://httpbin.org"
api_key = "demo-key-001"

header_response = requests.get(f"{BASE_URL}/get", headers={"X-API-Key": api_key})
query_response = requests.get(f"{BASE_URL}/get", params={"api_key": api_key})

header_json = header_response.json()
query_json = query_response.json()

print(f"Header API key: {header_json['headers'].get('X-Api-Key')}")
print(f"Query API key: {query_json['args'].get('api_key')}")
```

✅ *Check*: Key appears once in echoed headers and once in echoed args.

---

### Exercise 4: Session Cookies

```python
import requests

BASE_URL = "https://httpbin.org"

session = requests.Session()
session.get(f"{BASE_URL}/cookies/set/course_token/python-lesson-10")
response = session.get(f"{BASE_URL}/cookies")

print(response.status_code)
print(response.json())
```

✅ *Check*: `course_token` appears in the returned cookies object.

---

## Stretch (Optional) Solution

### Auth Wrapper with Safe Secret Handling

```python
import os
import requests


def auth_get(url: str, token_env: str = "API_TOKEN"):
    token = os.getenv(token_env)
    if not token:
        print(f"Missing token. Set environment variable: {token_env}")
        return None

    try:
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {token}"},
            timeout=3,
        )
        response.raise_for_status()
        print(f"Success: {url} -> {response.status_code}")
        return response
    except requests.exceptions.Timeout:
        print(f"Timeout while calling {url}")
    except requests.exceptions.HTTPError as err:
        status = err.response.status_code if err.response is not None else "unknown"
        print(f"HTTP error ({status}) for {url}")
    except requests.exceptions.RequestException as err:
        print(f"Request error for {url}: {err}")

    return None


# Run once without env var set, then set API_TOKEN and run again.
auth_get("https://httpbin.org/bearer")
```

✅ *Check*: Missing-token case is graceful, and valid-token case succeeds.
