class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += str(len(i))
            encoded_str += "#"
            encoded_str += i
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        curr = 0
        while curr < len(s):
            start = s.find("#", curr)
            length = int(s[curr:start])
            string = s[start + 1:start + 1 + length]
            decoded_str.append(string)
            curr = start + 1 + length
        return decoded_str

