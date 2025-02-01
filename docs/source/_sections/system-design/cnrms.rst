Clinical Notes Record Management System
---------------

This documentation outlines the entity relationship (ER) model for the Clinical Notes Record Management System within DermVision. 
The ER model defines the structure of the data and the relationships between various entities involved in managing clinical notes records. 
Below is a detailed description of one of the key tables in the system: the **Clinical Notes** table.


Clinical Note Entity
^^^^^^^^^^^^^^^^^^^^
The **ClinicalNote** entity stores information about clinical notes recorded by healthcare providers. 
This table is essential for managing and tracking clinical notes related to patients.

**Attributes**

.. csv-table:: 
   :header: "Attribute", "Description", "Data Type", "Constraints"
   :widths: 20, 40, 20, 20

   "_id", "A unique identifier for each clinical note.", "Integer", "Primary Key, Auto-increment, Not Null"
   "title", "", "", "Not Null"
   "note", "", "", "Not Null"
   "derma", "", "", "Not Null"
   "patient", "", "", "Not Null"
   "created", "", "", "Not Null"
   "modified", "", "", "Not Null"
   "deleted", "", "", "Not Null"


**Relationships**

.. csv-table:: 
   :header: "Relationship", "Type", "Description", "Related Entity", "Foreign Key"
   :widths: 20, 20, 40, 20, 20

   "Patients", "Many-to-One", "Multiple clinical notes can belong to one patient.", "Patient", "PatientID in the ClinicalNote table references PatientID in the Patient table."
   "Derma", "Many-to-One", "Multiple clinical notes can belong to one patient.", "Patient", "PatientID in the ClinicalNote table references PatientID in the Patient table."

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

Get all clinical notes
~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/notes`

**Method:** `GET`

**Description:**  Get all clinical notes

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

    fetch('https://api.dermvision.com/notes', {
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

Create clinical note
~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/notes/add`

**Method:** `POST`

**Description:**  Add new clinical note

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

    fetch('https://api.dermvision.com/notes/add', {
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


Update clinical note
~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/notes/update`

**Method:** `POST`

**Description:**  update clinical note

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

    fetch('https://api.dermvision.com/notes/update', {
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

Fetch notes by dermatologist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/notes/derma/:id`

**Method:** `GET`

**Description:**  Get clinical records by a dermatologist

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

    fetch('https://api.dermvision.com/diagnostic/derma/1234', {
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

Fetch note records for a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/notes/patient/:id`

**Method:** `GET`

**Description:**  Get clinical notes records for a patient

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

    fetch('https://api.dermvision.com/notes/patient/1234', {
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
