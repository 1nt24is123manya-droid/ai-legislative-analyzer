from flask import Flask, request, render_template_string
import pdfplumber

app = Flask(__name__)

# Load law text
text = ""
with pdfplumber.open("../documents/it_act_2000.pdf") as pdf:
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text.lower()

lines = text.split("\n")

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
        for line in lines:
            if query in line:
                results.append(line.strip())
    return render_template_string(HTML_PAGE, results=results)

if __name__ == "__main__":
    app.run(debug=True)