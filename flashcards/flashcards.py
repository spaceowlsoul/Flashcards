import random

dictionary = {}


class TermExistError(Exception):
    def __init__(self, a):
        self.message = 'The term "%s" already exists. Try again:' % a
        super().__init__(self.message)


class DefinitionExistError(Exception):
    def __init__(self, b):
        self.message = 'The definition "%s" already exists. Try again:' % b
        super().__init__(self.message)


def add_term():
    print('The card:')
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
    add_definition(term)


def add_definition(t):
    print('The definition of the card:')
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
    dictionary[t] = definition
    print(f'The pair ("{t}":"{definition}") has been added.')


def remove_card():
    card = input('Which card?\n')
    if card in dictionary.keys():
        dictionary.pop(card)
        print('The card has been removed.')
    else:
        print(f'Can\'t remove "{card}": there is no such card.')


def import_from_file():
    try:
        file = open(str(input('File:\n')))
    except FileNotFoundError:
        print('File not found.')
    else:
        count = 0
        for line in file:
            term, definition = line.split(':')
            dictionary[term] = definition.rstrip('\n')
            count += 1
        print(f'{count} cards have been loaded.')
        file.close()


def get_term(val):
    for k, v in dictionary.items():
        if val == v:
            return k


def ask_card(d):
    if d is None:
        print('The dictionary is empty. Fill it in via "add" command.')
    else:
        times = int(input('How many times to ask?\n'))
        for _ in range(times):
            term = random.choice([x for x in dictionary.keys()])
            answer = input(f'Print the definition of "{term}":\n')
            if answer == dictionary[term]:
                print('Correct!')
            else:
                result = get_term(answer)
                if result is None:
                    print(f'Wrong. The right answer is "{dictionary[term]}".')
                else:
                    print(f'Wrong. The right answer is "{dictionary[term]}", '
                          f'but your definition is correct for "{result}".')


def export_file(d):
    if d is None:
        print('The dictionary is empty. Fill it in via "add" command.')
    else:
        count = 0
        with open(str(input('File:\n')), 'w') as file:
            for key, value in d.items():
                file.write(f'{key}:{value}\n')
                count += 1
            print(f'{count} cards have been saved.')


def main():
    while True:
        action = input('Input the action (add, remove, import, export, ask, exit):\n')
        if action == 'add':
            add_term()
        elif action == 'remove':
            remove_card()
        elif action == 'import':
            import_from_file()
        elif action == 'export':
            export_file(dictionary)
        elif action == 'ask':
            ask_card(dictionary)
        elif action == 'exit':
            print('Bye bye!')
            break
    print()


if __name__ == '__main__':
    main()
