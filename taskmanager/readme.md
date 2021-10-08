## Task Manager [React+Django]
this is a simple task manager where user can **Create**, **Read**, **Update** and **Delete** tasks. this Porject is build with react(frontend) which gives the application async power and django(backend)

---
### Tools:
- Backend
    - Django
    - Django Rest-Framework
- Frontend
    - React
---
### REST API
 **API-Overview**
```
http://localhost:8000/api/
```
 **Task-List**
```
http://localhost:8000/api/task-list/
```
 **Create-Task**
```
http://localhost:8000/api/task-create/
```
 **Update-Task**
```
http://localhost:8000/api/task-update/<int:pk>/
```
**Delete-Task**
```
http://localhost:8000/api/task-delete/<int:pk>/
```
---
### Developer Setup:
- Fork this repository.
- Verify if the Django project is working by running the development server.
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```