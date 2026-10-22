"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is
decoded back to the original list of strings.

Machine 1 (sender) has the function:

String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}
So Machine 1 does:

String encoded_string = encode(strs);
and Machine 2 does:

List<String> decoded_strs = decode(encoded_string);
decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: strs = ["Hello","World"]

Output: ["Hello","World"]
Explanation:

Solution solution = new Solution();
String encoded_string = solution.encode(strs);

// Machine 1 ---encoded_string---> Machine 2

List<String> decoded_strs = solution.decode(encoded_string);

Example 2:

Input: strs = [""]

Output: [""]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters
"""

class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_strs: str = ""
        for s in strs:
            s_len = len(s)
            # encoded_strs += str(s_len) + '#' + s
            encoded_strs += '<' + str(s_len) + '>' + s
        return encoded_strs

    def decode(self, s: str) -> list[str]:
        split_lists = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != ">":
                j += 1
            s_len = int((s[i:j]).strip('<'))
            split_lists.append(s[j + 1 : j + 1 + s_len])
            i = j + 1 + s_len
        return split_lists


strings1 = ["Hello, world", "Awesome&*%$#!", "Are y#ou do*}'{''}]ing fine?"]
print(f"strings1: {strings1}")

encoded_strings1 = Solution().encode(strings1)
print(f"encoded strings1: {encoded_strings1}")

decoded_strings1 = Solution().decode(encoded_strings1)
print(f"decoded strings1: {decoded_strings1}")
