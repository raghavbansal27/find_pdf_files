#! python3
# find_pdfs.py Program that walks through a folder tree and searches for files with
#                          extension .pdf and print absolute file of that path.
import os
from path_file import path

PATH = path


def filePath(folder):
    pdf_files = []
    os.path.abspath(folder)
    for folderName, subFolders, filesname in os.walk(folder):
        for files in filesname:
            if files.endswith('.pdf'):
                pdf_files.append(os.path.join(folderName, files))

    return pdf_files, len(pdf_files)


print("Finding pdfs...")
pdf_files, num = filePath(PATH)

print("Found {} pdfs".format(num))
for pdf in pdf_files:
    print(pdf)