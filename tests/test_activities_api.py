def test_get_activities_returns_expected_shape(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "participants" in payload["Chess Club"]
    assert "max_participants" in payload["Chess Club"]


def test_get_activities_includes_seed_participants(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert "michael@mergington.edu" in payload["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in payload["Chess Club"]["participants"]
