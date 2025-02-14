# Dispatch

**Table Name:** `dispatch`  
**Description:** Stores information about registered users.

## Columns

| Column Name        | Data Type                                                         | Description                                    |
| ------------------ | ----------------------------------------------------------------- | ---------------------------------------------- |
| id                 | `INT` `(PK)`                                                      | Unique identifier for each agent.              |
| agent              | `VARCHAR(255)`                                                    | Agent's unique identifier or code.             |
| name               | `VARCHAR(255)`                                                    | Full name of the agent.                        |
| phone              | `VARCHAR(20)`                                                     | Phone number of the agent.                     |
| email              | `VARCHAR(255)` `(UNIQUE)`                                         | Email address of the agent.                    |
| avatar             | `VARCHAR(255)`                                                    | Profile picture URL of the agent.              |
| auth               | `VARCHAR(255)`                                                    | Authentication token or method.                |
| address            | `TEXT`                                                            | Full address of the agent.                     |
| latitude           | `DECIMAL(10,7)`                                                   | Latitude coordinate for the agent’s location.  |
| longitude          | `DECIMAL(10,7)`                                                   | Longitude coordinate for the agent’s location. |
| created            | `TIMESTAMP DEFAULT CURRENT_TIMESTAMP`                             | Timestamp when the agent was registered.       |
| modified           | `TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` | Last updated timestamp.                        |
| state              | `VARCHAR(100)`                                                    | State or province where the agent operates.    |
| location           | `VARCHAR(255)`                                                    | City or specific area of the agent's location. |
| status             | `ENUM('active', 'inactive', 'banned')`                            | Current status of the agent.                   |
| location_latitude  | `DECIMAL(10,7)`                                                   | Latitude coordinate for a secondary location.  |
| location_longitude | `DECIMAL(10,7)`                                                   | Longitude coordinate for a secondary location. |

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
