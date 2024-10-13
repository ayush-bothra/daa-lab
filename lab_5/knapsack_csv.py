import numpy as np
import pandas as pd

# Generate 4 more CSV files with different random values but the same structure
file_paths = []
for i in range(1, 5):
    # Generate new random data
    data = {
        "No.": np.arange(1, 101),  # No. from 1 to 100
        "Capacity": np.random.randint(1, 50, size=100),  # Random integers < 50
        "Life": np.random.randint(1, 50, size=100),  # Random integers < 50
        "Value": np.random.randint(1, 50, size=100)  # Random integers < 50
    }

    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Save to a CSV file with a unique name
    file_path = f"lab_5/items_data_{i}.csv"
    df.to_csv(file_path, index=False)
    file_paths.append(file_path)

file_paths
