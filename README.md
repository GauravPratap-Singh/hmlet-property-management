# Property Management System API

A REST API for a Property Management System built with **Django + Django REST Framework**, using **JWT authentication**. Staff users can register/log in, manage Properties and their Units, register Members (tenants), and create Contracts that link a Member to a Unit — with automatic double-booking prevention, total contract value calculation, and unit status sync.

## Tech stack

- Python 3.10
- Django 5.2 + Django REST Framework
- PostgreSQL (via `dj-database-url`)
- JWT auth via `djangorestframework-simplejwt`

## Project structure

The project is organized domain-first, one Django app per entity:

```
hmlet_backend/
├── apps/
│   ├── users/        # staff auth (register/login, JWT)
│   ├── properties/   # properties
│   ├── units/        # units (nested under a property)
│   ├── members/      # tenants
│   └── contracts/    # member <-> unit contracts
├── models/base.py    # BaseModel: is_active, created_at/by, updated_at/by
├── utils/            # shared response envelope helpers
├── settings/
└── urls.py           # root URL config, mounts each app's api/v1/urls.py
```

Each app follows the same internal layout: `models/{requests,responses,entities}` (plain data classes), `serializers/{requests,responses,entities}` (DRF (de)serialization), `impl/` (business logic), and a `*_views.py` (thin DRF `ViewSet` that wires request → impl → response).

## Setup — running on localhost

### 1. Prerequisites

- Python 3.10+
- A running PostgreSQL server (SQLite also works if you'd rather not stand up Postgres — see note below)

### 2. Clone and create a virtualenv

```bash
git clone <this-repo-url>
cd hmlet
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements/development.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```bash
DATABASE_URL=postgres://<user>:<password>@localhost:5432/<db_name>
```


Make sure the database in the URL already exists (Postgres does not auto-create it):

```bash
createdb <db_name>
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for `/admin`)

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

The API is now available at `http://127.0.0.1:8000/`.

## Authentication

Every endpoint except `register`/`login` requires a JWT access token:

```
Authorization: Bearer <access_token>
```

Get a token via `POST /api/auth/register` or `POST /api/auth/login` (see below). Access tokens last 60 minutes; refresh tokens last 7 days (`POST /api/auth/refresh/` exchanges a refresh token for a new access token).

All users created via `/register` are staff (`is_staff=True`) — there is no separate non-staff account type in this system; **Members** (tenants) are a plain data record, not an authenticatable account.

## Response envelope

Every endpoint returns the same shape:

```json
{
  "message": "human-readable status message",
  "reason_code": 200,
  "data": { }
}
```

---

## API Reference

### Auth

#### `POST /api/auth/register`

```json
// Request
{
  "username": "readme_admin",
  "email": "readme_admin@example.com",
  "password": "ReadmePass123!",
  "first_name": "Readme",
  "last_name": "Admin"
}
```

```json
// 201 Response
{
  "message": "User registered successfully",
  "reason_code": 201,
  "data": {
    "user": {
      "id": 2,
      "username": "readme_admin",
      "email": "readme_admin@example.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2026-09-12T02:25:19.453689Z"
    },
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

#### `POST /api/auth/login`

```json
// Request
{
  "username": "readme_admin",
  "password": "ReadmePass123!"
}
```

```json
// 200 Response
{
  "message": "Login successful",
  "reason_code": 200,
  "data": {
    "user": {
      "id": 2,
      "username": "readme_admin",
      "email": "readme_admin@example.com",
      "is_staff": true,
      "is_active": true,
      "date_joined": "2026-09-12T02:25:19.453689Z"
    },
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

---

### Properties

#### `POST /api/properties`

```json
// Request
{
  "property_name": "Sunset Apartments",
  "address_line1": "123 Main St",
  "postcode": "560001",
  "country": "India"
}
```

```json
// 201 Response
{
  "message": "Property created successfully",
  "reason_code": 201,
  "data": {
    "property": {
      "id": 2,
      "is_active": true,
      "created_by": 2,
      "updated_by": null,
      "property_name": "Sunset Apartments",
      "address_line1": "123 Main St",
      "address_line2": null,
      "postcode": "560001",
      "country": "India"
    }
  }
}
```

#### `GET /api/properties`

```json
// 200 Response
{
  "message": "Properties fetched successfully",
  "reason_code": 200,
  "data": {
    "properties": [
      {
        "id": 2,
        "is_active": true,
        "created_by": 2,
        "updated_by": null,
        "property_name": "Sunset Apartments",
        "address_line1": "123 Main St",
        "address_line2": null,
        "postcode": "560001",
        "country": "India"
      }
    ]
  }
}
```

#### `GET /api/properties/:property_id`

Embeds the property's units.

```json
// 200 Response
{
  "message": "Property fetched successfully",
  "reason_code": 200,
  "data": {
    "property": {
      "id": 2,
      "units": [
        {
          "id": 2,
          "is_active": true,
          "created_by": 2,
          "updated_by": null,
          "unit_number": "101",
          "monthly_rent": "1500.00",
          "status": "available",
          "properties": 2
        }
      ],
      "is_active": true,
      "created_by": 2,
      "updated_by": null,
      "property_name": "Sunset Apartments",
      "address_line1": "123 Main St",
      "address_line2": null,
      "postcode": "560001",
      "country": "India"
    }
  }
}
```

```json
// 404 Response — unknown property_id
{
  "message": "Property not found",
  "reason_code": 404,
  "data": { "property": null }
}
```

---

### Units

#### `POST /api/properties/:property_id/units`

```json
// Request
{
  "unit_number": "101",
  "monthly_rent": "1500.00"
}
```
`status` is optional and defaults to `"available"`.

```json
// 201 Response
{
  "message": "Unit created successfully",
  "reason_code": 201,
  "data": {
    "unit": {
      "id": 2,
      "is_active": true,
      "created_by": 2,
      "updated_by": null,
      "unit_number": "101",
      "monthly_rent": "1500.00",
      "status": "available",
      "properties": 2
    }
  }
}
```

```json
// 404 Response — unknown property_id
{ "message": "Property not found", "reason_code": 404, "data": { "unit": null } }
```

#### `GET /api/units` (supports `?status=available|occupied`)

```json
// GET /api/units/?status=available
{
  "message": "Units fetched successfully",
  "reason_code": 200,
  "data": {
    "units": [
      {
        "id": 2,
        "is_active": true,
        "created_by": 2,
        "updated_by": null,
        "unit_number": "101",
        "monthly_rent": "1500.00",
        "status": "available",
        "properties": 2
      }
    ]
  }
}
```

---

### Members

#### `POST /api/members`

```json
// Request
{
  "first_name": "Alice",
  "last_name": "Tenant",
  "email": "alice.tenant@example.com"
}
```

```json
// 201 Response
{
  "message": "Member created successfully",
  "reason_code": 201,
  "data": {
    "member": {
      "id": 2,
      "is_active": true,
      "created_by": 2,
      "updated_by": null,
      "first_name": "Alice",
      "last_name": "Tenant",
      "email": "alice.tenant@example.com"
    }
  }
}
```

```json
// 409 Response — duplicate email
{
  "message": "A member with this email already exists",
  "reason_code": 409,
  "data": { "member": null }
}
```

#### `GET /api/members`

```json
// 200 Response
{
  "message": "Member fetched successfully",
  "reason_code": 200,
  "data": {
    "members": [
      {
        "id": 2,
        "is_active": true,
        "created_by": 2,
        "updated_by": null,
        "first_name": "Alice",
        "last_name": "Tenant",
        "email": "alice.tenant@example.com"
      }
    ]
  }
}
```

---

### Contracts

#### `POST /api/contracts`

```json
// Request
{
  "member_id": 2,
  "unit_id": 2,
  "start_date": "2026-01-01",
  "end_date": "2026-12-31"
}
```
`monthly_rent` is optional — omit it to default to the unit's `monthly_rent`. `total_value` is computed automatically (`monthly_rent × number of months in the range`), and the unit's `status` is flipped to `"occupied"`.

```json
// 201 Response
{
  "message": "Contract created successfully",
  "reason_code": 201,
  "data": {
    "contract": {
      "id": 3,
      "is_active": true,
      "created_by": 2,
      "updated_by": null,
      "start_date": "2026-01-01",
      "end_date": "2026-12-31",
      "monthly_rent": "1500.00",
      "total_value": "18000.00",
      "member": 2,
      "unit": 2
    }
  }
}
```

```json
// 404 Response — unknown member_id or unit_id
{ "message": "Member not found", "reason_code": 404, "data": { "contract": null } }
```

```json
// 409 Response — overlapping dates on the same unit (double-booking)
{
  "message": "This unit already has a contract for overlapping dates",
  "reason_code": 409,
  "data": { "contract": null }
}
```

```json
// 400 Response — end_date <= start_date
{ "non_field_errors": ["end_date must be after start_date."] }
```

#### `GET /api/contracts`

```json
// 200 Response
{
  "message": "Contracts fetched successfully",
  "reason_code": 200,
  "data": {
    "contracts": [
      {
        "id": 3,
        "is_active": true,
        "created_by": 2,
        "updated_by": null,
        "start_date": "2026-01-01",
        "end_date": "2026-12-31",
        "monthly_rent": "1500.00",
        "total_value": "18000.00",
        "member": 2,
        "unit": 2
      }
    ]
  }
}
```

#### `GET /api/contracts?active=true`

Returns only contracts whose date range covers today (`start_date <= today <= end_date`).

```json
{
  "message": "Contracts fetched successfully",
  "reason_code": 200,
  "data": {
    "contracts": [
      {
        "id": 3,
        "is_active": true,
        "created_by": 2,
        "updated_by": null,
        "start_date": "2026-01-01",
        "end_date": "2026-12-31",
        "monthly_rent": "1500.00",
        "total_value": "18000.00",
        "member": 2,
        "unit": 2
      }
    ]
  }
}
```

---

## Business rules implemented

- **Default rent**: `monthly_rent` on a contract defaults to the unit's `monthly_rent` when omitted.
- **Total contract value**: computed as `monthly_rent × number_of_months(start_date, end_date)` at creation time.
- **Double-booking prevention**: a new contract is rejected with `409` if an existing (non-deleted) contract on the same unit overlaps its date range. This is enforced at two levels — an explicit pre-check in the service layer, and a model-level `clean()`/`full_clean()` safety net for race conditions.
- **Unit status sync**: creating a contract sets the unit's `status` to `"occupied"` in the same transaction.
- **Active contracts**: `?active=true` is a date-range check (`start_date <= today <= end_date`), independent of the `is_active` soft-delete flag every model carries.
