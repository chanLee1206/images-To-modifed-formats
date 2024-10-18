import pytesseract
from PIL import Image
import os

# Path to the Tesseract executable (if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the folder containing images
image_folder = 'src_sample'

# Output folder for text files
output_folder = 'output_txt_folder'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all images in the folder
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        image_path = os.path.join(image_folder, filename)
        img = Image.open(image_path)
        
        # Use Tesseract to extract text from the image
        text = pytesseract.image_to_string(img, lang='eng')
        
        # Save the extracted text to a .txt file
        txt_file_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
        with open(txt_file_path, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f"Processed {filename} -> {txt_file_path}")
