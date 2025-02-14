# Agents

**Table Name:** `agents`  
**Description:** Stores information about registered users.

### Columns

| Column Name      | Data Type                                                         | Description                                          |
| ---------------- | ----------------------------------------------------------------- | ---------------------------------------------------- |
| id               | `INT` (PK )                                                       | Unique identifier for users.                         |
| name             | `VARCHAR(255)`                                                    | Full name of the agent.                              |
| phone            | `VARCHAR(20)`                                                     | Phone number of the agent.                           |
| email            | `VARCHAR(255)` (UNIQUE)                                           | Email address of the agent.                          |
| username         | `VARCHAR(100)` (UNIQUE)                                           | Unique username for login.                           |
| address          | `TEXT`                                                            | Full address of the agent.                           |
| latitude         | `DECIMAL(10,7)`                                                   | Latitude coordinate for the agent’s location.        |
| longitude        | `DECIMAL(10,7)`                                                   | Longitude coordinate for the agent’s location.       |
| state            | `VARCHAR(100)`                                                    | State or province of the agent.                      |
| subscription     | `ENUM('free', 'premium', 'enterprise')`                           | Subscription type of the user.                       |
| fleet            | `INT` (DEFAULT 0)                                                 | Number of vehicles owned (for fleet managers).       |
| logo             | `VARCHAR(255)`                                                    | URL path to the agent’s logo.                        |
| description      | `TEXT`                                                            | Profile description of the agent.                    |
| referral         | `VARCHAR(50)`                                                     | Referral code used by the agent.                     |
| bank_name        | `VARCHAR(100)`                                                    | Name of the agent’s bank.                            |
| bank_code        | `VARCHAR(20)`                                                     | Bank code of the agent’s bank.                       |
| bank_account     | `VARCHAR(20)`                                                     | Bank account number of the agent.                    |
| paystack_account | `VARCHAR(255)`                                                    | Paystack account ID for payments.                    |
| bvn              | `VARCHAR(11)`                                                     | Bank Verification Number (BVN) of the agent.         |
| auth             | `BOOLEAN`                                                         | Whether the agent is authenticated (`TRUE`/`FALSE`). |
| login_count      | `INT` (DEFAULT 0)                                                 | Number of times the agent has logged in.             |
| login_status     | `BOOLEAN`                                                         | Whether the agent is currently logged in.            |
| status           | `ENUM('active', 'inactive', 'banned')`                            | Current status of the agent.                         |
| created          | `TIMESTAMP DEFAULT CURRENT_TIMESTAMP`                             | Time when the user was created.                      |
| modified         | `TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` | Last modified timestamp.                             |
| whatsapp         | `VARCHAR(20)`                                                     | WhatsApp number of the agent.                        |
| facebook         | `VARCHAR(255)`                                                    | Facebook profile link.                               |
| instagram        | `VARCHAR(255)`                                                    | Instagram profile link.                              |
| twitter          | `VARCHAR(255)`                                                    | Twitter profile link.                                |
| available        | `BOOLEAN`                                                         | Whether the agent is available for service.          |

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
