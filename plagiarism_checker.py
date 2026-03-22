from difflib import SequenceMatcher

def check_similarity(ans1,ans2):

    similarity = SequenceMatcher(None,ans1,ans2).ratio()

    return similarity