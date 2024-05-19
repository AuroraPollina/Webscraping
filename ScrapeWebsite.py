from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'html.parser')
xml_content = soup.prettify()

# pagination
pagination = soup.find('ul',class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = page[-2].text

links = []

for page in range(1, int(last_page)+1): #to limit pages add [:2] in front of colon
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')
    xml_content = soup.prettify()


    box = soup.find('article', class_='main-article')


    for link in box.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
            print(link)
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'html.parser')

            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            transcipt = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
            # Open file in utf-8 encoding
            with open(f'{title}.txt', 'w', encoding='utf-8') as file:
                file.write(transcipt)

        except:
            print('Link not working')
            print(link)


