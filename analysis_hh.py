import requests
import predict_rub_salary

POPULAR_PROGRAMMING_LANGUAGES = [
    'TypeScript',
    'Swift',
    'Scala',
    'Objective-C',
    'Shell',
    'Go',
    'C',
    'C#',
    'C++',
    'PHP',
    'Ruby',
    'Python',
    'Java',
    'JavaScript'
]


def analys_programmer_job():
    hh_url = 'https://api.hh.ru/vacancies'
    programmer_job_analysis = {}
    for language in POPULAR_PROGRAMMING_LANGUAGES:
        page = 0
        pages_number = 1
        vacancies = []
        hh_params = {
            'text': f'Программист {language}',
            'area': 1,
            'period': 30,
        }
        response = requests.get(hh_url, params=hh_params)
        vacancies_found = response.json()['found']
        while page < pages_number:
            hh_params['page'] = page
            response = requests.get(hh_url, params=hh_params)
            vacancies_on_page = response.json()['items']
            vacancies += vacancies_on_page
            pages_number = response.json()['pages']
            page += 1
        vacancies_processed = 0
        total_processed_salary = 0
        for vacancy in vacancies:
            if vacancy['salary'] is not None:
                lower_salary, upper_salary, currency, _ = vacancy['salary'].values()
                vacancies_processed += 1
                total_processed_salary += predict_rub_salary.predict_rub_salary(lower_salary, upper_salary, currency)
        if vacancies_processed:
            average_salary = int(total_processed_salary / vacancies_processed)
        else:
            average_salary = 0
        programmer_job_analysis[language] = {
            "vacancies_found": vacancies_found,
            "vacancies_processed": vacancies_processed,
            "average_salary": average_salary
        }
    return programmer_job_analysis
