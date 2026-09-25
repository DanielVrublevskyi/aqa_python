import requests
from core.utils.logger import cli_logger

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

def get_nasa_ids_list(response):
    items = response.json().get("collection").get("items")
    cli_logger.info(f"GET {response.url}")
    id_list = []
    for item in items:
        id_list.append(item.get("data")[0].get("nasa_id"))
    return id_list

def get_nasa_url_list(nasa_ids_list, limit):
    get_asset_url = f"{BASE_URL}/asset/{{nasa_id}}"
    assets_urls_list = []
    for nasa_id in nasa_ids_list:
        asset_url = get_asset_url.format(nasa_id=nasa_id)

        cli_logger.info(f"GET {asset_url}")
        response = requests.get(asset_url).json()
        items = response.get("collection").get("items")

        for item in items:
            href = item.get("href")

            if href.endswith(".jpg"):
                assets_urls_list.append(href)
                break
        if len(assets_urls_list) == limit:
            break
    return assets_urls_list


def download_images(assets_url_list):
    for index, asset_url in enumerate(assets_url_list, start=1):
        with open(f"mars_photo{index}.jpg", "wb") as f:
            cli_logger.info(f"GET {asset_url}")
            f.write(requests.get(asset_url).content)


nasa_response = requests.get(search_url, params=search_params)

nasa_id_list = get_nasa_ids_list(response=nasa_response)

nasa_url_list = get_nasa_url_list(nasa_ids_list=nasa_id_list, limit=2)

download_images(assets_url_list=nasa_url_list)