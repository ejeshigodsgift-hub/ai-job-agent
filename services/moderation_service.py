blocked_words = [
    "spam",
    "scam"
]


def moderate_text(text):
    for word in blocked_words:
        if word in text.lower():
            return False

    return True