# Places

```{tip}
Helpful tips can be added like this.
```

**Table Name:** `places` <br>
**Description:** Stores information about registered users.

## Columns

| Column Name | Data Type                               | Description                                             |
| ----------- | --------------------------------------- | ------------------------------------------------------- |
| id          | `INT` `(PK, AUTO_INCREMENT)`            | Unique identifier for each location.                    |
| client_id   | `INT` `(FK → clients.id)`               | Reference to the client who saved the location.         |
| title       | `VARCHAR(255)`                          | Name or label for the location.                         |
| address     | `TEXT`                                  | Full address of the location.                           |
| latitude    | `DECIMAL(10,7)`                         | Latitude coordinate of the location.                    |
| longitude   | `DECIMAL(10,7)`                         | Longitude coordinate of the location.                   |
| status      | `ENUM('active', 'inactive', 'expired')` | Current status of the saved location.                   |
| expires     | `DATETIME NULL`                         | Expiry date/time of the saved location (if applicable). |
| modified    | `DATETIME`                              | Last updated timestamp.                                 |

## Relationships

- **Orders (`orders.user_id` → `users.id`)**: Each user can place multiple orders.
- **Transactions (`transactions.user_id` → `users.id`)**: Each user can make payments.
