Appointment Records Management System
-------------------------------------


This documentation outlines the entity relationship (ER) model for the Appointment Record Management System within DermVision. 
The ER model defines the structure of the data and the relationships between various entities involved in managing appointment records. 
Below is a detailed description of one of the key tables in the system: the **Appointment** table.


Appointment Entity
^^^^^^^^^^^^^^^^^^
The **Appointment** entity stores essential information about appointment records. This table is central to the Appointment Record Management System, 
as it contains the primary data necessary for identifying and managing patient records.

**Attributes**

.. csv-table:: 
   :header: "Attribute", "Description", "Data Type", "Constraints"
   :widths: 20, 40, 20, 20

   "_id", "A unique identifier for each patient.", "Integer", "Primary Key, Auto-increment, Not Null"
   "derma", "The id of the dermatologist that created the patient record", "Varchar(255)", "Not Null"
   "patient", "", "", "Not Null"
   "title", "", "", "Not Null"
   "notes", "", "", "Not Null"
   "date", "", "", "Not Null"
   "from", "", "", "Not Null"
   "to", "", "", "Not Null"
   "created", "The date the record was created", "DateTime", "Not Null"
   "modified", "The date the record was updated", "DateTime", "Not Null"
   "status", "", "", ""


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
      
      'style options 
      skinparam monochrome true
      skinparam circledCharacterRadius 0
      skinparam circledCharacterFontSize 0
      skinparam classAttributeIconSize 0
      hide empty members
      
      Class01 <|-- Class02
      Class03 *-- Class04
      Class05 o-- Class06
      Class07 .. Class08
      Class09 -- Class10
      
      @enduml


API
^^^

Get all appointment records
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/appointment/`

**Method:** `GET`

**Description:**  Get all appointment records

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

    fetch('https://api.dermvision.com/apppointment/', {
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


Add new appointment record
~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/appointment/add`

**Method:** `POST`

**Description:**  Add new patient record

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

    fetch('https://api.dermvision.com/appointment/add', {
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

Update appointment record
~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/appointment/add`

**Method:** `POST`

**Description:**  Update appointment record

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

    fetch('https://api.dermvision.com/appointment/add', {
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


Cancel an appointment record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/appointment/cancel/:id`

**Method:** `GET`

**Description:**  Cancel an appointment record

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

    fetch('https://api.dermvision.com/apppointment/cancel/1234', {
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

Fetch appointment records for a dermatologist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/appointment/derma/:id`

**Method:** `GET`

**Description:**  Fetch appointment records for a dermatologist

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

    fetch('https://api.dermvision.com/apppointment/derma/1234', {
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

Fetch appointment records for a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/appointment/patient/:id`

**Method:** `GET`

**Description:**  Fetch appointment records for a patient

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

    fetch('https://api.dermvision.com/apppointment/patient/1234', {
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