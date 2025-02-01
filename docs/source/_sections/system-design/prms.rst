Patient Record Management System
--------------------------------

.. _system-design-prms:

This documentation outlines the entity relationship (ER) model for the Patient Record Management System within DermVision. 
The ER model defines the structure of the data and the relationships between various entities involved in managing patient records. 
Below is a detailed description of one of the key tables in the system: the **Patient** table.


Patient Entity
^^^^^^^^^^^^^^
The **Patient** entity stores essential information about patients. This table is central to the Patient Record Management System, 
as it contains the primary data necessary for identifying and managing patient records.

**Attributes**

.. csv-table:: 
   :header: "Attribute", "Description", "Data Type", "Constraints"
   :widths: 20, 40, 20, 20

   "_id", "A unique identifier for each patient.", "Integer", "Primary Key, Auto-increment, Not Null"
   "name", "The full name of the patient.", "", "Not Null"
   "email", "The email address of the patient", "", "Not Null"
   "phone", "The phone number of the patient", "", "Not Null"
   "nationality", "The nationality of the patient", "", "Not Null"
   "gender", "The gender of the patient", "", "Not Null"
   "dob", "The date of birth of the patient", "", "Unique, Not Null"
   "derma", "The id of the dermatologist that created the patient record", "", "Not Null"
   "created", "The date the record was created", "", "Not Null"
   "updated", "The date the record was updated", "", "Nullable"


**Relationships**

.. csv-table:: 
   :header: "Relationship", "Type", "Description", "Related Entity", "Foreign Key"
   :widths: 20, 20, 40, 20, 20

   "Appointments", "One-to-Many", "A patient can have multiple appointments.", "Appointment", "PatientID in the Appointment table references PatientID in the Patient table."
   "Diagnostics", "One-to-Many", "A patient can have multiple diagnostic records.", "Diagnostic", "PatientID in the Diagnostic table references PatientID in the Patient table."
   "ClinicalNotes", "One-to-Many", "A patient can have multiple clinical notes.", "ClinicalNote", "PatientID in the ClinicalNote table references PatientID in the Patient table."
   "Prescriptions", "One-to-Many", "A patient can have multiple prescriptions.", "Prescription", "PatientID in the Prescription table references PatientID in the Patient table."
   "Derma", "Many-to-One", "A dermatolgist can have multiple patients", "Prescription", "PatientID in the Prescription table references PatientID in the Patient table."



.. uml::

    @startuml

        entity "User" {
        * id : int
        ---
        name : varchar
        email : varchar
        }

        entity "Order" {
        * id : int
        ---
        user_id : int
        amount : decimal
        }

        entity "Product" {
        * id : int
        ---
        name : varchar
        price : decimal
        }

        User ||--o{ Order : places
        Order ||--|{ Product : contains
    @enduml

API
^^^
Get all patient record
~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/patient/`

**Method:** `GET`

**Description:**  Get all patient records

**Headers:**

.. code-block:: http

    Authorization: Bearer {token}
    Content-Type: application/json

**Response:**
- `200 OK`: A JSON object containing user data.
- `404 Not Found`: If the user does not exist.
- `401 Unauthorized`: If the authentication token is invalid or missing.

**Example Request:**

.. code-block:: javascript

    fetch('https://api.dermvision.com/patient/', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

**Example Response:**

.. code-block:: json

    {
        
    }

Add new patient record
~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/patient/add`

**Method:** `POST`

**Description:**  Add new patient record

**Headers:**

.. code-block:: http

    Authorization: Bearer {token}
    Content-Type: application/json



**Body:**

.. code-block:: json

    {
        "derma": 123,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+966507133905"
        "dob": "08-Nov-1980" 
    }


**Response:**
- `200 OK`: A JSON object containing user data.
- `404 Not Found`: If the user does not exist.
- `401 Unauthorized`: If the authentication token is invalid or missing.

**Example Request:**

.. code-block:: javascript

    fetch('https://api.dermvision.com/patient/add', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

**Example Response:**

.. code-block:: json

    {
     
    }

Get all patients belonging to a dermatologist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/patient/derma/:id`

**Method:** `GET`

**Description:**  Get all patients belonging to a dermatologist

**Headers:**

.. code-block:: http

    Authorization: Bearer {token}
    Content-Type: application/json


**Parameters:**
- ``id`` - dermatologist id



**Response:**
- `200 OK`: A JSON object containing user data.
- `404 Not Found`: If the user does not exist.
- `401 Unauthorized`: If the authentication token is invalid or missing.

**Example Request:**

.. code-block:: javascript

    fetch('https://api.dermvision.com/patient/derma/123456', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

**Example Response:**

.. code-block:: json

    {
        
    }


Update patient record
~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/patient/update`

**Method:** `POST`

**Description:**  Update patient record

**Headers:**

.. code-block:: http

    Authorization: Bearer {token}
    Content-Type: application/json

**Body:**

.. code-block:: json

    {
      
    }

**Response:**
- `200 OK`: A JSON object containing user data.
- `404 Not Found`: If the user does not exist.
- `401 Unauthorized`: If the authentication token is invalid or missing.

**Example Request:**

.. code-block:: javascript

    fetch('https://api.dermvision.com/patient/add', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));


**Example Response:**

.. code-block:: json

    {
        
    }
