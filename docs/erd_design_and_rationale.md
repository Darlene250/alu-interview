# MoMo Transaction Analyzer ERD Design and Rationale

## Entity List and Attributes

### 1. Users (Customers)
- user_id (PK, INT, AUTO_INCREMENT)
- phone_number (VARCHAR, UNIQUE)
- name (VARCHAR, NULLABLE)
- created_at (DATETIME)

### 2. Transactions
- transaction_id (PK, INT, AUTO_INCREMENT)
- transaction_code (VARCHAR, UNIQUE)
- transaction_date (DATETIME)
- amount (DECIMAL)
- description (VARCHAR)
- sender_id (FK to Users.user_id)
- receiver_id (FK to Users.user_id, NULLABLE)
- category_id (FK to Transaction_Categories.category_id)

### 3. Transaction_Categories
- category_id (PK, INT, AUTO_INCREMENT)
- category_name (VARCHAR, UNIQUE)
- description (VARCHAR)

### 4. System_Logs
- log_id (PK, INT, AUTO_INCREMENT)
- log_time (DATETIME)
- log_level (VARCHAR)
- message (TEXT)
- transaction_id (FK to Transactions.transaction_id, NULLABLE)

### 5. Transaction_Participants (Junction Table for M:N)
- transaction_id (FK to Transactions.transaction_id)
- user_id (FK to Users.user_id)
- role (ENUM: 'sender', 'receiver', 'other')
- PRIMARY KEY (transaction_id, user_id)

## Relationships
- One user can participate in many transactions (as sender or receiver)
- Each transaction has one category
- System logs may reference a transaction
- Many-to-many between Users and Transactions resolved by Transaction_Participants

## Rationale (to be expanded to 250+ words)

The design of the MoMo Transaction Analyzer database is driven by the need to efficiently store, process, and analyze mobile money transaction data, while ensuring data integrity, scalability, and ease of reporting. The core entities—Users, Transactions, Transaction_Categories, System_Logs, and Transaction_Participants—were identified based on the structure of typical MoMo SMS/XML data and the business requirements for transaction analysis.

The Users table captures unique customer information, using phone numbers as a key identifier. This allows the system to distinguish between senders and receivers, and to support future features such as user profiles or contact management. The Transactions table is central to the schema, recording all transaction details, including references to the sender, receiver, and transaction category. By using foreign keys, the design enforces referential integrity and ensures that every transaction is linked to valid users and categories.

The Transaction_Categories table enables flexible classification of transactions (e.g., received, sent, payment, transfer, airtime), making it easy to add new categories as business needs evolve. The System_Logs table is included to provide robust traceability and auditing for all data processing activities, supporting both operational monitoring and compliance requirements.

A key design decision is the inclusion of the Transaction_Participants junction table, which resolves the many-to-many relationship between users and transactions. This supports scenarios where multiple users may be involved in a single transaction (such as group payments or shared accounts), and allows for clear role assignment (sender, receiver, or other).

Overall, this schema is designed for clarity, normalization, and future growth. It supports efficient queries, accurate reporting, and easy integration with analytics or dashboard tools. The use of primary and foreign keys, appropriate data types, and normalization principles ensures both data quality and performance.

[Replace this file with your diagram export (PNG/PDF) and expand the rationale as needed.]
