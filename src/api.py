import requests


def url_building(url, viewport, width):
    access_key = "bac5c602062770b4bdba66d6a234a233"
    url = f"http://api.screenshotlayer.com/api/capture?access_key={access_key}&url={url}&viewport={viewport}&width={width}"
    return url


def get_image_and_convert_to_blob(url):
    response = requests.get(url)
    image = response.content
    return image
