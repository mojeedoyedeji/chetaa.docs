# Subscription Table

```{tip}
Helpful tips can be added like this.
```

**Table Name:** `users` <br>
**Description:** Stores information about registered users.

## Columns

| Column Name | Data Type                             | Description                                               |
| ----------- | ------------------------------------- | --------------------------------------------------------- |
| id          | `INT` `(PK, AUTO_INCREMENT)`          | Unique identifier for each subscription.                  |
| client      | `INT` `(FK → users.id)`               | Reference to the client associated with the subscription. |
| plan        | `VARCHAR(255)`                        | Name or type of the subscription plan.                    |
| amount      | `DECIMAL(10,2)`                       | Cost of the subscription plan.                            |
| created     | `TIMESTAMP DEFAULT CURRENT_TIMESTAMP` | Timestamp when the subscription was created.              |
| expires     | `TIMESTAMP`                           | Expiration date of the subscription.                      |

## Relationships

- **Orders (`orders.user_id` → `users.id`)**: Each user can place multiple orders.
- **Transactions (`transactions.user_id` → `users.id`)**: Each user can make payments.
