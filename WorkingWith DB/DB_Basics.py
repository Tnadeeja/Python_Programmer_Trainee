"""
CSV Database Management System

This module provides a simple database system using CSV files for storage.
It implements basic CRUD (Create, Read, Update, Delete) operations.

Database Structure:
- Uses a single table stored in a CSV file
- Each row represents one record
- First row contains column headers (field names)
- First column is always the unique ID (primary key)

Example CSV structure:
ID,Title,Author,Genre,Year,Location
1,Harry Potter,Rowling,Fantasy,1997,Shelf A
"""

# Import required modules
import csv
import os

# Global Variables
current_ID = 1       # Primary key counter for new records
new_additions = []   # Temporary storage for new records before saving to file
filename = "database.csv"  # Default CSV database filename
fields = []          # List to store column headers
data = []            # List to store all records from the CSV file

def read_csv_file():
    """
    Read data from the CSV file and populate the global data list.
    Also updates the current_ID to be one more than the maximum ID found.
    """
    global current_ID, fields, data
    
    # Clear existing data
    data = []
    
    try:
        with open(filename, mode='r', newline='') as file:
            # Use DictReader to read rows as dictionaries
            reader = csv.DictReader(file)
            
            # Store field names if file is not empty
            if reader.fieldnames:
                fields = reader.fieldnames
                
                # Read all rows and convert to list of dictionaries
                for row in reader:
                    data.append(row)
                    
                    # Update current_ID to be max ID + 1
                    try:
                        row_id = int(row.get('ID', 0))
                        if row_id >= current_ID:
                            current_ID = row_id + 1
                    except (ValueError, TypeError):
                        pass
                        
    except FileNotFoundError:
        # If file doesn't exist, create it with default fields
        fields = ['ID', 'Name', 'Email', 'Phone']
        write_csv_file()

def write_csv_file():
    """
    Write data from global data list and new_additions to the CSV file.
    """
    try:
        # Check if we need to write headers (new file or empty file)
        write_header = not os.path.exists(filename) or os.path.getsize(filename) == 0
        
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            
            if write_header:
                writer.writeheader()
                
            # Write existing data
            writer.writerows(data)
            
            # Write new additions and clear the list
            if new_additions:
                writer.writerows(new_additions)
                new_additions.clear()
                
    except Exception as e:
        print(f"Error writing to file: {e}")

def add_record(record_data):
    """
    Add a new record to the database.
    
    Args:
        record_data (dict): Dictionary containing field-value pairs for the new record
    """
    global current_ID
    
    # Add ID to the record
    record_data['ID'] = current_ID
    current_ID += 1
    
    # Add to new additions (will be written to file on save)
    new_additions.append(record_data)
    return record_data

def search_records(field, value):
    """
    Search for records where the specified field matches the given value.
    
    Args:
        field (str): Field name to search in
        value: Value to search for
        
    Returns:
        list: List of matching records
    """
    results = []
    
    # Search in existing data
    for record in data:
        if str(record.get(field, '')).lower() == str(value).lower():
            results.append(record)
            
    # Search in new additions
    for record in new_additions:
        if str(record.get(field, '')).lower() == str(value).lower():
            results.append(record)
            
    return results

def update_record(record_id, updated_data):
    """
    Update an existing record with new data.
    
    Args:
        record_id: ID of the record to update
        updated_data (dict): Dictionary of fields to update
        
    Returns:
        bool: True if update was successful, False otherwise
    """
    # Search in existing data
    for record in data:
        if str(record.get('ID', '')) == str(record_id):
            record.update(updated_data)
            return True
            
    # Search in new additions
    for record in new_additions:
        if str(record.get('ID', '')) == str(record_id):
            record.update(updated_data)
            return True
            
    return False

def delete_record(record_id):
    """
    Delete a record from the database.
    
    Args:
        record_id: ID of the record to delete
        
    Returns:
        bool: True if deletion was successful, False otherwise
    """
    # Search in existing data
    for i, record in enumerate(data):
        if str(record.get('ID', '')) == str(record_id):
            del data[i]
            return True
            
    # Search in new additions
    for i, record in enumerate(new_additions):
        if str(record.get('ID', '')) == str(record_id):
            del new_additions[i]
            return True
            
    return False

def display_record(record):
    """
    Display a single record in a readable format.
    
    Args:
        record (dict): The record to display
    """
    if not record:
        print("No record to display")
        return
        
    print("\n" + "="*50)
    for field, value in record.items():
        print(f"{field}: {value}")
    print("="*50 + "\n")

def save_changes():
    """
    Save all changes to the CSV file.
    """
    write_csv_file()
    print("Changes saved successfully!")

def display_all_records():
    """
    Display all records in a tabular format.
    """
    if not data and not new_additions:
        print("No records found in the database.")
        return
    
    # Get all records
    all_records = data + new_additions
    
    # Print header
    print("\n" + "="*80)
    print("DATABASE RECORDS")
    print("="*80)
    
    # Print column headers
    if fields:
        header = " | ".join(field.ljust(15) for field in fields)
        print(header)
        print("-" * len(header))
    
    # Print each record
    for record in all_records:
        row = " | ".join(str(record.get(field, '')).ljust(15) for field in fields)
        print(row)
    
    print("="*80 + "\n")

def search_database(search_term):
    """
    Search for records containing the search term in any field.
    
    Args:
        search_term (str): The term to search for
        
    Returns:
        list: List of matching records
    """
    if not search_term:
        return []
        
    search_term = str(search_term).lower()
    results = []
    
    # Search in both existing data and new additions
    for record in data + new_additions:
        for value in record.values():
            if search_term in str(value).lower():
                results.append(record)
                break
                
    return results

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("DATABASE MANAGEMENT SYSTEM")
    print("="*50)
    print("1. View all records")
    print("2. Add new record")
    print("3. Search records")
    print("4. Update a record")
    print("5. Delete a record")
    print("6. Save changes")
    print("0. Exit")
    print("="*50)

def get_user_choice():
    """Get and validate user's menu choice."""
    while True:
        try:
            choice = int(input("\nEnter your choice (0-6): "))
            if 0 <= choice <= 6:
                return choice
            print("Please enter a number between 0 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_record_data():
    """Get field values for a new record from the user."""
    record = {}
    for field in fields:
        if field != 'ID':  # Skip ID as it's auto-generated
            value = input(f"Enter {field}: ")
            record[field] = value
    return record

if __name__ == "__main__":
    # Initialize the database
    read_csv_file()
    
    print("\n" + "="*50)
    print("WELCOME TO THE DATABASE MANAGEMENT SYSTEM")
    print("="*50)
    print(f"Database file: {filename}")
    print(f"Current ID counter: {current_ID}")
    print(f"Fields: {', '.join(fields)}")
    print(f"Total records: {len(data) + len(new_additions)}")
    
    # Main program loop
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 0:  # Exit
            if new_additions:
                save = input("\nYou have unsaved changes. Save before exiting? (y/n): ").lower()
                if save == 'y':
                    save_changes()
            print("\nThank you for using the Database Management System!")
            break
            
        elif choice == 1:  # View all records
            display_all_records()
            
        elif choice == 2:  # Add new record
            print("\nADD NEW RECORD")
            print("-" * 30)
            record_data = get_record_data()
            new_record = add_record(record_data)
            print("\nRecord added successfully!")
            display_record(new_record)
            
        elif choice == 3:  # Search records
            search_term = input("\nEnter search term: ")
            if search_term:
                results = search_database(search_term)
                if results:
                    print(f"\nFound {len(results)} matching records:")
                    for i, record in enumerate(results, 1):
                        print(f"\nRecord {i}:")
                        display_record(record)
                else:
                    print("\nNo matching records found.")
                    
        elif choice == 4:  # Update record
            record_id = input("\nEnter the ID of the record to update: ")
            if record_id:
                # Find the record
                found = False
                all_records = data + new_additions
                for record in all_records:
                    if str(record.get('ID', '')) == record_id:
                        print("\nCurrent record:")
                        display_record(record)
                        print("\nEnter new values (press Enter to keep current value):")
                        updates = {}
                        for field in fields:
                            if field != 'ID':  # Don't allow changing the ID
                                current_val = record.get(field, '')
                                new_val = input(f"{field} [{current_val}]: ")
                                if new_val:  # Only update if user entered a new value
                                    updates[field] = new_val
                        
                        if updates:
                            update_record(record_id, updates)
                            print("\nRecord updated successfully!")
                        else:
                            print("\nNo changes made.")
                        found = True
                        break
                        
                if not found:
                    print("\nRecord not found.")
                    
        elif choice == 5:  # Delete record
            record_id = input("\nEnter the ID of the record to delete: ")
            if record_id:
                if delete_record(record_id):
                    print("\nRecord deleted successfully!")
                else:
                    print("\nRecord not found.")
                    
        elif choice == 6:  # Save changes
            save_changes()
