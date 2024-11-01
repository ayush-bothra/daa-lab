import pandas as pd
from typing import List

class LCSFinder:
    """Class responsible for finding the longest common subsequence among multiple sequences."""

    @staticmethod
    def calculate_lcs(seq1: str, seq2: str) -> str:
        """Calculates the LCS between two sequences using dynamic programming."""
        dp = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
        directions = [[None] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]

        for i in range(1, len(seq1) + 1):
            for j in range(1, len(seq2) + 1):
                if seq1[i - 1] == seq2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    directions[i][j] = "diag"
                elif dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    directions[i][j] = "up"
                else:
                    dp[i][j] = dp[i][j - 1]
                    directions[i][j] = "left"

        return LCSFinder._build_lcs_string(directions, seq1, len(seq1), len(seq2))

    @staticmethod
    def _build_lcs_string(directions: List[List[str]], seq1: str, i: int, j: int) -> str:
        """Builds the LCS string from the direction matrix."""
        lcs_string = []
        while i > 0 and j > 0:
            if directions[i][j] == "diag":
                lcs_string.append(seq1[i - 1])
                i -= 1
                j -= 1
            elif directions[i][j] == "up":
                i -= 1
            else:
                j -= 1
        return ''.join(reversed(lcs_string))

    @classmethod
    def find_lcs_across_sequences(cls, sequences: List[str]) -> str:
        """Finds the longest common subsequence across a list of sequences."""
        if not sequences or all(s == "" for s in sequences):
            return ""

        common_sequence = sequences[0]
        for sequence in sequences[1:]:
            common_sequence = cls.calculate_lcs(common_sequence, sequence)
            if not common_sequence:
                break
        return common_sequence


class GradeLCSProcessor:
    """Class to process grades and compute the LCS."""

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.student_grades = self._load_student_grades()

    def _load_student_grades(self) -> List[List[str]]:
        """Loads student grades from a CSV file."""
        data = pd.read_csv(self.csv_path).fillna("").to_numpy()
        return [[str(grade).strip() for grade in row if pd.notna(grade) and grade.strip()] for row in data]

    def process_grades(self):
        """Processes each row of grades and finds the LCS if the row meets requirements."""
        for grades in self.student_grades:
            if not grades:
                print("Error: No grades provided")
                continue
            if len(grades) < 20:
                print("Error: Number of sequences less than 20")
                continue

            lcs_result = LCSFinder.find_lcs_across_sequences(grades)
            if lcs_result:
                print(f"Longest common sequence: {lcs_result}. Length of sequence: {len(lcs_result)}")
            else:
                print("Error: No common subsequence found")


processor = GradeLCSProcessor("lab_6/student_grades.csv")
processor.process_grades()
