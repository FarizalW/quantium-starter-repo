import pandas as pd
my_value = "pink morsel"
# Create a new empty DataFrame to store the combined data.
combined_df = pd.read_csv("combined.csv")
combined_df['sales'] = combined_df['price'].str.replace('$', '').   astype('float')* combined_df['quantity']
summary_df= combined_df.loc[combined_df['product'] == my_value]
summary_df = summary_df.drop(columns=['price', 'quantity'])
summary_df = summary_df[['sales', 'date', 'region']]
print(summary_df.head(8))

summary_df.to_csv("pink_morsel_sales.csv", index=False)