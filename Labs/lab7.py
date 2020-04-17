"""This script uses the docx2python module, which extracts .docx headers,
footers, text, footnotes, endnotes, properties, and images to a Python object."""

from docx2python import docx2python

#Show file properties
print ("Properties:")
print (docx2python('./Lab7.docx').properties)
print ('\n')

print ("Press enter to continue")
keypress = input()
print ('\n')

#Show Header
print ("Header:")
print (docx2python('./Lab7.docx').header)
print ('\n')

print ("Press enter to continue")
keypress = input()
print ('\n')

#Show Footer
print ("Footer:")
print (docx2python('./Lab7.docx').footer)
print ('\n')

