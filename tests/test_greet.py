from greet.location import greet

def test_greet():
    result = greet("America/New_York")
    assert "New York!" in result
