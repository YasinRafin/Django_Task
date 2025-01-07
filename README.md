# Project Management API


## Setup Instructions

1. Clone the repository
   ```
   https://github.com/YasinRafin/Django_Task
   cd Registration_API
   code .
   ``` 

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

``` Visit http://localhost:8000/api/schema/swagger-ui/ for API documentation. ```
