import csv
import json

# 2. create a game, where a user has to get through as many items in the list (i.e. answer them correctly), and when they ultimately fail, then they get a high score and have to start again (which also forces them to continue practicing)
# 2.1 is to create the functions to read both the long list of space-repeated words so that we can loop over them and test the user continuously until they fail, at which point we give them a score, and also the word definitions so that we may show a user a word definition if it's their first time encountering the word
def load_words_from_csv(file_path):
    '''Loads a list of words from a csv file'''
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        words = []
        for row in reader:
            if row:
                words.append(row[0])  
        return words
    
def load_definitions_from_json(file_path):
    '''Load definitions from a json file'''
    with open(file_path, 'r') as f:
        definitions = json.load(f)
    return definitions

# 2.2 define a continuous while loop, that tests the user on each word in the list, one after another in the provided order, and will only exit when each word has been mastered, or the user makes a mistake

def test_user(words, definitions):
    '''Test the user on the words and their definitions'''
    
    top_score = 0
    encounter_words = set() # track which words the user has already encountered

    for word in words:
        print(f'\nDefine: {word}')

        # If we have a word that isn't defined, skip it because its an error
        if word not in definitions:
            print('Definition not found for this word. Skipping...')

        # Can confirm word has a definition, so we can test a user
        definition = definitions[word]

        # if its the first time encountering the word, show the definition
        if word not in encounter_words:
            print(f'{word} -> {definition}')

        user_input = input('Answer: ')

        # Check if the user input matches the definition
        if user_input.lower() != definition.lower():
            print('\nGame Over!')
            print(f'Top Score: {top_score}')
            print(f'You failed on the word: {word}')
            print(f'Correct Definition: {definition}')
            return
    
        # Add the word to encountered words and increment the score as they asnwered correctly
        encounter_words.add(word)
        top_score += 1
        print('Correct!')

    # We have finished the entire for loop, completed every word in the list and the user has won the game
    print('\nCongratulations! You have completed the game :)')
    print(f'Top Score: {top_score}')

# 2.3 print the new high score when they fail or win, and also a command to start again
if __name__ == "__main__":
    # file paths
    csv_file_path = 'words_history.csv'
    json_file_path = 'definitions.json'

    # load data
    words = load_words_from_csv(csv_file_path)
    definitions = load_definitions_from_json(json_file_path)

    # start the game
    print('Welcome to the Word Definition Game!')
    test_user(words, definitions)