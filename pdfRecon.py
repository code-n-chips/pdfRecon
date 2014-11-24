#=====pdfRecon========
# A script to extract metadata from a pdf file.
# Useful for finding out who authored, created or modified a pdf
#Author: Ed Fish efish001@gold.ac.uk Nov 2014
#Bugs: none
#Use: python pdfRecon.py -F file.pdf
#========================

import pyPdf                     #import pdf python pdf reader
import optparse                  #optparse for command line use
from pyPdf import PdfFileReader  #file reader from pypdf

#this function gets the meta data of the pdf file
def printMeta(fileName):
    pdfFile=PdfFileReader(file(fileName, 'rb'))    #load and read pdf
    docInfo = pdfFile.getDocumentInfo()            #get the meta data
    print '[*] PDF MetaData For:' + str(fileName)  #print the metadata
    for metaItem in docInfo:
        print'[+]' + metaItem + ':' + docInfo[metaItem] #list items and info

def main():
    #opt parser for command line option (file name)
    parser = optparse.OptionParser('usage %prog ' + '-F <PDF file name> \n Example: python pdfRecon -F file.pdf')
    parser.add_option('-F', dest='fileName', type='string', help='specify PDF file name')
    (options,args) = parser.parse_args()
    #get file from commandline option
    fileName = options.fileName
    if fileName == None:
        print parser.usage #print parser error and usage
        exit(0)
    else:
        printMeta(fileName)   #print the metadata

if __name__ == '__main__':
    main()
