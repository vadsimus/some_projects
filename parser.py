import requests
from bs4 import BeautifulSoup as bs


def hh_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('ok')
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        vacancies = []
        for div in divs:
            vacancy = {}
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            text1 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            text2 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            text = text1 + text2
            vacancy['title'] = title
            vacancy['href'] = href
            vacancy['company'] = company
            vacancy['text'] = text
            vacancies.append(vacancy)
        return vacancies
    else:
        return None


def print_vac(vacancies):
    for vacancy in vacancies:
        if len(vacancy['title']) > 19:
            vacancy['title'] = vacancy['title'][:20]
        if len(vacancy['company']) > 19:
            vacancy['company'] = vacancy['company'][:20]

        print('{:^20}'.format(vacancy['title']), '|',
              '{:^20}'.format(vacancy['company']), '|',
              vacancy['href'], '|',
              vacancy['text'])


if __name__ == '__main__':
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    search_line = input('Search vacancy:')
    base_url = 'https://nn.hh.ru/search/vacancy?area=66&st=searchVacancy&text={}'.format(search_line)
    vac = hh_parse(base_url, headers)
    if vac:
        print_vac(vac)
    else:
        print('Error')
