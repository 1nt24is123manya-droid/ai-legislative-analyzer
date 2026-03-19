import re

def compress_chunk(chunk):

    compressed = {
        "section": None,
        "crime": None,
        "punishment": None,
        "fine": None
    }

    lines = chunk.split("\n")

    for line in lines:
        line = line.strip().lower()

        if not line:
            continue

        # Extract section number
        sec_match = re.search(r'\b\d+[a-z]?\.', line)
        if sec_match:
            compressed["section"] = sec_match.group()

        # Detect crime
        if "identity theft" in line:
            compressed["crime"] = "Identity Theft"
        elif "cheating" in line:
            compressed["crime"] = "Online Cheating"
        elif "privacy" in line:
            compressed["crime"] = "Privacy Violation"

        # Detect punishment
        if "imprisonment" in line:
            compressed["punishment"] = "Jail punishment"

        # Detect fine
        if "fine" in line:
            compressed["fine"] = "Monetary fine"

    return compressed