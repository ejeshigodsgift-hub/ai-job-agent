from services.auth_service import create_user


def test_create_user():
    data = {
        "full_name": "Test User",
        "email": "test@test.com",
        "password": "123456"
    }

    user = create_user(data)

    assert user.email == "test@test.com"