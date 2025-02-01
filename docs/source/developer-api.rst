Developer API
=============

Welcome to the DermVision API documentation. DermVision provides advanced AI-powered diagnostic tools for dermatological analysis. 
This API allows developers to seamlessly integrate DermVision's diagnostic capabilities into their applications. With endpoints for image uploads, 
diagnostic result retrieval, and image management, the DermVision API is designed to be easy to use while providing robust and accurate diagnostic insights. 
By leveraging this API, developers can enhance their applications with cutting-edge dermatological analysis, enabling early detection and better management of 
skin conditions. Whether you are building mobile apps, web services, or integrating with electronic health records, 
the DermVision API offers a comprehensive solution for AI-based skin diagnostics.

Base URL: https://api.dermvision.com

Endpoints
---------


Perform a diagnosis
~~~~~~~~~~~~~~~~~~~

**Endpoint URL:** `/dev/diagnose?api_key=key123`

**Method:** `POST`

**Description:**  Get all patient records

**Headers:**

.. code-block:: http

    Authorization: Bearer {token}
    Content-Type: application/json



**Body:**

.. csv-table:: 
   :header: "Name", "Description", "Type", "Required"
   :widths: 20, 40, 20, 20

   "image", "", "", "Not Null"
   "elevation", "", "", "Not Null"
   "bleed", "", "", "Not Null"
   "gender", "The gender of the patient.", "", "Not Null"
   "changed", "", "", "Not Null"
   "hurt", "", "", "Not Null"
   "grew", "", "", "Not Null"
   "itch", "", "", "Not Nullable"
   "region", "", "", "Not Nullable"
   "age", "The date of birth of the patient.", "", "Not Null"



**Response:**
- `200 OK`: A JSON object containing user data.
- `404 Not Found`: If the user does not exist.
- `401 Unauthorized`: If the authentication token is invalid or missing.

**Example Request:**

.. code-block:: javascript
    fetch(`https://api.dermvision.com/dev/diagnose?api_key={$key}`, {
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
      "cam": "20240526212255_XLRKAo.png_cam.jpg",
	    "image": "20240526212255_XLRKAo.png",
	    "model_type": "meta",
	    "prediction": "positive",
	    "probabilities": [
		    6.390391718014143e-06,
		    0.9999935626983643
	    ],
	    "request": "66537e00b58e5abfba26c382"
    }


