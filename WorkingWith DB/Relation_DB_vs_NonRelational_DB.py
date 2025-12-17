"""
📘 3.2 Relational vs Non-Relational Databases (Brief Notes)

--------------------------------------------------
1️⃣ Fundamentals of RDBMS (Relational Databases)
--------------------------------------------------
• RDBMS stores data in tables (also called relations)
• Tables consist of:
  - Rows → Records / Tuples
  - Columns → Attributes

Example:
Student Table
Attributes: student_id, name, city, age
Records: Each student row

• A relation is a set of tuples
• Duplicate records are NOT allowed
• Each table has a PRIMARY KEY
  - Uniquely identifies each record

--------------------------------------------------
2️⃣ Relationships & Foreign Keys
--------------------------------------------------
• Tables can be connected using FOREIGN KEYS
• A foreign key:
  - References the primary key of another table

Example:
Student Table → student_id (PK)
Course Table → course_id (PK)
Enrollment Table:
  - student_id (FK)
  - course_id (FK)
  - marks

• Combined student_id + course_id
  → Primary key of Enrollment table

--------------------------------------------------
3️⃣ Indexes
--------------------------------------------------
• Index improves database performance
• Helps fetch records faster
• Index is a special data structure
• Reduces disk access time

--------------------------------------------------
4️⃣ SQL (Structured Query Language)
--------------------------------------------------
• Used to interact with RDBMS
• SQL operations:
  - INSERT  → Create
  - SELECT  → Read
  - UPDATE  → Update
  - DELETE  → Delete

• Known as CRUD operations
• SQL keywords are NOT case sensitive

--------------------------------------------------
5️⃣ Domains & Cardinality
--------------------------------------------------
Domain:
• Set of valid values for an attribute
• Example: Age → Only positive integers

Cardinality:
• Measures uniqueness of values in a column
• High Cardinality → Mostly unique values (Primary Key)
• Low Cardinality → Many repeated values (Gender, City)

--------------------------------------------------
6️⃣ Integrity Constraints
--------------------------------------------------
Used to maintain accuracy and consistency

Entity Integrity:
• Every table must have a primary key
• Primary key must be unique and NOT NULL

Referential Integrity:
• Foreign key must match a primary key
• Or must be NULL

--------------------------------------------------
7️⃣ Entity Relationships
--------------------------------------------------
One-to-One:
• One record relates to one record
• Example: Person ↔ Passport

One-to-Many:
• One record relates to many records
• Example: Customer ↔ Orders

Many-to-Many:
• Many records relate to many records
• Example: Students ↔ Courses
• Implemented using a junction table

--------------------------------------------------
8️⃣ Centralized vs Distributed Databases
--------------------------------------------------
Centralized DB:
• All data stored in one location
• Simple but hard to scale

Distributed DB:
• Data stored across multiple locations
• Example:
  - Sri Lanka data in Sri Lanka
  - India data in India
• Improves scalability and availability

--------------------------------------------------
9️⃣ Big Data Concept
--------------------------------------------------
Big Data is defined by 4 Vs:

Volume:
• Huge amounts of data

Variety:
• Structured, Semi-Structured (JSON, XML)
• Unstructured (Images, Videos, Text)

Velocity:
• High speed data generation

Veracity:
• Data quality uncertainty

--------------------------------------------------
🔟 Why RDBMS Fails for Big Data
--------------------------------------------------
• Hard to scale for massive volume
• Not designed for high-speed data
• Poor support for unstructured data

--------------------------------------------------
1️⃣1️⃣ NoSQL Databases
--------------------------------------------------
• NoSQL = Not Only SQL
• Non-tabular data storage
• Designed for Big Data & scalability

Types of NoSQL Databases:

1. Document Store
   - JSON-like documents

2. Key-Value Store
   - Simple key-value pairs

3. Wide-Column Store
   - Column-based storage

4. Graph Store
   - Nodes, edges, relationships

--------------------------------------------------
✅ Summary
--------------------------------------------------
• RDBMS → Structured, relational, SQL-based
• NoSQL → Flexible, scalable, Big Data friendly
• Choose DB type based on data & use case
"""
