import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
base_url = 'https://kiev.hh.ua/search/vacancy?area=5&search_period=3&text=python&page=0'


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
