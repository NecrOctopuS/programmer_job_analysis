import requests


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

VERSION = '2.27'


def predict_rub_salary(vacancie):
    lower_salary = vacancie['payment_from']
    upper_salary = vacancie['payment_to']
    currency = vacancie['currency']
    if lower_salary and upper_salary:
        middle_salary = (lower_salary + upper_salary) / 2
    elif lower_salary:
        middle_salary = lower_salary * 1.2
    elif upper_salary:
        middle_salary = upper_salary * 0.8
    else:
        return None
    if currency == 'rub':
        return middle_salary
    else:
        return None


def analys_programmer_job(SUPERJOB_SECRET_KEY):
    programmer_job_analysis = {}
    method_name = 'vacancies'
    sj_url = f'https://api.superjob.ru/{VERSION}/{method_name}/'
    header = {'X-Api-App-Id': SUPERJOB_SECRET_KEY}
    for language in POPULAR_PROGRAMMING_LANGUAGES:
        sj_params = {
            'X-Api-App-Id': SUPERJOB_SECRET_KEY,
            'keywords': [[1, '', language], [3, '', language]],
            'town': 'Москва',
            'catalogues': 48
        }
        page = 0
        pages_number = 1
        vacancies = []
        response = requests.get(sj_url, headers=header, params=sj_params)
        vacancies_found = response.json()['total']
        while page < pages_number:
            sj_params['page'] = page
            response = requests.get(sj_url, headers=header, params=sj_params)
            vacancies_on_page = response.json()['objects']
            vacancies += vacancies_on_page
            if response.json()['more']:
                page += 1
            else:
                break
        vacancies_processed = 0
        total_processed_salary = 0
        for vacancie in vacancies:
            if predict_rub_salary(vacancie):
                vacancies_processed += 1
                total_processed_salary += predict_rub_salary(vacancie)
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
