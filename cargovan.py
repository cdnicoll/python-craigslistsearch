from craigslist import CraigslistForSale

filters = {
    'query': {'cargo van', 'chevy express', 'Savana', 'Sprinter'},
    'search_titles':True,
    'min_price': 5000,
    'max_price': 11000
}

cl_h = CraigslistForSale(
    site='vancouver', 
    area={'van', 'nvm', 'bnc', 'rds', 'pml', 'rch'}, 
    category='cta',
    filters=filters
)

for result in cl_h.get_results(sort_by='newest', limit=10):
    print result['name']
    print result['url']
    print result['price']
    print result['datetime']
    print '\n'





# {'name': u'GMC Savana/Chevy Express Benches',
#  'repost_of': None,
#  'has_image': True,
#  'url': u'https://vancouver.craigslist.org/bnc/pts/d/burnaby-gmc-savana-chevy-express-benches/6830377298.html',
#  'has_map': True,
#  'price': u'$250',
#  'geotag': (49.210858,
#  -122.955551),
#  'where': u'Burnaby',
#  'id': u'6830377298',
#  'datetime': u'2019-03-21 16:34'
#  }