Customer CRUD Operations
========================

This document describes the (Create, Read, Login) operations for the `Customer` model in the application.

Customer Model
==============

The `Customer` model represents a user in the system and includes the following fields:

- `org_id` (integer): The organization ID associated with the customer.
- `email` (string): The email address of the customer.
- `password` (string): The hashed password of the customer (stored securely).
- `first_name` (string): The first name of the customer.
- `last_name` (string): The last name of the customer.
- `city` (string): The city where the customer resides.
- `mobile_number` (string): The mobile phone number of the customer.
- `is_active` (boolean): Indicates whether the customer is active.
- `is_super_admin` (boolean): Indicates whether the customer has super admin privileges.
- `is_admin` (boolean): Indicates whether the customer has admin privileges.
- `is_customer` (boolean): Indicates whether the user is marked as a customer.

API Endpoints
-------------

### GetAll Customer

**Endpoint:** `GET baseUrl/org_id/api/customer/get-customer/`

**Response Body:**

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "last_login": null,
            "org_id": 3,
            "email": "example@example.com",
            "password": "pbkdf2_sha256$870000$u6iZn1Yfho8aca2ORYPM51$9gT/uIUu74ThrP/sOhOZXIAlAEvSnljEO3OhXQ4ZoBY=",
            "first_name": "John",
            "last_name": "Doe",
            "city": "New York",
            "mobile_number": "+1234567890",
            "is_active": true,
            "is_super_admin": false,
            "is_admin": false,
            "is_customer": true
        }
    ]
}

### GetById Customer

**Endpoint:** `GET baseUrl/org_id/api/customer/get-customer/?id=1/`

**Response Body:**

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "last_login": null,
            "org_id": 3,
            "email": "example@example.com",
            "password": "pbkdf2_sha256$870000$u6iZn1Yfho8aca2ORYPM51$9gT/uIUu74ThrP/sOhOZXIAlAEvSnljEO3OhXQ4ZoBY=",
            "first_name": "John",
            "last_name": "Doe",
            "city": "New York",
            "mobile_number": "+1234567890",
            "is_active": true,
            "is_super_admin": false,
            "is_admin": false,
            "is_customer": true
        }
    ]
}

### Create a Customer

**Endpoint:** `POST baseUrl/org_id/api/customer/create-customer/`

**Request Body:**

```json
{
  "org_id": 1,
  "email": "example@example.com",
  "password": "password",
  "first_name": "John",
  "last_name": "Doe",
  "city": "New York",
  "mobile_number": "+1234567890",
  "is_active": true,
  "is_super_admin": false,
  "is_admin": false,
  "is_customer": true
}

**Response Body:**

'''json
{
    "id": 1,
    "last_login": null,
    "org_id": 3,
    "email": "example@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "city": "New York",
    "mobile_number": "+1234567890",
    "is_active": true,
    "is_super_admin": false,
    "is_admin": false,
    "is_customer": true
}

### Login a Customer

**Endpoint:** `POST baseUrl/org_id/api/customer/login-customer/`

**Request Body:**

```json
{
    "email": "example@example.com",
    "password": "password"
}

**Response Body:**

'''json
{
    "status": "success",
    "data": {
        "status": 200,
        "user_id": 1,
        "is_super_admin": false,
        "is_admin": false,
        "is_customer": true,
        "displayName": "John",
        "emailId": "example@example.com",
        "message": "Logged-in Successfully",
        "Token": "612e9a50ad61e6c2c6b5f9b8cbc9dd773981958c82cf276156904920c79d2664"
    }
}