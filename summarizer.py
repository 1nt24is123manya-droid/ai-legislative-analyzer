from compressor import compress_chunk

def generate_summary(chunk):

    data = compress_chunk(chunk)

    if not data["crime"]:
        return {"summary": "No major legal rule found."}

    summary = f"""
    Section {data['section']} deals with {data['crime']}.
    Punishment: {data['punishment'] if data['punishment'] else 'Not specified'}.
    Fine: {data['fine'] if data['fine'] else 'Not specified'}.
    """

    return {
        "summary": summary.strip(),
        "section": data["section"],
        "crime": data["crime"]
    }