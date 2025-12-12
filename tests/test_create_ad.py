class TestCreateAd:
    def test_create_ad_success(self, user_token, create_ad_api, random_ad_payload):
        payload_data = random_ad_payload["data"]
        payload_files = random_ad_payload["files"]

        response = create_ad_api.create_ad(
            token=user_token,
            data=payload_data,
            files=payload_files
        )

        assert response.status_code == 201
        assert response.json()['name'] == payload_data['name']