
import re #import Counter
from collections import Counter # Added import for Counter

def top_3_words(text):
    # Find all valid words (letters + apostrophes)
    words = re.findall(r"[a-zA-Z']+", text.lower()) # Extract words, ignore case

    # Filter out strings that are only apostrophes like "''" or "'"
    words = [w for w in words if re.search(r"[a-z]", w)] # Keep words with at least one letter

    if not words:
        return []

    # Count occurrences
    counts = Counter(words) # Count word frequencies

    # Return the top 3 words
    return [word for word, _ in counts.most_common(3)]  
# Test cases
print(top_3_words("In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, some lean chorizo, and a pigeon or so, constituted his whole diet."))
print(top_3_words("  //wont won't won't "))  # Expected: ["won't", "wont"]
print(top_3_words("  , e   .. "))          # Expected: ["e"]
