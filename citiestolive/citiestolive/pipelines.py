# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CitiestolivePipeline:
    def process_item(self, item, spider):
        return item



import mysql.connector

class SaveToMySQLPipeLine:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '25652zxc',
            database = 'citiestolive'
            )
        
        self.cur = self.conn.cursor()
           
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS cities(
            id int NOT NULL auto_increment,
            city text,
            country text,
            cost_of_living float,
            safety float,
            health_care float,
            pollution float,
            PRIMARY KEY (id)
            )
            """)
        
    def process_item(self,item,spider):
        adapter = ItemAdapter(item)
            
        sql = """insert into cities (city, country, cost_of_living, safety, heath_care, pollution) values (%s, %s, %s, %s, %s, %s) """
        a = item['city_name']
        b = item['country_name']
        c = item['cost_of_living']
        e = item['safety']
        f = item['health_care']
        g = item['pollution']
        val = (a,b,c,e,f,g)
        
        self.cur.execute(sql,val)

        self.conn.commit()
        return item

    def close_spider(self,spider):
        
        self.cur.close()
        self.conn.close()