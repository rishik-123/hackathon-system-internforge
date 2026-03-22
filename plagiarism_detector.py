from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def check_plagiarism(answer_list):
    plag_pairs = []

    for i in range(len(answer_list)):
        for j in range(i + 1, len(answer_list)):
            sim = similarity(answer_list[i], answer_list[j])

            if sim > 0.8:
                plag_pairs.append((i, j))

    return plag_pairs