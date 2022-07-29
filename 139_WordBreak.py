"""
Leetcode- https://leetcode.com/problems/word-break/ (submitted)
TC- ,SC-
Challenges-
Lecture-
FAQ-


Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""


class Solution:
    """
    Ideation- Brute Force, TC- O(N^N), SC- O(1)

    The idea is to find all the combinations of the partitions that can be made and check if each of the string in those
     partitions are in word dictionary. If so, return true, else once all the possible combinations have been
     processed, return false.

    Lookup in the word dictionary can be done by either taking hash set or Trie. Hashmap will be more time efficient,
    since hashing of the string will be saved at the beginning of defining hashset O(1). Whereas, we will need to
    traverse the trie to search for the word which will be O(N)
    """

    def wordBreak(self, s, wordDict):
        dictS = set(wordDict)
        return self.helper(s, dictS)

    def helper(self, s, dictS):
        # base - no more characters left to process. Since, we are passing right characters to the string in the
        # recursive call, that would mean empty string as input.
        if len(s) == 0:
            return True

        # logic - left to the partition in word list and remaining right can be partitioned more.
        for i in range(len(s)):
            subS = s[:i + 1]
            if subS in dictS and self.helper(s[i + 1:], dictS):
                return True

        return False


s = "applepenapple"
wordDict = ["apple", "pen"]
result = Solution().wordBreak(s, wordDict)
print(result)
