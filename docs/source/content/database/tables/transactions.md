# Transactions

```{tip}
Helpful tips can be added like this.
```

**Table Name:** `users` <br>
**Description:** Stores information about registered users.

## Columns

| Column Name | Data Type                                                         | Description                                          |
| ----------- | ----------------------------------------------------------------- | ---------------------------------------------------- |
| id          | `INT` `(PK, AUTO_INCREMENT)`                                      | Unique identifier for each transaction.              |
| agent       | `INT` `(FK → agents.id)`                                          | Reference to the agent involved in the transaction.  |
| client      | `INT` `(FK → users.id)`                                           | Reference to the client involved in the transaction. |
| amount      | `DECIMAL(10,2)`                                                   | Amount of the transaction.                           |
| transaction | `VARCHAR(255)` `(UNIQUE)`                                         | Unique transaction reference or ID.                  |
| purpose     | `TEXT`                                                            | Description of the transaction purpose.              |
| category    | `VARCHAR(100)`                                                    | Category of the transaction (e.g., payment, refund). |
| status      | `ENUM('pending', 'completed', 'failed')`                          | Current status of the transaction.                   |
| created     | `TIMESTAMP DEFAULT CURRENT_TIMESTAMP`                             | Timestamp when the transaction was created.          |
| modified    | `TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` | Last updated timestamp.                              |

## Relationships

- **Orders (`orders.user_id` → `users.id`)**: Each user can place multiple orders.
- **Transactions (`transactions.user_id` → `users.id`)**: Each user can make payments.
