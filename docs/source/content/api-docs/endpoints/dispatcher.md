# Dispatcher

Version: `1.0`  
Base URL: `https://api.chetaa.com/`

###### Introduction

The Dispatcher API provides endpoints for managing dispatch agents, allowing businesses and customers to request delivery services efficiently. The API supports creating, updating, and removing dispatchers, as well as fetching delivery records and managing dispatcher profiles. This documentation outlines the necessary authentication, request formats, and expected responses for seamless integration.

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

###### Add new dispatcher (agent)

```{http:post} {base_uri}/agent/dispatch/add/

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
console.log("Hello, World!");
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

###### Update dispatcher details

```{http:post} {base_uri}/agent/dispatch/update/

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

###### Remove dispatcher (agent)

```{http:get} {base_uri}/agent/dispatch/remove/

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

###### Fetch all dispatchers (agent)

```{http:get} {base_uri}/agent/dispatch/all/

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

###### Find dispatcher record

```{http:get} {base_uri}/dispatch/find

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

###### Create dispatcher profile

```{http:get} {base_uri}/dispatch/profile/create

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

###### Get dispatcher's agent

```{http:get} {base_uri}/dispatch/agent/get

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

###### Update profile

```{http:post} {base_uri}/dispatch/profile/update/

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

###### Upload photo (dispatcher)

```{http:post} {base_uri}/dispatch/images/upload/

```

Update the dispatcher's avatar photo.

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
