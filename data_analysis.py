import pandas as pd
import matplotlib.pyplot as plt

try:
    # Load the CSV file
    data = pd.read_csv('attrition_availabledata_08.csv')

    # Check if the file is empty
    if data.empty:
        print("Error: The file is empty.")
    else:
        # Identify the last column name
        last_column = data.columns[-1]

        # Count 'Yes' and 'No' values
        counts = data[last_column].value_counts()

        # Print results
        print(f"Counts in column '{last_column}':")
        print(f"Yes: {counts.get('Yes', 0)}")
        print(f"No: {counts.get('No', 0)}")

        null_counts = data.isnull().sum()
        print("Total null values per column:")
        print(null_counts)

        for col in data.columns:
            #Descomentar para generar los plots de cada variable
            """plt.figure(figsize=(8, 5))  # Set figure size

            # If the column is numeric, plot a histogram
            if pd.api.types.is_numeric_dtype(data[col]):
                plt.hist(data[col].dropna(), bins=20, color='skyblue', edgecolor='black')
                plt.xlabel(col)
                plt.ylabel("Frequency")
                plt.title(f"Distribution of {col}")

            # If the column is categorical, plot a bar chart
            else:
                value_counts = data[col].value_counts()
                plt.bar(value_counts.index, value_counts.values, color='orange')
                plt.xlabel(col)
                plt.ylabel("Count")
                plt.title(f"Distribution of {col}")
                plt.xticks(rotation=45)  # Rotate labels for readability

            # Save the plot as an image
            filename = f"{col}.png"
            plt.savefig(filename, bbox_inches='tight')
            plt.close()  # Close figure to avoid overlap

            print(f"Saved plot: {filename}")"""

            print(f"Column: {col}")

            # If the column is numeric, show min-max range
            if pd.api.types.is_numeric_dtype(data[col]):
                print(f"  Min: {data[col].min()}, Max: {data[col].max()}")

            # If the column is categorical, show unique values
            else:
                unique_values = data[
                    col].dropna().unique()  # Drop NaN values before getting unique ones
                print(f"  Categories: {list(unique_values)}")

            print("-" * 40)  # Separator for readability

except FileNotFoundError:
    print("Error: The file 'attrition_availabledata_08.csv' was not found.")
except pd.errors.ParserError:
    print("Error: There was an issue parsing the CSV file.")
except Exception as e:
    print(f"Unexpected error: {e}")
