import csv

# Data to be written to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John Doe', 28, 'New York'],
    ['Jane Smith', 35, 'Los Angeles'],
    ['Mike Johnson', 42, 'Chicago']
]

# File path/name where CSV will be saved
csv_file = 'example.csv'

# Writing data to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'CSV file "{csv_file}" has been created successfully.')
