from app import app

def test_index():
    #Given
    client = app.test_client()

    #When
    response = client.get ('/')

    #Then
    assert response.status_code == 200
    assert b'Hello, Insighta!' in response.data