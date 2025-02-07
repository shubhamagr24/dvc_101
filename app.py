import pandas as pd
import os
# import boto3
from io import StringIO

# Create a sample DataFrame with column names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }

df = pd.DataFrame(data)

# Adding new row to df for V2
new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# Adding new row to df for V3
new_row_loc2 = {'Name': 'GF2', 'Age': 30, 'City': 'City2'}
df.loc[len(df.index)] = new_row_loc2


# # Convert DataFrame to CSV string
# csv_buffer = StringIO()
# df.to_csv(csv_buffer, index=False)

# # Initialize S3 client
# s3_client = boto3.client('s3')

# # S3 bucket and file details
# bucket_name = 'myfirsts3bucket0657'
# file_name = 'sample_data.csv'

# # Upload CSV to S3
# s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=csv_buffer.getvalue())

# print('CSV file uploaded successfully to S3')




# Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")