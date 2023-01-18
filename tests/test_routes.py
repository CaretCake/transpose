from src.index import app

def test_v1_transpose():
    response = app.test_client().get("/v1/transpose")
    assert b"x" in response.data   