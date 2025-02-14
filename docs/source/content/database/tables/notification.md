# Notification

**Table Name:** `notification`  
**Description:** Stores information about registered users.

### Columns

| Column Name | Data Type                                      | Description                                     |
| ----------- | ---------------------------------------------- | ----------------------------------------------- |
| id          | `INT` `(PK)`                                   | Unique identifier for each message.             |
| sender      | `VARCHAR(255)`                                 | Name or unique identifier of the sender.        |
| recipient   | `VARCHAR(255)`                                 | Name or unique identifier of the recipient.     |
| message     | `TEXT`                                         | Content of the message.                         |
| title       | `VARCHAR(255)` `(UNIQUE)`                      | Subject or title of the message.                |
| channel     | `VARCHAR(100)`                                 | Communication channel (e.g., email, chat, SMS). |
| created     | `DATETIME`                                     | Timestamp when the message was sent.            |
| updated     | `DATETIME`                                     | Last updated timestamp.                         |
| status      | `ENUM('pending', 'sent', 'delivered', 'read')` | Current status of the message.                  |

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
