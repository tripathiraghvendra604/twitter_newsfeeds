import twitter
import json
import string
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
from urllib.error import URLError


def get_tags(woe_id):
    """
    takes woe id of the country and uses twitter api to get top #tags
    and news of that country
    :param woe_id: unique WOE ID of the country
    :return: list of trending #tags and top news from twitter
    """
    consumer_key = 'NNWRNbrJAAovWOkvlNuPh6WOL'
    consumer_secret = 'rTtPwwRNP2Pfs84jycp2It0SsVzGa9oRcmqtYmoJDGCUbdE8Ml'
    oauth_token = '2638839127-niBkABwiXSo4HwNJPc0n0eMVp7AB4cJPIwh3nfN'
    oauth_token_secret = 'PSfT6Pgx3smsRVjRIEkVbnDkH6ngkgQX6iv4luuMRM4nc'

    auth = twitter.oauth.OAuth(oauth_token, oauth_token_secret,
                               consumer_key, consumer_secret)

    # instantiating twitter api to get top #tags and news
    twitter_api = twitter.Twitter(auth=auth)
    in_woe_id = woe_id
    # Prefix ID with the underscore for query string parameterization.
    # Without the underscore, the twitter package appends the ID value
    # to the URL itself as a special case keyword argument.

    country_trends = twitter_api.trends.place(_id=in_woe_id)
    trend_list = country_trends[0].get('trends')
    return [(tag.get('name'), keyword_generator(tag.get('name')))
            for tag in trend_list]


def keyword_generator(hash_tag):
        """
        takes a string hash_tag as argument and returns another string
        which is in searchable form
         """
        new_hash_tag = ''
        if hash_tag[0] == '#':
            hash_tag = hash_tag[1:]
            uppercase = string.ascii_uppercase
            for i in range(len(hash_tag)):
                if hash_tag[i] in uppercase:
                    new_hash_tag += ' '
                new_hash_tag += hash_tag[i]
        else:
            new_hash_tag = hash_tag
        return new_hash_tag.strip()


def get_urls(search_for):
    query = urllib.parse.urlencode({'q': search_for})
    url = 'http://ajax.googleapis.com/ajax/services/search/news?v=1.0&%s'\
          % query
    search_response = urllib.request.urlopen(url)
    search_results = search_response.read().decode('utf8')
    results = json.loads(search_results)
    data = results.get('responseData')
    hits = data.get('results')
    urls = []
    for h in hits:
        urls.append(h['url'])
    return urls


def get_articles(news_url):
    token = 'b123a52fd0d52aa91b4dd97556c82887'  # replace with your own token
    url = ('http://api.diffbot.com/v2/article?token=' +
           token + '&url=' + news_url)
    request = Request(url)
    response = urlopen(request)
    str_res = response.read().decode('utf-8')
    data = json.loads(str_res)
    if data.get('images'):
        return {
            'title': data.get('title'),
            'text': data.get('text'),
            'image_url': data.get('images')[0].get('url'),
            }
    else:
        return {
            'title': data.get('title'),
            'text': data.get('text'),
            }

if __name__ == '__main__':
    india_trends = get_tags(23424848)
    print(json.dumps(india_trends, indent=1))

    for trend in india_trends:
        for key in trend["trends"]:
            print(key["name"])