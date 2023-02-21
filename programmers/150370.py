
'''
["A 6", "B 12", "C 3"]

["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
'''


def add_months(today, expiration_period_month):
    year, month, days = map(int, today.split('.'))
    return year*12*28 + month * 28 + days-int(expiration_period_month)*28


def convert_days(reg_date):
    year, month, days = map(int, reg_date.split('.'))
    return year*12*28 + month * 28 + days


def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    for term in terms:
        term_type, expiration_period_month = term.split()
        terms_dict[term_type] = int(add_months(today, expiration_period_month))
    for privacy_idx in range(len(privacies)):
        reg_dte, term = privacies[privacy_idx].split()
        if convert_days(reg_dte) <= terms_dict[term]:
            answer.append(privacy_idx+1)
   
    return answer


