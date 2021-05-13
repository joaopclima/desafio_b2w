import scrapy
from ..items import QuotesChallengeItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    base_url = 'http://quotes.toscrape.com'
    author = {'name': '', 'url': ''}

    start_urls = [
        base_url,
    ]

    def parse(self, response):
        all_divs = response.css('div.quote')

        items = QuotesChallengeItem()

        for quote in all_divs:
            title = quote.css('span.text::text').extract_first()
            author_name = quote.css('.author::text').extract_first()
            author_url = quote.xpath('//span//@href').extract_first()
            self.author['name'], self.author['url'] = (
                author_name,
                self.base_url + author_url,
            )
            
            tags = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = self.author
            items['tags'] = tags

            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            
            yield response.follow(next_page, callback=self.parse)