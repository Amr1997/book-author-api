
# Book_Author REST API with JWT

 This is a Django REST API that uses Djoser for JWT authentication.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework
- Djoser

### Installation

1. Clone the repository: `git clone https://github.com/yourusername/your-repo.git`
2. Install dependencies: `pip install -r requirements.txt`
4. Apply database migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## Usage

The API has the following endpoints:

### Authentication

- `POST /auth/token/login/`: Obtain a JWT token by providing a valid username and password
- `POST /auth/token/logout/`: Invalidate the current JWT token

### Users

- `GET /api/users/`: Get a list of all users
- `GET /api/users/:id/`: Get a single user by ID
- `POST /auth/users/create/`: Create a new user
- `PUT /api/users/:id/`: Update an existing user by ID
- `DELETE /api/users/:id/`: Delete a user by ID

### Books

- `GET /api/books/`: Get a list of all books
- `GET /api/books/:id/`: Get a single book by ID
- `POST /api/books/`: Create a new book
- `PUT /api/books/:id/`: Update an existing book by ID
- `DELETE /api/books/:id/`: Delete a book by ID

### Pages

- `GET /api/books/:book_id/pages/`: Get a list of all pages for a book
- `GET /api/books/:book_id/pages/:id/`: Get a single page by ID for a book
- `POST /api/books/:book_id/pages/`: Create a new page for a book
- `PUT /api/books/:book_id/pages/:id/`: Update an existing page by ID for a book
- `DELETE /api/books/:book_id/pages/:id/`: Delete a page by ID for a book

### Example Requests

To obtain a JWT token:

```
POST /auth/token/login/
Content-Type: application/json

{
  "username": "myusername",
  "password": "mypassword"
}
```

To get a list of all pages for a book:

```
GET /api/books/1/pages/
Authorization: JWT your_jwt_token_here
```

To create a new page for a book:

```
POST /api/books/1/pages/
Content-Type: application/json
Authorization: JWT your_jwt_token_here

{
  "number": 5,
  "text": "This is the text for page 5 of book 1."
}
```



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
