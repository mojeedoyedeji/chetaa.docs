Prescription Record Management System
---------------


This documentation outlines the entity relationship (ER) model for the Prescription Record Management System within DermVision. 
The ER model defines the structure of the data and the relationships between various entities involved in managing prescription records. 
Below is a detailed description of one of the key tables in the system: the **Treatment** table.


Treatment Entity
^^^^^^^^^^^^^^^^
The **Treatment** entity stores essential information about patients. This table is central to the Prescription Record Management System, 
as it contains the primary data necessary for identifying and managing prescription records.

**Attributes**

.. csv-table:: 
   :header: "Attribute", "Description", "Data Type", "Constraints"
   :widths: 20, 40, 20, 20

   "_id", "A unique identifier for each patient.", "Integer", "Primary Key, Auto-increment, Not Null"
   "derma", "", "", "Not Null"
   "patient", "", "", "Not Null"
   "type", "", "", "Not Null"
   "mode", "", "", "Not Null"
   "title", "", "", "Not Null"
   "description", "", "", "Not Null"
   "dosage_quantity", "", "", "Not Null"
   "dosage_unit", "", "", "Not Null"
   "duration_number", "", "", "Not Null"
   "duration_period", "", "", "Not Null"
   "frequency_value", "", "", "Not Null"
   "frequency_period", "", "", "Not Null"
   "created", "", "DateTime", "Not Null"
   "modified", "", "DateTime", "Not Null" 

**Relationships**

.. csv-table:: 
   :header: "Relationship", "Type", "Description", "Related Entity", "Foreign Key"
   :widths: 20, 20, 40, 20, 20

   "Patients", "One-to-Many", "A patient can have multiple prescription records", "Patients", "PatientID in the Appointment table references _id in the Patient table."
   "Derma", "One-to-Many", "A dermatologists can create multiple prescription records.", "Dermatologist", "DermatologistID in the Diagnostic table references _id in the Dermatologist table."
   



API
^^^
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

Get all treatment records
~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/treatment`

**Method:** `GET`

**Description:**  Get all treatment records

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

    fetch('https://api.dermvision.com/treatment', {
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

Create new treatment record
~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/treatment/add`

**Method:** `POST`

**Description:**  Add new treatment record

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

    fetch('https://api.dermvision.com/treatment/add', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'Content-Type': 'application/json'
        },
        body: body
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));


**Example Response:**

.. code-block:: json

    {
       
    }

Update treatment record
~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/treatment/update`

**Method:** `POST`

**Description:**  Update treatment record

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

    fetch('https://api.dermvision.com/treatment/update', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
            'Content-Type': 'application/json'
        },
        body: body
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

**Example Response:**

.. code-block:: json

    {
       
    }

Fetch treatment records by dermatologist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/treatment/derma/:id`

**Method:** `GET`

**Description:**  Get treatment records by a dermatologist

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

    fetch('https://api.dermvision.com/treatment/derma/1234', {
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


Fetch treatment records for a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/treatment/patient/:id`

**Method:** `GET`

**Description:**  Get treatment records for a patient

**Headers:**

.. code-block:: http

    Authorization: Bearer {token}
    Content-Type: application/json

**Parameters:**
- ``id`` - patient id

**Response:**
- `200 OK`: A JSON object containing user data.
- `404 Not Found`: If the user does not exist.
- `401 Unauthorized`: If the authentication token is invalid or missing.

**Example Request:**

.. code-block:: javascript

    fetch('https://api.dermvision.com/treatment/patient/1234', {
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