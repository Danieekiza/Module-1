# averege score
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_alp = list(students) # создадим список из множества students
students_alp.sort() # упорядочим список имен в алфавитном порядке
dict_stud = dict(zip(students_alp, grades)) # создадим словарь методом zip
aver_score_0 = sum(grades[0])/len(grades[0]) # среднее значение по отдельному ученику
aver_score_1 = sum(grades[1])/len(grades[1])
aver_score_2 = sum(grades[2])/len(grades[2])
aver_score_3 = sum(grades[3])/len(grades[3])
aver_score_4 = sum(grades[4])/len(grades[4])
dict_stud[students_alp[0]] = aver_score_0 # замена списка оценок на среднее значение по отдельному ученику
dict_stud[students_alp[1]] = aver_score_1
dict_stud[students_alp[2]] = aver_score_2
dict_stud[students_alp[3]] = aver_score_3
dict_stud[students_alp[4]] = aver_score_4
print(dict_stud)
# Не очень правильно создавать отдельную переменную для каждого ученика.
# Но с учетом того, что учеников в классе около 2‑х десятков и численность их за год не меняется,
# то программу можно использовать, заменяя в ней только список оценок.
# Правда работать будет только для одного отдельного класса.
# Как автоматизировать процесс без циклов не вижу способов.
