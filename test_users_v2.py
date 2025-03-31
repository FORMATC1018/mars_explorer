from requests import get, post, delete

print(1, get('http://localhost:5000/api/v2/users').json())
print(2, get('http://localhost:5000/api/v2/users/2').json())
print(3, get('http://localhost:5000/api/v2/users/52').json())  # нет пользователя
print(4, get('http://localhost:5000/api/v2/users/q').json())  # не число

print(5, post('http://localhost:5000/api/v2/users', json={}).json())  # нет словаря
print(6, post('http://localhost:5000/api/v2/users', json={'name': 'Sonya'}).json())  # не все поля
print(7, post('http://localhost:5000/api/v2/users', json={'name': 'VOVA', 'position': 'senior programmer',
                                                       'surname': 'PILOTOV', 'age': 35, 'address': 'module_3',
                                                       'speciality': 'computer sciences',
                                                       'hashed_password': 'pil', 'email': 'pilotov@mars.org'}).json())

print(8, delete('http://localhost:5000/api/v2/users/999').json())  # id = 999 нет в базе
# print(delete('http://localhost:5000/api/v2/users/10').json())
