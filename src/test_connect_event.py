from .connect_event import get_parameters
def test_get_parameters():
    event = {
        "Details": {
            "Parameters": {
                "date": "1994-03-30"
            }
        }
    }
    assert get_parameters(event) == {"date": "1994-03-30"}