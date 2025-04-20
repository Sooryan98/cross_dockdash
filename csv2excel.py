import pandas as pd

# Load CSV file
csv_file = "/home/soorya/Documents/RobotUnloadingStatus.csv"
df = pd.read_csv(csv_file)

# Save to Excel
excel_file = "output/OverallTripData.xlsx"
df.to_excel(excel_file, index=False)

print(f"Converted '{csv_file}' to '{excel_file}'")
