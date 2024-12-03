import os
import csv

# Define the column index to check (H corresponds to index 7 since it's the 8th column, zero-indexed)
COLUMN_INDEX = 7
EMAIL_OUTPUT_FILE = "all_emails.csv"
EXCLUDED_EMAIL = "landon@postoakrealty.com"

# Get all CSV files in the current directory
csv_files = [file for file in os.listdir() if file.endswith('.csv')]

# Set to collect unique email addresses
unique_emails = set()

# Process each CSV file
for file in csv_files:
    try:
        # Read the CSV file
        with open(file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        if len(rows) == 0:
            print(f"File {file} is empty. Skipping.")
            continue

        # Separate header and data
        header = rows[0]
        data = rows[1:]

        # Check if COLUMN_INDEX is valid
        if COLUMN_INDEX >= len(header):
            print(f"Column index {COLUMN_INDEX} out of range in {file}. Skipping.")
            continue

        # Sort rows: Rows with values in column H come first
        rows_with_values = [row for row in data if row[COLUMN_INDEX].strip()]
        rows_without_values = [row for row in data if not row[COLUMN_INDEX].strip()]
        sorted_data = rows_with_values + rows_without_values

        # Collect email addresses
        for row in rows_with_values:
            email = row[COLUMN_INDEX].strip()
            if email and email != EXCLUDED_EMAIL:  # Ensure email is not empty and not excluded
                unique_emails.add(email)

        # Overwrite the original file with sorted data
        with open(file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(sorted_data)

        print(f"Processed and updated the file: {file}.")

    except Exception as e:
        print(f"An error occurred while processing {file}: {e}")

# Write all collected unique email addresses to a single CSV file
try:
    with open(EMAIL_OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Email'])  # Write header
        for email in sorted(unique_emails):  # Sort emails for consistent order
            writer.writerow([email])
    print(f"Collected all unique email addresses (excluding '{EXCLUDED_EMAIL}') and saved them to {EMAIL_OUTPUT_FILE}.")
except Exception as e:
    print(f"An error occurred while saving email addresses: {e}")
