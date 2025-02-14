# Issue

**Table Name:** `dispatch`  
**Description:** Stores information about registered users.

## Columns

| Column Name | Data Type                                                  | Description                                      |
| ----------- | ---------------------------------------------------------- | ------------------------------------------------ |
| id          | `INT` **`(PK, AUTO_INCREMENT)`**                           | Unique identifier for each delivery.             |
| client      | `VARCHAR(255)`                                             | Name or unique identifier of the client.         |
| agent       | `VARCHAR(255)`                                             | Name or unique identifier of the assigned agent. |
| delivery    | `VARCHAR(50)`                                              | Delivery type (e.g., express, scheduled).        |
| name        | `VARCHAR(255)` **`(UNIQUE)`**                              | Unique name associated with the delivery.        |
| phone       | `VARCHAR(20)`                                              | Contact phone number of the agent.               |
| email       | `VARCHAR(255)`                                             | Email address of the agent.                      |
| category    | `VARCHAR(255)`                                             | Category of delivery (e.g., logistics, food).    |
| title       | `VARCHAR(255)`                                             | Title or label associated with the delivery.     |
| description | `TEXT`                                                     | Additional information about the delivery.       |
| created     | `DATETIME`                                                 | Timestamp when the delivery was created.         |
| modified    | `DATETIME`                                                 | Last updated timestamp.                          |
| status      | `ENUM('pending', 'in-progress', 'completed', 'cancelled')` | Current status of the delivery.                  |

### Relationships

- **Orders (`orders.user_id` → `users.id`)**: Each user can place multiple orders.
- **Transactions (`transactions.user_id` → `users.id`)**: Each user can make payments.

## `sp_get_user_orders`

**Purpose:** Retrieves all orders for a given user.

### Parameters:

- `user_id` (INT) - The ID of the user.

### SQL Definition:

```sql
CREATE PROCEDURE sp_get_user_orders(IN user_id INT)
BEGIN
    SELECT * FROM orders WHERE orders.user_id = user_id;
END;
```
