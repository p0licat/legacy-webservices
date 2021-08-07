#!/usr/bin/env python
import sys
from Modules.StringOperations import WhitelistStripping
import matplotlib
matplotlib.use('Agg')

import math
from matplotlib import pyplot
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

class Text:
    def __init__(self, filename):
        self.fileSize = None
        self.words = None
        self.fileName = filename
        self.bytes = None
        self.fo = None
        self.strippedWords = []

        self.numbersToWordsRatio = None

        try:
            self.fo = file(self.fileName) if int(sys.version.split()[0].split('.')[0]) == 2 else open(self.fileName)
        except IOError:
            print("Filename error.")
            return

        self.fo = file(self.fileName) if int(sys.version.split()[0].split('.')[0]) == 2 else open(self.fileName, 'r') # python
        self.bytes = self.fo.read()
        self.words = self.bytes.split()
        for i in self.words:
            self.strippedWords.append(WhitelistStripping(i))

    
    def __del__(self):
        self.fo.close()
    
    def SurfaceMapSquare(self, rval, pathname):
        fig = pyplot.figure()
        ax = fig.add_subplot(111, projection='3d')

        r = np.arange(0, len(rval[0]))
        p = np.arange(0, len(rval))

        R, P = np.meshgrid(r, p)

        maxelement = 10
        for i in rval:
            for j in i:
                maxelement = max(maxelement, j)

        #ax.plot_surface(R, P, np.array(rval), cmap=pyplot.cm.YlGnBu_r)
        ax.plot_surface(R, P, np.array(rval), alpha=0.3)
        ax.set_zlim(-10, maxelement)
        cset = ax.contour(R, P, np.array(rval), zdir='z', offset=-10, cmap=cm.coolwarm)
        pyplot.savefig(pathname)
        pyplot.clf()
        return pathname

    def SurfaceMapNormalized(self, rval, pathname):
        fig = pyplot.figure()
        ax = fig.add_subplot(111, projection='3d')

        p = np.arange(0, len(rval))
        r = np.arange(0, len(rval[0]))

        R, P = np.meshgrid(r, p)

        maxelement = 0
        for i in rval:
            for k in i:
                maxelement = max(maxelement, k) 
        ax.plot_surface(R, P, np.array(rval), cmap=pyplot.cm.coolwarm)
        ax.set_zlim(0, 6.2*maxelement)
        pyplot.savefig(pathname)
        pyplot.clf()
        return pathname

    def Plot3DHeights(self, pathname):
        elist = self.bytes[:]
        def FillMatrix2(elist):
            def FillMatrix(dlist):
                density_matrix = []
                words = ""
                for i in dlist:
                    for car in i:
                        words+=car
                words = words.split(' ') 
                wnums = []
                for word in words:
                    nword = [k for k in range(len(word))]
                    revkw = [k for k in range(len(word))[::-1]]
                    wnums.append([1 + min(nword[i], revkw[i]) for i in range(len(nword))])
                    
                fline = []
                for i in wnums:
                    for k in i:
                        fline.append(k)
                    fline.append(0)
                lc = 0
                for i in range(len(dlist)):
                    cline = []
                    for k in range(len(dlist[0])):
                        cline.append(fline[lc*len(dlist[0]) + k])
                    density_matrix.append(cline)
                    lc += 1
                return density_matrix

            # transform 1line ; find x|y ; return filled matrix

            superstring = ""
            for i in elist:
                if i != '\n':
                    superstring += i
                else:
                    superstring += " "

            x = len(superstring)
            # 2y^2 < x | 2y < sqrt(x) | y < sqrt(x)/2 ? >=!
            y = int(math.sqrt(x/2.+1))
            ccount = 0
            lcount = 0
            clist = ""
            dlist = []
            for i in superstring:
                if ccount == 2*y:
                    ccount = 0
                    lcount += 1
                    dlist.append(clist)
                    clist = ""
                clist += i
                ccount += 1
            return FillMatrix(dlist)
        
        rval = FillMatrix2(elist)
        #prval = self.SurfaceMapNormalized(rval, pathname)
        prval = self.SurfaceMapSquare(rval, pathname)
        return prval

    def AverageLength(self):
        mathrage = 0
        mathcoun = 0
        for i in self.words:
            mathrage += len(i)
            mathcoun += 1 # COMPILER WIZARD OF THE GREAT UNTOLD WIZARDRIES OF ;.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        return float(mathrage)/mathcoun#;

    
    def GetUniqueWords(self):
        uniqueWordsDict = dict()
        uniqueWordsList = list()
        for i in self.words:
            if i not in uniqueWordsDict:
                uniqueWordsDict[i] = 1
                uniqueWordsList.append(i)
        
        return uniqueWordsList


    def GetNumberOfUniqueWords(self):
        uniqueWords = self.GetUniqueWords()
        return len(uniqueWords)

    
    def GetNumberOfWords(self):
        return len(self.words)
 
    def GraphWordLengthDensity(self, pathname):
        wbase = self.strippedWords
        uniqdict = dict()
        for i in wbase:
            b = WhitelistStripping(i)
            uniqdict[b] = 1 if b not in uniqdict else uniqdict[b] + 1
        len_occ_dict = dict()
        for i in uniqdict:
            len_occ_dict[len(i)+1] = uniqdict[i] if len(i)+1 not in len_occ_dict else uniqdict[i] + len_occ_dict[len(i)+1]
        
        tfinalList = [k for k in len_occ_dict.keys()]
        tfinalYist = [k for k in len_occ_dict.values()]

        #pyplot.plot(len_occ_dict.keys(), len_occ_dict.values())
        pyplot.plot(tfinalList, tfinalYist)
        pyplot.ylabel("occurences")
        pyplot.xlabel("length of word")
        pyplot.savefig(pathname)
        pyplot.clf()
        return pathname

    
    def GraphTextWordLength(self, pathname):
        xaxis = [i for i in range(len(self.strippedWords))]
        yaxis = [len(k) for k in self.strippedWords]

        pyplot.plot(xaxis, yaxis)
        pyplot.xlabel("index of word")
        pyplot.ylabel("length of word")
        pyplot.savefig(str(pathname))
        pyplot.clf()
        return pathname

    
    def GraphOccurencesToLength(self, pathname):
        occurenceDict = dict()
        for i in self.words:
            i = WhitelistStripping(i)
            occurenceDict[i] = 1 if i not in occurenceDict else occurenceDict[i] + 1

        notUniqueList = []
        for i in occurenceDict:
            if occurenceDict[i] > 1:
                notUniqueList.append((occurenceDict[i], i))

        notUniqueList.sort()

        xplot = [i for i in range(notUniqueList[-1:][0][0]+1)]
        yplot = [0 for k in range(len(xplot))]

        for i in notUniqueList:
            yplot[i[0]] = len(i[1])

        pyplot.scatter(xplot, yplot)
        pyplot.plot(xplot, yplot)

        pyplot.ylabel("length of word occuring more than once")
        pyplot.xlabel("occurences")
        pyplot.savefig(pathname)
        pyplot.clf()
        return pathname
    
    def GetNumbersToWordsRatio(self):
        if self.numbersToWordsRatio is not None:
            return self.numbersToWordsRatio

        text = self.words
        num="1234567890"
        alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        numbers = []
        words = []

        for i in text:
            typeflag = ""
            for k in range(len(i)):
                if i[k] in num:
                    typeflag += "n"
                elif i[k] in alp:
                    typeflag += "a"
                else:
                    typeflag += "!"

            while typeflag[-1:] == "!":
                i = i[:-1]
                typeflag = typeflag[:-1]

            if "!" not in typeflag:
                if "a" not in typeflag:
                    numbers.append(i)
                elif "n" not in typeflag:
                    words.append(i)

        self.numbersToWordsRatio = float(len(numbers)) / float(len(words))
        return self.numbersToWordsRatio

    
    def ContextPermutations(self, minl, count):
        completeMap = []
        if count >= len(self.strippedWords):
            return None
        
        f = 0
        for i in range(count, len(self.strippedWords)):
            f = 1
            for k in range(count):
                if len(self.strippedWords[i-k]) < minl:
                    f = 0
                    break
            if f == 0:
                continue

            beautyList = []
            for k in range(count)[::-1]:
                beautyList.append(self.strippedWords[i - k])
            completeMap.append(beautyList)

        completeMap = self.SortWordMap(completeMap)
        return completeMap[::-1] 


    def SortWordMap(self, wmap):
        wmapt = []
        resl = []
        for i in wmap:
            total = 0
            for e in i:
                total += len(e)
            wmapt.append((total, i))
        wmapt.sort()
        for i in wmapt:
            resl.append(i[1])
        return resl


    def WordFrequencies(self):
        frDict = dict()
        for i in self.words:
            frDict[i] = 1 if i not in frDict else frDict[i]+1
        
        frList = list()
        for i in frDict:
            frList.append((frDict[i], i))
        frList.sort()

        return [(i[1], i[0]) for i in frList][::-1]

    
    def MostCommonList(self, l, minWordLength):
        """
           l - most common l words
           minWordLength - lower length bound
        """
        def sortTupleListWithCountValues(tupleListWithCountValues):
            """
                a list of tuples : [(a, b), (etc, etc), (word, 11), (word, count)]
                bubble sort flags
                Will sort tuple list by count (second tuple element).
            """
            done = False
            while not done:
                done = True
                for i in range(1, len(tupleListWithCountValues)):
                    if tupleListWithCountValues[i-1][1] > tupleListWithCountValues[i][1]:
                        tupleListWithCountValues[i-1] , tupleListWithCountValues[i] = tupleListWithCountValues[i] , tupleListWithCountValues[i-1]
                        done = False

        
        t = self.words
        li = []
        countey = dict()
        for i in t:
            i = WhitelistStripping(i)
            if i not in countey:
                countey[i] = 0
            else:
                countey[i] += 1
        # dict of stripped words mapped to count exists here (countey)

        # parse countey, generate list and keep sorted
        for i in countey.items():
            if len(li) < l and len(i[0]) >= minWordLength:
                li.append(i)
            elif len(li) >= l and len(i[0]) >= minWordLength:
                sortTupleListWithCountValues(li)
                if li[0][1] < i[1]:
                    li[0] = i
                sortTupleListWithCountValues(li)

        # return sorted list of unique (word, count)
        print(li)
        return li
   
    
    def SortedWords(self):
        rval = []
        for i in self.words:
            if (len(i), i) not in rval:
                rval.append((len(i), i))
        
        rval.sort()
        rrval = [k[1] for k in rval]

        return rrval
    
   
    """
        Getters and Util.
    """
    def PrintNthWord(self, n):
        return self.words[n]

    def WordSequence(self, lb, ub):
        return self.words[lb:ub]

    def GetFO(self):
        return self.fo

    def GetBytes(self):
        return self.bytes

    def GetWords(self):
        return self.words

    def PrintText(self):
        print(self.bytes)



