import json
from db_models import Author, Quote
import connect

with open('authors.json', 'r', encoding='utf-8') as authors:
    authors_data = json.load(authors)

for author_data in authors_data:
    author = Author(**author_data)
    author.save()

with open('quotes.json', 'r', encoding='utf-8') as quotes:
    quotes_data = json.load(quotes)

for quote_data in quotes_data:
    author = Author.objects.get(fullname=quote_data['author'])

    quote = Quote(**quote_data)
    quote.save()
