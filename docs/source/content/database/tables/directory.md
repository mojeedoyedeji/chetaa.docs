# Directory

```{tip}
Helpful tips can be added like this.
```

**Table Name:** `directory` <br>
**Description:** Stores information about registered users.

## Columns

| Column Name   | Data Type                              | Description                                             |
| ------------- | -------------------------------------- | ------------------------------------------------------- |
| id            | `INT` `(PK)`                           | Unique identifier for each business.                    |
| slug          | `VARCHAR(255)` `UNIQUE`                | SEO-friendly unique identifier (e.g., URL slug).        |
| name          | `VARCHAR(255)`                         | Business name.                                          |
| phone         | `VARCHAR(20)`                          | Contact phone number.                                   |
| email         | `VARCHAR(255)` `UNIQUE`                | Business email address.                                 |
| description   | `TEXT`                                 | Short description of the business.                      |
| whatsapp      | `VARCHAR(20)`                          | WhatsApp contact number.                                |
| twitter       | `VARCHAR(255)`                         | Twitter profile link.                                   |
| facebook      | `VARCHAR(255)`                         | Facebook profile link.                                  |
| instagram     | `VARCHAR(255)`                         | Instagram profile link.                                 |
| locations     | `TEXT`                                 | Areas or locations where the business operates.         |
| routes        | `TEXT`                                 | Common routes or coverage areas.                        |
| services      | `TEXT`                                 | List of services offered.                               |
| average_price | `DECIMAL(10,2)`                        | Average service price.                                  |
| min_price     | `DECIMAL(10,2)`                        | Minimum service price.                                  |
| state         | `VARCHAR(100)`                         | State or province where the business is based.          |
| address       | `TEXT`                                 | Full address of the business.                           |
| latitude      | `DECIMAL(10,7)`                        | Latitude coordinate of the business location.           |
| longitude     | `DECIMAL(10,7)`                        | Longitude coordinate of the business location.          |
| rating        | `DECIMAL(3,2)`                         | Business rating (1-5 scale).                            |
| auth          | `BOOLEAN`                              | Whether the business is authenticated (`TRUE`/`FALSE`). |
| verified      | `BOOLEAN`                              | Whether the business is verified (`TRUE`/`FALSE`).      |
| created       | `TIMESTAMP DEFAULT CURRENT_TIMESTAMP`  | Timestamp when the business was created.                |
| status        | `ENUM('active', 'inactive', 'banned')` | Current status of the business.                         |

## Relationships

- **Orders (`orders.user_id` → `users.id`)**: Each user can place multiple orders.
- **Transactions (`transactions.user_id` → `users.id`)**: Each user can make payments.
