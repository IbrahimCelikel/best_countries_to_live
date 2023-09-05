import scrapy
import csv

class CitiespiderSpider(scrapy.Spider):
    name = "citiespider"
    allowed_domains = ["www.numbeo.com"]
    start_urls = ["https://www.numbeo.com/cost-of-living/"]

    def parse(self, response):
        countries = response.css('div form select option::attr(value)').getall()
        for country in countries:
            country_ = country.replace(" ", "+")
            country_url = "https://www.numbeo.com/cost-of-living/country_result.jsp?country=" + country_
            yield response.follow(country_url, callback= self.parse_country_link)
    
    def parse_country_link(self, response):
        city_links = response.css('tbody tr td a::attr(href)').getall()
        for city_link in city_links:
            yield response.follow(city_link, callback= self.parse_city_link)
    
    def parse_city_link(self, response):
        quality_of_life_link = response.css('body div div div div ul li a::attr(href)').get()
        yield response.follow(quality_of_life_link, callback= self.parse_scores)
        
    def parse_scores(self, response): 

        city_name = response.css('body div h1::text').getall()
        country_name = response.css('nav span a span[itemprop="name"]::text').getall()[1]
        cost_of_living = response.css('td[style="text-align: right"]::text').getall()[5]
        safety = response.css('td[style="text-align: right"]::text').getall()[2]
        health_care = response.css('td[style="text-align: right"]::text').getall()[3]
        pollution = response.css('td[style="text-align: right"]::text').getall()[8]
        
        file = open("C:/depo/repositories/best_countries_to_live/citiestolive/scraped.csv", "a", newline='')
        writer = csv.writer(file)
        
        writer.writerow([city_name, country_name, cost_of_living, safety, health_care, pollution])
        
        file.close()