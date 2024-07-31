import pandas as pd
import os

# Create a simple DataFrame
df = pd.DataFrame({
    'Metric': ['Accuracy', 'Response Time', 'User Satisfaction'],
    'Value': [0.95, 1.2, 0.9]
})

# Define the path where the report will be saved
report_path = 'dummy_report.xlsx'

# Save DataFrame to an Excel file
df.to_excel(report_path, index=False)

print(f"Report saved to {os.path.abspath(report_path)}")

