import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# Страна, Город, Вакансия
print('city')
name_city = input()

url_https = 'https://'
url_country = str('ua') + '/search/vacancy?'
url_city = name_city + '.hh.'
url_area = 'area=' + str(5) + '&'
url_period = 'search_period=' + str(3) + '&'
url_vacancy = 'text=' + str('python') + '&'
url_page = 'page=' + str(0)
base_url = url_https + url_city + url_country + url_area + url_period + url_vacancy + url_page


def hh_parse(base_url, headers):
    jobs = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div',
                             attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a',
                             attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a',
                            attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a',
                               attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            content = div.find('div',
                               attrs={'data-qa': 'vacancy-serp__vacancy_requirement'})
            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'content': content
            })
            # print(soup)
            # print(len(divs))
            print(len(jobs), end=') ')
            print(title)
            print(company)
            print(href + '\n\n')
    else:
        print('ERROR')


hh_parse(base_url, headers)
