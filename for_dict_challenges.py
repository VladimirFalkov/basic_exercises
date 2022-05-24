# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = [s['first_name'] for s in students]
for i in set(names):
    print(f'{i}: {names.count(i)}')
    
    

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = [s['first_name'] for s in students]
leader_name = " "
leader_count = 0 

for i in set(names):
    if leader_count < names.count(i):
        leader_name = i
        leader_count = names.count(i)


print(f"Самое частое имя среди учеников: {leader_name}")


# Задание 
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for j in range(len(school_students)):
   
    names = [s['first_name'] for s in school_students[j]]
    leader_name = " "
    leader_count = 0 
  
    for i in set(names):
       
        if leader_count < names.count(i):
            leader_name = i
            leader_count = names.count(i)
    print(f"Самое частое имя в классе {j+1}: {leader_name}")
    





# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


for j in school:
    print(f'В классе {j["class"]} ', end="")
    girls = 0
    boys = 0
    for kids in j['students']:
        if is_male.get(kids['first_name']) == False:
            girls +=1
        if is_male.get(kids['first_name']) == True:
            boys +=1
    print(f'девочки {girls}, мальчики {boys}')
    
    #names_kids = [x['first_name'] for x in students_list]





#print(*students_list)

    
#for i in range(len(students_list)):
        
    #names = students_list[i]
        #print(names)
    
   

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

for group in school:
    class_number = group['class']
    girls_total_in_group = 0
    boys_total_in_group = 0

    for kids in group["students"]:
        if is_male.get(kids['first_name']) == True:
            boys_total_in_group +=1
        if is_male.get(kids['first_name']) == False:
            girls_total_in_group +=1

    if boys_total_in_group > girls_total_in_group:
        print(f'Больше всего мальчиков в классе {class_number}')
    else:
        print(f'Больше всего девочек в классе {class_number}')


