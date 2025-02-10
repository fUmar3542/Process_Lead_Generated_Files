import os
import csv
from urllib.parse import urlparse


def extract_company_name(url):
    """Extracts the company name from a given URL."""
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        domain = domain.replace("www.", "")  # Remove www.
        company_name = domain.split('.')[0]  # Get the main company name
        return company_name
    except Exception as e:
        print(f"Error extracting company name from {url}: {e}")
        return None


def generate_email(company_name):
    """Generates an email like careers@company.com"""
    if company_name:
        return f"careers@{company_name}.com"
    return None


def process_csv_files():
    """Reads all CSV files in the directory, extracts websites, and creates emails."""
    output_data = [["Website", "Company Name", "Generated Email"]]

    for file in os.listdir():
        if file.endswith(".csv"):
            with open(file, mode="r", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                if 'Website' in reader.fieldnames:
                    for row in reader:
                        url = row['Website'].strip()
                        if url:
                            company_name = extract_company_name(url)
                            email = generate_email(company_name)
                            output_data.append([url, company_name, email])

    # Save to a new CSV file
    with open("result.csv", mode="w", newline="", encoding="utf-8") as out_file:
        writer = csv.writer(out_file)
        writer.writerows(output_data)

    print("Result saved to result.csv")


if __name__ == "__main__":
    process_csv_files()
