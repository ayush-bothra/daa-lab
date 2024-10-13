# imports
import os
import heapq
import PyPDF2  
import docx    
from bs4 import BeautifulSoup  # To read HTML files
from collections import defaultdict

class ProcessFile:
    def __init__(self):
        pass

    def take_file(self, file_path):
        # Check the file extension and process accordingly
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension == ".txt":
            return self.process_txt(file_path)
        elif file_extension == ".pdf":
            return self.process_pdf(file_path)
        elif file_extension == ".docx":
            return self.process_docx(file_path)
        elif file_extension == ".html":
            return self.process_html(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
        
    def process_txt(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def process_pdf(self, file_path):
        text = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text

    def process_docx(self, file_path):
        doc = docx.Document(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text

    def process_html(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, "html.parser")
            return soup.get_text()


class TreeNode:
    def __init__(self, character, freq):
        self.freq = freq
        self.character = character
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class Encoder:
    
    def encode_tree(self, file_string):
        if not file_string:
            raise ValueError("Input file is empty.")
        
        if not all(ord(char) < 128 for char in file_string):
            raise ValueError("Input contains non-ASCII characters.")

        unique_variables = list(set(file_string))
        frequency = {char: file_string.count(char) for char in unique_variables}
        number_of_unique_variables = len(unique_variables)

        if number_of_unique_variables == 1:
            raise ValueError("Input contains only a single unique character. compression will not be useful")

        if len(frequency) > 1 and all(freq == list(frequency.values())[0] for freq in frequency.values()):
            print("All characters have the same frequency. The heap might have some ambiguity")

        heap = [TreeNode(char, freq) for char, freq in frequency.items()]
        heapq.heapify(heap)
            
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            value = left.freq + right.freq
            merged = TreeNode(None, value)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        return heap[0]
    
    def generate_code(self, node, prefix="", code_book={}):
        if node is not None:
            if node.character is not None:
                code_book[node.character] = prefix
            else:
                self.generate_code(node.left, prefix + "0", code_book)
                self.generate_code(node.right, prefix + "1", code_book)
        
        return code_book
    
    def calculate_encoded_size(self, file_string, code_book):
        frequency = {char: file_string.count(char) for char in list(set(file_string))}
        total_bits = 0

        for char, freq in frequency.items():
            total_bits += freq * len(code_book[char])

        return total_bits
    
    def decode(self, encoded_data, huffman_tree_root):
        decoded_string = ""
        current_node = huffman_tree_root

        for bit in encoded_data:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.left is None and current_node.right is None:
                decoded_string += current_node.character
                current_node = huffman_tree_root

        return decoded_string


# Main execution part
if __name__ == "__main__":
    process_file = ProcessFile()
    encoder = Encoder()

    # Define the list of files to process
    file_list = [
        "lab_5/huffman_text/case_1.txt",
        "lab_5/huffman_text/case_2.txt",
        "lab_5/huffman_text/case_3.txt",
        "lab_5/huffman_text/case_4.txt",
        "lab_5/huffman_text/case_5.txt",
        "lab_5/huffman_text/case_6.txt",
        "lab_5/huffman_text/case_7.txt",
        "lab_5/huffman_text/case_8.docx",  # Adding case_8.docx
        "lab_5/huffman_text/case_9.pdf",   # Adding case_9.pdf
        "lab_5/huffman_text/case_10.html"   # Adding case_10.html
    ]

    for file_path in file_list:
        print(f"\nProcessing file: {file_path}")
        print("-" * 40)
        
        try:
            # Read the file content
            file_string = process_file.take_file(file_path)

            # Encode the tree
            huffman_tree_root = encoder.encode_tree(file_string)

            # Generate Huffman codes
            huffman_codes = encoder.generate_code(huffman_tree_root)

            # Encode the file content
            encoded_data = "".join([huffman_codes[char] for char in file_string])

            # Calculate the size of the original and encoded content
            original_size = len(file_string) * 8
            encoded_size = encoder.calculate_encoded_size(file_string, huffman_codes)

            # Print results
            print("Huffman Codes:", huffman_codes)
            print(f"Original Size (bits): {original_size}")
            print(f"Encoded Size (bits): {encoded_size}")
            print(f"Compression Ratio: {encoded_size / original_size * 100:.2f}%")

            # Decode the encoded data
            decoded_string = encoder.decode(encoded_data, huffman_tree_root)
            print("Is the decoded string the same? :", decoded_string == file_string)

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
