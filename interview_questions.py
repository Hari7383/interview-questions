# -*- coding: utf-8 -*-
"""interview questions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Nc_-DyJFcGDXGGBcTvjdIBBI7rKGZEN
"""

pip install pdfplumber

import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_sections(text):
    # Debugging: Print raw text
    print("Extracted Text:\n", text)

    # Adjusted patterns based on raw text structure
    patterns = {
        'skills': r'Skills.*?\n(.*?)\n(?:\n|$)',
        'experience': r'Experience.*?\n(.*?)\n(?:\n|$)',
        'projects': r'Projects.*?\n(.*?)\n(?:\n|$)'
    }

    extracted = {}
    for section, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            section_text = match.group(1).strip()
            extracted[section] = section_text
            print(f"{section.capitalize()} Extracted: {section_text}")
        else:
            print(f"{section.capitalize()} Not Found")
            extracted[section] = ""

    return extracted

def combine_sections(extracted_sections):
    combined = f"Skills: {extracted_sections['skills']}\n" \
               f"Experience: {extracted_sections['experience']}\n" \
               f"Projects: {extracted_sections['projects']}"
    return combined

def main():
    pdf_path = '/content/HARIHARASUTHAN S.pdf'  # Replace with your actual file path
    text = extract_text_from_pdf(pdf_path)
    extracted_sections = extract_sections(text)
    combined_content = combine_sections(extracted_sections)
    #print("Final Combined Content:\n", combined_content)

if __name__ == "__main__":
    main()

import requests
from google.generativeai import GenerativeModel,configure
import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_relevant_sections(text):
    # Regex patterns for specific sections
    patterns = {
        'skills': r'Skills(?:\s*|:)\n?(.*?)(?:\n\n|$)',
        'achievements': r'Achievements(?:\s*|:)\n?(.*?)(?:\n\n|$)',
        'experience': r'(?:Working Experience|Experience)(?:\s*|:)\n?(.*?)(?:\n\n|$)',
        'projects': r'Projects(?:\s*|:)\n?(.*?)(?:\n\n|$)'
    }

    extracted = {}
    for section, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            # Clean and store extracted content
            extracted[section] = match.group(1).strip().replace("\n", " ")
        else:
            extracted[section] = "Not Found"

    return extracted

def combine_extracted_sections(extracted_sections):
    combined = (
        f"Skills: {extracted_sections['skills']}\n"
        f"Achievements: {extracted_sections['achievements']}\n"
        f"Working Experience: {extracted_sections['experience']}\n"
        f"Projects: {extracted_sections['projects']}"
    )
    return combined

def main():
    pdf_path = '/content/HARIHARASUTHAN S.pdf'  # Replace with your PDF file path
    text = extract_text_from_pdf(pdf_path)
    relevant_sections = extract_relevant_sections(text)
    combined_content = combine_extracted_sections(relevant_sections)
    #print("Extracted Content:\n", combined_content)
    string = ". ( Give me interview qustions above the content )"
    promt = combined_content + string
    print(promt)
    configure(api_key="AIzaSyC7m8U8F6ibWOsuZUGOf3SE83TqgZZOLlA")
    model = GenerativeModel("gemini-1.5-pro")
    r=model.generate_content(promt)
    print("Chatbot:",r.text)

if __name__ == "__main__":
    main()