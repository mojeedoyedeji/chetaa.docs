# Delivery

Version: `1.0`  
Base URL: `https://api.chetaa.com/`

###### About

Delivery requests can be either a `service` or `quote` request. A service request is a request made by selecting a fixed price service from a delivery agent. A delivery quote request can be requested from the delivery agent by the user (customer or business) owner.

---

###### Preamble

Most endpoints require a `Bearer` token for authentication.

**Request Header**

```http
Content-Type: application/json
Authorization: Bearer {token}
```

**Base URI** `/deliveries/`

**Request Headers:**

---

###### Fetch all delivery requests

```{http:get} {base_uri}/agent/delivery/all/

```

Get all delivery requests

**Request Body**

| Parameter     | Type    | Description |
| ------------- | ------- | ----------- |
| `status`      | string  |             |
| `driver_id`   | integer |             |
| `customer_id` | integer |             |
| `page`        | integer |             |
| `limit`       | integer |             |

**Response JSON Object**

| Parameter     | Type    | Description |
| ------------- | ------- | ----------- |
| `status`      | string  |             |
| `driver_id`   | integer |             |
| `customer_id` | integer |             |
| `page`        | integer |             |
| `limit`       | integer |             |

**Status Codes**

| Code  | Description |
| ----- | ----------- |
| `200` |             |
| `400` |             |

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

###### Confirm request (delivery)

```{http:post} {base_uri}/agent/delivery/confirm_service/

```

Confirm the delivery request

```{admonition} Description
After the user(customer or business) makes a request. The request needs to be confirmed by the delivery agent (offline payment mode) after the payment is confirmed independently by the delivery agent. Upon confirmation, the service is confirmed. This triggers a sequence of events. The transaction is logged as an offline transaction in the transaction logs. A notification object is created to the agent and the dispatchers registered under that agent via email and sms modes. An sms message is also sent to the pickup and delivery ends of the request. A delivery log object is created with the payment status updated to confirmed.
```

**Request Body**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  |             |
| `driver_id` | integer |             |

**Response JSON Object**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  |             |
| `driver_id` | integer |             |

**Status Codes**

| Code  | Description |
| ----- | ----------- |
| `200` |             |
| `400` |             |

**Example Request**

```http
GET /deliveries/?status=pending&page=1&limit=10 HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_ACCESS_TOKEN
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

###### Confirm request (quote)

```{http:post} {base_uri}/agent/delivery/confirm_quote/

```

**Request Body**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  |             |
| `driver_id` | integer |             |

**Response JSON Object**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  |             |
| `driver_id` | integer |             |

**Status Codes**

| Code  | Description |
| ----- | ----------- |
| `200` |             |
| `400` |             |

**Example Request**

```http
GET /deliveries/?status=pending&page=1&limit=10 HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_ACCESS_TOKEN
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

###### Cost quote

```{http:post} {base_uri}/agent/delivery/cost_quote/

```

Cost a delivery quote

**Request Body**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  |             |
| `driver_id` | integer |             |

**Response JSON Object**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  |             |
| `driver_id` | integer |             |

**Status Codes**

| Code  | Description |
| ----- | ----------- |
| `200` | XXXXXX      |
| `400` | XXXXXX      |

**Example Request**

```http
GET /deliveries/?status=pending&page=1&limit=10 HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_ACCESS_TOKEN
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

###### Fetch delivery logs

```{http:post} {base_uri}/agent/delivery/logs/

```

Fetch all logs for a delivery request

**Request Body**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  | XXXXXXXX    |
| `driver_id` | integer | XXXXXXXX    |

**Response JSON Object**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  | XXXXXXX     |
| `driver_id` | integer | XXXXXXX     |

**Status Codes**

| Code  | Description |
| ----- | ----------- |
| `200` | XXXXXXXX    |
| `400` | XXXXXXXX    |

**Example Request**

```http
GET /deliveries/?status=pending&page=1&limit=10 HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_ACCESS_TOKEN
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

###### New delivery request

```{http:post} {base_uri}/user/delivery/new/

```

Make new delivery request

**Request Body**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  | XXXXXX      |
| `driver_id` | integer | XXXXXX      |

**Response JSON Object**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  | XXXXX       |
| `driver_id` | integer | XXXXX       |

**Status Codes**

| Code  | Description |
| ----- | ----------- |
| `200` | XXXXXXXX    |
| `400` | XXXXXXXX    |

**Example Request**

```http
GET /deliveries/?status=pending&page=1&limit=10 HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_ACCESS_TOKEN
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

###### Fetch delivery requests (user)

```{http:post} {base_uri}/user/delivery/requests/

```

Fetch all delivery requests by user

**Request Body**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  | XXXXXXX     |
| `driver_id` | integer | XXXXXXX     |

**Response JSON Object**

| Parameter   | Type    | Description |
| ----------- | ------- | ----------- |
| `status`    | string  | XXXXXX      |
| `driver_id` | integer | XXXXXX      |

**Status Codes**

| Code  | Description |
| ----- | ----------- |
| `200` | XXXXXXX     |
| `400` | XXXXXXX     |

**Example Request**

```http
GET /deliveries/?status=pending&page=1&limit=10 HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_ACCESS_TOKEN
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

###### New (quote) request

```{http:post} {base_uri}/saas/delivery/quote/

```

---

###### Confirm quote payment

```{http:post} {base_uri}/saas/delivery/payment_quote/

```

---

###### Track delivery

```{http:post} {base_uri}/saas/delivery/track

```

---

###### Get delivery request details

```{http:post} {base_uri}/saas/delivery/get

```

---

###### Get delivery request details

```{http:post} {base_uri}/saas/delivery/service

```

---

###### Get delivery request details

```{http:post} {base_uri}/saas/delivery/fetch

```

---

###### Get request status

```{http:post} {base_uri}/saas/delivery/status

```

---

###### Get delivery requests (dispatch)

```{http:post} {base_uri}/dispatch/delivery/all

```

---

###### Start delivery request

```{http:post} {base_uri}/dispatch/delivery/start

```

---

###### Accept delivery request

```{http:post} {base_uri}/dispatch/delivery/accept

```

---

###### Complete delivery request

```{http:post} {base_uri}/dispatch/delivery/complete

```

---

###### Update delivery request status

```{http:post} {base_uri}/dispatch/delivery/status

```

---
