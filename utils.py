from fuzzywuzzy import fuzz

def is_similar_to_any(string, string_list, threshold=70):
    for item in string_list:
        similarity_score = fuzz.token_set_ratio(string, item)
        if similarity_score >= threshold:
            return True
    return False