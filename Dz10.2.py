def first_word(text):
    text = text.lstrip(" .")
    word = ""
    for ch in text:
        if ch.isalpha() or ch == "'":
            word += ch
        else:
            break
    return word
