"""
📘 Database Basics – Python (CSV Based)

1️⃣ What is a Database?
A database is an organized collection of data that allows:
- Easy storage
- Easy searching
- Easy updating
- Easy maintenance

In this project:
- We use ONE table
- The table is stored in a CSV file
- CSV = Comma Separated Values (works like a spreadsheet such as Excel)

--------------------------------------------------

2️⃣ Database Structure (Table Concept)

- Fields       → Column names (ID, Title, Author, Genre, Year, Location)
- Record       → One complete row (one book)
- Attributes   → Data values of a single record
- Primary Key → A unique value for each record (ID)

Example table:

ID, Title, Author, Genre, Year, Location
1, Harry Potter, Rowling, Fantasy, 1997, Shelf A

--------------------------------------------------

3️⃣ Requirements of Our Database

The database should be able to:
- Save data to a file
- Read data from a file
- Create new records
- Display all records
- Search records
- Display search results

--------------------------------------------------

4️⃣ CSV Files

- Data is stored line by line
- Each line represents ONE record
- Values are separated using commas
- First line contains field names (headers)
- CSV files can be opened using Excel, Word, etc.

--------------------------------------------------

5️⃣ Import Statements

- External modules must be imported first
- We use the csv module

Purpose of csv module:
- Read CSV files
- Write CSV files
- Convert rows into dictionaries automatically

--------------------------------------------------

6️⃣ Global Variables (Used Across the Program)

current_ID      → Used as the primary key (unique ID)
new_additions   → Stores newly added records before saving
filename        → Name of the CSV database file
fields          → List of column names
data            → Stores all records read from the file

These variables are shared across multiple functions.

--------------------------------------------------

7️⃣ Reading Data from the CSV File

- Open the CSV file in read mode
- Use csv.DictReader
- Each row becomes a dictionary
- Store each record inside the data list
- Update current_ID to avoid duplicate IDs

Why DictReader?
- It maps column names to values
- Makes searching and displaying easier

--------------------------------------------------

8️⃣ Creating a New Record

- Each record is stored as a dictionary
- Keys match the field names
- Values come from user input
- ID is generated automatically
- New records are stored in new_additions list
- ID is incremented after each addition

--------------------------------------------------

9️⃣ Displaying the Database

- Display column headers first
- Display all existing records
- Display newly added records
- Data is formatted to look like a table
- Uses spacing to align columns

--------------------------------------------------

🔟 Searching the Database

- User enters a search term
- Search runs across ALL fields
- Matches are case-insensitive
- Results are collected in a list
- If matches exist, display them
- If not, show "No records found"

--------------------------------------------------

1️⃣1️⃣ Main Program Loop

- Menu-driven program
- User can:
  1 → Add a book
  2 → Display all books
  3 → Search books
  X → Exit program
- Loop runs until user exits

--------------------------------------------------

1️⃣2️⃣ Saving Data to CSV

- Save only new records
- Open file in append mode
- Append means "add to the end"
- csv.DictWriter writes dictionaries as rows
- Prevents overwriting existing data

--------------------------------------------------

✅ Summary

- Database = structured data storage
- CSV acts as a simple database
- Python dictionaries map perfectly to database fields
- This system supports basic database operations:
  - Create
  - Read
  - Search
"""