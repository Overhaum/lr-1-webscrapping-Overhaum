import requests
from bs4 import BeautifulSoup
import json


def fetch_wikipedia_page(url):
    # Додавання заголовка User-Agent для імітації запиту з браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Перевірка на помилки HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Сталася помилка при отриманні сторінки: {e}")
        return None


def extract_title(soup):
    title = soup.find('h1', {'id': 'firstHeading'})
    return title.get_text() if title else None


def extract_first_sentence(soup):
    first_paragraph = soup.find('p')
    if first_paragraph:
        text = first_paragraph.get_text()
        sentences = text.split('.')
        return sentences[0] + '.' if sentences else None
    return None


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Дані успішно збережені у {filename}")


def main():
    # Заміна URL на ваш
    url = 'https://uk.wikipedia.org/wiki'
    html_content = fetch_wikipedia_page(url)

    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')

        title = extract_title(soup)
        first_sentence = extract_first_sentence(soup)

        extracted_data = {
            "title": title,
            "first_sentence": first_sentence
        }

        save_to_json(extracted_data, 'extracted_wikipedia_data.json')


if __name__ == "__main__":
    main()
