import pandas as pd
csv_files = ["data\daily_sales_data_0.csv", "data\daily_sales_data_1.csv", "data\daily_sales_data_2.csv"]
# Create a new empty DataFrame to store the combined data.
combined_df = pd.DataFrame()

# Iterate over the list of CSV file paths and read each CSV file into a DataFrame.
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    combined_df = combined_df._append(df, ignore_index=True)

# Save the combined DataFrame to a new CSV file.
combined_df.to_csv("combined.csv", index=False)