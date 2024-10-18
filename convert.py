import os
import pytesseract
from PIL import Image
from docx import Document
from docx.shared import Inches

# Define the path to the directory containing images
src_dir = "src_sample"
# Output Word document path
output_doc = "output.docx"

# Create a new Document
doc = Document()

# Process each image in the specified directory
for filename in os.listdir(src_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # You can add more extensions if needed
        # Full path to the image
        img_path = os.path.join(src_dir, filename)
        
        # Open the image using Pillow
        img = Image.open(img_path)
        
        # Use pytesseract to extract text and get the color information
        text = pytesseract.image_to_string(img)

        # Add the image to the document
        doc.add_picture(img_path, width=Inches(5))  # Adjust width as needed
        
        # Add the extracted text to the document
        # Here you could customize how to add color or format if needed
        doc.add_paragraph(text)

# Save the document
doc.save(output_doc)

print(f"Converted images in '{src_dir}' to '{output_doc}' successfully!")
