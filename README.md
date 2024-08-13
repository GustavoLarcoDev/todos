# To-Do App

This is a To-Do list application project developed with Django. The application allows users to create, view, update, and delete task lists and their associated items.

## Features

- **Task Lists**: You can create and manage multiple task lists.
- **Task Items**: Within each list, you can add, view, update, or delete items.
- **User Interface**: The application uses HTML and CSS for the presentation of the views.
- **CRUD Operations**: Full support for CRUD (Create, Read, Update, Delete) operations for lists and items.

## Requirements

- Python 3.x
- Django 4.x

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your_repository
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the database migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and visit `http://127.0.0.1:8000/` to see the application in action.

## Usage

- **Home Page**: Displays a list of all task lists.
- **List Details**: Click on a list to view the items it contains.
- **Create New List**: You can create a new list from the home page.
- **Add Items**: Once in the list details view, you can add new items.
- **Update Items or Lists**: Edit the name of an existing list or item.
- **Delete Items or Lists**: Delete any list or item you no longer need.

## Project Structure

```
|-- manage.py
|-- myproject/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- todo/
|   |-- migrations/
|   |-- templates/
|   |-- static/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|   |-- forms.py
```

- **`myproject/`**: Contains the Django project’s configuration files.
- **`todo/`**: Contains the "To-Do" application with models, views, templates, and static files.

## Contributing

Feel free to fork this project and submit pull requests with improvements or new features.
