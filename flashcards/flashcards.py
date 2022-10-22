cards = int(input('Input the number of cards:\n'))
dictionary = {}


class TermExistError(Exception):
    def __init__(self, a):
        self.message = 'The term "%s" already exists. Try again:' % a
        super().__init__(self.message)


class DefinitionExistError(Exception):
    def __init__(self, b):
        self.message = 'The definition "%s" already exists. Try again:' % b
        super().__init__(self.message)


for card in range(1, cards + 1):
    print(f'The term for card #{card}:')
    while True:
        try:
            term = input()
            if term in dictionary.keys():
                raise TermExistError(term)
            else:
                break
        except TermExistError as err:
            print(err)
            continue
    print(f'The definition for card #{card}:')
    while True:
        try:
            definition = input()
            if definition in dictionary.values():
                raise DefinitionExistError(definition)
            else:
                break
        except DefinitionExistError as err:
            print(err)
            continue
    dictionary[term] = definition


def get_key(val):
    for k, v in dictionary.items():
        if val == v:
            return k


for key in dictionary:
    answer = input(f'Print the definition of "{key}":\n')
    if answer == dictionary[key]:
        print('Correct!')
    else:
        result = get_key(answer)
        if result is None:
            print(f'Wrong. The right answer is "{dictionary[key]}".')
        else:
            print(f'Wrong. The right answer is "{dictionary[key]}",'
                  f'but your definition is correct for "{result}".')
