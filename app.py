from flask import Flask, request, render_template_string
import pdfplumber

# 🔥 NEW IMPORTS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from summarizer import generate_summary   # make sure file exists

app = Flask(__name__)

# Load law text
text = ""
with pdfplumber.open("documents/it_act_2000.pdf") as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text.lower()

# ❌ OLD (no longer needed)
# lines = text.split("\n")

# ✅ STEP 3: CREATE CHUNKS (THIS WAS YOUR CONFUSION)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200
)

chunks = splitter.split_text(text)

print("Total chunks created:", len(chunks))  # optional debug


# ✅ SEARCH FUNCTION (ADD THIS)
def search_chunks(query, chunks):
    results = []

    for chunk in chunks:
        if query in chunk.lower():
            results.append(chunk)

    return results[:5]  # limit results


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Legislative Analyzer</title>
</head>
<body>
    <h1>AI Legislative Analyzer</h1>
    <form method="post">
        <input type="text" name="query" placeholder="Enter your legal query" required>
        <button type="submit">Search</button>
    </form>
    <h2>Results:</h2>
    <ul>
        {% for r in results %}
        <li>{{ r }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        query = request.form["query"].lower()

        # 🔥 NEW FLOW
        matched_chunks = search_chunks(query, chunks)

        for chunk in matched_chunks:
            summary = generate_summary(chunk)
            results.append(summary["summary"])

    return render_template_string(HTML_PAGE, results=results)
@app.route("/api/search", methods=["POST"])
def api_search():
    data = request.get_json()
    query = data["query"].lower()

    matched_chunks = search_chunks(query, chunks)

    results = []

    for chunk in matched_chunks:
        summary = generate_summary(chunk)
        results.append(summary)

    return {"results": results}

if __name__ == "__main__":
   import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
