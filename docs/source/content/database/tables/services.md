# Services

```{tip}
Helpful tips can be added like this.
```

**Table Name:** `users` <br>
**Description:** Stores information about registered users.

## Columns

| Column Name | Data Type                                    | Description                                       |
| ----------- | -------------------------------------------- | ------------------------------------------------- |
| id          | `INT` `(PK, AUTO_INCREMENT)`                 | Unique identifier for each service.               |
| agent       | `VARCHAR(255)` `(FK → agents.id)`            | Reference to the agent offering the service.      |
| title       | `VARCHAR(255)`                               | Name or title of the service.                     |
| description | `TEXT`                                       | Detailed description of the service.              |
| fromState   | `VARCHAR(100)`                               | State from which the service is available.        |
| toState     | `VARCHAR(100)`                               | Destination state where the service operates.     |
| withinState | `BOOLEAN`                                    | Whether the service is restricted to a state.     |
| exceptions  | `TEXT`                                       | Any restrictions or exceptions for the service.   |
| coverage    | `VARCHAR(255)`                               | Geographic coverage area of the service.          |
| tags        | `TEXT`                                       | Tags for categorization (e.g., logistics, cargo). |
| pricing     | `ENUM('fixed', 'negotiable')`                | Pricing type of the service.                      |
| price       | `DECIMAL(10,2)`                              | Standard price of the service.                    |
| maxprice    | `DECIMAL(10,2)`                              | Maximum price if pricing is negotiable.           |
| minprice    | `DECIMAL(10,2)`                              | Minimum price if pricing is negotiable.           |
| status      | `ENUM('active', 'inactive', 'discontinued')` | Current status of the service.                    |
| created     | `DATETIME`                                   | Timestamp when the service was created.           |
| modified    | `DATETIME`                                   | Last updated timestamp.                           |

## Relationships

- **Orders (`orders.user_id` → `users.id`)**: Each user can place multiple orders.
- **Transactions (`transactions.user_id` → `users.id`)**: Each user can make payments.
