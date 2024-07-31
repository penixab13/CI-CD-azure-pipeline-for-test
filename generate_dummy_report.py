import pandas as pd

# Create a simple DataFrame
df = pd.DataFrame({
    'Metric': ['Accuracy', 'Response Time', 'User Satisfaction'],
    'Value': [0.95, 1.2, 0.9]
})

# Save DataFrame to an Excel file
df.to_excel('dummy_report.xlsx', index=False)
