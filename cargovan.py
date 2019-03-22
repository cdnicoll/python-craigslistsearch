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
    
    for result in cl_h.get_results(sort_by='newest', limit=10):
        print result['name']
        print result['url']
        print result['price']
        print result['datetime']
        print '\n'

print 'Fetching ----> Cargo Van'
get_result('cargo van')
print '\n\n'

print 'Fetching ----> Chevy Express'
get_result('chevy express')
print '\n\n'

print 'Fetching ----> savana'
get_result('savana')
print '\n\n'

print 'Fetching ----> sprinter'
get_result('sprinter')
print '\n\n'
