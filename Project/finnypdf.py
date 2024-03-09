import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Usage
pdf_path = "vetdata/4_22_16_5905728.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
#print(extracted_text)
print(type(extracted_text))

words = extracted_text.split()
#print(words)

#attributelist = {"Species":words[words.index("Species")+1],"Sample" }
species = words[words.index("Species")+1]
if species == "C":
    species = "cat"
elif species == "D":
    species = "dog"

sample = []
sampleword = ""
n = 1
m = ["Method", "Methods"]
while sampleword not in m:
    try:
        sampleword = words[words.index("samples", words.index("samples")+1)+n]
        sample.append(sampleword)
    except:
        sampleword = words[words.index("sample", words.index("sample")+1)+n]
        sample.append(sampleword) 
    n += 1
    #print(sample)
sample.pop()
sample = ' '.join(sample)
print(sample)

bacteria = []
bacteriaword = ""
n = 1
while bacteriaword != "Results":
    bacteriaword = words[words.index("identification")+n]
    bacteria.append(bacteriaword)
    n += 1

bacteria.pop()
bacteria = ' '.join(bacteria)
print(bacteria)