from pdfminer.high_level import extract_text
import pdfminer
import re
from skilllist import skills_list

def textextractor(pdf_path):
    return extract_text(pdf_path)

    
def extract_name_from_resume(text):
    name = None
    pattern =r"([A-Z][a-zğüşıöç]+\b)\s([A-Z][a-z]+\b)"
    match = re.search(pattern, text)
    if match:
        name = match.group()

    return name

def extract_contact_number_from_resume(text):
    contact_number = None

    # Use regex pattern to find a potential contact number
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()

    return contact_number

def extract_email_from_resume(text):
    email=None
    pattern = r"[a-z0-9\.\-+_]+@[a-z\.\-]+\.[a-z]+"
    match = re.search(pattern, text)
    if match:
        email = match.group()
    
    return email





def extract_skills(text,skills_list):
    skills = []
    # Search for skills in the resume text
    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)

    return skills    

def extract_education(text):
    education = []
    pattern = r"(?i)(?:(?:Bachelor|B\.S\.|B\.A\.|Master|M\.S\.|M\.A\.|Ph\.D\.)\s(?:[A-Za-z]+\s)*[A-Za-z]+)"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())
    return education
    

def extract_college_name(text):
    lines = text.split('\n')
    University_pattern = r"(?i).*Universty*"
    for line in lines:
        if re.match(University_pattern, line):
            return line.strip()
    return None


def print_resume_info(text):
    # Extract and print name
    name = extract_name_from_resume(text)
    print("\n=== Personal Information ===")
    print(f"Name: {name if name else 'Not found'}")

    # Extract and print contact number
    contact = extract_contact_number_from_resume(text)
    print(f"Contact: {contact if contact else 'Not found'}")

    # Extract and print email
    email = extract_email_from_resume(text)
    print(f"Email: {email if email else 'Not found'}")

    # Extract and print university
    university = extract_college_name(text)
    print("\n=== Education ===")
    print(f"University: {university if university else 'Not found'}")

    # Extract and print degrees
    degrees = extract_education(text)
    print("\nDegrees:")
    if degrees:
        for degree in degrees:
            print(f"- {degree}")
    else:
        print("- No degrees found")

    # Extract and print skills
    skills = extract_skills(text, skills_list)
    print("\n=== Skills ===")
    if skills:
        for skill in skills:
            print(f"- {skill}")
    else:
        print("- No skills found")

# Replace your existing print statements with this:
text = textextractor(r"C:\Users\yagiz\OneDrive\Masaüstü\Uygulamalar\kodlar\Resume Parser\YağızTerziCV.pdf")
print_resume_info(text)

