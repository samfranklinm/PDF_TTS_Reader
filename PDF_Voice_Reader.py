# Created by Sam Jagan Mohan
# Please see usage license for more details

import PyPDF2
import pyttsx3

# Ask user for the location of the PDF file
filePath = input('Insert file path to your pdf: ')

# Get the specific file name
fileName = filePath.split('/')[-1]
print('The file to opened is ', fileName)

pdfRead = PyPDF2.PdfFileReader(open(filePath, 'rb'))
textToSpeech = pyttsx3.init()

# Let the user know how many pages there are in the PDF
for i in range(0, pdfRead.numPages):
    numOfPages = i
print('There are ', numOfPages, ' pages in this PDF.')

# Ask user if there is a specific page that they would like to listen to
pageOrNot = input(
    'Is there a specific page you want me to read? (yes or no):  ')
cleanedUpText = ''

# If so, ask user for page number and then extract the test from the page
if pageOrNot == 'yes':
    pageNumber = int(input('Ok, which page? '))
    extractedText = pdfRead.getPage(pageNumber).extract_text()
    cleanedUpText = extractedText.strip().replace('/n', ' ')
    print(cleanedUpText)
# Otherwise, extract text from all pages
else:
    for pageNumber in range(pdfRead.numPages):
        extractedText = pdfRead.getPage(pageNumber).extract_text()
        cleanedUpText = extractedText.strip().replace('/n', ' ')
        print(cleanedUpText)

# Read the extracted text to the user
textToSpeech.say(cleanedUpText)
print('Reading...')
textToSpeech.runAndWait()
print('Completed.')
