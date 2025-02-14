# Users

```{tip}
Helpful tips can be added like this.
```

**Table Name:** `users` <br>
**Description:** Stores information about registered users.

## Columns

| Column Name  | Data Type                              | Description                                         |
| ------------ | -------------------------------------- | --------------------------------------------------- |
| id           | `INT` `(PRIMARY KEY)`                  | Unique identifier for each user.                    |
| type         | `ENUM('admin', 'customer', 'vendor')`  | Type of user in the system.                         |
| name         | `VARCHAR(255)`                         | Full name of the user.                              |
| phone        | `VARCHAR(20)`                          | Contact phone number.                               |
| email        | `VARCHAR(255)` `(UNIQUE)`              | Email address of the user.                          |
| description  | `TEXT`                                 | Additional information about the user.              |
| address      | `TEXT`                                 | Full physical address of the user.                  |
| latitude     | `DECIMAL(10,7)`                        | Latitude coordinate of the user’s location.         |
| longitude    | `DECIMAL(10,7)`                        | Longitude coordinate of the user’s location.        |
| avatar       | `VARCHAR(255)`                         | URL of the user's profile image.                    |
| login_status | `BOOLEAN`                              | Whether the user is currently logged in.            |
| created      | `DATETIME`                             | Timestamp when the user was created.                |
| modified     | `DATETIME`                             | Last updated timestamp.                             |
| status       | `ENUM('active', 'inactive', 'banned')` | Current status of the user.                         |
| auth         | `BOOLEAN`                              | Whether the user is authenticated (`TRUE`/`FALSE`). |
| login_count  | `INT` `(DEFAULT 0)`                    | Number of times the user has logged in.             |

## Relationships

- **Orders (`orders.user_id` → `users.id`)**: Each user can place multiple orders.
- **Transactions (`transactions.user_id` → `users.id`)**: Each user can make payments.
