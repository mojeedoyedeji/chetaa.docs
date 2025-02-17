(delivery_table)=

# Delivery

```{tip}
Helpful tips can be added like this.
```

**Table Name:** `delivery` <br>
**Description:** Stores information about registered users.

## Columns

| Column Name           | Data Type                                                  | Description                                                 |
| --------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| id                    | `VARCHAR(255)` `(PK)`                                      | Unique identifier for each order.                           |
| type                  | `VARCHAR(50)`                                              | Type of service (e.g., delivery, transportation).           |
| channel               | `VARCHAR(50)`                                              | The platform where the delivery service was requested from  |
| category              | `ENUM('service', 'quote')`                                 | Order category (e.g., logistics, moving, express delivery). |
| period                | `VARCHAR(50)`                                              |                                                             |
| pickup_date           | `DATETIME`                                                 | Scheduled pickup date and time.                             |
| pickup_name           | `VARCHAR(255)`                                             | Name of the sender at the pickup location.                  |
| pickup_address        | `TEXT`                                                     | Full address for pickup.                                    |
| pickup_phone          | `VARCHAR(20)`                                              | Contact phone number at pickup location.                    |
| pickup_latitude       | `DECIMAL(10,7)`                                            | Latitude coordinate of pickup location.                     |
| pickup_longitude      | `DECIMAL(10,7)`                                            | Longitude coordinate of pickup location.                    |
| destination_name      | `VARCHAR(255)`                                             | Name of the receiver at the delivery location.              |
| destination_address   | `TEXT`                                                     | Full address for delivery.                                  |
| destination_phone     | `VARCHAR(20)`                                              | Contact phone number at the delivery location.              |
| destination_latitude  | `DECIMAL(10,7)`                                            | Latitude coordinate of delivery location.                   |
| destination_longitude | `DECIMAL(10,7)`                                            | Longitude coordinate of delivery location.                  |
| tags                  | `TEXT`                                                     | Tags or labels for categorization.                          |
| description           | `TEXT`                                                     | Additional details about the order.                         |
| client_id             | `INT` `(FK)`                                               | Reference to the `users.id` (Client placing the order).     |
| agent_id              | `INT` `(FK)`                                               | Reference to the `agents.id` (Assigned delivery agent).     |
| agent_name            | `VARCHAR(255)`                                             | Name of the assigned agent.                                 |
| service_id            | `INT` `(FK)`                                               | Reference to the `services.id` (Selected service).          |
| service_title         | `VARCHAR(255)`                                             | Title of the selected service.                              |
| dispatch              | `BOOLEAN`                                                  | Whether the order has been dispatched.                      |
| created               | `DATETIME`                                                 | Time when the order was created.                            |
| service_price         | `DECIMAL(10,2)`                                            | Price of the service.                                       |
| service_description   | `TEXT`                                                     | Description of the service selected.                        |
| service_tags          | `TEXT`                                                     | Tags for the service.                                       |
| service_coverage      | `VARCHAR(255)`                                             | Geographic coverage area of the service.                    |
| service_withinState   | `BOOLEAN`                                                  | Whether the service is available within the state only.     |
| payment_ref           | `VARCHAR(50)`                                              | Reference number for payment transaction.                   |
| service_fromState     | `VARCHAR(100)`                                             | State from which the service starts.                        |
| service_toState       | `VARCHAR(100)`                                             | Destination state for the service.                          |
| service_exceptions    | `TEXT`                                                     | Any exceptions or restrictions for the service.             |
| quote_price           | `DECIMAL(10,2)`                                            | Estimated price for the service quote.                      |
| quote_status          | `ENUM('pending', 'accepted', 'rejected')`                  | Status of the price quote.                                  |
| total                 | `DECIMAL(10,2)`                                            | Total price of the order.                                   |
| weight                | `DECIMAL(10,2)`                                            | Total price of the order.                                   |
| status                | `ENUM('pending', 'in-progress', 'completed', 'cancelled')` | Current status of the order.                                |
| modified              | `DATETIME`                                                 | Last updated timestamp.                                     |

## Relationships

- Orders (`orders.user_id` → `users.id`): Each user can place multiple orders.
- Transactions (`transactions.user_id` → `users.id`): Each user can make payments.
