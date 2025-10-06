import requests
import os

class ImageService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        if not api_key:
            raise ValueError("Pexels API Key not provided.")
        self.url = "https://api.pexels.com/v1/search"

    def download_image(self, query: str, save_path="temp_image.jpg"):
        headers = {"Authorization": self.api_key}
        params = {"query": query, "per_page": 1, "orientation": "landscape"}

        response = requests.get(self.url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        if not data.get("photos"):
            raise ValueError("No photos found")

        image_url = data["photos"][0]["src"]["original"]
        img_resp = requests.get(image_url)

        with open(save_path, "wb") as f:
            f.write(img_resp.content)

        return save_path
