import imagehash
import requests
import scrapy
from bs4 import BeautifulSoup
from odnoklassniki_parser.database import get_groups
from PIL import Image


class OdnoklassnikiSpider(scrapy.Spider):
    name = "odnoklassniki"
    allowed_domains = ["ok.ru"]

    def start_requests(self):
        for url in get_groups():
            yield scrapy.Request(
                url=url,
                callback=self.get_posts,
                meta=dict(
                    playwright=True,
                ),
            )

    def get_posts(self, response):
        soup = BeautifulSoup(
            response.text,
            features="lxml",
        )
        posts = soup.find_all(attrs={"class": "feed-w"})
        for post in posts:
            images = post.find_all("img", {"class": "collage_img"})
            if len(images) == 1:
                image_url = images[0]["src"]

                description = None
                description_container = post.find(
                    attrs={"class": "media-text_cnt_tx"},
                )
                if description_container:
                    description = description_container.text
                yield dict(
                    hashsum=self.get_hashsum(image_url),
                    image_url=image_url,
                    description=description,
                    group_url=response.url,
                )

    def get_hashsum(self, url):
        image_data = Image.open(requests.get(url, stream=True).raw)
        hash = imagehash.average_hash(image_data)
        return str(hash)
