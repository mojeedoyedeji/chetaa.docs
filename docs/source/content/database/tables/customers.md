# Customers

```{tip}
Helpful tips can be added like this.
```

**Table Name:** `customers` <br>
**Description:** Stores information about registered users.

## Columns

| Column Name     | Data Type                                                         | Description                                         |
| --------------- | ----------------------------------------------------------------- | --------------------------------------------------- |
| id              | `INT` `PK, AUTO_INCREMENT`                                        | Unique identifier for users.                        |
| name            | `VARCHAR(255)`                                                    | Full name of the user.                              |
| phone           | `VARCHAR(20)`                                                     | Contact phone number of the user.                   |
| email           | ` VARCHAR(255)``UNIQUE `                                          | Email address of the user.                          |
| password        | `VARCHAR(255)`                                                    | Hashed password for authentication.                 |
| address         | `TEXT`                                                            | Full address of the user.                           |
| subscription_id | `INT` `FK → subscriptions.id`                                     | Reference to the user's subscription type.          |
| type            | `ENUM('admin', 'customer', 'vendor')`                             | User type or role in the system.                    |
| description     | `TEXT`                                                            | Additional user details or profile description.     |
| auth            | `BOOLEAN`                                                         | Whether the user is authenticated (`TRUE`/`FALSE`). |
| referral        | `VARCHAR(50)`                                                     | Referral code used by the user.                     |
| login_count     | `INT` `(DEFAULT 0)`                                               | Number of times the user has logged in.             |
| login_status    | `BOOLEAN`                                                         | Whether the user is currently logged in.            |
| account_status  | `ENUM('active', 'inactive', 'banned')`                            | Current status of the user's account.               |
| created         | `TIMESTAMP DEFAULT CURRENT_TIMESTAMP`                             | Timestamp when the user was created.                |
| modified        | `TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` | Last modified timestamp.                            |

## Relationships

- **Orders (`orders.user_id` → `users.id`)**: Each user can place multiple orders.
- **Transactions (`transactions.user_id` → `users.id`)**: Each user can make payments.
