# HTTP and APIs

This repository introduces HTTP fundamentals and shows how APIs use HTTP for application-to-application communication.

## 🎯 Lesson Objectives

* Understand HTTP request/response flow and stateless behavior.
* Recognize common methods, status codes, and message structure.
* Use tools like `curl`, Postman, browser dev tools, and Python `requests`.
* Read API docs to identify endpoints, parameters, and pagination.
* Explain common authentication approaches (Basic Auth, tokens, cookies, OAuth).

## 🌐 HTTP Fundamentals

HTTP follows a request/response model: clients initiate communication and servers listen and respond.

- One request maps to one response.
- HTTP is stateless, so applications use cookies or tokens to maintain continuity across requests.

## 📩 Request and Response Anatomy

Each HTTP message is built from a start line, headers, and an optional body.

- Requests commonly include path, query string, headers, and body.
- Responses include a status line plus metadata and optional content payload.

## 🛠️ Methods and Status Codes

This lesson emphasizes practical methods and response interpretation.

- Methods: GET, HEAD, POST
- Status code families: 2xx success, 3xx redirect, 4xx client error, 5xx server error

## 🧰 Tooling and Workflow

Students use both command-line and GUI tools to inspect and test HTTP behavior.

- curl, Postman, and browser dev tools for quick endpoint testing
- Python `requests` for scripted calls, response parsing, and automation-friendly workflows

## 🔤 Encoding and Payload Handling

Because all transmitted data is bytes, encoding choices affect correctness and interoperability.

- Character encodings define how text maps to binary
- Base64 provides a text-safe way to transport binary-like data in HTTP contexts

## 📚 API Documentation Literacy

Students practice reading docs with implementation in mind.

- Identify required vs optional parameters
- Determine where each parameter belongs (path, query, or body)
- Recognize pagination and other multi-response patterns

## 🔐 Authentication Overview

The lesson compares common approaches used in stateless protocols.

- Basic Authentication
- API keys/tokens
- Session cookies
- OAuth

Discussion prompts include token lifetime, issuing authority, revocation strategy, and resource scope.

## 🧪 Hands-On Activities

- [Hands-On #1: Python `requests` Basics](http_exercises.md)
- [Hands-On #1 Solutions](http_exercises_solution.md)
- [Hands-On #2: Authentication with Python `requests`](http_exercises.md#hands-on-2-authentication-with-python-requests)

## 🔗 References

- HTTP status code reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
- Python requests quickstart: https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request
