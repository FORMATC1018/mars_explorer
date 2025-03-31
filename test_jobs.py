from requests import get, post

#print(get('http://localhost:5000/api/jobs').json())
#print(get('http://localhost:5000/api/jobs/1').json())
#print(get('http://localhost:5000/api/jobs/500').json())
#print(get('http://localhost:5000/api/jobs/sdsd').json())
print(post('http://localhost:5000/api/jobs/',
           json={'job': 'test',
                 'team_leader': 1,
                 'work_size': 5,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())