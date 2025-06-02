from .test_filters import send_request

def test_invalid_year_does_not_crash_server():
    filters = {"brand": "Honda", "year": "abc"}
    response = send_request(filters)
    assert isinstance(response, list)
