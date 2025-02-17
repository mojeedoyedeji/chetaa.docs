# Delivery

Version: `1.0`  
Base URL: `https://api.chetaa.com/`

###### Introduction

Delivery requests can be either a `service` or `quote` request.

- Service: A service request is a request made by selecting a fixed price service from a delivery agent.
- Quote: A delivery quote request can be requested from the delivery agent by the user (customer or business) owner.

Different behaviours are expected depending on the delivery `category` attribute in the {ref}`delivery_table` table schema

###### Fetch all delivery requests

```{http:post} /{base_uri}/agent/delivery/all/

```

Returns all delivery requests for an agent

**Request Body**

| Parameter | Type   | Description                        |
| --------- | ------ | ---------------------------------- |
| `agent`   | string | The unique identifier of the agent |

**Response JSON Object**

| Parameter  | Type   | Description               |
| ---------- | ------ | ------------------------- |
| `delivery` | Array  | List of delivery requests |
| `message`  | String | API response message      |
| `status`   | String | API response status       |

**Status Codes**

| Code  | Description                               |
| ----- | ----------------------------------------- |
| `200` | Successful retrieval of delivery requests |
| `400` | Bad request (invalid parameters)          |

**Example Request**

```javascript
// Sample JavaScript code to interact with Chetaa API

const apiUrl = "https://api.chetaa.com/agent/delivery/all";
const apiKey = "your_api_key_here";

async function fetchDeliveries() {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ agent: "your_agent_id_here" }),
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
  "response": {
    "delivery": [
      {
        "id": "079715730682879",
        "type": "instant",
        "channel": "saas",
        "category": "service",
        "period": "",
        "pickup_date": "",
        "pickup_name": "Opeyemi",
        "pickup_address": "Ikotun - Egbe Road, Lagos, Nigeria",
        "pickup_phone": "07065363100",
        "pickup_latitude": "6.5397223",
        "pickup_longitude": "3.2923167",
        "destination_name": "Opeyemi",
        "destination_address": "Oshodi Bridge, Oshodi pedestrian Overpass, Ikeja, Nigeria",
        "destination_phone": "07065363100",
        "destination_latitude": "6.5560772",
        "destination_longitude": "3.3518473",
        "tags": "Any,Heavy",
        "description": "",
        "client_id": "",
        "user_id": null,
        "agent_id": "068711885506646",
        "agent_name": "Delivery Hub",
        "service_id": "501749082987583",
        "service_title": "Hello world",
        "dispatch": "919010122704826",
        "created": "2021-12-03T10:41:06+00:00",
        "service_price": "2000",
        "service_description": "Hello world. Helli world. Hello world. Hello world. Hello world. ",
        "service_tags": "Any",
        "service_coverage": "intra",
        "service_withinState": "Anambra",
        "payment_ref": "OFFLINE",
        "service_fromState": "",
        "service_toState": "",
        "service_exceptions": "None",
        "quote_price": null,
        "quote_status": null,
        "total": "2130",
        "weight": null,
        "status": "completed",
        "modified": "2021-12-03T10:41:06+00:00"
      }
    ]
  },
  "message": "ok",
  "status": "success"
}
```

---

###### Confirm request (service)

```{http:post} {base_uri}/agent/delivery/confirm_service/

```

Confirm the delivery request

```{admonition} Description

After the user (customer or business) makes a request, the request needs to be confirmed by the delivery agent in offline payment mode. Once the payment is confirmed independently by the delivery agent, the service is confirmed. This triggers a sequence of events:

  - The transaction is logged as an offline transaction.

  - A notification object is created for the agent and registered dispatchers via email and SMS.

  - SMS messages are sent to both the pickup and delivery locations.

  - A delivery log object is created, and the payment status is updated to "confirmed."
```

```{warning}
⚠️ **Upcoming Change:** This API endpoint will be updated in a future release.
- The `POST /agent/delivery/all/` request format **will change**.
- Expect an update to authentication handling.
- Ensure you follow future release notes.
```

**Request Body**

| Parameter | Type   | Description                           |
| --------- | ------ | ------------------------------------- |
| `id`      | object | The unique id of the delivery request |

**Response JSON Object**

| Parameter  | Type   | Description                      |
| ---------- | ------ | -------------------------------- |
| `delivery` | object | Delivery request details         |
| `logs`     | array  | List of related transaction logs |
| `message`  | String | API response message             |
| `status`   | String | API response status              |

**Status Codes**

| Code  | Description                             |
| ----- | --------------------------------------- |
| `200` | Successfully confirmed delivery request |
| `400` | Bad request (invalid parameters)        |

**Example Request**

```javascript
// Sample JavaScript code to interact with Chetaa API

const apiUrl = "https://api.chetaa.com/agent/delivery/confirm_service";
const apiKey = "your_api_key_here";

async function confirmDelivery() {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: "delivery_request_id" }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
  } catch (error) {
    console.error("Error confirming delivery:", error);
  }
}

// Call the function
confirmDelivery();
```

**Example Response**

```json
{
  "response": {
    "delivery": {
      "id": "079715730682879",
      "type": "instant",
      "channel": "saas",
      "category": "service",
      "period": "",
      "pickup_date": "",
      "pickup_name": "Opeyemi",
      "pickup_address": "Ikotun - Egbe Road, Lagos, Nigeria",
      "pickup_phone": "07065363100",
      "pickup_latitude": "6.5397223",
      "pickup_longitude": "3.2923167",
      "destination_name": "Opeyemi",
      "destination_address": "Oshodi Bridge, Oshodi pedestrian Overpass, Ikeja, Nigeria",
      "destination_phone": "07065363100",
      "destination_latitude": "6.5560772",
      "destination_longitude": "3.3518473",
      "tags": "Any,Heavy",
      "description": "",
      "client_id": "",
      "user_id": null,
      "agent_id": "068711885506646",
      "agent_name": "Delivery Hub",
      "service_id": "501749082987583",
      "service_title": "Hello world",
      "dispatch": "919010122704826",
      "created": "2021-12-03T10:41:06+00:00",
      "service_price": "2000",
      "service_description": "Hello world. Helli world. Hello world. Hello world. Hello world. ",
      "service_tags": "Any",
      "service_coverage": "intra",
      "service_withinState": "Anambra",
      "payment_ref": "OFFLINE",
      "service_fromState": "",
      "service_toState": "",
      "service_exceptions": "None",
      "quote_price": null,
      "quote_status": null,
      "total": "2130",
      "weight": null,
      "status": "new",
      "modified": "2021-12-03T10:41:06+00:00",
      "agent": {
        "id": "068711885506646",
        "name": "Delivery Hub",
        "phone": "07065363100",
        "email": "mojeed.oyedeji@gmail.com",
        "username": "deliveryhub",
        "address": "Lagos Nigeria",
        "latitude": null,
        "longitude": null,
        "state": "Lagos",
        "subscription": "100",
        "fleet": "10",
        "logo": "003435182804451.png",
        "description": "Hello World",
        "referral": "M7yxZlAB",
        "bank_name": "Guaranty Trust Bank",
        "bank_code": "058",
        "bank_account": "0152922008",
        "paystack_account": "ACCT_s416q4ketrh0qjf",
        "bvn": "1234",
        "auth": "013712",
        "login_count": "0",
        "login_status": "false",
        "status": "verified",
        "created": "2021-09-25T10:14:04+00:00",
        "modified": "2021-09-25T10:14:04+00:00",
        "whatsapp": "07065363100",
        "facebook": null,
        "instagram": "deliveryhub",
        "twitter": "deliveryhub",
        "available": "true"
      }
    },
    "logs": [
      {
        "id": "000642631975338",
        "request": "079715730682879",
        "type": "message",
        "message": "Payment confirmed",
        "author": "Delivery Hub",
        "channel": "all",
        "created": "2025-02-16 20:40:11",
        "modified": "2025-02-16 20:40:11",
        "status": "active"
      }
    ]
  },
  "message": "ok",
  "status": "success"
}
```

###### Fetch delivery logs

```{http:post} {base_uri}/agent/delivery/logs/

```

Fetches the logs associated with a specific delivery request.

**Request Body**

| Parameter  | Type   | Description                           |
| ---------- | ------ | ------------------------------------- |
| `delivery` | string | The unique id of the delivery request |

**Response JSON Object**

| Parameter | Type   | Description              |
| --------- | ------ | ------------------------ |
| `logs`    | Array  | List of transaction logs |
| `message` | String | API response message     |
| `status`  | String | API response status      |

**Status Codes**

| Code  | Description                             |
| ----- | --------------------------------------- |
| `200` | Successfully confirmed delivery request |
| `400` | Bad request (invalid parameters)        |

**Example Request**

```javascript
// Sample JavaScript code to interact with Chetaa API
const apiUrl = "https://api.chetaa.com/agent/delivery/logs";
const apiKey = "your_api_key_here";

async function fetchDeliveryLogs() {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: "delivery_request_id" }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
  } catch (error) {
    console.error("Error confirming delivery:", error);
  }
}

// Call the function
fetchDeliveryLogs();
```

**Example Response**

```json
{
  "response": {
    "logs": [
      {
        "id": "000642631975338",
        "request": "079715730682879",
        "type": "message",
        "message": "Payment confirmed",
        "author": "Delivery Hub",
        "channel": "all",
        "created": "2025-02-16 20:40:11",
        "modified": "2025-02-16 20:40:11",
        "status": "active"
      }
    ]
  },
  "message": "ok",
  "status": "success"
}
```

---

###### New Delivery Request (Service, Store Front)

```{http:post} {base_uri}/saas/delivery/service

```

Make new delivery (service) request

**Request Body**

| Parameter               | Type    | Description                                       |
| ----------------------- | ------- | ------------------------------------------------- |
| `type`                  | string  | Type of delivery request (e.g., "instant")        |
| `period`                | string  | Time period for the delivery (empty if not set)   |
| `pickup_date`           | string  | Pickup date (empty if not set)                    |
| `pickup_name`           | string  | Name of the person at pickup location             |
| `pickup_phone`          | string  | Contact number at pickup location                 |
| `pickup_address`        | string  | Full address of pickup location                   |
| `pickup_latitude`       | float   | Latitude of pickup location                       |
| `pickup_longitude`      | float   | Longitude of pickup location                      |
| `destination_name`      | string  | Name of the person at destination                 |
| `destination_address`   | string  | Full address of destination location              |
| `destination_phone`     | string  | Contact number at destination location            |
| `destination_latitude`  | float   | Latitude of destination location                  |
| `destination_longitude` | float   | Longitude of destination location                 |
| `tags`                  | string  | Comma-separated tags for delivery (e.g., "Heavy") |
| `description`           | string  | Additional description of delivery request        |
| `client_id`             | string  | Unique identifier for the client                  |
| `agent_id`              | string  | Unique identifier for the agent handling delivery |
| `agent_name`            | string  | Name of the agent handling delivery               |
| `service_id`            | string  | Unique identifier for the service being used      |
| `service_title`         | string  | Title of the service                              |
| `dispatch`              | string  | Dispatch reference ID                             |
| `created`               | string  | Timestamp of request creation                     |
| `service_price`         | string  | Price of the service                              |
| `service_description`   | string  | Description of the delivery service               |
| `service_tags`          | string  | Tags related to the service                       |
| `service_coverage`      | string  | Coverage type (e.g., "intra")                     |
| `service_withinState`   | string  | Name of the state where the service operates      |
| `service_fromState`     | string  | Origin state for the service                      |
| `service_toState`       | string  | Destination state for the service                 |
| `service_exceptions`    | string  | Exceptions or limitations for the service         |
| `payment_ref`           | string  | Reference for payment (e.g., "OFFLINE")           |
| `total`                 | integer | Total amount to be paid                           |
| `service_pricing`       | string  | Pricing type (e.g., "fixed")                      |
| `mode`                  | string  | Payment mode (e.g., "offline")                    |

**Response JSON Object**

| Parameter     | Type   | Description                     |
| ------------- | ------ | ------------------------------- |
| `delivery_id` | String | Unique id of the delivery entry |
| `message`     | String | API response message            |
| `status`      | String | API response status             |

**Example Request**

```javascript
const apiUrl = "https://api.chetaa.com/saas/delivery/service";
const apiKey = "your_api_key_here";

async function newDeliveryService() {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: "delivery_request_id" }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
  } catch (error) {
    console.error("Error confirming delivery:", error);
  }
}

// Call the function
newDeliveryService();
```

**Example Response**

```json
{
  "response": {
    "id": "000642631975338"
  },
  "message": "ok",
  "status": "success"
}
```

---

###### Track delivery (Storefront)

```{http:post} {base_uri}/saas/delivery/track

```

Track the delivery request status

**Request Body**

| Parameter | Type   | Description                           |
| --------- | ------ | ------------------------------------- |
| id        | string | The unique id of the delivery request |

**Response JSON Object**

| Parameter  | Type   | Description                                             |
| ---------- | ------ | ------------------------------------------------------- |
| `delivery` | object | An object containing attributes of the delivery request |
| `logs`     | Array  | A delivery log array                                    |
| `message`  | String | API response message                                    |
| `status`   | String | API response status                                     |

**Example Request**

```javascript
const apiUrl = "https://api.chetaa.com/saas/delivery/track";
const apiKey = "your_api_key_here";

async function trackRequest() {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: "delivery_request_id" }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
  } catch (error) {
    console.error("Error confirming delivery:", error);
  }
}

// Call the function
trackRequest();
```

**Example Response**

```json
{
  "response": {
    "delivery": {
      "id": "079715730682879",
      "type": "instant",
      "channel": "saas",
      "category": "service",
      "period": "",
      "payment_mode": null,
      "pickup_date": "",
      "pickup_name": "Opeyemi",
      "pickup_address": "Ikotun - Egbe Road, Lagos, Nigeria",
      "pickup_phone": "07065363100",
      "pickup_latitude": "6.5397223",
      "pickup_longitude": "3.2923167",
      "destination_name": "Opeyemi",
      "destination_address": "Oshodi Bridge, Oshodi pedestrian Overpass, Ikeja, Nigeria",
      "destination_phone": "07065363100",
      "destination_latitude": "6.5560772",
      "destination_longitude": "3.3518473",
      "tags": "Any,Heavy",
      "description": "",
      "client_id": "",
      "user_id": null,
      "agent_id": "068711885506646",
      "agent_name": "Delivery Hub",
      "service_id": "501749082987583",
      "service_title": "Hello world",
      "dispatch": "919010122704826",
      "created": "2021-12-03T10:41:06+00:00",
      "service_price": "2000",
      "service_description": "Hello world. Helli world. Hello world. Hello world. Hello world. ",
      "service_tags": "Any",
      "service_coverage": "intra",
      "service_withinState": "Anambra",
      "payment_ref": "OFFLINE",
      "service_fromState": "",
      "service_toState": "",
      "service_exceptions": "None",
      "quote_price": null,
      "quote_status": null,
      "total": "2130",
      "weight": null,
      "status": "new",
      "modified": "2021-12-03T10:41:06+00:00",
      "agent": {
        "id": "068711885506646",
        "name": "Delivery Hub",
        "phone": "07065363100",
        "email": "mojeed.oyedeji@gmail.com",
        "username": "deliveryhub",
        "address": "Lagos Nigeria",
        "latitude": null,
        "longitude": null,
        "state": "Lagos",
        "subscription": "100",
        "fleet": "10",
        "logo": "003435182804451.png",
        "description": "Hello World",
        "referral": "M7yxZlAB",
        "bank_name": "Guaranty Trust Bank",
        "bank_code": "058",
        "bank_account": "0152922008",
        "paystack_account": "ACCT_s416q4ketrh0qjf",
        "bvn": "1234",
        "auth": "013712",
        "login_count": "0",
        "login_status": "false",
        "status": "verified",
        "created": "2021-09-25T10:14:04+00:00",
        "modified": "2021-09-25T10:14:04+00:00",
        "whatsapp": "07065363100",
        "facebook": null,
        "instagram": "deliveryhub",
        "twitter": "deliveryhub",
        "available": "true"
      }
    },
    "logs": [
      {
        "id": "000642631975338",
        "request": "079715730682879",
        "type": "message",
        "message": "Payment confirmed",
        "author": "Delivery Hub",
        "channel": "all",
        "created": "2025-02-16 20:40:11",
        "modified": "2025-02-16 20:40:11",
        "status": "active"
      }
    ]
  },
  "message": "ok",
  "status": "success"
}
```

---

###### Get delivery requests (dispatch)

```{http:post} {base_uri}/dispatch/delivery/all

```

Fetch all request registered under the host agent

**Request Body**

| Parameter | Type   | Description                                                           |
| --------- | ------ | --------------------------------------------------------------------- |
| agent     | string | The unique id of the delivery agent the dispatcher is registered with |

**Response JSON Object**

| Parameter  | Type   | Description                                             |
| ---------- | ------ | ------------------------------------------------------- |
| `delivery` | Object | An object containing attributes of the delivery request |
| `message`  | String | API response message                                    |
| `status`   | String | API response status                                     |

**Example Request**

```javascript
const apiUrl = "https://api.chetaa.com/saas/dispatch/delivery/all";
const apiKey = "your_api_key_here";

async function fetchAllDelivery() {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ agent: "delivery_request_id" }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
  } catch (error) {
    console.error("Error confirming delivery:", error);
  }
}

// Call the function
fetchAllDelivery();
```

**Example Response**

```json
{
  "response": {
    "delivery": [
      {
        "id": "079715730682879",
        "type": "instant",
        "channel": "saas",
        "category": "service",
        "period": "",
        "payment_mode": null,
        "pickup_date": "",
        "pickup_name": "Opeyemi",
        "pickup_address": "Ikotun - Egbe Road, Lagos, Nigeria",
        "pickup_phone": "07065363100",
        "pickup_latitude": "6.5397223",
        "pickup_longitude": "3.2923167",
        "destination_name": "Opeyemi",
        "destination_address": "Oshodi Bridge, Oshodi pedestrian Overpass, Ikeja, Nigeria",
        "destination_phone": "07065363100",
        "destination_latitude": "6.5560772",
        "destination_longitude": "3.3518473",
        "tags": "Any,Heavy",
        "description": "",
        "client_id": "",
        "user_id": null,
        "agent_id": "068711885506646",
        "agent_name": "Delivery Hub",
        "service_id": "501749082987583",
        "service_title": "Hello world",
        "dispatch": "919010122704826",
        "created": "2021-12-03T10:41:06+00:00",
        "service_price": "2000",
        "service_description": "Hello world. Helli world. Hello world. Hello world. Hello world. ",
        "service_tags": "Any",
        "service_coverage": "intra",
        "service_withinState": "Anambra",
        "payment_ref": "OFFLINE",
        "service_fromState": "",
        "service_toState": "",
        "service_exceptions": "None",
        "quote_price": null,
        "quote_status": null,
        "total": "2130",
        "weight": null,
        "status": "new",
        "modified": "2021-12-03T10:41:06+00:00"
      }
    ]
  },
  "message": "ok",
  "status": "success"
}
```

---

###### Accept delivery request

```{http:post} {base_uri}/dispatch/delivery/accept

```

Delivery dispatcher accepts the delivery request

**Request Body**

| Parameter  | Type   | Description                              |
| ---------- | ------ | ---------------------------------------- |
| `delivery` | string | The unique id of the delivery request    |
| `agent`    | string | The unique id of the delivery agent      |
| `dispatch` | string | The unique id of the delivery dispatcher |

**Response JSON Object**

| Parameter  | Type   | Description                                             |
| ---------- | ------ | ------------------------------------------------------- |
| `delivery` | Object | An object containing attributes of the delivery request |
| `logs`     | Array  | An array object containing delivery logs                |
| `message`  | String | API response message                                    |
| `status`   | String | API response status                                     |

**Example Request**

```javascript
const apiUrl = "https://api.chetaa.com/saas/dispatch/delivery/all";
const apiKey = "your_api_key_here";

async function acceptRequest(body) {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
  } catch (error) {
    console.error("Error confirming delivery:", error);
  }
}

acceptRequest(body);
```

**Example Response**

```json
{
  "response": {
    "delivery": {
      "id": "079715730682879",
      "type": "instant",
      "channel": "saas",
      "category": "service",
      "period": "",
      "payment_mode": null,
      "pickup_date": "",
      "pickup_name": "Opeyemi",
      "pickup_address": "Ikotun - Egbe Road, Lagos, Nigeria",
      "pickup_phone": "07065363100",
      "pickup_latitude": "6.5397223",
      "pickup_longitude": "3.2923167",
      "destination_name": "Opeyemi",
      "destination_address": "Oshodi Bridge, Oshodi pedestrian Overpass, Ikeja, Nigeria",
      "destination_phone": "07065363100",
      "destination_latitude": "6.5560772",
      "destination_longitude": "3.3518473",
      "tags": "Any,Heavy",
      "description": "",
      "client_id": "",
      "user_id": null,
      "agent_id": "068711885506646",
      "agent_name": "Delivery Hub",
      "service_id": "501749082987583",
      "service_title": "Hello world",
      "dispatch": "919010122704826",
      "created": "2021-12-03T10:41:06+00:00",
      "service_price": "2000",
      "service_description": "Hello world. Helli world. Hello world. Hello world. Hello world. ",
      "service_tags": "Any",
      "service_coverage": "intra",
      "service_withinState": "Anambra",
      "payment_ref": "OFFLINE",
      "service_fromState": "",
      "service_toState": "",
      "service_exceptions": "None",
      "quote_price": null,
      "quote_status": null,
      "total": "2130",
      "weight": null,
      "status": "new",
      "modified": "2021-12-03T10:41:06+00:00"
    },
    "logs": []
  },
  "message": "ok",
  "status": "success"
}
```

---

###### Start delivery request

```{http:post} {base_uri}/dispatch/delivery/start

```

Delivery dispatcher starts fulfilling the delivery request

**Request Body**

| Parameter  | Type   | Description                              |
| ---------- | ------ | ---------------------------------------- |
| `delivery` | string | The unique id of the delivery request    |
| `dispatch` | string | The unique id of the delivery dispatcher |

**Response JSON Object**

| Parameter  | Type   | Description                                             |
| ---------- | ------ | ------------------------------------------------------- |
| `delivery` | Object | An object containing attributes of the delivery request |
| `logs`     | Array  | An array object containing delivery logs                |
| `message`  | String | API response message                                    |
| `status`   | String | API response status                                     |

**Example Request**

```javascript
const apiUrl = "https://api.chetaa.com/saas/dispatch/delivery/all";
const apiKey = "your_api_key_here";

async function startRequest(body) {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
  } catch (error) {
    console.error("Error confirming delivery:", error);
  }
}

startRequest(body);
```

**Example Response**

```json
{
  "response": {
    "delivery": {
      "id": "079715730682879",
      "type": "instant",
      "channel": "saas",
      "category": "service",
      "period": "",
      "payment_mode": null,
      "pickup_date": "",
      "pickup_name": "Opeyemi",
      "pickup_address": "Ikotun - Egbe Road, Lagos, Nigeria",
      "pickup_phone": "07065363100",
      "pickup_latitude": "6.5397223",
      "pickup_longitude": "3.2923167",
      "destination_name": "Opeyemi",
      "destination_address": "Oshodi Bridge, Oshodi pedestrian Overpass, Ikeja, Nigeria",
      "destination_phone": "07065363100",
      "destination_latitude": "6.5560772",
      "destination_longitude": "3.3518473",
      "tags": "Any,Heavy",
      "description": "",
      "client_id": "",
      "user_id": null,
      "agent_id": "068711885506646",
      "agent_name": "Delivery Hub",
      "service_id": "501749082987583",
      "service_title": "Hello world",
      "dispatch": "919010122704826",
      "created": "2021-12-03T10:41:06+00:00",
      "service_price": "2000",
      "service_description": "Hello world. Helli world. Hello world. Hello world. Hello world. ",
      "service_tags": "Any",
      "service_coverage": "intra",
      "service_withinState": "Anambra",
      "payment_ref": "OFFLINE",
      "service_fromState": "",
      "service_toState": "",
      "service_exceptions": "None",
      "quote_price": null,
      "quote_status": null,
      "total": "2130",
      "weight": null,
      "status": "new",
      "modified": "2021-12-03T10:41:06+00:00"
    },
    "logs": []
  },
  "message": "ok",
  "status": "success"
}
```

---

###### Complete delivery request

```{http:post} {base_uri}/dispatch/delivery/complete

```

Delivery dispatcher marks the delivery request complete

**Request Body**

| Parameter  | Type   | Description                              |
| ---------- | ------ | ---------------------------------------- |
| `delivery` | string | The unique id of the delivery request    |
| `dispatch` | string | The unique id of the delivery dispatcher |

**Response JSON Object**

| Parameter  | Type   | Description                                             |
| ---------- | ------ | ------------------------------------------------------- |
| `delivery` | Object | An object containing attributes of the delivery request |
| `logs`     | Array  | An array object containing delivery logs                |
| `message`  | String | API response message                                    |
| `status`   | String | API response status                                     |

**Example Request**

```javascript
const apiUrl = "https://api.chetaa.com/saas/dispatch/delivery/all";
const apiKey = "your_api_key_here";

async function completeRequest(body) {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
  } catch (error) {
    console.error("Error confirming delivery:", error);
  }
}

completeRequest(body);
```

**Example Response**

```json
{
  "response": {
    "delivery": {
      "id": "079715730682879",
      "type": "instant",
      "channel": "saas",
      "category": "service",
      "period": "",
      "payment_mode": null,
      "pickup_date": "",
      "pickup_name": "Opeyemi",
      "pickup_address": "Ikotun - Egbe Road, Lagos, Nigeria",
      "pickup_phone": "07065363100",
      "pickup_latitude": "6.5397223",
      "pickup_longitude": "3.2923167",
      "destination_name": "Opeyemi",
      "destination_address": "Oshodi Bridge, Oshodi pedestrian Overpass, Ikeja, Nigeria",
      "destination_phone": "07065363100",
      "destination_latitude": "6.5560772",
      "destination_longitude": "3.3518473",
      "tags": "Any,Heavy",
      "description": "",
      "client_id": "",
      "user_id": null,
      "agent_id": "068711885506646",
      "agent_name": "Delivery Hub",
      "service_id": "501749082987583",
      "service_title": "Hello world",
      "dispatch": "919010122704826",
      "created": "2021-12-03T10:41:06+00:00",
      "service_price": "2000",
      "service_description": "Hello world. Helli world. Hello world. Hello world. Hello world. ",
      "service_tags": "Any",
      "service_coverage": "intra",
      "service_withinState": "Anambra",
      "payment_ref": "OFFLINE",
      "service_fromState": "",
      "service_toState": "",
      "service_exceptions": "None",
      "quote_price": null,
      "quote_status": null,
      "total": "2130",
      "weight": null,
      "status": "new",
      "modified": "2021-12-03T10:41:06+00:00"
    },
    "logs": []
  },
  "message": "ok",
  "status": "success"
}
```

---

###### Update delivery request status

```{http:post} {base_uri}/dispatch/delivery/status

```

Delivery dispatcher adds a status message to the delivery logs

**Request Body**

| Parameter  | Type   | Description                              |
| ---------- | ------ | ---------------------------------------- |
| `delivery` | string | The unique id of the delivery request    |
| `dispatch` | string | The unique id of the delivery dispatcher |
| `message`  | string | The status text by the dispatcher        |

**Response JSON Object**

| Parameter  | Type   | Description                                             |
| ---------- | ------ | ------------------------------------------------------- |
| `delivery` | Object | An object containing attributes of the delivery request |
| `logs`     | Array  | An array object containing delivery logs                |
| `message`  | String | API response message                                    |
| `status`   | String | API response status                                     |

**Example Request**

```javascript
const apiUrl = "https://api.chetaa.com/saas/dispatch/delivery/all";
const apiKey = "your_api_key_here";

async function postStatus(body) {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
  } catch (error) {
    console.error("Error confirming delivery:", error);
  }
}

postStatus(body);
```

**Example Response**

```json
{
  "response": {
    "delivery": {
      "id": "079715730682879",
      "type": "instant",
      "channel": "saas",
      "category": "service",
      "period": "",
      "payment_mode": null,
      "pickup_date": "",
      "pickup_name": "Opeyemi",
      "pickup_address": "Ikotun - Egbe Road, Lagos, Nigeria",
      "pickup_phone": "07065363100",
      "pickup_latitude": "6.5397223",
      "pickup_longitude": "3.2923167",
      "destination_name": "Opeyemi",
      "destination_address": "Oshodi Bridge, Oshodi pedestrian Overpass, Ikeja, Nigeria",
      "destination_phone": "07065363100",
      "destination_latitude": "6.5560772",
      "destination_longitude": "3.3518473",
      "tags": "Any,Heavy",
      "description": "",
      "client_id": "",
      "user_id": null,
      "agent_id": "068711885506646",
      "agent_name": "Delivery Hub",
      "service_id": "501749082987583",
      "service_title": "Hello world",
      "dispatch": "919010122704826",
      "created": "2021-12-03T10:41:06+00:00",
      "service_price": "2000",
      "service_description": "Hello world. Helli world. Hello world. Hello world. Hello world. ",
      "service_tags": "Any",
      "service_coverage": "intra",
      "service_withinState": "Anambra",
      "payment_ref": "OFFLINE",
      "service_fromState": "",
      "service_toState": "",
      "service_exceptions": "None",
      "quote_price": null,
      "quote_status": null,
      "total": "2130",
      "weight": null,
      "status": "new",
      "modified": "2021-12-03T10:41:06+00:00"
    },
    "logs": []
  },
  "message": "ok",
  "status": "success"
}
```

---

###### Get delivery request details

```{http:post} {base_uri}/saas/delivery/get

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

###### New (quote) request

```{http:post} {base_uri}/saas/delivery/quote/

```

---

###### Confirm payment (quote)

```{http:post} {base_uri}/saas/delivery/payment_quote/

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
