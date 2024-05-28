# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open('jobs_updated.json', 'w')
        self.file.write("[\n")  # Start writing a JSON array

    def close_spider(self, spider):
        self.file.write("\n]")  # Close the JSON array
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"  # Convert item to JSON format
        self.file.write(line)  # Write the JSON to the file
        return item