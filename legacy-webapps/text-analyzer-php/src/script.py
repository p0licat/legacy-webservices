#!/usr/bin/env python
from Modules.TextHandlers import Text
from Modules.Controllers import FileController
import sys
import hashlib

def ParagraphWrap(string):
    ptago = '<p>'
    ptagc = '</p>'

    return ptago + string + ptagc

def SymmetricTagWrap(tag, string):
    otag = '<' + tag + '>'
    ctag = '</' + tag + '>'

    return otag + string + ctag

def CrappyListFormatter(listObj, reverse=False, maxcount=None):
    fstr = ""
    fstr += "<p>"
    effList = listObj[:] if not reverse else listObj[::-1]
    for i in effList[::-1]:
        fstr += i + " "
        if maxcount is not None:
            if maxcount > 1:
                maxcount -= 1
            else:
                return fstr + " ... " + "</p>"
    return fstr + "</p>"

def MapPrint(mapObj, maxcount=None):
    fstr = "<ul>"
    for row in mapObj:
        fstr += "<li>"
        for col in row:
            fstr += col + " "
        fstr += "</li>"
        if maxcount is not None:
            if maxcount > 1:
                maxcount = maxcount - 1
            else:
                return fstr + "<li> ... </li>"  + "</ul>"
    return fstr + "</ul>"

def TupleListPrint(tList, maxcount=None):
    fstr = "<ul>"
    for elem in tList:
        fstr += "<li>"
        fstr += str(elem[0]) + " " + str(elem[1])
        fstr += "</li>"
        if maxcount is not None:
            if maxcount > 1:
                maxcount = maxcount - 1
            else:
                return fstr + "<li> ... </li>"  + "</ul>"
    return fstr + "</ul>"

def ImageWrap(pathI):
    return "<img src=\"{0}\"/>".format(pathI)

def ShaSum(stringToSum):
    m = hashlib.md5()
    m.update(str(stringToSum).encode(encoding="utf-8"))
    return m.hexdigest()

def ParagraphPrint(fileController, filename, textObject, plotDir, averageLength):
    print(ParagraphWrap("Number of words: {0}".format(str(fileController.GetNumberOfWords()))))
    print(ParagraphWrap("Number of unique words: {0}".format(str(fileController.GetNumberOfUniqueWords()))))
    print(ParagraphWrap("Average word length is: {0}".format(str(fileController.GetAverageWordLength()))))
    print(ParagraphWrap("Ratio of numbers to words is: {0}".format(str(fileController.GetNumbersToWordsRatio()))))
    print(ParagraphWrap("Contexts of minimum length {0} with 3 neighbours are: (first {1})".format(averageLength, 5)))
    print(MapPrint(fileController.GetContextPermutations(averageLength, 3), maxcount=5))
    print(ParagraphWrap("Word frequencies are: (first {0}) ".format(10)))
    print(TupleListPrint(fileController.WordFrequencies(), maxcount=10))
    print(ParagraphWrap("Unique words are: "))
    print(CrappyListFormatter(fileController.UniqueWords(), maxcount=50))
    print(ImageWrap(fileController.GraphWordLength(plotDir + ShaSum(filename) + "_fig1" + '.jpg')))
    print(ImageWrap(fileController.GraphWordLengthDensity(plotDir + ShaSum(filename) + "_fig2" + '.jpg')))
    print(ImageWrap(fileController.GraphOccurencesToLength(plotDir + ShaSum(filename) + "_fig3" + '.jpg')))
    print(ImageWrap(fileController.Plot3DHeights(plotDir + ShaSum(filename) + "_fig43D" + '.jpg')))

def SecondPrintTablePrint(fileController, filename, textObject, plotDir, averageLength):
    numberOfWords = str(fileController.GetNumberOfWords())
    numberOfUniques = (str(fileController.GetNumberOfUniqueWords()))
    avgWordLength = str(fileController.GetAverageWordLength())
    numToWordsRatio = str(fileController.GetNumbersToWordsRatio())

    strList = list()
    strList.append(("Number of words: ", numberOfWords))
    strList.append(("Number of uniques words: ", numberOfUniques))
    strList.append(("Average word length: ", avgWordLength))
    strList.append(("Numbers to words ratio: ", numToWordsRatio))
    
    rows_string = ""
    for i in strList:
        e1 = "<td>" + str(i[0]) + "</td>"
        e2 = "<td>" + str(i[1]) + "</td>"
        rows_string += "<tr>" + e1 + e2 + "</tr>"
    

    head_value_1 = "Feature"
    head_value_2 = "Value"
    thead_string = "<thead>" + "<tr>" + "<th>" + head_value_1 + "</th>" + "<th>" + head_value_2 + "</th>" + "</tr>" + "</thead>"

    tbody_string = "<tbody>" + rows_string + "</tbody>"
    table_format = "<h4>Stats:</h4>" + "<table class=\"alt\">" + thead_string + tbody_string + "</table>"
    
    print(table_format)
    return table_format

def ListFormat(wordMap, maxlength):
    rows = ""
    ctr = 0
    for row in wordMap:
        rlist = ""
        for k in row:
            rlist += str(k) + " "
        rows += "<li>" + rlist + "</li>"
        ctr += 1
        if ctr >= maxlength:
            rows += "<li> ... </li>"
            return "<ul>" + rows + "</ul>"

    return "<ul>" + rows + "</ul>"

def SecondPrintVerticals(fileController, filename, textObject, plotDir, averageLength):
    tableLengths = 5

    div_row_string = "<div class=\"row\">"
    div_vert_string = "<div class=\"6u 12u$(small)\">"

    title1 = str("Contexts of minimum length {0} with {2} neighbours: (first {1})".format(averageLength, tableLengths, 2))
    title2 = str("Word frequencies are: (first {0}) ".format(tableLengths))

    contextPermutations = fileController.GetContextPermutations(averageLength, 3)
    wordFrequencies = fileController.WordFrequencies()
    
    # formatting wordFrequencies into list
    wordFrequenciesList = list()
    for i in wordFrequencies:
        l_elem = []
        l_elem.append(i[0])
        l_elem.append(i[1])
        wordFrequenciesList.append(l_elem)
    wordFrequencies = wordFrequenciesList
    # end format
    formattedTag = div_row_string[:]
    formattedTag += div_vert_string + "<h4>" + title1 + "</h4>" + ListFormat(contextPermutations, tableLengths) + "</div>"
    formattedTag += div_vert_string + "<h4>" + title2 + "</h4>" + ListFormat(wordFrequencies, tableLengths) + "</div>"
    formattedTag += "</div>"

    print(formattedTag)
    return formattedTag

def SecondPrintBox(fileController, filename, textObject, plotDir, averageLength):
    uniqueWordsList = fileController.UniqueWords()
    
    uniqueWordsString = ""
    for i in uniqueWordsList[::-1]:
        uniqueWordsString += str(i) + " "
   
    headingTitle = "<h4>" + "Unique words:" + "</h4>"
    boxTag = "<div class=\"box\">"
    formatTag = headingTitle + boxTag + "<p>" + uniqueWordsString + "</p>" + "</div>"

    print(formatTag)
    return formatTag

def SecondPrintImagePrints(fileController, filename, textObject, plotDir, averageLength):
    print(ImageWrap(fileController.GraphWordLength(plotDir + ShaSum(filename) + "_fig1" + '.jpg')))
    print(ImageWrap(fileController.GraphWordLengthDensity(plotDir + ShaSum(filename) + "_fig2" + '.jpg')))
    print(ImageWrap(fileController.GraphOccurencesToLength(plotDir + ShaSum(filename) + "_fig3" + '.jpg')))
    print(ImageWrap(fileController.Plot3DHeights(plotDir + ShaSum(filename) + "_fig43D" + '.jpg')))


def main():
    filename = sys.argv[1]
    plotDir = 'MplPlots/'
    textObject = Text(filename)
    fileController = FileController(textObject)

    averageLength = int(fileController.GetAverageWordLength())
    SecondPrintTablePrint(fileController, filename, textObject, plotDir, averageLength)
    SecondPrintVerticals(fileController, filename, textObject, plotDir, averageLength)
    SecondPrintBox(fileController, filename, textObject, plotDir, averageLength)
    SecondPrintImagePrints(fileController, filename, textObject, plotDir, averageLength)
    #ParagraphPrint(fileController, filename, textObject, plotDir, averageLength)
    # todo: print uses right stream !
    # try construct table

main()

