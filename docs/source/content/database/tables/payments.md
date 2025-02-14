# Payments

**Table Name:** `notification`  
**Description:** Stores information about registered users.

### Columns

| Column Name | Data Type                                | Description                                   |
| ----------- | ---------------------------------------- | --------------------------------------------- |
| id          | `INT` **`(PK, AUTO_INCREMENT)`**         | Unique identifier for each transaction.       |
| client      | `VARCHAR(255)`                           | Name or unique identifier of the client.      |
| transaction | `VARCHAR(255)`                           | Transaction reference ID or unique code.      |
| purpose     | `TEXT`                                   | Purpose or description of the transaction.    |
| amount      | `DECIMAL(10,2)` **`(UNIQUE)`**           | Amount involved in the transaction.           |
| method      | `VARCHAR(100)`                           | Payment method (e.g., credit card, PayPal).   |
| status      | `ENUM('pending', 'completed', 'failed')` | Current status of the transaction.            |
| created     | `DATETIME`                               | Timestamp when the transaction was initiated. |
| modified    | `DATETIME`                               | Last updated timestamp.                       |

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
