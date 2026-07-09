# Urban Grocers API Testing
## About the Project

This project was developed as the final assignment for the **Introduction to Test Automation** module of the TripleTen QA Engineering Bootcamp.

The objective was to automate API tests for the **Urban Grocers** application by validating the creation of personal kits through HTTP requests. The project follows a structured approach using **Python**, **Pytest**, and the **Requests** library to verify both successful and unsuccessful scenarios based on API requirements.

The test suite covers positive and negative validations for the `name` field, ensuring the API correctly handles boundary values, special characters, missing parameters, and invalid data types.

---

## Technologies Used

- Python
- Pytest
- Requests
- PyCharm
- Git
- GitHub
- REST API

---

## Project Structure

```
qa-project/
│
├── configuration.py
├── data.py
├── sender_stand_request.py
├── create_kit_name_kit_test.py
└── README.md
```

---

## Test Coverage

The automated test suite validates the following scenarios for the **Create Kit** endpoint:

| Test Case | Expected Result |
|-----------|-----------------|
| Name with 1 character | 201 Created |
| Name with 511 characters | 201 Created |
| Empty name | 400 Bad Request |
| Name with 512 characters | 400 Bad Request |
| Special characters | 201 Created |
| Spaces in name | 201 Created |
| Numeric characters | 201 Created |
| Missing `name` parameter | 400 Bad Request |
| Invalid data type (`number`) | 400 Bad Request |

---

## Test Design

The project follows a modular structure to improve readability and maintainability.

- **configuration.py** stores the API base URL and endpoints.
- **data.py** contains request bodies and headers.
- **sender_stand_request.py** centralizes all API requests.
- **create_kit_name_kit_test.py** contains reusable helper functions and automated test cases.

The tests are organized using reusable assertion methods for both positive and negative scenarios, reducing code duplication and improving scalability.

---

## Prerequisites

- Python 3.x
- PyCharm (recommended)
- Git

Install the required dependencies:

```bash
pip install requests
pip install pytest
```

---

## Running the Tests

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd qa-project
```

Run all automated tests:

```bash
pytest
```

Or execute only the kit creation test suite:

```bash
pytest create_kit_name_kit_test.py
```

---

## Skills Demonstrated

- API Testing
- Test Automation with Python
- HTTP GET and POST requests
- Authentication using Bearer Tokens
- Positive and Negative Testing
- Boundary Value Analysis
- Test Case Design
- Assertions with Pytest
- Modular Test Architecture
- REST API Validation

---

## About Me

After completing the **QA Engineering Bootcamp**, I have been building practical projects focused on manual testing, API testing, SQL, and test automation with Python. This repository is part of my learning journey and reflects my ability to design maintainable automated tests while applying QA best practices.

In addition to my technical training, I bring more than 10 years of professional experience in process improvement, documentation, and cross-functional collaboration, which strengthens my analytical approach to software quality.

