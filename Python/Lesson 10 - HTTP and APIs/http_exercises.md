# HTTP and APIs

This exercise set focuses on basic HTTP processing with Python's `requests` module.

- [HTTP and APIs](#http-and-apis)
  - [Hands-On #1: Python `requests` Basics](#hands-on-1-python-requests-basics)
    - [Exercise 1: First GET Request](#exercise-1-first-get-request)
    - [Exercise 2: Read Response Metadata](#exercise-2-read-response-metadata)
    - [Exercise 3: Parse JSON Safely](#exercise-3-parse-json-safely)
    - [Exercise 4: Send Query Parameters](#exercise-4-send-query-parameters)
  - [Stretch (Optional)](#stretch-optional)
    - [Handle HTTP and Network Errors](#handle-http-and-network-errors)
  - [Hands-On #2: Authentication with Python `requests`](#hands-on-2-authentication-with-python-requests)
    - [Exercise 1: Basic Authentication](#exercise-1-basic-authentication)
    - [Exercise 2: Bearer Token Header](#exercise-2-bearer-token-header)
    - [Exercise 3: API Key in Header and Query String](#exercise-3-api-key-in-header-and-query-string)
    - [Exercise 4: Session Cookies](#exercise-4-session-cookies)
  - [Stretch (Optional)](#stretch-optional-1)
    - [Auth Wrapper with Safe Secret Handling](#auth-wrapper-with-safe-secret-handling)


## Hands-On #1: Python `requests` Basics

- Create and activate a virtual environment.
- Install requests:

```bash
pip install requests
```

Use this base URL for the exercises:

- `https://jsonplaceholder.typicode.com`

---

### Exercise 1: First GET Request

**Goal**: Send a `GET` request to `/posts/1`, then print the HTTP status code and response reason phrase.

✅ *Check*: Your program prints `200` and `OK`.

---

### Exercise 2: Read Response Metadata

**Goal**: Request `/posts/1` and print:

- `Content-Type` response header
- Total response time in milliseconds (`response.elapsed`)

✅ *Check*: Output shows a `Content-Type` containing `application/json` and a numeric time value.

---

### Exercise 3: Parse JSON Safely

**Goal**: Request `/posts/1`, parse JSON, and print:

- `userId`
- `id`
- `title`

Also add a `try/except` block that handles JSON parse errors gracefully.

✅ *Check*: The three fields print correctly, and your code does not crash if JSON parsing fails.

---

### Exercise 4: Send Query Parameters

**Goal**: Request `/comments` with query params (`postId=1`) using `params={...}` and print:

- Number of comments returned
- Email from the first comment

✅ *Check*: Program reports a non-zero comment count and prints a valid email string.

---

## Stretch (Optional)

### Handle HTTP and Network Errors

**Goal**: Build a small helper function `fetch(url)` that:

- Uses `timeout=3`
- Calls `response.raise_for_status()`
- Catches and prints friendly messages for:
  - `requests.exceptions.Timeout`
  - `requests.exceptions.HTTPError`
  - `requests.exceptions.RequestException`

Test with:

- A valid endpoint: `/posts/1`
- An invalid endpoint: `/not-a-real-route`

✅ *Check*: Valid request succeeds; invalid request prints a clear error without crashing.

---

## Hands-On #2: Authentication with Python `requests`

This exercise set focuses on common authentication patterns used with HTTP APIs.

For these exercises, use:

- `https://httpbin.org`

Security note:

- Do not hardcode real credentials or tokens in source code.
- Prefer environment variables for secrets.

---

### Exercise 1: Basic Authentication

**Goal**: Use HTTP Basic Auth to call:

- `/basic-auth/student/pass123`

Use username `student` and password `pass123` in your request.

✅ *Check*: Successful call returns status code `200` and JSON showing authentication success.

---

### Exercise 2: Bearer Token Header

**Goal**: Send a request to `/bearer` with an `Authorization` header in this format:

- `Authorization: Bearer <token>`

Use a placeholder token value such as `abc123`.

✅ *Check*: Response indicates bearer authentication succeeded.

---

### Exercise 3: API Key in Header and Query String

**Goal**: Send two requests to `/get`:

- One with header: `X-API-Key: demo-key-001`
- One with query param: `?api_key=demo-key-001`

Print the echoed value from the response JSON each time.

✅ *Check*: You can see the API key echoed once under headers and once under args.

---

### Exercise 4: Session Cookies

**Goal**: Use `requests.Session()` to:

1. Set a cookie with `/cookies/set/course_token/python-lesson-10`
2. Fetch `/cookies` with the same session
3. Print the stored cookies from the response

✅ *Check*: The `course_token` cookie appears in the final `/cookies` response.

---

## Stretch (Optional)

### Auth Wrapper with Safe Secret Handling

**Goal**: Write a function `auth_get(url, token_env="API_TOKEN")` that:

- Reads a token from `os.getenv(token_env)`
- If missing, prints a helpful message and returns without crashing
- If present, sends `Authorization: Bearer <token>`
- Uses `timeout=3` and `raise_for_status()`
- Handles `Timeout`, `HTTPError`, and generic `RequestException`

Test with:

- `auth_get("https://httpbin.org/bearer")` with no env var set
- Set env var and run again

✅ *Check*: Missing-token case is handled cleanly, and valid-token case succeeds.
