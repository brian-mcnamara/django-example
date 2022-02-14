# Example server

Create virtual environment:  
`python3 -m venv .venv`

Install requirements:  
`pip install -r requirements.txt`

Create superuser:  
`python manage.py createsuperuser`

Run migrations:  
`python manage.py makemigrations`
`python manage.py migrate`

Run server:
`python manage.py runserver`

Navigate to:  
http://localhost:8000 or http://localhost:8000/nodes to see node api