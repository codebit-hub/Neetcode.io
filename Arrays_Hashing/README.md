ARRAYS & HASHING
Quick overall view:

- This folder focuses on hash-based and array-based patterns.
- Common techniques include frequency maps, set membership checks, prefix/suffix products, and canonical grouping.
- Most solutions are optimized to linear or near-linear time, which is ideal for interview-style problems.

| File | Problem | Method Used | Time Complexity | Space Complexity | Quick Review |
|---|---|---|---:|---:|---|
| 01_contains_duplicate.py | Contains Duplicate | Hash set to track seen numbers while iterating | O(n) | O(n) | Efficiently detects duplicates by checking whether a value has already appeared. |
| 02_valid_anagram.py | Valid Anagram | Frequency map / counting characters in both strings | O(n) | O(k) | Compares character counts; if both strings have the same counts, they are anagrams. |
| 03_two_sum.py | Two Sum | Hash map storing previously seen values and complements | O(n) | O(n) | Uses target - num to find the matching partner in a single pass. |
| 04_group_anagrams.py | Group Anagrams | Sort each string to form a canonical key and group by it | O(sum(s_i log s_i)) | O(total characters) | Groups words with the same letters together by normalizing them into a common form. |
| 05_top_k_frequent_elements.py | Top K Frequent Elements | Counter + sorting by frequency | O(n + u log u) | O(n) | Counts occurrences, then selects the K most frequent values. |
| 06_product_of_array_except_self.py | Product of Array Except Self | Prefix and suffix product accumulation | O(n) | O(1) extra | Computes each result without division by building products from left and right. |
| 07_valid_sudoku.py | Valid Sudoku | Sets for rows, columns, and 3x3 boxes | O(81) ≈ O(1) | O(81) ≈ O(1) | Validates the board by ensuring each digit appears only once in each unit. |
| 08_longest_consecutive_sequence.py | Longest Consecutive Sequence | Set + checking only sequence starts | O(n) | O(n) | Finds long runs by skipping numbers that are not the start of a consecutive chain. |
| 09_encode_decode_str.py | Encode and Decode Strings | Length-prefix encoding with delimiter; parse prefix length and slice string | O(n) total across all strings | O(n) total output size | Encodes a list of strings into one compact string and decodes it back without ambiguity. |



