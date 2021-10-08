## Expense Tracker [Js+Django]
Expense tracker build with django rest-api and async javascript with CRUD functionalities. this Porject is build with async javascript(frontend) and django rest-api(backend)

---
### Tools:
- Backend
    - Django
    - Django Rest-Framework
- Frontend
    - React
---
### REST API
**Expenses**
```
http://localhost:8000/api/expense-list/
```
**Add-Expense**
```
http://localhost:8000/api/expense-add/
```
**Update-Expense**
```
http://localhost:8000/api/expense-update/<int:pk>/
```
**Delete-Expense**
```
http://localhost:8000/api/expense-delete/<int:pk>/
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