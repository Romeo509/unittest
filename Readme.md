# My Python Unit Testing Project

This project demonstrates advanced unit testing using Python. The goal is to simulate a typical backend service for user authentication, including a mocked database and thorough unit tests.

## Project Structure

- `auth_service.py`: Contains the `AuthService` class responsible for authenticating users.
- `database.py`: Simulates a database for storing and retrieving user information.
- `test_auth_service.py`: Unit tests for `auth_service.py`.
- `test_database.py`: Unit tests for `database.py`.

## How to Run the Tests

Install `unittest` (comes with Python):

```bash
python -m unittest discover
```

Or run specific test files:
```bash
python -m unittest test_auth_service.py
python -m unittest test_database.py
```


### **Features of the Tests**

1. **Mocking**: The `test_auth_service.py` file uses `unittest.mock.patch` to mock the database calls, making the tests fast and isolated from real database interactions.
2. **Multiple Test Cases**: Covers successful login, incorrect password, and nonexistent user scenarios.
3. **Test Setup and Teardown**: Uses `setUp()` and `tearDown()` methods for preparing test environments (though here they're simple, in more complex projects, these might involve initializing more resources).
4. **Separation of Concerns**: Each component (`auth_service` and `database`) is tested independently.

### **Advanced Topics to Explore**

You could extend the project to include:
- **Continuous Integration (CI)**: Set up automated testing with GitHub Actions or Travis CI.
- **Test Coverage**: Use `coverage.py` to measure how much of your code is covered by tests.
- **Parameterized Tests**: Use `pytest` to run tests with multiple input parameters.

This structure will demonstrate to employers that you are familiar with best practices in testing, mocking, and isolation, as well as the importance of reliable unit tests for scalable code.
