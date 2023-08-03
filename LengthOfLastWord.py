class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Question : https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
        #Separate words by space
        lastword = list(s.split())

        #Get the total number of words
        totalWords=len(lastword)

        #Get the last word
        words = lastword[totalWords-1]

        #Get the length of the last word
        lengthOfWords = len(words)
        
        return lengthOfWords
