import os
import zipfile
import tempfile
import shutil
import py7zr
import rarfile
from io import BytesIO
from email import policy
from email.parser import BytesParser

import docx
import PyPDF2
import pytesseract
from PIL import Image

try:
    from pdf2image import convert_from_path
except ImportError:
    convert_from_path = None

# Determine the file format based on the file extension. Then, call the corresponding function to extract the text content from that file.
def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.txt':
        return extract_text_from_txt(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    elif ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.eml':
        return extract_text_from_eml(file_path)
    elif ext in ['.zip', '.7z', '.rar']:
        return extract_text_from_archive(file_path)
    elif ext in ['.jpg', '.jpeg', '.png', '.tiff']:
        return extract_text_from_image(file_path)
    else:
        return ""

# Read text file (.txt)
def extract_text_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return ""

# Read Word file (.docx)
def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception:
        return ""

# Read PDF files (.pdf)
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception:
        text = ""
    if not text and convert_from_path:
        try:
            pages = convert_from_path(file_path)
            for page in pages:
                text += pytesseract.image_to_string(page)
            return text
        except Exception:
            return ""
    return text

# Read EML file (.eml)
def extract_text_from_eml(file_path):
    try:
        with open(file_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
        if msg.is_multipart():
            parts = [part.get_content() for part in msg.walk() if part.get_content_type() == 'text/plain']
            return "\n".join(parts)
        else:
            return msg.get_content()
    except Exception:
        return ""

# Read and process compressed files
def extract_text_from_archive(file_path):
    temp_dir = tempfile.mkdtemp()
    extracted_text = ""
    try:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.zip':
            with zipfile.ZipFile(file_path, 'r') as z:
                z.extractall(temp_dir)
        elif ext == '.7z':
            with py7zr.SevenZipFile(file_path, mode='r') as z:
                z.extractall(path=temp_dir)
        elif ext == '.rar':
            with rarfile.RarFile(file_path, 'r') as z:
                z.extractall(temp_dir)
        for root, _, files in os.walk(temp_dir):
            for file in files:
                extracted_text += extract_text(os.path.join(root, file)) + "\n"
    except Exception:
        pass
    finally:
        shutil.rmtree(temp_dir)
    return extracted_text

# Read text from image
def extract_text_from_image(file_path):
    try:
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)
    except Exception:
        return ""
