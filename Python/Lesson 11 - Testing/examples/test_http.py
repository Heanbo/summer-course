import pytest
from http import get_user_name


def test_get_user_name_success(mocker):
    """Test get_user_name with a mocked requests.get"""

    # Create a mock response object
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"name": "Alice"}

    # Patch requests.get to return our mock response
    mocker.patch("http.requests.get", return_value=mock_response)

    # Call the function under test
    result = get_user_name(123)

    # Assertions
    assert result == "Alice"
    app_requests_get = mocker.patch("http.requests.get")
    app_requests_get.assert_called_once_with("https://api.example.com/users/123")


def test_get_user_name_failure(mocker):
    """Test get_user_name when API returns non-200"""
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {}

    mocker.patch("http.requests.get", return_value=mock_response)

    result = get_user_name(999)
    assert result is None
