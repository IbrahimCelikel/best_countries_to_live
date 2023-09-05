# Project Description
Goal
	Provide candidate cities and countries to relocate
Personal preferences
	Social state not low tax, high risk high return countries
	High iq average, good education
	Strong institutions and others general things(democracy, media, etc)
	Suitable for working remote and entrepreneurs




# data collection

--collected data from various sources, copy paste to excel
--saved as csv files




# mysql data cleaning

create database countryForFreelanceRemote

-- imported csv files

create table countries (
	city varchar(255),
	states varchar(255),
    country varchar(255),
    cost_of_living double,
    cost_of_rent double,
    health_care_index double,
    internet_mbps double,
    pollution_index double,
    safety_index double,
    taxes double);

alter table countryforfreelanceremote.countries
add column a varchar(255) FIRST;

--insert city/state/country, cost of living index and rent index to main table
insert into countryforfreelanceremote.countries (a, cost_of_living, cost_of_rent)
select `City`, `Cost of Living Index`, `Rent Index`
from countryforfreelanceremote.costs

-- update healthcareindex of the main table on city
update 
	countryforfreelanceremote.countries as c
inner join
	countryforfreelanceremote.healthcare as h
on c.a = h.city
set
	c.health_care_index = h.`health care index`;

-- update pollutionindex of the main table on city
update 
	countryforfreelanceremote.countries as c
inner join
	countryforfreelanceremote.pollution as p
on c.a = p.City
set
	c.pollution_index = p.`Pollution Index`;

-- update safetyindex of the main table on city
update 
	countryforfreelanceremote.countries as c
inner join
	countryforfreelanceremote.safety as s
on c.a = s.City
set
	c.safety_index = s.`Safety Index`;

-- split a(city/states/country) to city, states, country columns
update 
	countryforfreelanceremote.countries
set
	city = (
    select
		substring_index(`a`,',',1));

update 
	countryforfreelanceremote.countries
set
	country = (
    select
		substring_index(`a`,',',-1));

-- for states
update
	countryforfreelanceremote.countries
set states = replace(`a`,`city`,"");

update
	countryforfreelanceremote.countries
set a = replace(`states`,`country`,"");

update
	countryforfreelanceremote.countries
set states = replace(`a`,',',"");

-- trim
update
	countryforfreelanceremote.countries
set city = trim(`city`), states = trim(`states`), country = trim(`country`);

-- drop a
alter table countryforfreelanceremote.countries
drop column a;

-- update internet_mbps of the main table on city
update countryforfreelanceremote.internet
set Country = 'Hong Kong'
where Country = 'Hong Kong (SAR) '

update countryforfreelanceremote.internet
set Country = 'Macao'
where Country = 'Macau (SAR) '

update countryforfreelanceremote.internet
set Country = trim(Country)

update countryforfreelanceremote.countries
set country = 'Hong Kong'
where country = 'Hong Kong (China)'

update countryforfreelanceremote.countries
set country = 'Macao'
where country = 'Macao (China)';

update countryforfreelanceremote.countries
set country = 'Kosovo'
where country = 'Kosovo (Disputed Territory)';

update 
	countryforfreelanceremote.countries as c
inner join
	countryforfreelanceremote.internet as i
on c.country = i.Country
set
	c.internet_mbps = i.`Mbps`;

-- update taxes of the main table on city
update countryforfreelanceremote.taxes
set Country = trim(Country);

alter table countryforfreelanceremote.countries
add column personal_income_taxes double;

update countryforfreelanceremote.taxes
set `Income Tax` = replace(`Income Tax`,'%','');

update countryforfreelanceremote.taxes
set `Sales Tax` = replace(`Sales Tax`,'%','');

update countryforfreelanceremote.taxes
set `Corporate Tax` = replace(`Corporate Tax`,'%','');

update countryforfreelanceremote.taxes
set `Corporate Tax` = trim(`Corporate Tax`), `Sales Tax` = trim(`Sales Tax`), `Income Tax` = trim(`Income Tax`);

update 
	countryforfreelanceremote.countries as c
inner join
	countryforfreelanceremote.taxes as t
on c.country = t.Country
set
	c.personal_income_taxes = t.`Income Tax`;

alter table countryforfreelanceremote.countries
add column sales_taxes double;

alter table countryforfreelanceremote.countries
add column corporate_taxes double;

update 
	countryforfreelanceremote.countries as c
inner join
	countryforfreelanceremote.taxes as t
on c.country = t.Country
set
	c.sales_taxes = t.`Sales Tax`;

update 
	countryforfreelanceremote.countries as c
inner join
	countryforfreelanceremote.taxes as t
on c.country = t.Country
set
	c.corporate_taxes = t.`Corporate Tax`;

-- drop tables

-- delete rows with missing data

delete from countryforfreelanceremote.countries
where `health_care_index` is Null or internet_mbps is Null or pollution_index is Null or safety_index is Null or personal_income_taxes is Null;

alter table countryforfreelanceremote.countries
drop column taxes;




# more data collection
-- collected more data
-- saved as csv file




# data cleaning

--imported csvs

--create new fields on main table
alter table countryforfreelanceremote.countries
add column(
	corruption double,
	economic_complexity double,
    democracy double,
    liberal_democracy double,
    innovation double,
    competitiveness double,
    labour_skills double,
    infrastructure double,
    access_to_capital double,
    openness_for_business double,
    gdp_per_capita double,
    gender_inequality double,
    gini double,
    iq double,
    press_freedom double,
    pisa double,
    public_social_exp_as_gdp double
    );

--update corruption of the main table on country
update countryforfreelanceremote.corruption
set Country = trim(Country)

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.corruption as cr
on c.country = cr.Country
set c.corruption = cr.corruption

--update economic_complexty of the main table on country
update `countryforfreelanceremote`.`country complexity rankings 2021`
set `ï»¿Country` = trim(`ï»¿Country`)

update `countryforfreelanceremote`.`country complexity rankings 2021`
set `ï»¿Country` = 'United States'
where `ï»¿Country` = 'United States of America';

update `countryforfreelanceremote`.`country complexity rankings 2021`
set `ï»¿Country` = 'Turkey'
where `ï»¿Country` = 'Turkiye';

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.`country complexity rankings 2021` as ec
on c.country = ec.`ï»¿Country`
set c.economic_complexity = ec.ECI

--update democracy and liberal_democracy fields of the main table on country
update `countryforfreelanceremote`.`democracy`
set `MyUnknownColumn` = trim(`MyUnknownColumn`)

update `countryforfreelanceremote`.`democracy`
set `MyUnknownColumn` = 'United States'
where `MyUnknownColumn` = 'United States of America';

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.`democracy` as d
on c.country = d.`MyUnknownColumn`
set c.democracy = d.democracy;

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.`democracy` as d
on c.country = d.`MyUnknownColumn`
set c.liberal_democracy = d.`liberal democracy`;

--update entrepreneurship related fields of main table on country
update countryforfreelanceremote.entrepreneurship
set `MyUnknownColumn` = trim(`MyUnknownColumn`)

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.entrepreneurship as e
on c.country = e.MyUnknownColumn
set c.innovation = e.`innovation`;

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.entrepreneurship as e
on c.country = e.MyUnknownColumn
set c.competitiveness = e.`competitiveness`;

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.entrepreneurship as e
on c.country = e.MyUnknownColumn
set c.labour_skills = e.`labour skills`;

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.entrepreneurship as e
on c.country = e.MyUnknownColumn
set c.infrastructure = e.`infrastructure`;

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.entrepreneurship as e
on c.country = e.MyUnknownColumn
set c.access_to_capital = e.`access to capital`;

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.entrepreneurship as e
on c.country = e.MyUnknownColumn
set c.openness_for_business = e.`openness for business`;

--update gdp_per_capita of main table on country
update countryforfreelanceremote.gdp_per_capita
set `country` = trim(`country`)

update countryforfreelanceremote.gdp_per_capita
set gdp_per_capita = replace(gdp_per_capita,'$','')

update countryforfreelanceremote.gdp_per_capita
set gdp_per_capita = trim(gdp_per_capita)

update countryforfreelanceremote.gdp_per_capita
set gdp_per_capita = replace(gdp_per_capita,',','')

alter table countryforfreelanceremote.gdp_per_capita
modify column gdp_per_capita double

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.gdp_per_capita as g
on c.country = g.country
set c.gdp_per_capita = g.`gdp_per_capita`;

--update entrepreneurship related fields of main table on country
update countryforfreelanceremote.gender_inequality
set `country` = trim(`country`)

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.gender_inequality as g
on c.country = g.country
set c.gender_inequality = g.`gii`;

--update gini of main table on country
update countryforfreelanceremote.gini
set `country` = trim(`country`)

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.gini as g
on c.country = g.country
set c.gini = g.`gini`;

--update iq of main table on country
update countryforfreelanceremote.iq
set `Country` = trim(`Country`)

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.iq as g
on c.country = g.country
set c.iq = g.`IQ`;

--update media of main table on country
update countryforfreelanceremote.media
set `country` = trim(`country`)

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.media as g
on c.country = g.country
set c.press_freedom = g.`press`;

--update pisa of main table on country

update countryforfreelanceremote.pisa
set `Country` = trim(`Country`)

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.pisa as g
on c.country = g.country
set c.pisa = g.`PISA`;

--update social_exp_gdp of main table on country
update countryforfreelanceremote.social_exp
set `Country` = trim(`Country`)

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.social_exp as g
on c.country = g.country
set c.public_social_exp_as_gdp = g.`public_social_expenditure_as_gdp`;

-- some corrections
update countryforfreelanceremote.countries
set pisa = '483'
where country = 'Spain'

update countryforfreelanceremote.countries
set pisa = '498'
where country = 'Switzerland'

update countryforfreelanceremote.countries
set press_freedom = '78.51'
where country = 'United Kingdom'

update countryforfreelanceremote.countries
set press_freedom = '71.22'
where country = 'United States'




# collect data
-- collect innovation, competitiveness and human capital indexes
-- save as csvs




# clean data
--import csvs

-- drop some columns
alter table countryforfreelanceremote.countries
drop column innovation, 
drop column competitiveness, 
drop column labour_skills, 
drop column infrastructure, 
drop column access_to_capital, 
drop column openness_for_business;

--add columns
alter table countryforfreelanceremote.countries
add column innovation double,
add column`competitiveness` double,
add column `human_capital` double;

--update competitiveness of main table on country

update countryforfreelanceremote.competitiveness
set `country` = trim(`country`);

update countryforfreelanceremote.competitiveness
set `country` = 'United States'
where `country` = 'USA'

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.competitiveness as g
on c.country = g.country
set c.competitiveness = g.`competitiveness`;

--update innovation of main table on country

update countryforfreelanceremote.innovation
set `country` = trim(`country`);

update countryforfreelanceremote.innovation
set `country` = 'United States'
where `country` = 'USA'

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.innovation as g
on c.country = g.country
set c.innovation = g.`innovation`;

--update human_capital of main table on country
update countryforfreelanceremote.human_capital
set `country` = trim(`country`);

update countryforfreelanceremote.human_capital
set `country` = substring(`country`,2);

update countryforfreelanceremote.countries as c
inner join countryforfreelanceremote.human_capital as g
on c.country = g.country
set c.human_capital = g.`potential_reached`;

--drop tables

-- small fixes
update countryforfreelanceremote.countries
set innovation = '59.7'
where country = 'United Kingdom'

-- gini*gpd_per_capita
alter table countryforfreelanceremote.countries
add column giniXgdp_per_capita double

update countryforfreelanceremote.countries
set giniXgdp_per_capita = `public_social_exp_as_gdp` / `gini`

-- import data before deleting null rows(some countries will be deleted)

-- delete null rows
delete from countryforfreelanceremote.countries
where 
    corruption is null or 
    economic_complexity is null or  
    democracy is null or  
    liberal_democracy is null or  
    gdp_per_capita is null or 
    gender_inequality is null or 
    gini is null or 
    iq is null or 
    press_freedom is null or 
    pisa is null or  
    public_social_exp_as_gdp is null or 
    innovation is null or 
    competitiveness is null or 
    human_capital is null or 
    giniXgdp_per_capita is null;




# data analysis
-- csv to columns and xlsx

-- re arranged values(best = 100)

-- calculated averages of benefifts

-- for best countries added more cities

-- calculated averages of costs and taxes

-- calculated pros/cons




# web scraping
--created scrapyproject
scrapy startproject citiestolive
scrapy genspider citiespider https://www.numbeo.com/cost-of-living/

-- added ipython shell to scrapy.cfg

--spider
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




# Final
-- added new cities
-- changed formulas
-- result
Cities from Finland, Denmark, Norway, Sweden, Netherlands, Switzerland and Germany are candidates.