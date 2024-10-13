"""
Author: Ayush Bothra
Date: 09-10-2024
Aim: Implement the fractional knapsack problem 
     and understand its greedy approach with CSV data.
"""

# imports
import os
import pandas as pd


class SelectGoods:
    """
    Class for selecting goods based on the fractional knapsack approach.
    Minimizes the shelf-life and maximizes the cost.
    """

    def __init__(self):
        pass

    def is_numeric(self, value):
        """Check if the value is numeric."""
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    def processfiles(self, csv_file):
        """
        Load data from CSV file and return it in the form of a list of tuples.
        Each row of the CSV should have 'cost', 'shelf_life', and 'weight'.
        """
        file_extension = os.path.splitext(csv_file)[1].lower()
        if file_extension != ".csv":
            raise ValueError(f"Unsupported file format: {file_extension}")

        try:
            data = pd.read_csv(csv_file)
        except Exception as e:
            raise ValueError(f"Error reading {csv_file}: {e}")

        # Check for required columns
        if not all(col in data.columns for col in ['Cost', 'Shelf_Life', 'Weight']):
            raise ValueError(f"CSV file {csv_file} must contain 'Cost', 'Shelf_Life', and 'Weight' columns.")

        if data.empty:
            print(f"Warning: The CSV file {csv_file} is empty.")
            return []

        goods = []
        for index, row in data.iterrows():
            # Check for invalid values
            if not self.is_numeric(row['Weight']):
                print(f"Warning: Item {index} has a non-numeric weight '{row['Weight']}'. Skipping this item.")
                continue
            if not self.is_numeric(row['Cost']):
                print(f"Warning: Item {index} has a non-numeric cost '{row['Cost']}'. Skipping this item.")
                continue
            if not self.is_numeric(row['Shelf_Life']):
                print(f"Warning: Item {index} has a non-numeric shelf life '{row['Shelf_Life']}'. Skipping this item.")
                continue

            weight = float(row['Weight'])
            cost = float(row['Cost'])
            shelf_life = float(row['Shelf_Life'])

            # Additional checks for negative values
            if weight < 0:
                print(f"Warning: Item {index} has negative weight. Skipping this item.")
                continue
            if cost < 0:
                print(f"Warning: Item {index} has negative cost. Skipping this item.")
                continue
            
            goods.append((cost, shelf_life, weight))

        return goods

    def knapsack(self, goods, total_weight):
        """
        Fractional knapsack algorithm.
        goods[i] = (cost, shelf_life, weight)
        total_weight = maximum weight capacity of the knapsack
        """
        if not goods:
            print("No valid goods to process.")
            return 0

        fractional_goods = []
        # create new list = {(cost/weight), shelf_life, weight, index}
        for i, good in enumerate(goods):
            if good[2] == 0:
                print(f"Warning: Item {i} has zero weight, skipping this item.")
                continue
            
            value = good[0] / good[2]
            fractional_goods.append((value, good[1], good[2], i))

        # sort by (cost/weight) in descending order and shelf_life in ascending order
        fractional_goods = sorted(fractional_goods, key=lambda x: (-x[0], x[1]))

        total_value = 0
        for good in fractional_goods:
            if good[2] <= total_weight:
                total_value += good[0] * good[2]
                total_weight -= good[2]
                print(f"Whole of good {good[3]}.")
            else:
                # if the remaining weight is less than the weight of the item
                total_value += good[0] * total_weight
                print(f"{(total_weight * 100) / good[2]:.2f}% of good {good[3]}.")
                return total_value

        return total_value


if __name__ == "__main__":
    select_goods = SelectGoods()

    # Example CSV files (replace with actual paths)
    csv_files = [
        "lab_5/knapsack_items/items_data_1.csv", 
        "lab_5/knapsack_items/items_data_2.csv", 
        "lab_5/knapsack_items/items_data_3.csv", 
        "lab_5/knapsack_items/items_data_4.csv",
        "lab_5/knapsack_items/items_data_5.csv",  # Edge cases
        "lab_5/knapsack_items/items_data_6.csv",
        "lab_5/knapsack_items/items_data_7.csv",
        "lab_5/knapsack_items/items_data_8.csv",
        "lab_5/knapsack_items/items_data_9.csv",
        "lab_5/knapsack_items/items_data_10.csv",
    ]

    total_weight = 200  # Maximum capacity of the knapsack

    for csv_file in csv_files:
        print(f"Processing file: {csv_file}")
        try:
            goods = select_goods.processfiles(csv_file)  # Load goods from CSV
            total_value = select_goods.knapsack(goods, total_weight)  # Run knapsack algorithm
            print(f"Total value obtained: {total_value:.2f}")
        except ValueError as e:
            print(f"Error processing file {csv_file}: {e}")
        print("-----------------------")
