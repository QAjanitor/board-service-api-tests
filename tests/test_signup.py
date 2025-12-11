class TestSignUp:
    def test_new_user_create_success(self, create_user_api, random_user_payload_for_signup):
        response = create_user_api.create_user(random_user_payload_for_signup)

        assert response.status_code == 201
        assert response.json()['user']['email'] == random_user_payload_for_signup['email']

    def test_new_user_create_dublicate_error(self, create_user_api, random_user_payload_for_signup):
        create_user_api.create_user(random_user_payload_for_signup)
        response = create_user_api.create_user(random_user_payload_for_signup)

        assert response.status_code == 400
        assert response.json()['message'] == 'Почта уже используется'