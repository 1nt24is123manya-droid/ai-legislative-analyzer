import pdfplumber
from langchain_text_splitters import RecursiveCharacterTextSplitter
from compressor import compress_chunk
text = ""

# Read PDF
with pdfplumber.open("../documents/it_act_2000.pdf") as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200
)

chunks = splitter.split_text(text)

print("Total chunks created:", len(chunks))

print("\nCompressed Output (First 3 Chunks):\n")

for i in range(3):
    compressed = compress_chunk(chunks[i])

    print(f"\nChunk {i+1} Compressed:\n")
    print(compressed)
    print("\n---------------------------")