# Исходные данные: В словаре dict_users_network заданы взаимосвязи (дружба) пользователей социальной сети, где ключ --
# имя пользователя; значение -- список друзей пользователя. Для простоты будем считать, что оношение дружба не
# является биективным, т.е. если у A другом является B, то не обязательно, что у B в друзьях A.
#
# Задания:
# 1.Создайте функцию, определяющую количество друзей у выбранного (каждого) пользователя.
# 2.Создайте функцию, выводящую на экран пользователей, отсортированных по количеству друзей.
# 3.Создайте функцию, определяющую наличие однофамильцев.
# 4.Создайте функцию, определяющую наличие пользователей с одинаковыми инициалами.
# 5.Создайте функцию, возвращающую список уникальных пользователей сети в формате Фамилия И.О..
# 6.Создайте функцию, возвращающую список из уникальных фамилий пользователей сети.

dict_users_network = ({ 
    'С.В. Сидоров': ['П.В. Сидоров', 'И.И. Иванов', 'А.С. Никифоров',
                     'Ф.С. Афеногонов', 'А.К. Парфенов'],
    'П.В. Сидоров': ['С.В. Сидоров', 'А.С. Шебалова', 'М.Л. Кривов'],
    'И.И. Иванов': ['Л.Т. Тимофеев', 'С.В. Сидоров', 'П.В. Сидоров',
                    'М.Л. Кривов'],
    'А.С. Никифоров': ['С.В. Сидоров', 'П.В. Сидоров'],
    'Ф.С. Афеногонов': ['С.В. Сидоров', 'П.В. Сидоров', 'А.К. Парфенов'],
    'А.С. Шебалова': ['Л.Т. Тимофеев'],
    'Л.Т. Тимофеев': ['К.К. Петров', 'А.С. Крылов']
})

def get_friend(dict_user):
    return len(dict_user)

def get_all_user(len_all_user : dict):

    for key, value in len_all_user.items():
        print(f'У пользователя {key} - {len(value)} друзей')

def get_raiting(dict_user : dict):
    dict_int = {}    
    for key, value in dict_user.items():
        dict_int[key] = len(value)
    с = sorted(dict_int.items(), key=lambda x: x[1])    
    for i in с:
        print(i)
    
    return dict_int  

def find_homonym(dict_user : dict):
    a = set()
    b = {}
    for key in dict_user.keys():
        for value in dict_user[key]:
            a.add(value.strip())
    for user in a:
        name, last_name = user.split()
        list_name = []
        for user2 in a.difference(set(user)):
            name2, last_name2 = user2.split()
            if (name != name2) and (last_name == last_name2):
                list_name.append(user2.strip())
        b[user] = list_name
    for i in b.keys(): 
        if len(b[i]) > 0:
            print(f"У пользователя {i} : однофамильцы: {b[i]}")
        else:
            print(f"У пользователя {i} : нет однофамильцев ")    

def find_initials(dict_user : dict):
    a = set()
    b = {}
    for key in dict_user.keys():
        for value in dict_user[key]:
            a.add(value.strip())
    for user in a:
        name, last_name = user.split()
        list_name = []
        for user2 in a.difference(set(user)):
            name2, last_name2 = user2.split()
            if (name == name2) and (last_name != last_name2):# изменил условие (name == name2)
                list_name.append(user2.strip())
        
        b[user] = list_name
    for i in b.keys(): 
        if len(b[i]) > 0:
            print(f"У пользователя {i} : пользователей с одинаковыми инициалами {b[i]}")
        else:
            print(f"У пользователя {i} : нет пользователей с одинаковыми инициалами ")   


def reverse_name_users(dict_user : list):
    a = set()
    list_users = []
    for key in dict_user.keys():
        a.add(key.strip())
        for value in dict_user[key]:
            a.add(value.strip())
    
    for user in a:
        name, last_name = user.split()
        reverse_user = last_name + " " + name
        list_users.append(reverse_user)
    print(list_users)

def get_last_name(dict_user : list):
    a = set()
    list_users = []
    for key in dict_user.keys():
        a.add(key.strip())
        for value in dict_user[key]:
            a.add(value.strip())
    
    for user in a:
        name, last_name = user.split()
        list_users.append(last_name)
    print(f"Фамилии пользователей сайта:{list_users}")
    
       

find_initials(dict_users_network)

