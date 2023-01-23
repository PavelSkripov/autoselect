import json
import requests
from bs4 import BeautifulSoup
from transliterate import translit, get_available_language_codes, slugify


PAGES_COUNT = ['ВБИ-П18В-36У-1111-С']

def get_soup(url, **kwargs):
    response = requests.get(url, **kwargs)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features='html.parser')
    else:
        soup = None
    return soup


#def crawl_products(pages_count):
#    urls = []
#    fmt = 'https://sensor-com.ru/sensors/{marking}'

#    for page_n in range(1, 1 + pages_count):
#        print('page: {}'.format(page_n))

#        page_url = fmt.format(marking=page_n)
#        soup = get_soup(page_url)
#        if soup is None:
#            break

#        for tag in soup.select('.product-card .title'):
#            href = tag.attrs['href']
#            url = 'https://parsemachine.com{}'.format(href)
#            urls.append(url)

#    return urls

def urls_list(markings):
    urls = []
    print(f'markings = {markings}')
    fmt = 'https://sensor-com.ru/sensors/{marking}'
    for mark in markings:
        print(f'mark = {mark}')
        mark_slug = slugify(mark)
        print(f'mark_slug = {mark_slug}')
        page_url = fmt.format(marking=mark_slug)
        print('product: {}'.format(mark))
        soup = get_soup(page_url)
        if soup is None:
            print(f'status_code != 200')
            break

        urls.append(page_url)
    return urls


def parse_products(markings):
    data = []
    urls = urls_list(markings)
    for url in urls:
        print('url: {}'.format(url))
        soup = get_soup(url)
        if soup is None:
            break

        techs = {}
        item = {}
        type = soup.select_one('.product-page__intro.for-desktop').text.strip()
        sens_type = type.split(' ')[0]
        item['Тип датчика'] = sens_type
        data.append(item)
        
        for row in soup.select('.char-table__item'):
            #cols = row.select('char-table__name')
            #cols = [c.text.strip() for c in cols]
            #techs[cols[0]] = cols[1]
            name = row.select_one('.char-table__name').text.strip()
            value = row.select_one('.char-table__value').text.strip()
            techs[name] = value
            data.append(techs)
            techs = {}
        
    return data

def main():
    #urls = crawl_products(PAGES_COUNT)
    #data = parse_products(urls)
    print(parse_products(PAGES_COUNT))

if __name__ == '__main__':
    main()


    