def compress_chunk(chunk):

    lines = chunk.split("\n")

    compressed = {
        "policy_area": "Cyber Law",
        "key_points": []
    }

    for line in lines:
        line = line.strip()
        if line:
            compressed["key_points"].append(line)

    return compressed


# Example usage
if __name__ == "__main__":

    sample_chunk = """
    66C. Punishment for identity theft
    66D. Punishment for cheating by personation
    66E. Punishment for violation of privacy
    """

    result = compress_chunk(sample_chunk)

    print("Compressed Output:\n")
    print(result)