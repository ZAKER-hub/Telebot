import random
import pickle
from bs4 import BeautifulSoup
import requests


def find_all_category():
    category = {}
    page = requests.get(f'https://nekdo.ru/page/')
    b = BeautifulSoup(page.text, "html.parser")
    li = b.find_all('li')
    for j,i in enumerate(li):
        if j > 3 and not j == len(li)-1:
            category[i.a.get('href')] = [i.text]
    return category


def find_max(cat):
    categorys = cat
    try:
        for category in cat:
            sign = 1
            while True:
                page = requests.get(f'https://nekdo.ru{category}{sign}/')
                b = BeautifulSoup(page.text, "html.parser")
                list_a = b.find_all('a', {'class': 'nav'})
                list_a_sel = b.find_all('a', {'class': 'sel'})
                list_a_text = []
                for i in list_a:
                    list_a_text.append(int(i.text))
                for i in list_a_sel:
                    if i.text.isnumeric():
                        list_a_text.append(int(i.text))

                max_page = max(list_a_text)
                if max_page == sign:
                    categorys[category].append(max_page)
                    break
                else:
                    sign = max_page
    except:
        pass

    return categorys


def get_category():
    while True:
        try:
            with open('category_dict', 'rb') as f:
                dict_category = pickle.load(f)
                break

        except:
            with open('category_dict', 'wb') as f:
                pickle.dump(find_max(find_all_category()), f)

    if dict_category:
        return dict_category


def get_random_anegdot(sign=random.randint(1, 3161)):
    all_anecdots = []
    page = requests.get(f'https://nekdo.ru/page/{sign}/')
    b = BeautifulSoup(page.text, "html.parser")
    divs = b.find_all('div', {"class": "text"})
    for i in divs:
        all_anecdots.append(i.text)
    return random.choice(all_anecdots)


def get_random_from_category(category, categorys):
    all_anecdots = []
    page = requests.get(f'https://nekdo.ru{category}{random.randint(1, categorys[category][1])}/')
    b = BeautifulSoup(page.text, "html.parser")
    divs = b.find_all('div', {"class": "text"})
    for i in divs:
        all_anecdots.append(i.text)
    return random.choice(all_anecdots)


def get_random_image(categorys):
    all_image = []
    page = requests.get(f'https://nekdo.ru/image/{random.randint(1, categorys["/image/"][1])}/')
    b = BeautifulSoup(page.text, "html.parser")
    links = b.find_all('a', {'target': '_blank'})
    for a in links:
        all_image.append(a.get('href'))
    return 'https://nekdo.ru'+random.choice(all_image)
