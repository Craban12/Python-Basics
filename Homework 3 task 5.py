def get_jokes(number_attempts):
    from random import choice

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    world_joke = []

    for i in range(int(number_attempts)):
        a = choice(nouns), choice(adverbs), choice(adjectives)
        world_joke.append(a)
    return world_joke

print(get_jokes(input()))