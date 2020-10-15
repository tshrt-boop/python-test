from handler import hello
import json

def test_hello():
    expect = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Go Serverless v1.0! Your function executed successfully!",
            "input": {
                "body": "value"
            }
        })
    }
    actual = hello({"body": "value"}, {})

    assert expect == actual