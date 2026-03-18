import pdfplumber

query = input("Enter your legal query: ").lower()

text = ""

# Load the law document
with pdfplumber.open("../documents/it_act_2000.pdf") as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text.lower()

# Split lines
lines = text.split("\n")

print("\nRelevant Law Sections:\n")

for line in lines:
    if query in line:
        print("\nMatching Law Found:\n")
        print("Law:", line.strip())
        print("Source: Information Technology Act 2000")
        print("-----------------------------")