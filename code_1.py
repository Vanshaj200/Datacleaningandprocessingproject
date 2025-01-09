import pandas as pd

# Load the CSV file
file_path = '/mnt/data/test_energy_data.csv'
df = pd.read_csv(file_path)
# Inspect the data
print(df.info())
print(df.describe())
print(df.head())

# Handle missing values
# Example: Fill missing numerical values with the mean, drop rows with missing categorical values
df.fillna(df.mean(), inplace=True)
df.dropna(subset=['categorical_column_name'], inplace=True)

# Convert data types if necessary
# Example: Convert date columns to datetime
df['date_column_name'] = pd.to_datetime(df['date_column_name'])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Rename columns if needed
df.rename(columns={'old_column_name': 'new_column_name'}, inplace=True)

# Optional: Normalize or filter data
# Example: Filter rows based on a condition
df = df[df['numerical_column_name'] > threshold_value]

# Save the cleaned data to a new CSV file
df.to_csv('/mnt/data/cleaned_energy_data.csv', index=False)


# import pandas as pd

# # Load the CSV file with error handling
# file_path = '/mnt/data/test_energy_data.csv'

# try:
#     # Load the CSV file
#     df = pd.read_csv(file_path)

#     # Rename the columns
#     df.rename(columns={
#         'Building Type  ': 'Building_Type',
#         'Square Footage': 'Square_Footage',
#         'Number of Occupants': 'Number_of_Occupants',
#         'Appliances Used\n': 'Appliances_Used',
#         ' Average Temperature': 'Average_Temperature',
#         ' Day of Week\n': 'Day_of_Week',
#         'Energy Consumption\n': 'Energy_Consumption'
#     }, inplace=True)

#     # Inspect the data
#     print("Data Info:")
#     print(df.info())  # Summary of the DataFrame
#     print("\nData Description:")
#     print(df.describe())  # Descriptive statistics for numerical columns
#     print("\nFirst 5 Rows of Data:")
#     print(df.head())  # First few rows of the DataFrame

#     # Handle missing values (Example: filling or dropping)
#     df.fillna(df.mean(), inplace=True)  # Fill missing numerical values with mean
#     df.dropna(subset=['Building_Type'], inplace=True)  # Drop rows where 'Building_Type' is missing

#     # Convert data types (if applicable)
#     # Example: Assuming there's a date column (replace 'date_column_name' with actual name)
#     # df['date_column_name'] = pd.to_datetime(df['date_column_name'])

#     # Check for duplicates and remove if any
#     df.drop_duplicates(inplace=True)

#     # Save the cleaned data to a new CSV file
#     cleaned_file_path = '/mnt/data/cleaned_energy_data.csv'
#     df.to_csv(cleaned_file_path, index=False)
#     print(f"Cleaned data saved to {cleaned_file_path}")

# except FileNotFoundError:
#     print(f"Error: The file at {file_path} was not found.")
# except pd.errors.EmptyDataError:
#     print("Error: The file is empty.")
# except pd.errors.ParserError:
#     print("Error: There was a problem parsing the file.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

