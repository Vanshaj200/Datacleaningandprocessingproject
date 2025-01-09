# Datacleaningandprocessingproject
Datacleaningandprocessingproject over the following dataset ---

Import Pandas: It imports the Pandas library for data manipulation.
Load CSV: It reads the CSV file from the specified path.
Rename Columns: It renames the columns based on the provided mapping.
Inspect Data: It prints the first few rows of the DataFrame to verify the renaming.
Save Data: It saves the modified DataFrame to a new CSV file.

Data Inspection: You may want to inspect more details (like df.info(), df.describe(), etc.) to understand the structure and content of your data.
Error Handling: Adding basic error handling (e.g., try-except blocks) could be useful to handle potential issues like file not found or incorrect file format.
Further Cleaning: Depending on your data, you might need additional preprocessing steps like handling missing values, type conversions, or data filtering.

Error Handling:

FileNotFoundError: Catches if the file path is incorrect.
pd.errors.EmptyDataError: Catches if the file is empty.
pd.errors.ParserError: Catches parsing errors.
General Exception: Catches any other unexpected errors.
Data Inspection:

df.info(): Provides a summary of the DataFrame, including data types and non-null counts.
df.describe(): Gives descriptive statistics for numerical columns.
df.head(): Shows the first 5 rows of the DataFrame.
Handling Missing Values:

Fills missing numerical values with the mean.
Drops rows where 'Building_Type' is missing.
Checking for Duplicates:

Removes duplicate rows using df.drop_duplicates().
Saving the Cleaned Data:

Saves the cleaned DataFrame to a new CSV file.
