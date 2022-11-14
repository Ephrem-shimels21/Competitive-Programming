class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        sentenceList=s.split()
        correctedSentence = [None] * len(sentenceList)
        for words in sentenceList:
            position = int(words[-1]) -1
            correctedSentence[position] = words[:len(words)-1]
        return " ".join(correctedSentence)
            
