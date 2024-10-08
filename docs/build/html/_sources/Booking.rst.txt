CRUD Operations
========================

This document describes the (Create, Read, Update) operations for the `Booking` model in the application.

Booking Model
-------------


The `Booking` model represents a user in the system and includes the following fields:

- org_id (integer): The organization ID associated with the customer.
- email (string): The email address of the customer.
- property_type (string): The type of property (e.g., hotel, apartment, etc.).
- guest_name (string): The name of the guest.
- mobile_no (decimal): The mobile number of the guest.
- check_in_date (date): The check-in date for the booking.
- check_out_date (date): The check-out date for the booking.
- num_guests (decimal): The number of guests in the booking.
- num_rooms (decimal): The number of rooms booked.
- special_requests (string): Any special requests made by the guest.
- total_price (decimal): The total price of the booking.

**URL**
-------
**Local Development URL:**

- `baseurl`` = "http://localhost:7777/1/api/"

**Production URL:**

- `baseurl`` = "https://api.sunandsandapi.com/1/api/"

Booking
=======

GetBooking 
----------

- **Endpoint:** ``GET baseUrl/org_id/api/booking/get-bookings//``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": [
        {
            "id": 3,
            "org_id": 1,
            "property_type": "Villa",
            "guest_name": "Onkii",
            "email": "onkii@gmail.com",
            "mobile_no": "9087654321",
            "check_in_date": "2024-09-21",
            "check_out_date": "2024-09-25",
            "num_guests": 2,
            "num_rooms": 1,
            "special_requests": "Late check-in if possible.",
            "total_price": "2500.00"
        }
            ]
    }
GetBookingById
--------------

- **Endpoint:** ``GET /{org_id}/api/booking/get-booking/{Id}/``

- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 5,
        "org_id": 1,
        "property_type": "Villa",
        "guest_name": "krishna",
        "email": "abc@gmail.com",
        "mobile_no": "7719912920",
        "check_in_date": "2024-09-24",
        "check_out_date": "2024-09-26",
        "num_guests": 2,
        "num_rooms": 2,
        "special_requests": "veg",
        "total_price": "30870.00"
             }
    }


CreateBooking
-------------

- **Endpoint:** ``POST baseUrl/org_id/api/booking/create-booking/``

- **Request Body:**

.. code-block:: json

    {
  "property_type": "Bungalow",
  "guest_name": "vaishaliDeokar",
  "email": "vaishliDeo@example.com",
  "mobile_no": "3214567890",
  "check_in_date": "2023-09-20",
  "check_out_date": "2023-09-25",
  "booking_status": "Pending",
  "num_guests": 4,
  "num_rooms":5,
  "special_requests": "Vegetarian meals",
  "total_price": 500.00
    }


.. - **Response Body:**

.. .. code-block:: json

..     {
    
            
..     }

UpdateBooking
-------------

- **Endpoint:** ``Patch baseUrl/org_id/api/booking/update-booking/{Id}/``
- **Request Body:**

.. code-block:: json

    {
  "property_type": "Bungalow",
  "guest_name": "vaishali kadbhane",
  "email": "johndoe@example.com",
  "mobile_no": "1234567890",
  "check_in_date": "2023-09-20",
  "check_out_date": "2023-09-25",
  "booking_status": "Pending",
  "num_guests": 4,
  "special_requests": "Vegetarian meals",
  "total_price": 500.00
    }


- **Response Body:**

.. code-block:: json

    {
    "status": "success",
    "data": {
        "id": 3,
        "org_id": 1,
        "property_type": "Bungalow",
        "guest_name": "vaishali kadbhane",
        "email": "johndoe@example.com",
        "mobile_no": "1234567890",
        "check_in_date": "2023-09-20",
        "check_out_date": "2023-09-25",
        "num_guests": 4,
        "num_rooms": 1,
        "special_requests": "Vegetarian meals",
        "total_price": "500.00"
            }
    }