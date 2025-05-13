import pandas as pd
import os

# Define input and output root directories
input_root = 'Legend Stats Dataset'
output_root = 'Processed_Legend_Stats'

# Walk through the folder tree
for subdir, _, files in os.walk(input_root):
    for file in files:
        if file.endswith('.csv'):
            input_path = os.path.join(subdir, file)
            print(f'Processing: {input_path}')
            
            # Load the data
            df = pd.read_csv(input_path)

            # Add player_name column
            df.insert(0, 'player_name', [f'User_{i+1}' for i in range(len(df))])

            # Construct the output path
            relative_path = os.path.relpath(subdir, input_root)
            output_dir = os.path.join(output_root, relative_path)
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, file)

            # Save the new file
            df.to_csv(output_path, index=False)
