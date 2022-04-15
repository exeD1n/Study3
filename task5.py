import random

def get_jokes(n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    
    
    list_shutok = []
    for _ in range(n):
        word_nouns = random.choice(nouns)
        word_adverbs = random.choice(adverbs)
        word_adjectives = random.choice(adjectives)
        list_shutok.append(f'{word_nouns} {word_adverbs} {word_adjectives}')
        
    print(list_shutok)
    
    
if __name__ == "__main__":
    get_jokes(2)