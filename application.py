import os
import sys
import glob

from PyPDF2 import PdfFileMerger

'''
Takes one or more PDF files from folder "PDF",
sorts the list, and it into a single document.

David Metcalfe, February 11 2017
'''

fileLocation = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'PDF')
fileList = glob.glob(fileLocation + "\\*.pdf")

if len(fileList) < 1:
    sys.exit("* No PDF files found in \"" + fileLocation + "\"")

merge = PdfFileMerger()

for pdf in fileList.sort():
    merge.append(open(pdf, 'rb'))

with open('Merged_PDF.pdf', 'wb') as fout:
    merge.write(fout)
