import analysis_superjob
import analysis_hh
from terminaltables import AsciiTable


def print_table(programmer_job_analysis, title):
    table_data = [['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]
    for language in programmer_job_analysis:
        language_data = []
        language_data.append(language)
        for values in programmer_job_analysis[language]:
            language_data.append(programmer_job_analysis[language][values])
        table_data.append(language_data)
    table_instance = AsciiTable(table_data, title)
    print(table_instance.table)
    print()


def main():
    title_hh = 'HeadHunter Moscow'
    title_sj = 'SuperJob Moscow'
    sj_dict = analysis_superjob.analys_programmer_job()
    hh_dict = analysis_hh.analys_programmer_job()
    print_table(sj_dict, title_sj)
    print_table(hh_dict, title_hh)


if __name__ == '__main__':
    main()
