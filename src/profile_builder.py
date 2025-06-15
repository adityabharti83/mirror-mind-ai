from textblob import TextBlob

def analyze_text_profile(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    word_count = len(text.split())
    traits = {
        "positivity": round(polarity, 2),
        "analytical": "high" if "analyze" in text.lower() else "moderate",
        "peaceful": "yes" if "peace" in text.lower() else "unknown",
        "subjectivity": round(subjectivity, 2),
        "wordiness": "verbose" if word_count > 20 else "concise"
    }
    return traits
