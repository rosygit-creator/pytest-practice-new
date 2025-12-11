

from  practice.api_response_size import *
import json

#pytest -s <filename> to run tests

def test_get_request():
    # response=requests.get("https://api.example.com/data")
    response=get_request()

    # print(f"Received data: {response.json()}")
    print(f"Received data: {response.text}")


    expected_data=\
    {
        "val1":{
         'userId': 1,
         'id': 1,
         'title': 'delectus aut autem',
         'completed': False
        },

        "val2":{
        'userId': 2,
        'id': 2,
        'title': 'delectus',
        'completed': False
         }

    }

    print(expected_data["val1"])
    assert expected_data["val1"]==response.json()

    print(response.json()['title'])
    assert response.json()['title'] =="delectus aut autem"

    assert "userId" in response.json()
    assert "title" in response.json()

    assert len(response.text) > 0
    assert response.status_code == 200  # Check for a successful HTTP status code
    assert len(response.json()) > 0  # Ensure the response body is not empty


def test_post_request():
    header = {"Content-Type": "application/json; charset=utf-8"}
    input = {
        'userId': 9,
        'id': 122,
        'title': 'delectus aut autem',
        'completed': False
    }
    response=post_request(input, header)
    assert response.status_code==201
    assert response.json()==input
