Diagnostic Model Management System
---------------


This documentation outlines the entity relationship (ER) model for the Diagnostic Model Management System within DermVision. 
The ER model defines the structure of the data and the relationships between various entities involved in managing patient records. 
Below is a detailed description of one of the key tables in the system: the **Library** table.


Library Entity
^^^^^^^^^^^^^^
The **Library** entity stores essential information about diagnostic model. This table is central to the Diagnostic Model Management System, 
as it contains the primary data necessary for identifying and managing model version.

**Attributes**

.. csv-table:: 
   :header: "Attribute", "Description", "Data Type", "Constraints"
   :widths: 20, 40, 20, 20

   "_id", "A unique identifier for each patient.", "Integer", "Primary Key, Auto-increment, Not Null"
   "model_name", "", "", ""
   "model_type", "", "", ""
   "model_filename", "", "", ""
   "model_accuracy", "", "", ""
   "model_auc", "", "", ""
   "model_recall", "", "", ""
   "default", "", "", ""
   "created", "The date the record was created", "DateTime", "Not Null"
   "updated", "The date the record was updated", "DateTime", "Not Null"


**Relationships**

.. csv-table:: 
   :header: "Relationship", "Type", "Description", "Related Entity", "Foreign Key"
   :widths: 20, 20, 40, 20, 20

  
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
Get all model records
~~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/library/`

**Method:** `GET`

**Description:**  Get all model records

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

    fetch('https://api.dermvision.com/library/', {
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


Add model to library
~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/library/add`

**Method:** `POST`

**Description:**  Add model to library

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

    fetch('https://api.dermvision.com/library/add', {
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


Update model record
~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/library/update`

**Method:** `POST`

**Description:**  Update model record

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

    fetch('https://api.dermvision.com/library/update', {
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



Make model default
~~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/library/default`

**Method:** `POST`

**Description:**  Make a model default for diagnosis tasks

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

    fetch('https://api.dermvision.com/library/default', {
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
