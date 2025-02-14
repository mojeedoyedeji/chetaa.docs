# Services

Version: `1.0`  
Base URL: `https://api.chetaa.com/`

###### About

---

###### Preamble

---

###### Fetch all delivery service

```{http:get} {base_uri}/agent/services/all/

```

Get all delivery requests

**Request Body**

| Parameter     | Type    | Description                                           |
| ------------- | ------- | ----------------------------------------------------- |
| `status`      | string  | Filter by status (`pending`, `delivered`, `canceled`) |
| `driver_id`   | integer | Filter by driver ID                                   |
| `customer_id` | integer | Filter by customer ID                                 |
| `page`        | integer | Page number                                           |
| `limit`       | integer | Number of results per page                            |

**Response JSON Object**

| Parameter     | Type    | Description                                           |
| ------------- | ------- | ----------------------------------------------------- |
| `status`      | string  | Filter by status (`pending`, `delivered`, `canceled`) |
| `driver_id`   | integer | Filter by driver ID                                   |
| `customer_id` | integer | Filter by customer ID                                 |
| `page`        | integer | Page number                                           |
| `limit`       | integer | Number of results per page                            |

**Status Codes**

| Code  | Description                                           |
| ----- | ----------------------------------------------------- |
| `200` | Filter by status (`pending`, `delivered`, `canceled`) |
| `400` | Filter by driver ID                                   |

**Example Request**

```javascript
// Sample JavaScript code to interact with Chetaa API

const apiUrl = "https://api.chetaa.com/v1/deliveries";
const apiKey = "your_api_key_here";

async function fetchDeliveries() {
  try {
    const response = await fetch(apiUrl, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log("Deliveries:", data);
  } catch (error) {
    console.error("Error fetching deliveries:", error);
  }
}

// Call the function
fetchDeliveries();
```

**Example Response**

```json
{
  "order_id": 12345,
  "customer_id": 6789,
  "driver_id": 12,
  "status": "pending",
  "pickup_address": "123 Main St, Toronto",
  "delivery_address": "456 Elm St, Toronto",
  "expected_delivery_time": "2025-02-15T14:00:00Z"
}
```

---

###### Add a delivery service

```{http:get} {base_uri}/agent/service/add/

```

---

###### Update delivery service

```{http:get} {base_uri}/agent/service/update/

```

---

###### Remove delivery service

```{http:get} {base_uri}/agent/service/remove/

```

---

###### Fetch all services (admin)

```{http:get} {base_uri}/admin/service/all/

```

---
