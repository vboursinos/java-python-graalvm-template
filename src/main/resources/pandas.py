import pandas as pd

# Create a new DataFrame from scratch
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}
new_df = pd.DataFrame(data)
print(new_df)