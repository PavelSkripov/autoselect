import json
import requests
from bs4 import BeautifulSoup
from transliterate import translit, get_available_language_codes, slugify
#from .models import Analog, Sensor


PAGES_COUNT = ['ВБИ-П18В-36УР-1122-С']

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
        mark_norm = mark
        if '.' in mark:
            mark_norm = mark.replace('.', '_') 
        mark_slug = slugify(mark_norm)
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
        techs['Тип датчика'] = sens_type
        data.append(item)
        
        for row in soup.select('.char-table__item'):
            #cols = row.select('char-table__name')
            #cols = [c.text.strip() for c in cols]
            #techs[cols[0]] = cols[1]
            name = row.select_one('.char-table__name').text.strip()
            value = row.select_one('.char-table__value').text.strip()
            techs[name] = value
            data.append(techs)
            #techs = {}
    return induct(techs)

def induct(data):
    x = 0
    if data['Тип корпуса'] == 'Цилиндрический с резьбой':
        data['Тип корпуса'] = 'Цилиндрический резьбовой'
    elif data['Тип корпуса'] == 'Цилиндрический гладкий':
        data['Тип корпуса'] = 'Цилиндрический'
    elif data['Тип корпуса'] == 'Фланцевый':
        data['Тип корпуса'] = 'Прямоугольный'
    if data['Вид подключения'] == 'Разъем M12 × 1':
        data['Вид подключения'] = 'Разъем'
        data['Тип разъема'] = 'М12х1'
    elif 'Кабель с разъемом' in data['Вид подключения']:
        x = data['Вид подключения'].split(' ', 3)
        data['Вид подключения'] = 'Кабель с разъемом'
        data['Тип разъема'] = x[3]
        x = data['Тип разъема'].replace(' ', '')
        data['Тип разъема'] = x
    elif data['Вид подключения'] == 'Клеммная коробка':
        data['Вид подключения'] = 'Клеммы'
    if 'DC' in data['Рабочее напряжение, В']:
        data['Тип напряжения'] = 'DC'
    elif 'AC' in data['Рабочее напряжение, В']:
        data['Тип напряжения'] = 'AC'
    elif 'AC/DC' in data['Рабочее напряжение, В']:
        data['Тип напряжения'] = 'AC/DC'
    if data['Материал корпуса'] == 'Латунь никелированная':
        data['Материал корпуса'] = 'Латунь'
    elif data['Материал корпуса'] == 'Полиамид':
        data['Материал корпуса'] = 'Пластик'
    if '-' in data['Рабочее напряжение, В']:
        x = data['Рабочее напряжение, В'].replace('-', '...') 
        data['Рабочее напряжение, В'] = x
    if ' / L = ' in data['Габаритный размер, мм']:
        x = data['Габаритный размер, мм'].replace(' / L = ', 'х') 
        data['Габаритный размер, мм'] = x
    if ' ' in data['Габаритный размер, мм']:
        x = data['Габаритный размер, мм'].replace(' ', '') 
        data['Габаритный размер, мм'] = x
    if 'Ø ' in data['Размер корпуса']:
        x = data['Размер корпуса'].replace('Ø ', '') 
        data['Размер корпуса'] = x
        x = data['Размер корпуса'].replace(' мм', '')
        data['Размер корпуса'] = x
    elif 'х' in data['Размер корпуса']:
        x = data['Размер корпуса'].split('х')
        data['Размер корпуса'] = x[1]
        x = data['Размер корпуса'].replace(' мм', '')
        data['Размер корпуса'] = x
    if data['Монтажное исполнение'] == 'Утапливаемое':
        data['Монтажное исполнение'] = 'Встраиваемый'
    elif data['Монтажное исполнение'] == 'неутапливаемое':
        data['Монтажное исполнение'] = 'невстраиваемый'
    if data['Функция выхода'] == 'НО':
        data['Функция выхода'] = 'NO'
    elif data['Функция выхода'] == 'НЗ':
        data['Функция выхода'] = 'NC'
    elif data['Функция выхода'] == 'НО/НЗ':
        data['Функция выхода'] = 'NO/NC'
    elif data['Функция выхода'] == 'НО/НЗ прогр.':
        data['Функция выхода'] = 'NO/NC программируемый'
    if '…' in data['Температура окружающей среды']:
        x = data['Температура окружающей среды'].replace(' °С', '')
        x = x.split('…')
        if int(x[0]) >= -30 and int(x[1]) <= 80:
            data['Класс температуры'] = 'Стандартный'
        elif int(x[0]) < -30 and int(x[0]) > -45 and int(x[1]) <= 80:
            data['Класс температуры'] = 'Низкотемпературный'
        elif int(x[0]) < -45:
            data['Класс температуры'] = 'Сверхнизкотемпературный'
        elif int(x[1]) > 80 and int(x[1]) < 105 and int(x[0]) >= -30:
            data['Класс температуры'] = 'Высокотемпературный'
        elif int(x[1]) > 105:
            data['Класс температуры'] = 'Сверхвысокотемпературный'
        else:
            data['Класс температуры'] = 'Широкий темп. диапазон'
    return data
    

def create(marking):
    x = 1
    data = parse_products(marking)
    #analog = Analog.objects.get(marking=marking)
    types = {
            'Индуктивный': ('руб', x),
            'Оптический': ('Euro', x),
            'Емкостный': ('USD', x)
        }
    if data[0]['Тип датчика'] not in types:
            return print('Не найден тип датчика')
        #else: 
            
        






#def main():
    #urls = crawl_products(PAGES_COUNT)
    #data = parse_products(urls)
print(parse_products(PAGES_COUNT))

#if __name__ == '__main__':
    #main()


    