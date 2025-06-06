# 📁 File: test_ocr.py
# Description: Test script to verify Tesseract OCR is working on a sample image

from PIL import Image
import pytesseract

# If you're using Windows and Tesseract is not added to PATH,
# uncomment the line below and specify the path to tesseract.exe
# Example: r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def test_image_ocr(image_path):
    """
    Performs OCR on the input image and returns extracted text.
    """
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    img_path = "C:/Users/monda/OneDrive/Desktop/ChatBot_Theme_Identifier/data/tree.jpg"  # Update path as needed
    extracted = test_image_ocr(img_path)
    print("\n📜 Extracted Text from Image:\n")
    print(extracted)
