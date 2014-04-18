###################################################################################
# Twitter API scraper - designed to be forked and used for more interesting things
###################################################################################

import scraperwiki
import simplejson
import urllib2

# Get results from the Twitter API! Change QUERY to your search term of choice. 
# Examples: 'PCC "Police Commissioner"
QUERY = 'Lincoln AND pic.twitter.com OR flic.kr OR twitpic.com OR yfrog.com OR twitgoo.com OR pinterest.com OR instagr.am OR flickr.com OR imgur.com' 
RESULTS_PER_PAGE = '1000'
LANGUAGE = 'en'
NUM_PAGES = 100 

for page in range(1, NUM_PAGES+1):
    base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=%s' \
         % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE, page)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        for result in results_json['results']:
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            print data['from_user'], data['text']
            scraperwiki.sqlite.save(["id"], data) 
    except:
        print 'Oh dear, failed to scrape %s' % base_url
        
    