import pytest
from api.create_ad import CreateAd
from api.delete_ad import DeleteAd
from api.get_ads import GetAds
from api.signin import SignIn
from api.signup import SignUp
from faker import Faker
import tempfile
from PIL import Image
import random
import os

from api.update_ad import UpdateAd


@pytest.fixture
def create_user_api():
    return SignUp()


@pytest.fixture
def get_ads_api():
    return GetAds()


@pytest.fixture
def login_user_api():
    return SignIn()


@pytest.fixture
def create_ad_api():
    return CreateAd()


@pytest.fixture
def delete_ad_api():
    return DeleteAd()


@pytest.fixture
def update_ad_api():
    return UpdateAd()


@pytest.fixture
def random_user_payload_for_signup():
    fake = Faker('ru_RU')
    password = fake.password()
    email = fake.email()
    return {
        'email': email,
        'password': password,
        'submitPassword': password
    }


@pytest.fixture
def user_token(create_user_api, login_user_api, random_user_payload_for_signup):
    create_user_api.create_user(random_user_payload_for_signup)
    response = login_user_api.login_user(random_user_payload_for_signup)
    return response.json()['token']['access_token'].replace('Bearer ', '')


@pytest.fixture
def random_image():
    temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)

    img = Image.new('RGB', (800, 600), color=(100, 150, 200))
    img.save(temp_file.name, 'JPEG', quality=85)

    temp_file.close()

    file_obj = open(temp_file.name, 'rb')

    image_tuple = ('test_image.jpg', file_obj, 'image/jpeg')

    yield image_tuple

    file_obj.close()
    if os.path.exists(temp_file.name):
        os.unlink(temp_file.name)


@pytest.fixture
def random_ad_payload(random_image):
    fake = Faker('ru_RU')

    data = {
        "name": fake.catch_phrase()[:50],
        "category": random.choice(['Авто', 'Книги', 'Садоводство', 'Хобби', 'Технологии']),
        "condition": random.choice(['Новый', 'Б/У']),
        "city": random.choice(['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань']),
        "description": fake.text(max_nb_chars=200),
        "price": str(random.randint(100, 100000)),
    }

    files = {
        "images": random_image
    }

    return {
        "data": data,
        "files": files
    }


@pytest.fixture
def new_ad_payload(random_ad_payload, create_ad_api, user_token):
    payload_data = random_ad_payload["data"]
    payload_files = random_ad_payload["files"]

    # Передаем в API
    response = create_ad_api.create_ad(
        token=user_token,
        data=payload_data,
        files=payload_files
    )
    result = response.json()
    result["token"] = user_token
    return result