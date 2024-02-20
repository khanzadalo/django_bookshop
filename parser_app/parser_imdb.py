import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

URL = 'https://www.imdb.com/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
}


# start
@csrf_exempt
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


# get data
@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div',
                          class_="ipc-poster-card ipc-poster-card--baseAlt ipc-poster-card--dynamic-width top-picks-title ipc-sub-grid-item ipc-sub-grid-item--span-2")
    imdb_list = []
    for item in items:
        imdb_list.append({
            'title': item.find('div', class_="title").get_text(),
            'rating': item.find('div',
                                class_="ipc-rating-star ipc-rating-star--baseAlt ipc-rating-star--imdb ipc-rating-star-group--imdb").get_text(),
            'image': URL + item.find('div',
                                     class_="ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--baseAlt ipc-media--poster-m ipc-poster__poster-image poster-card-image ipc-media__img").find('img').get('src'),
        })
    return imdb_list


# parsing
@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        imdb_list_all_films = []
        for page in range(0, 1):
            html = get_html(f'https://www.imdb.com/what-to-watch/top-picks/?ref_=hm_tpks_sm', params=page)
            imdb_list_all_films.extend(get_data(html.text))
            print(imdb_list_all_films)
    else:
        raise Exception('error in parse')

#
# print(parser())