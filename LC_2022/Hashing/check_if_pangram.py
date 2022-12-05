class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # There are 26 letters in the alphabet. 
        # Sets do not store duplicates so we can convert the sentence to a set
        # and ensure it's length is = 26
        alphabet = set(sentence)
        if len(alphabet) == 26:
            return True
        return False