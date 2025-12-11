import requests
import pytest


# def test_api_response_size():
#     url = "https://jsonplaceholder.typicode.com/posts/1"  # Replace with your API endpoint
#     response = requests.get(url)
#
#     print(response)
#
#     # Assert that the request was successful
#     assert response.status_code == 200
#
#     # Get the size of the response content in bytes
#     response_size_bytes = len(response.content)
#
#     print(f"Response size: {response_size_bytes} bytes")
#
#     # Assert that the response size is within a certain range (example)
#     expected_min_size = 100
#     expected_max_size = 500
#     assert expected_min_size <= response_size_bytes <= expected_max_size, \
#         f"Response size {response_size_bytes} is not within the expected range ({expected_min_size}-{expected_max_size} bytes)"

# You can run this test using: pytest your_test_file.py


def test_api_response():
    response=requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code==200

    print(response.json)