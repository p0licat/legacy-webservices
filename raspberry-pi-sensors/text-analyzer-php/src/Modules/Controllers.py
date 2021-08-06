#!/usr/bin/env python
import sys # sys.version

class FileController(object):
    def __init__(self, text):
        self._text = text
        self._version_int = int(sys.version.split()[0].split('.')[0])

    def WordFrequencies(self):
        """
            returns: dict()
        """
        wordDict = self._text.WordFrequencies()
        return wordDict

    def GetContextPermutations(self, length, contextSize):
        """
            returns: map of lists
        """
        contextMap = self._text.ContextPermutations(length, contextSize)
        return contextMap

    def GetAverageWordLength(self):
        """
            returns: float()
        """
        return self._text.AverageLength()

    def UniqueWords(self):
        """
            returns: list()
            List of unique words sorted by length, descending order.
        """
        sortedWords = self._text.SortedWords()
        return sortedWords

    def GraphOccurencesToLength(self, pathName):
        """
            returns: str()
            Path to created plot image. Words indexed by length, mapped to occurences (at least 2).
        """
        return self._text.GraphOccurencesToLength(pathName)

    def GraphWordLengthDensity(self, pathName):
        """
            returns: str() 
            Returns path to created plot image.
        """
        rval = self._text.GraphWordLengthDensity(pathName)
        return rval if type(rval) is str else None

    def GraphWordLength(self, pathName):
        """
            returns: str()
            Returns path to created image.
        """
        rval = self._text.GraphTextWordLength(pathName)
        return rval if type(rval) is str else None

    def Plot3DHeights(self, pathname):
        rval = self._text.Plot3DHeights(pathname)
        return rval if type(rval) is str else None
  
    def GetNumberOfWords(self):
        """
            returns: int()
            Number of words (regex: \w, separator ' ') in text.
        """
        nwords = self._text.GetNumberOfWords()
        return nwords

    def GetNumberOfUniqueWords(self):
        """
            returns: int()
            Number of unique words, delimiter ' '.
        """
        nwords = self._text.GetNumberOfUniqueWords()
        return nwords

    def GetNumbersToWordsRatio(self):
        """
            returns: float()
            Ratio of words to numbers, with delimiter ' '.            
        """
        return self._text.GetNumbersToWordsRatio()

