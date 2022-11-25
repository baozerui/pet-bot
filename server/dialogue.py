from flair.data import Sentence
import random

intents = [
    "background",
    "search-desc",
    "search-end",
    "want-more",
    "details",
    "reset",
    "bye"
]


def get_tags(sentence : Sentence):
    return [{"text": "black", "tag": "color", "confidence": 0.9837}]


def dialogue(input : str):
    random.seed(0)
    
    # TODO: Load models
    classifier = None
    tagger = None
    
    sent = Sentence(input)
    
    # TODO: Predict intent
    intent = intents[random.randrange(len(intents))]
    
    # TODO: Tag sentence
    if intent == "search-desc":
        # sent_copy = tagger.predict(sent_copy)
        tags = get_tags(sent)
        return intent, tags
    else:
        return intent, None
    
if __name__ == "__main__":
    print(dialogue("I want a black cat"))