CRUD Operations
===============

This document describes the (Create, Read, Login) operations for the `Agent` model in the application.

Agent Model
===========

The `Agent` model represents a user in the system and includes the following fields:
- `org_id` (integer): The organization ID associated with the Agent.
- `email` (string): The email address of the Agent.
- `last_login` (string): The last login date and time of the Agent.
- `password` (string): The hashed password of the Agent (stored securely).
- `first_name` (string): The first name of the Agent.
- `last_name` (string): The last name of the Agent.
- `city` (string): The city where the Agent resides.
- `mobile_number` (string): The mobile phone number of the Agent.
- `total_sales` (string): The total sales closed by the Agent.
- `hire_date` (date): The date the Agent was hired.
- `is_active` (boolean): Indicates whether the Agent is currently active.
- `is_super_admin` (boolean): Indicates whether the Agent has super admin privileges.
- `is_admin` (boolean): Indicates whether the Agent has admin privileges.
-` is_agent` (boolean): Indicates whether the user is an Agent.

**URL**
-------
**Local Development URL:**

- `baseurl`` = "http://localhost:7777/1/api/"

**Production URL:**

- `baseurl`` = "https://api.sunandsandapi.com/1/api/"

Agent
=====

GetAllAgent
-----------

- **Endpoint:** ``GET baseUrl/org_id/api/agent/get-agent/``
- **Response Body:**

.. code-block:: json
    {
    "status": "success",
    "data": [
        {
            "id": 4,
            "last_login": null,
            "org_id": 1,
            "email": "vaishalikadbhane@gmail.com",
            "password": "pbkdf2_sha256$870000$05CxW5X7crPLLtG1uXvUX8$ah7V65EOpb+Gz6bJdMWMeeSZMvrjwpjK//dc1zuMaRk=",
            "first_name": "vaishali",
            "last_name": "kadbhane",
            "mobile_number": "07719912920",
            "city": "Pune",
            "total_sales": "1000000.00",
            "hire_date": null,
            "is_active": true,
            "is_super_admin": false,
            "is_admin": false,
            "is_agent": true
        }
    ]
}

GetAgentbyId
------------

- **Endpoint:** ``GET baseUrl/org_id/api/customer/get-customer/?id=2/``

- **Response Body:**

.. code-block:: json
    {
    "status": "success",
    "data": [
        {
            "id": 9,
        "last_login": null,
        "org_id": 1,
        "email": "agent@gmail.com",
        "password": "pbkdf2_sha256$870000$B8zWENQ1GOW8XEEGgbdc2i$IIZ4pr5jjdDD3DxYTuGotrgiSUJ5Hf7MJ/LcJNdBFxI=",
        "first_name": "John",
        "last_name": "Doe",
        "mobile_number": "1234567890",
        "city": "New York",
        "total_sales": "25000.00",
        "hire_date": null,
        "is_active": true,
        "is_super_admin": false,
        "is_admin": false,
        "is_agent": true
        }
    ]
}

CreateAgent
-----------

- **Endpoint:** ``POST baseUrl/org_id/api/agent/create-agent/``

- **Request Body:**

.. code-block:: json
    {
  
    "email": "qwer@gmail.com",
    "password": "qaz",
    "first_name": "John",
    "last_name": "Doe",
    "city": "New York",
    "mobile_number": "1234567890",
    "total_sales": 25000
    }


- **Response Body:**

.. code-block:: json
    {
    "id": 13,
    "last_login": null,
    "org_id": 1,
    "email": "qwer@gmail.com",
    "first_name": "John",
    "last_name": "Doe",
    "mobile_number": "1234567890",
    "city": "New York",
    "total_sales": "25000.00",
    "hire_date": null,
    "is_active": true,
    "is_super_admin": false,
    "is_admin": false,
    "is_agent": true
    }

.. ### Login a Agent

.. **Endpoint:** `POST baseUrl/org_id/api/agent/login-agent/`

.. **Request Body:**

.. ```json
.. {
..     "email": "agent@gmail.com",
..     "password": "agent"
.. }

.. **Response Body:**

.. '''json
.. {
    
            
.. }

UpdateAgent
---------------

- **Endpoint:** ``POST baseUrl/org_id/api/agent/update-agent/{Id}/``

- **Request Body:**

.. code-block:: json
    {
    "email": "admin@gmail.com",
    "password": "admin@123",
    "first_name": "admin",
    "last_name": "D",
    "mobile_number": "7719912929",
    "city": "Parali",
    "total_sales": "10000.00",
    "hire_date": null,
    "is_active": true,
    "is_super_admin": false,
    "is_admin": false,
    "is_agent": true

    }
- **Response Body**


.. code-block:: json
   
    {
    "status": "success",
    "data": {
        "id": 8,
        "last_login": null,
        "org_id": 1,
        "email": "admin@gmail.com",
        "password": "pbkdf2_sha256$870000$nPNvntukcyTDuJPrqSYWoX$GwIpAXYIvJ8zF/2wUhdP0sYC8Sm2vCGDQWucSD0NJvQ=",
        "first_name": "admin",
        "last_name": "D",
        "mobile_number": "7719912929",
        "city": "Mumbai",
        "total_sales": "10000.00",
        "hire_date": null,
        "is_active": true,
        "is_super_admin": false,
        "is_admin": false,
        "is_agent": true
            }
    }  