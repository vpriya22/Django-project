# Loginify

Django app for user registration, login, and CRUD operations.

## Setup

1.  ```bash
    pip install -r requirements.txt
    python manage.py migrate
    ```

2.  Run server:
    ```bash
    python manage.py runserver
    ```

## Endpoints

- **Get All Users:** `GET /loginify/get-all-data/`
- **Get User by Email:** `GET /loginify/get-single-data/<email>/`
- **Update User:** `PUT /loginify/get-single-data/<email>/`
- **Partial Update User:** `PATCH /loginify/get-single-data/<email>/`
- **Delete User:** `DELETE /loginify/get-single-data/<email>/`
