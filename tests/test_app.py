from app import app

def test_index():
    #Given
    app.testing = True                         #<---  Enable testing mode
    with app.test_client() as client:

        #When
        response = client.get ('/')

        #Then
        assert response.status_code == 200
        assert b'Hello, Insighta!' in response.data