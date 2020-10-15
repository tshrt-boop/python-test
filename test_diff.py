from diff import *

def test_diff_new_record1():
    """
    全くない状況で新しく1件入ってくる
    """
    expect = [
        {
            "code": "10100100100",
            "status": "down",
            "downtime": "2020-11-12 12:34:56",
            "restore":  ""
        }
    ]
    actual = diff(
        [], 
        [
            {
                "code": "10100100100",
                "downtime": "2020-11-12 12:34:56",
                "restore":  ""
            },
        ]
    )
    assert expect == actual

# def test_diff_new_record2():
#     """
#     全くない状況で新しく1件入ってくる(ちょっと違うレコード)
#     """
#     expect = [
#         {
#             "code": "10100100101",
#             "status": "down",
#             "downtime": "2020-11-12 12:34:56",
#             "restore":  ""
#         }
#     ]
#     actual = diff([], [
#         {
#             "code": "10100100101",
#             "downtime": "2020-11-12 12:34:56",
#             "restore":  ""
#         },
#     ])
#     assert expect == actual