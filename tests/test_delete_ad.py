class TestDeleteAd:
    def test_delete_ad_success(self, delete_ad_api, new_ad_payload):
        response = delete_ad_api.delete_ad(new_ad_payload['token'], new_ad_payload['id'])
        assert response.status_code == 200