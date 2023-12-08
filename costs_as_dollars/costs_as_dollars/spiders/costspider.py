import scrapy
import csv
import pandas as pd


class CostspiderSpider(scrapy.Spider):
    name = "costspider"
    allowed_domains = ["www.numbeo.com"]
    start_urls = ["https://www.numbeo.com/cost-of-living/"]

    def parse(self, response):
        cities = pd.read_csv('C:/depo/repositories/best_countries_to_live/city_names_for_costs_as_dollars.csv')
        for city in cities['city']:
            city_url = "https://www.numbeo.com/cost-of-living/in/" + city + "?displayCurrency=USD"
            yield response.follow(city_url, callback= self.parse_city)

    def parse_city(self, response):
        city_name = response.css('[class="breadcrumb_link"] span::text')[-1].get()
        cost_of_living = response.xpath('//li[text()="A single person estimated monthly costs are "]/span/text()').get()
        cost_of_rent = response.xpath('//td[text()="Apartment (1 bedroom) in City Centre "]/following-sibling::td/span/text()').get()
        
        file = open("C:/depo/repositories/best_countries_to_live/costs_as_dollars.csv", "a", newline='')
        writer = csv.writer(file)
        
        writer.writerow([city_name, cost_of_living, cost_of_rent])
        
        file.close()