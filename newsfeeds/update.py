from newsfeeds.models import Country, News
from .get_trending_tags import get_articles, get_urls, get_tags

all_countries = [country for country in Country.objects.all()]
all_countries.sort(key=lambda x: x.code)
list_1 = all_countries[:5]
list_2 = all_countries[5:10]
list_3 = all_countries[10:15]
list_4 = all_countries[15:]


def update(country_list):
    for country in country_list:
        keywords = get_tags(country.code)
        for k_word in keywords:
            urls = get_urls(k_word[1])
            if urls:
                article = get_articles(urls[0])
                if not article.get('errorCode'):
                    news = News(
                        tag=k_word[0],
                        heading=article.get('title'),
                        body=article.get('text'),
                        link=urls[0],
                        country=country,
                        image_url=article.get('image_url', ''),
                        )
                    news.save()
                    print('New news added: ', news.heading)
        print('Updated tweets of ' + country.name)


def update_1():
    update(list_1)


def update_2():
    update(list_2)


def update_3():
    update(list_3)


def update_4():
    update(list_4)
