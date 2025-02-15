from re import fullmatch


ANIMALS = ['aardvark', 'alligator', 'armadillo', 'antelope', 'baboon', 'bear',
           'bobcat', 'butterfly', 'cat', 'camel', 'cow', 'chameleon', 'dog',
           'dolphin', 'duck', 'dragonfly', 'eagle', 'elephant', 'emu',
           'echidna', 'fish', 'frog', 'flamingo', 'fox', 'goat', 'giraffe',
           'gibbon', 'gecko', 'hyena', 'hippopotamus', 'horse', 'hamster',
           'insect', 'impala', 'iguana', 'ibis', 'jackal', 'jaguar', 'yak',
           'kangaroo', 'kiwi', 'koala', 'killerwhale', 'lemur', 'leopard',
           'llama', 'lion', 'monkey', 'mouse', 'moose', 'meercat', 'numbat',
           'newt', 'ostrich', 'otter', 'octopus', 'orangutan', 'penguin',
           'panther', 'parrot', 'pig', 'quail', 'quokka', 'quoll', 'rat',
           'rhinoceros', 'racoon', 'reindeer', 'rabbit', 'snake', 'squirrel',
           'sheep', 'seal', 'turtle', 'tiger', 'turkey', 'tapir', 'unicorn',
           'vampirebat', 'vulture', 'wombat', 'walrus', 'wildebeast',
           'wallaby', 'jellyfish', 'zebra']


def road_kill(photo):
    if photo is None:
        return "??"
    remains = photo.replace('=', '')

    for animal in ANIMALS:
        parts = '^' + '+'.join(c for c in animal) + '+$'
        if fullmatch(parts, remains) or fullmatch(parts, remains[::-1]):
            return animal
    return "??"
