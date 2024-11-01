class MatrixChain:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def validate_dimensions(self):
        """Validate the input dimensions."""
        if not self.dimensions:
            raise ValueError("Dimensions cannot be empty.")
        if len(self.dimensions) < 2:
            raise ValueError("At least two dimensions are required.")
        if any(d <= 0 for d in self.dimensions):
            raise ValueError("Dimensions must be positive integers.")
    
    def calculate_order(self):
        """Calculate the minimum number of multiplications needed."""
        self.validate_dimensions()
        n = len(self.dimensions) - 1  # Number of matrices

        # Create a table to store the minimum number of multiplications
        m = [[0] * n for _ in range(n)]
        # Create a table to store the split points
        s = [[0] * n for _ in range(n)]

        # l is the chain length
        for l in range(2, n + 1):  # l = 2 to n
            for i in range(n - l + 1):
                j = i + l - 1  # j is the endpoint of the chain
                m[i][j] = float('inf')  # Initialize to a large number
                # Try all possible splits
                for k in range(i, j):
                    q = (m[i][k] + m[k + 1][j] +
                         self.dimensions[i] * self.dimensions[k + 1] * self.dimensions[j + 1])
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j] = k

        return m

    def get_minimum_multiplications(self):
        """Return the minimum number of multiplications required."""
        m = self.calculate_order()
        return m[0][len(self.dimensions) - 2]


def main():
    test_cases = [
        [7, 3, 7, 4, 7, 5, 7, 6],
        [7, 5, 7, 6, 7, 7, 7, 8],
        [7, 4, 7, 8, 7, 3, 7, 9],
        [7, 2, 7, 10, 7, 4, 7, 5],
        [7, 6, 7, 3, 7, 8, 7, 2],
        [7, 9, 7, 5, 7, 10, 7, 3],
        [7, 7, 7, 8, 7, 6, 7, 4],
        [7, 10, 7, 3, 7, 9, 7, 5],
        [7, 8, 7, 2, 7, 6, 7, 4],
        [7, 4, 7, 10, 7, 5, 7, 6],
        [],  # Empty dimensions
        [5],  # Single dimension
        [5, 0],  # Zero dimension
        [5, -3],  # Negative dimension
        [5, 10],  # Valid two elements
    ]

    for test_case in test_cases:
        try:
            matrix_chain = MatrixChain(test_case)
            min_steps = matrix_chain.get_minimum_multiplications()
            print(f"Dimensions: {test_case}, Minimum number of multiplications required: {min_steps}")
        except ValueError as e:
            print(f"Dimensions: {test_case}, Error: {e}")


if __name__ == "__main__":
    main()
