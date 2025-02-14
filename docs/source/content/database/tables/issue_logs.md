# Issue Logs

**Table Name:** `issue_logs`  
**Description:** Stores information about registered users.

## Columns

| Column Name | Data Type                                              | Description                                           |
| ----------- | ------------------------------------------------------ | ----------------------------------------------------- |
| id          | `INT` `(PK)`                                           | Unique identifier for each reported issue.            |
| agent       | `VARCHAR(255)`                                         | Name or unique identifier of the assigned agent.      |
| client      | `VARCHAR(255)`                                         | Name or unique identifier of the client.              |
| issue       | `VARCHAR(100)`                                         | Type of issue (e.g., late delivery, damaged item).    |
| message     | `TEXT` `(UNIQUE)`                                      | Unique message describing the issue.                  |
| postedBy    | `VARCHAR(255)`                                         | Name or identifier of the person reporting the issue. |
| created     | `DATETIME`                                             | Timestamp when the issue was reported.                |
| modified    | `DATETIME`                                             | Last updated timestamp.                               |
| status      | `ENUM('pending', 'in-progress', 'resolved', 'closed')` | Current status of the issue.                          |

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
