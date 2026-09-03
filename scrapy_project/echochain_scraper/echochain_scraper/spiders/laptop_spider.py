import scrapy


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

        yield {
            "product_name": product_name,
            "brand": brand,
            "price": response.css("span::text").re_first(r"₹[\d,]+"),
            "product_url": response.url
        }