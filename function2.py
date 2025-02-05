import re

# Normalize the case of a sentence (capitalize first letter)
def normalize_sentence_case(sentence):
    return sentence.capitalize()

# Normalize the text case while preserving the original format
def normalize_case(text):
    lines = text.split("\n")  # Split text by newlines
    lines[0] = "homEwork:"  # Ensure "homEwork:" remains unchanged

    sentences = re.split(r'(?<=[.!?])\s+', "\n".join(lines[1:]))  # Split into sentences
    return lines[0] + "\n" + " ".join(map(normalize_sentence_case, sentences))  # Normalize each sentence

# Fix occurrences of "iz" with the correct "is"
def fix_mistakes(text):
    return re.sub(r'\biz\b', 'is', text)

# Extract the last words of each sentence
def extract_last_words(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)  # Split into sentences
    return [re.findall(r'\b\w+\b(?=[.!?])', sentence)[-1] for sentence in sentences if re.findall(r'\b\w+\b(?=[.!?])', sentence)]

# Create an additional sentence using the last words from each sentence
def create_extra_sentence(last_words):
    return " ".join(last_words).capitalize() + "."

# Count the number of whitespace characters (spaces, tabs, newlines)
def count_whitespaces(text):
    return sum(1 for char in text if char.isspace())

# Main function to process the text
def process_text(text):
    initial_whitespace_count = count_whitespaces(text)
    print(f"Initial Whitespace Count: {initial_whitespace_count}")

    normalized_text = normalize_case(text)  # Normalize case
    normalized_text = fix_mistakes(normalized_text)  # Fix mistakes (like "iz" to "is")

    last_words = extract_last_words(normalized_text)  # Extract last words of each sentence
    extra_sentence = create_extra_sentence(last_words)  # Create additional sentence

    normalized_text += " " + extra_sentence  # Append the extra sentence

    final_whitespace_count = count_whitespaces(normalized_text)  # Count whitespace in the final text
    print(f"Final Whitespace Count: {final_whitespace_count}")

    return normalized_text

# Original text
text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Process the text
normalized_text = process_text(text)

# Output the normalized text
print("\nNormalized Text:\n", normalized_text)
