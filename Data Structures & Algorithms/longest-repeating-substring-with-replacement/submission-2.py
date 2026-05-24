class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left, right = 0, 0
        longest_substring = 0

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
    
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            longest_substring = max(longest_substring, right - left + 1)
            right += 1
        return longest_substring

