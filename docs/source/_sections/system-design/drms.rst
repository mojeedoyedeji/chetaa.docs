Diagnostics Record Management System
---------------

.. _system-design-drms:

This documentation outlines the entity relationship (ER) model for the Diagnostic Record Management System within DermVision. 
The ER model defines the structure of the data and the relationships between various entities involved in managing diagnostic records. 
Below is a detailed description of one of the key tables in the system: the **Diagnostic** table.


Diagnostic Entity
^^^^^^^^^^^^^^^^^
The **Diagnostic** entity stores essential information about the diagnosis for each patient. 
This table is central to the Diagnostic Record Management System,  as it contains the primary data necessary 
for identifying and managing patient records.

**Attributes**

.. csv-table:: 
   :header: "Attribute", "Description", "Data Type", "Constraints"
   :widths: 20, 40, 20, 20

   "_id", "A unique identifier for each patient.", "Integer", "Primary Key, Auto-increment, Not Null"
   "image", "", "", "Not Null"
   "patient", "", "", "Not Null"
   "age", "", "", "Not Null"
   "gender", "", "", "Not Null"
   "bleeding", "", "", "Not Null"
   "elevation", "", "", "Not Null"
   "changed", "", "", "Not Null"
   "hurt", "", "", "Not Null"
   "grew", "", "", "Not Null"
   "itchy", "", "", "Not Nullable"
   "region", "", "", "Not Nullable"
   "location", "", "", "Not Nullable"
   "tone", "", "", "Not Nullable"
   "symptoms", "", "", "Not Nullable"
   "cam", "", "", "Not Nullable"
   "prediction", "", "", "Not Nullable"
   "probabilities", "", "", "Not Nullable"
   "derma", "", "", "Not Nullable"
   "created", "", "", "Not Nullable"
   "modified", "", "", "Not Nullable"


**Relationships**

.. csv-table:: 
   :header: "Relationship", "Type", "Description", "Related Entity", "Foreign Key"
   :widths: 20, 20, 40, 20, 20

   "Patients", "One-to-Many", "A patient can have multiple diagnostic records", "Patients", "PatientID in the Appointment table references _id in the Patient table."
   "Derma", "One-to-Many", "A dermatologists can create multiple diagnostic records.", "Dermatologist", "DermatologistID in the Diagnostic table references _id in the Dermatologist table."
   

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

Get all diagnostic records
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/diagnostic`

**Method:** `GET`

**Description:**  Get all diagnostic records

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

    fetch('https://api.dermvision.com/diagnostic', {
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

Perform a diagnosis
~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/diagnostic/diagnose`

**Method:** `POST`

**Description:**  Perform a diagnosis using image and clinical data

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

    fetch('https://api.dermvision.com/diagnostic/diagnose', {
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

Save diagnosis result
~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/diagnostic/save`

**Method:** `POST`

**Description:**  Save the result of diagnosis

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

    fetch('https://api.dermvision.com/diagnostic/diagnose', {
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

Fetch diagnostic records by dermatologist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/diagnostic/derma/:id`

**Method:** `GET`

**Description:**  Get diagnostic records by a dermatologist

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

Fetch diagnostic records for a patient
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/diagnostic/patient/:id`

**Method:** `GET`

**Description:**  Get diagnostic records for a patient

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

    fetch('https://api.dermvision.com/diagnostic/patient/1234', {
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