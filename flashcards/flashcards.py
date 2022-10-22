cards = int(input('Input the number of cards:\n'))
dictionary = {}

for card in range(1, cards + 1):
    term = input(f'The term for card #{card}:\n')
    definition = input(f'The definition for card #{card}:\n')
    dictionary[term] = definition
for key in dictionary:
    answer = input(f'Print the definition of "{key}":\n')
    if answer == dictionary[key]:
        print('Correct!')
    else:
        print(f'Wrong. The right answer is "{dictionary[key]}".')