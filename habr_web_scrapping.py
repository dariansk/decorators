import requests
from bs4 import BeautifulSoup
from my_decorator import logger


@logger('log.txt')
def habr_preview(key_words, file='articles.txt'):

    # получаем страницу с самыми свежими постами с Хабра
    response = requests.get('https://habr.com/ru/all/')
    if not response.ok:
        raise ValueError('no response')

    soup = BeautifulSoup(response.text, features='html.parser')

    # извлекаем посты
    posts = soup.find_all('article', class_='post')
    for post in posts:
        post_id = post.parent.attrs.get('id')
        # если идентификатор не найден, это что-то странное, пропускаем
        if not post_id:
            continue
        # извлекаем превью из поста
        preview = post.find('div', class_='post__body post__body_crop')
        preview_lower = preview.text.lower()
        # ищем вхождение хотя бы одного ключевого слова
        for keyword in key_words:
            if preview_lower.find(keyword) != -1:
                title_element = post.find('a', class_='post__title_link')
                date_element = post.find('span', class_='post__time')
                with open(file, 'a') as new_file:
                    new_file.write(f"{date_element.text} - {title_element.text} - {title_element.attrs.get('href')}\n")
                break
    return file
