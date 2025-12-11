class TestSignIn:
    def test_sign_in_success(self, create_user_api, random_user_payload_for_signup, login_user_api):
        create_user_api.create_user(random_user_payload_for_signup)
        response = login_user_api.login_user(random_user_payload_for_signup)

        assert response.status_code == 201
        assert response.json()['user']['email'] == random_user_payload_for_signup['email']