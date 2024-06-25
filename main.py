from HtmlScraper import HtmlScraper
from FileHandler import read

fileData = read('./pathway.json', decode_json=True)

# for toscrape
tos = fileData['toscrape']
website = tos['website']
pathway = tos['pathway']
toscrape = HtmlScraper(website)
data = toscrape.jsonParser(pathway)
toscrape.storePage('./toscrape_scraped.json', data, '\n')


# for amazon
amz = fileData['amazon']
website = amz['website']
pathway = amz['pathway']
amazon = HtmlScraper(website)
data = amazon.jsonParser(pathway['products'])
amazon.storePage('./amazon_keyboard_products.json', data, '\n')