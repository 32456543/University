import random

from random import *


def birthday(count_groups, count_tipov_in_group):
    true_statement = 0  
    for l in range(count_groups):  
        k = 0  
        birthdays = [[randint(1, 28), randint(1, 12)] for x in range(count_tipov_in_group)]  
        # flag = False
        for i in range(count_tipov_in_group - 1):  
            for j in range(i + 1, count_tipov_in_group):  
                if birthdays[i] == birthdays[j]:  
                    k += 1
                    '''true_statement += 1 
                     flag = True 
                     print(birthdays)
                    break
            if flag == True:
                break'''
        if k > 0:  
            true_statement += 1
    return f"{int((true_statement / count_groups) * 100)} %"

 print(f"Парадокс дней рождения в группе из 23 человек среди 10000 экспериментов: {birthday(10000, 23)}")
 print(f"Парадокс дней рождения в группе из 60 человек среди 10000 экспериментов: {birthday(10000, 60)}")