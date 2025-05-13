# import pandas as pd

# # Load the CSV file
# df = pd.read_csv(r'C:\Users\Me\Documents\GitHub\Apex-Legends-Research-Dataset-Analysis\Player UIDs\usernames_with_uids_for_Xbox.csv')  # Replace with your actual file name

# # Replace Username with a placeholder using the UID
# df['Username'] = df['UID'].apply(lambda uid: f'User_{uid}')

# # Save the updated data to a new CSV
# df.to_csv('UIDs_for_Xbox.csv', index=False)

import pandas as pd

# Load the CSV file
df = pd.read_csv(r'C:\Users\Me\Documents\GitHub\Apex-Legends-Research-Dataset-Analysis\Career_Stats_Dataset\Total_Career_Stats.csv')  # Replace with your actual file name

# Replace player_name with a unique User_n label
df['player_name'] = [f'User_{i+1}' for i in range(len(df))]

# Save the updated file
df.to_csv('Total Player Career Stats.csv', index=False)
