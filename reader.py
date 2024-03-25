#Use PyPDF2
import PyPDF2

#Request the Pdf path to the user and create a variable for save the text in the pdf
pdf_path = input("Please enter the path of your PDF file ")
text = ""

#Create a context manager for the binary reading process
with open(pdf_path, "rb") as file:
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    
    #With a for cycle we review all the pages in the pdf file and return the text in this 
    for i in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[i]
        text += page.extract_text()

#Finlly print the text obtained
print(text)