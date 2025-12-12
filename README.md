# 📘 README - Midterm Final Checklist

This README **must remain in your repository** and **must be fully completed** before submitting the midterm.

---

## 1. API Test Coverage Table

Fill in the second column with the **name of the student** who implemented and tested each API.

| # | API Endpoint / Feature | Implemented & Tested By (Student Name) |
|---|------------------------|-----------------------------------------|
| 1 | Create Short Link - **POST /urls** | Saleh Sabagh |
| 2 | Redirect to Original URL - **GET /u/{code}** | Saleh Sabagh |
| 3 | Get All Shortened Links - **GET /urls** | Saleh Sabagh |
| 4 | Delete Short Link - **DELETE /urls/{code}** | Saleh Sabagh |

---

## 2. Code Generation Method (Section 6.4)

Check the method you used to generate the short code:

- [x] **1. Random Generation**
- [ ] **2. ID → Base62 Conversion**
- [ ] **3. Hash-based Generation**

**Implementation Details:**
The short code is generated using random selection from a combined alphabet of ASCII letters (uppercase and lowercase) and digits. The generation process includes:
- Alphabet: `string.ascii_letters + string.digits` (62 characters)
- Default length: 6 characters
- Uniqueness: Verified against existing codes with retry mechanism (up to 5 attempts)
- Location: `app/services/url_service.py` → `generate_short_code()` function

---

## 3. Bonus User Story: TTL (Expiration Time) for Shortened Links

If you implemented the bonus user story, mark the box and complete the required details.

- [ ] **TTL Feature Implemented**

**If checked, fill in the following information:**

- **ENV variable or config key used:** `N/A` (Not yet implemented)
- **Location of TTL Logic (File + Function):** `N/A`
- **How TTL cleanup is triggered:** `N/A`

---

## 4. Postman Collection (Required)

A **Postman Collection** has been created and includes all four API routes:

- **POST /urls** - Create Short Link
- **GET /u/{code}** - Redirect to Original URL
- **GET /urls** - Get All Shortened Links
- **DELETE /urls/{code}** - Delete Short Link

### Screenshots (included in GitHub)

For each route, two screenshots have been added:
- Successful response (2xx)
- Error-handled response (4xx)

Screenshots are located in:
```
/postman
```

### Naming Convention Example:

```
postman/
├── post-urls-201-success.png
├── post-urls-400-invalid-url.png
├── get-u-code-302-redirect.png
├── get-u-code-404-not-found.png
├── get-urls-200-success.png
├── delete-urls-code-200-success.png
└── delete-urls-code-404-not-found.png
```

Filenames clearly show:
- Route
- HTTP status
- Success or error

---

## Project Structure

```
url-shortener/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── url_router.py          # API endpoints
│   ├── core/
│   │   ├── config.py              # Configuration settings
│   │   ├── db.py                  # Database setup
│   │   └── deps.py                # Dependency injection
│   ├── models/
│   │   ├── __init__.py
│   │   └── url_model.py           # SQLAlchemy URL model
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── url_repository.py      # Database operations
│   ├── schemas/
│   │   └── url_schema.py          # Pydantic schemas
│   ├── services/
│   │   ├── __init__.py
│   │   └── url_service.py         # Business logic
│   ├── __init__.py
│   └── main.py                    # FastAPI app entry point
├── alembic/                       # Database migrations
├── .env                           # Environment variables (local)
├── .env.example                   # Environment template
├── pyproject.toml                 # Project dependencies
├── alembic.ini                    # Alembic configuration
└── README.md                      # This file
```

---

## Tech Stack

- **Framework:** FastAPI
- **Web Server:** Uvicorn
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Validation:** Pydantic v2
- **Environment:** Python 3.11+

---

## Setup Instructions

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Configure environment:**
   - Copy `.env.example` to `.env`
   - Update database credentials as needed

3. **Run database migrations:**
   ```bash
   poetry run alembic upgrade head
   ```

4. **Start the development server:**
   ```bash
   poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access API documentation:**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

---

## API Endpoints

### 1. Create Short Link
**POST** `/urls`

Request:
```json
{
  "original_url": "https://example.com/very/long/url"
}
```

Response (201):
```json
{
  "status": "success",
  "data": {
    "url": {
      "id": 1,
      "original_url": "https://example.com/very/long/url",
      "short_code": "abc123",
      "created_at": "2025-12-12T10:00:00"
    }
  }
}
```

### 2. Redirect to Original URL
**GET** `/u/{code}`

Response (302): Redirects to the original URL

### 3. Get All Shortened Links
**GET** `/urls`

Response (200):
```json
{
  "status": "success",
  "data": {
    "urls": [
      {
        "id": 1,
        "original_url": "https://example.com/very/long/url",
        "short_code": "abc123",
        "created_at": "2025-12-12T10:00:00"
      }
    ]
  }
}
```

### 4. Delete Short Link
**DELETE** `/urls/{code}`

Response (200):
```json
{
  "status": "success",
  "message": "URL deleted successfully"
}
```

---

✔️ **This README is fully completed and ready for submission.**
