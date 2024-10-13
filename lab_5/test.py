import heapq
from collections import defaultdict

class TreeNode:
    def __init__(self, character, freq):
        self.character = character  # character (None for internal nodes)
        self.freq = freq            # frequency of the node
        self.left = None            # left child
        self.right = None           # right child

    def __lt__(self, other):
        return self.freq < other.freq


class Encoder:
    def encode_tree(self, file_string):
        # Check if the string is empty
        if not file_string:
            raise ValueError("Input file is empty.")

        # Ensure the string contains only ASCII characters
        if not all(ord(char) < 128 for char in file_string):
            raise ValueError("Input contains non-ASCII characters.")

        # Count the frequency of each character in the file string
        frequency = defaultdict(int)
        for char in file_string:
            frequency[char] += 1

        # Handle the single character case
        if len(frequency) == 1:
            char = next(iter(frequency))
            print(f"Note: Input contains only one unique character ('{char}'). Compression not possible.")
            root = TreeNode(char, frequency[char])
            return root  # Return the single node Huffman tree

        # Create a min-heap based on character frequency
        heap = [TreeNode(char, freq) for char, freq in frequency.items()]
        heapq.heapify(heap)

        # If all characters have the same frequency, just warn the user
        if len(set(frequency.values())) == 1:
            print("Note: All characters have the same frequency. Compression may not be effective.")

        # Build the Huffman tree by combining the two least frequent nodes until only one node remains
        while len(heap) > 1:
            left = heapq.heappop(heap)  # Get the least frequent node
            right = heapq.heappop(heap)  # Get the second least frequent node

            # Merge these two nodes
            merged = TreeNode(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            # Push the new merged node back into the heap
            heapq.heappush(heap, merged)

        # Return the root of the Huffman tree (the only node left in the heap)
        return heap[0]
    
    def generate_code(self, node, prefix="", code_book={}):
        if node is not None:
            if node.character is not None:
                code_book[node.character] = prefix  # leaf node
            else:
                self.generate_code(node.left, prefix + "0", code_book)
                self.generate_code(node.right, prefix + "1", code_book)
        return code_book
    
    def print_huffman_tree(self, node, indent=0):
        """Helper function to print the structure of the Huffman tree."""
        if node is not None:
            if node.character is not None:
                print(" " * indent + f"Leaf: '{node.character}' | Frequency: {node.freq}")
            else:
                print(" " * indent + f"Internal Node | Frequency: {node.freq}")
            self.print_huffman_tree(node.left, indent + 4)
            self.print_huffman_tree(node.right, indent + 4)


# Test Cases
def test_huffman_cases():
    encoder = Encoder()

    # Test case 1: Single character
    print("\nTest Case 1: Single Character 'aaaaa'")
    file_string_1 = "aaaaa"
    tree_1 = encoder.encode_tree(file_string_1)
    encoder.print_huffman_tree(tree_1)

    # Test case 2: Equal frequency characters
    print("\nTest Case 2: Equal Frequency Characters 'abcabc'")
    file_string_2 = "abcabc"
    tree_2 = encoder.encode_tree(file_string_2)
    encoder.print_huffman_tree(tree_2)


if __name__ == "__main__":
    test_huffman_cases()
