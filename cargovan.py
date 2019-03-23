from craigslist import CraigslistForSale

filters = {
    'search_titles':True,
    'min_price': 5000,
    'max_price': 11000
}

def get_result(query):
    filters['query'] = query

    cl_h = CraigslistForSale(
        site='vancouver', 
        area={'van', 'nvm', 'bnc', 'rds', 'pml', 'rch'}, 
        category='cta',
        filters=filters
    )
    
    for result in cl_h.get_results(sort_by='newest', limit=3):
        print result['name']
        print result['url']
        print result['price']
        print result['datetime']
        print '---------------------------------------'


def fetching(type):
    print 'Fetching ----> ' + type
    get_result(type)
    print '\n\n'


fetching('cargo van')
fetching('chevy express')
fetching('e250')
fetching('savana')
fetching('sprinter')