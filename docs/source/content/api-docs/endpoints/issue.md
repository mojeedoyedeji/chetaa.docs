# Issue

Version: `1.0`  
Base URL: `https://api.chetaa.com/`

###### About

---

###### Preamble

Most endpoints require a `Bearer` token for authentication.

###### Create new issue

```{http:get} {base_uri}/user/issues/create/

```

**Request Body**

| Parameter | Type   | Description |
| --------- | ------ | ----------- |
| `status`  | string |             |

**Response JSON Object**

| Parameter | Type   | Description |
| --------- | ------ | ----------- |
| `status`  | string |             |

**Status Codes**

| Code  | Description |
| ----- | ----------- |
| `200` | XXXXX       |
| `400` | XXXXX       |

**Example Request**

```javascript
// Sample JavaScript code to interact with Chetaa API

const apiUrl = "https://api.chetaa.com/v1/issue";
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

###### Get issue details (user)

```{http:get} {base_uri}/user/issues/get/

```

---

###### Get list of issues (user)

```{http:get} {base_uri}/user/issues/all/

```

---

###### Get issue logs (user)

```{http:get} {base_uri}/user/issues/log/

```

---

###### Get all issues (delivery agent)

```{http:get} {base_uri}/agent/issues/all/

```

---

###### Mark an issue resolved (delivery agent)

```{http:get} {base_uri}/agent/issues/resolve/

```

---

###### Add to an issue log (delivery agent)

```{http:get} {base_uri}/agent/issues/log/

```

---

###### Create an issue (unregistered user)

```{http:get} {base_uri}/saas/issue/create/

```

---

###### Add message to issue logs (unregistered user)

```{http:get} {base_uri}/saas/issue/log/

```

---
