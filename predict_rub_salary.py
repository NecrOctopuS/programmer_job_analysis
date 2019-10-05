DOLLARS_TO_RUBLES = 65
EUROS_TO_RUBLES = 71


def predict_rub_salary(lower_salary, upper_salary, currency):
    if lower_salary and upper_salary:
        middle_salary = (lower_salary + upper_salary)/2
    elif lower_salary:
        middle_salary = lower_salary * 1.2
    elif upper_salary:
        middle_salary = upper_salary * 0.8
    else:
        return None
    if currency == 'RUR' or currency == 'rub':
        return middle_salary
    elif currency == 'EUR':
        return middle_salary * EUROS_TO_RUBLES
    elif currency == 'USD':
        return middle_salary * DOLLARS_TO_RUBLES
    else:
        return None
