# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Function to perform basic data analysis
def perform_data_analysis(csv_file):
    # Load data from CSV into a Pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Displaying the first few rows of the dataframe
    print("First few rows of the dataset:")
    print(df.head())
    
    # Basic statistics
    print("\nBasic statistics:")
    print(df.describe())
    
    # Calculate mean and median
    mean_value = df['Value'].mean()
    median_value = df['Value'].median()
    
    print(f"\nMean value: {mean_value}")
    print(f"Median value: {median_value}")
    
    # Plotting (optional)
    plt.figure(figsize=(10, 6))
    plt.hist(df['Value'], bins=20, color='blue', edgecolor='black')
    plt.title('Distribution of Values')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Filter data example (optional)
    filtered_data = df[df['Category'] == 'A']
    print("\nFiltered data where Category is 'A':")
    print(filtered_data.head())

# Example usage
if __name__ == "__main__":
    csv_file = 'data.csv'  # Replace with your actual CSV file name
    perform_data_analysis(csv_file)
