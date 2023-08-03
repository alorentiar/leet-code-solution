class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #Separate words by space
        lastword = list(s.split())

        #Get the total number of words
        totalWords=len(lastword)

        #Get the last word
        words = lastword[totalWords-1]

        #Get the length of the last word
        lengthOfWords = len(words)
        
        return lengthOfWords
