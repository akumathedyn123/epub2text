import os
from ebooklib import epub

# Set the path to the folder containing the EPUB files
epub_folder = 'path/to/folder'

# Loop through all EPUB files in the folder
for filename in os.listdir(epub_folder):
    if filename.endswith('.epub'):
        # Open the EPUB file using ebooklib
        book = epub.read_epub(os.path.join(epub_folder, filename))
        # Extract the text from each section of the book
        text = ''
        for item in book.get_items():
            if item.get_type() == epub.ITEM_DOCUMENT:
                text += item.get_content()
        # Save the text as a separate TXT file in the same folder
        with open(os.path.join(epub_folder, filename[:-5] + '.txt'), 'w') as txt_file:
            txt_file.write(text)