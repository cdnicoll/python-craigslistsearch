from craigslist import CraigslistForSale

filters = {
    'search_titles':True,
    'min_price': 5000,
    'max_price': 11000
}

# filters = {
#     'search_titles':True,
#     'min_price': 11000,
#     'max_price': 17000
# }

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

print 'Dont forget to checkout these sites:'
print 'https://www.autotrader.ca/heavy-trucks/cube-step-cargo%20vans/bc/?srt=3&pRng=%2C11000&oRng=%2C190000&prv=British%20Columbia&loc=v3m0c5&sts=Used'
print '------------------------'
print 'https://ca.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=untrackedExternal_false_0&newSearchFromOverviewPage=true&inventorySearchWidgetType=BODYSTYLE&bodyTypeGroup=bg8&zip=V6J&distance=100&startYear=2005&endYear=&minPrice=0&maxPrice=12000&maxMileage=190000&showNegotiable=false&modelChanged=undefined&filtersModified=true'
print '\n'