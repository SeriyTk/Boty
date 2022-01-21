import requests as rq
from pprint import pprint
response = rq.get('https://stepik.org/api/search-results',params={'query':'python'})
pprint(response.json())