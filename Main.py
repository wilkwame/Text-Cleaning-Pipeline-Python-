import re
import nltk
import string
from nltk.corpus import stopwords


# Loading sample text 

with open("sample_paragrph.txt", "r", encoding="utf-8") as file:
    text = file.read()

    print("----------------Original Text----------------")
    print(text)

    # Lowercasing text

    lower_text = text.lower()
    print("--------------Lowercasing-------------")
    print(lower_text)

# Removing Stopwords
myStopwords = set(stopwords.words('english'))

def removing_stopwords(sentence):
    token = sentence.split()
    filtered = [word for word in sentence if word not in myStopwords]
    return " ".join(filtered)

no_stopwords = removing_stopwords(lower_text)
print('-------- Without Stopwords --------')
print(no_stopwords)


# -------------------------------
#         * Remove puntuation
#         * Remove numbers
#         * Remove multiple spaces
# -------------------------------

def reg_clean(sentence):
    # Removing digits
    sentence = re.sub(r"[0-9]+", "", sentence)

    # Removing puctuations
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    # Fixing spaces
    sentence = re.sub(r"\s+", " ", sentence).strip()
    return sentence

cleaned_data = reg_clean(no_stopwords)
print("\n=== Regex-Cleaned Text ===")
print(cleaned_data)