# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 14:36:36 2023

@author: Kiarash Rahmani
"""
import PyPDF2

# Open the PDF file
pdf_file = open('your desired path for input.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Initialize an empty string to store the text
pdf_text = ""

# Loop through all the pages and extract text
for page in pdf_reader.pages:
    pdf_text += page.extract_text()

# Close the PDF file
pdf_file.close()

# Define the path for the text file
output_file_path = 'your desired path for output.txt'

# Write the extracted text to the text file
with open(output_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(pdf_text)

print(f'Text extracted from PDF has been saved to {output_file_path}')
