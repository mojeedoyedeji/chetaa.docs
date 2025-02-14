# Delivery Logs

```{tip}
Helpful tips can be added like this.
```

**Table Name:** `delivery_logs` <br>
**Description:** This table logs all user requests, including messages and their current status.

## Columns

| Column Name | Data Type                                           | Description                                     |
| ----------- | --------------------------------------------------- | ----------------------------------------------- |
| id          | `INT` `(PK)`                                        | Unique identifier for each request.             |
| request     | `TEXT`                                              | The content of the user's request.              |
| type        | `VARCHAR(100)`                                      | Type of request (e.g., complaint, inquiry).     |
| message     | `TEXT`                                              | Additional message details from the user.       |
| author      | `VARCHAR(255)`                                      | Name of the request's author.                   |
| channel     | `VARCHAR(100)`                                      | Source of the request (e.g., email, chat, API). |
| created     | `DATETIME`                                          | Timestamp when the request was created.         |
| modified    | `DATETIME`                                          | Last updated timestamp.                         |
| status      | `ENUM('pending', 'reviewed', 'resolved', 'closed')` | Current status of the request.                  |

## Relationships

- **Orders (`orders.user_id` → `users.id`)**: Each user can place multiple orders.
- **Transactions (`transactions.user_id` → `users.id`)**: Each user can make payments.
