def generate_hashtag(text):
    text = text.strip()
    text = ' '.join(text.split())
    hashtag = ''.join(word.capitalize() for word in text.split())
    if not hashtag:
        return False
    if len(hashtag) + 1 > 140:
        return False    
    return "#" + hashtag