import re

# Original text (preserving "homEwork:")
text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# Count initial whitespace characters
initial_whitespace_count = sum(1 for char in text if char.isspace())
print(f"Initial Whitespace Count: {initial_whitespace_count}")

# Normalize case for each sentence while keeping "homEwork:"
def normalize_case(text):
    lines = text.split("\n")  # Preserve newlines properly
    lines[0] = "homEwork:"  # Ensure "homEwork:" stays the same

    sentences = re.split(r'(?<=[.!?])\s+', "\n".join(lines[1:]))  # Split sentences while preserving formatting
    normalized_text = " ".join(sentence.capitalize() for sentence in sentences)  # Capitalize each sentence properly
    return lines[0] + "\n" + normalized_text  # Keep "homEwork:" at the beginning

# Apply normalization
normalized_text = normalize_case(text)

# Fix "iz" only when it's a mistake
normalized_text = re.sub(r'\biz\b', 'is', normalized_text)

# Extract last words of each sentence
sentences = re.split(r'(?<=[.!?])\s+', normalized_text)
last_words = [re.findall(r'\b\w+\b(?=[.!?])', sentence)[-1] for sentence in sentences if re.findall(r'\b\w+\b(?=[.!?])', sentence)]
extra_sentence = " ".join(last_words).capitalize() + "."

# Add extra sentence to the paragraph
normalized_text += " " + extra_sentence

# Count final whitespace characters
final_whitespace_count = sum(1 for char in normalized_text if char.isspace())
print(f"Final Whitespace Count: {final_whitespace_count}")

# Output results
print("\nNormalized Text:\n", normalized_text)
