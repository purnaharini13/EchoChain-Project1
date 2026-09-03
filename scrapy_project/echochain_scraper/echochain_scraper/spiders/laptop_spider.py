import scrapy
import re
from datetime import datetime


class LaptopSpider(scrapy.Spider):
    name = "laptop_spider"
    allowed_domains = ["justunboxed.co.in"]

    start_urls = [
        "https://justunboxed.co.in/product-category/alllaptops/"
    ]

    def parse(self, response):

        products = response.css("a.block.h-full")

        for product in products:

            product_url = product.attrib.get("href")
            product_name = product.css("span::text").get()

            if product_url:
                yield response.follow(
                    product_url,
                    callback=self.parse_product,
                    meta={
                        "product_name": product_name
                    }
                )

    def parse_product(self, response):

        product_name = response.meta["product_name"]

        brand = product_name.split()[0]

        processor = re.search(
            r"(Core™?\s*i[3579]-?\d*(?:th)?\s*Gen|Ryzen™?\s*\d)",
            product_name
        )

        ram = re.search(
            r"\d+GB RAM",
            product_name
        )

        storage = re.search(
            r"\d+(?:GB|TB)\s*(?:SSD|HDD)",
            product_name
        )

        screen_size = re.search(
            r"\d+\s*Inch",
            product_name
        )

        yield {
            "product_name": product_name,
            "brand": brand,
            "processor": processor.group() if processor else None,
            "ram": ram.group() if ram else None,
            "storage": storage.group() if storage else None,
            "screen_size": screen_size.group() if screen_size else None,
            "price": response.css("span::text").re_first(r"₹[\d,]+"),
            "product_url": response.url,
            "source": "JustUnboxed",
            "scraped_date": datetime.now().strftime("%Y-%m-%d")
        }