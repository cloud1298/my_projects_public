import re


def main():
    # Get text from the user
    text = input("Text: ")

    # Get list of sentences and words
    sentences = get_sentences(text)
    words = get_words(sentences)

    # Calculate number of sentences, words and letters
    sentences_count = calculate_sentences(sentences)
    words_count = calculate_words(words)
    letters_count = calculate_letters(words)

    # Calculate grade of the text
    grade = calculate_grade(letters_count, sentences_count, words_count)

    print_grade(grade)


def get_sentences(text):
    """
    Make a list filled with sentences from the text.

    Args:
        text: Text given by the user.

    Returns:
        List of sentences from the text.
    """
    # Split text to sentences
    sentences = text.replace('"', "")
    sentences = re.split(r"[.!?]", sentences)

    # Strip sentences to get rid of any spaces before and after text.
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    return sentences


def get_words(sentences):
    """
    Make a list, filled with words without non alpha chars, from the sentences.

    Args:
        sentences: A list of sentences.

    Returns:
        A list of words from the sentences.
    """
    words = []
    clean_sentence = ""
    for sentence in sentences:
        clean_sentence += "".join(
            char if char.isalpha() or char.isspace() else "" for char in sentence
        )
        clean_sentence += " "

    words.extend(clean_sentence.split())

    return words


def calculate_sentences(sentences):
    """
    Count every sentence.

    Args:
        sentences: List of sentences.

    Returns:
        Number of sentences.
    """
    return len(sentences)


def calculate_words(words):
    """
    Count every word.

    Args:
        words: List of words.

    Returns:
        Number of words.
    """
    return len(words)


def calculate_letters(words):
    """
    Count every letter.

    Args:
        sentences: List of words.

    Returns:
        Number of letters.
    """
    return sum(len(word) for word in words)


def calculate_grade(letters_count, sentences_count, words_count):
    """
    Calculate grade of the text.

    Args:
        letters_count: Number of letters
        sentences_count: Number of sentences
        words_count: Number of words

    Returns:
        Grade of the text.
    """
    L = letters_count / words_count * 100
    S = sentences_count / words_count * 100

    grade = round(0.0588 * L - 0.296 * S - 15.8)

    return grade


def print_grade(grade):
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


if __name__ == "__main__":
    main()
