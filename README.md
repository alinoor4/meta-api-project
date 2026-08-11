# Little Lemon Restaurant API

A fully functional RESTful back-end API for the **Little Lemon** restaurant, built as the final project for the **APIs course** in the [Meta Back-End Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer).

The API powers menu and category management, customer carts, and role-based user groups — all secured with token authentication.

---

## Features

- **Token authentication** — user registration, login, and logout via Djoser + DRF auth tokens
- **Menu & category management** — full CRUD for menu items and categories
- **Cart system** — add items by name, unit prices snapshot automatically, duplicate items merge and re-total, one-call cart clearing
- **Role management** — list, assign, and remove users from groups (e.g. `Manager`, `Delivery crew`)
- **Filtering, search, ordering & pagination** on menu items
- **Multiple renderers** — JSON, XML, and the browsable API out of the box

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.14 |
| Framework | Django + Django REST Framework |
| Auth | Djoser + DRF Token Authentication |
| Filtering | django-filter |
| Renderers | JSON, XML (`djangorestframework-xml`), Browsable API |
| Database | SQLite |
| Dependency management | Pipenv |

---

## Getting Started

### Prerequisites

- Python 3.14 (as pinned in the `Pipfile`)
- [Pipenv](https://pipenv.pypa.io/)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/alinoor4/meta-api-project.git
cd meta-api-project

# 2. Install dependencies & activate the virtual environment
pipenv install
pipenv shell

# 3. Apply migrations
python manage.py migrate

# 4. Create an admin user
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
```

The API is now live at `http://127.0.0.1:8000/`.

---

## Authentication

Authentication is handled by **Djoser** under the `/auth/` prefix.

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/users/` | Register a new user |
| `GET` | `/auth/users/me/` | Get the current user |
| `POST` | `/auth/token/login/` | Obtain an auth token |
| `POST` | `/auth/token/logout/` | Revoke the auth token |

Include the token on protected requests:

```
Authorization: Token <your-token>
```

---

## API Endpoints

All application endpoints live under the `/api/` prefix.

### Categories

| Method | Endpoint | Access | Description |
|---|---|---|---|
| `GET` | `/api/category` | Public | List all categories |
| `POST` | `/api/category` | Authenticated | Create a category |
| `GET / PUT / PATCH / DELETE` | `/api/category/{id}` | Authenticated | Retrieve, update, or delete a category |

### Menu Items

| Method | Endpoint | Access | Description |
|---|---|---|---|
| `GET` | `/api/menu-items` | Public | List menu items (filterable, searchable, paginated) |
| `POST` | `/api/menu-items` | Authenticated | Create a menu item |
| `GET / PUT / PATCH / DELETE` | `/api/menu-items/{id}` | Authenticated | Retrieve, update, or delete a menu item |

### Cart

| Method | Endpoint | Access | Description |
|---|---|---|---|
| `GET` | `/api/cart/menu-items` | Authenticated | View the current user's cart |
| `POST` | `/api/cart/menu-items` | Authenticated | Add an item (by title) — re-adding an item bumps its quantity and re-totals the price |
| `DELETE` | `/api/cart/menu-items` | Authenticated | Clear the entire cart |

### User Groups

| Method | Endpoint | Access | Description |
|---|---|---|---|
| `GET` | `/api/groups/{group_name}/users` | Authenticated | List users in a group |
| `POST` | `/api/groups/{group_name}/users` | Authenticated | Assign a user to a group |
| `DELETE` | `/api/groups/{group_name}/users/{id}` | Authenticated | Remove a user from a group |

---

## Filtering, Search, Ordering & Pagination

`GET /api/menu-items` supports the following query parameters:

| Parameter | Example | Description |
|---|---|---|
| `category` | `?category=desserts` | Filter by category title (case-insensitive) |
| `search` | `?search=lemon` | Search item and category titles |
| `ordering` | `?ordering=-price` | Sort by price (`price` asc, `-price` desc) |
| `page` | `?page=2` | Paginate results (5 items per page) |

**Example:**

```
GET /api/menu-items?category=main&ordering=-price&page=1
```

---

## Project Structure

```
meta-api-project/
├── LittleLemonAPI/     # Project config — settings, root URLconf, WSGI/ASGI
├── LemonAPI/           # Core app — models, views, serializers, filters
│   ├── models.py       # Category, MenuItem, Cart, Order, OrderItem
│   ├── views.py        # Class-based & generic API views
│   ├── serializers.py  # DRF serializers (incl. cart merge logic)
│   ├── filters.py      # Custom django-filter FilterSet
│   └── urls.py         # App routes
├── manage.py
├── Pipfile
└── Pipfile.lock
```

## Acknowledgments

Built as part of the **APIs** course in the Meta Back-End Developer Professional Certificate on Coursera. The Little Lemon restaurant is Meta's fictional brand used throughout the program.
