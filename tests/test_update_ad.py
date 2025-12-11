class TestUpdateAd:
    def test_update_ad_success(self, new_ad_payload, update_ad_api):
        new_ad_payload['price'] = 666
        response = update_ad_api.update_ad(new_ad_payload['token'], new_ad_payload['id'], new_ad_payload)
        assert response.status_code == 200
        assert response.json()['price'] == 666

    def test_update_ad_of_another_user(self, update_ad_api, get_ads_api, user_token):
        ad = get_ads_api.get_ads(user_token, 1).json()['offers'][0]
        ad['price'] = 666
        response = update_ad_api.update_ad(user_token, ad['id'], ad)
        assert response.status_code == 401
        assert response.json()['message'] == "Оффер не найден или у вас нет прав на его редактирование"