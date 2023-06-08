# https://github.com/GrandEmperorBinks

# Import the necessary module(s).
import json


# This function repeatedly prompts for input until an integer between 1 and max_value is entered.
def input_int(prompt, max_value):
    while True:
        try:
            value = int(input(f'{prompt}: '))
        except ValueError:
            print('Invalid value type')
            continue
        if value >= 1 and value <= max_value:
            return int(value)
            break
        else:
            print(f'Please enter an amount under {max_value}')


# This function repeatedly prompts for input until something other than whitespace is entered.
def input_something(prompt):
    while True:
        value = input(f'{prompt}: ')
        value = value.strip()
        if value == '':
            print('Please enter a valid response')
            continue
        else:
            return str(value)
            break


# This function opens "data.txt" in write mode and writes data to it in JSON format.
def save_data(data):
    file = open('data.txt', 'w')
    json.dump(data, file, indent = 4)
    file.close()
    print('Data written to data.txt.')



# Attempt to open data.txt and read the data into a "data" variable.
try:
    file = open('data.txt', 'r')
    data = json.load(file)
    file.close()
except:
    data = []


# Print welcome message, then enter the endless loop which prompts the user for a choice.
print('Welcome to the "Know It All" Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() 
        
    if choice == 'a':
        # Add a new category.
        new_data = {}
        new_data['category'] = input_something('Enter Category Name')
        answers = []
        while True:
            response = input_something('Enter an answer ("x" to end)')
            if response == 'x':
                break
            else:
                answers.append(response)
        new_data['answers'] = answers
        new_data['difficulty'] = input_int('Enter difficulty', 3)
        print('Category added.')
        data.append(new_data)
        save_data(data)

    
    elif choice == 'l':
        # List the current categories.
        if data == []:
            print('No categories saved')
        else:
            print('List of categories:')
            for index, categories in enumerate(data):
                print(f'{index+1}) {categories.get("category")}')


    elif choice == 's':
        # Search the current categories.
        if data == []:
            print('No categories saved')
        else:
            search_term = input_something('Enter search term')
            search_term = search_term.lower()
            count = 0
            for index, categories in enumerate(data):
                category = categories.get('category')
                category = category.lower()
                if category.find(search_term) == -1:
                    continue
                else:
                    print(f'{index+1}) {category}')
                    count += 1
            if count == 0:
                print('No results found')


    elif choice == 'v':
        # View a category.
        if data == []:
            print('No categories saved')
        else:
            view_index = input_int('Category number to view',  len(data))
            view_category = data[view_index-1]
            category = view_category.get('category')
            answer = view_category.get('answers')
            answers = ''
            for value in answer:
                answers = answers + str(value) + ', '
            answers = answers.rstrip(',')
            difficulty = view_category.get('difficulty')
            print(f'  Category:    {category}')
            print(f'  Answers:     {answers}')
            print(f'  Difficulty:  {difficulty}')

        
    elif choice == 'd':
        # Delete a category.
        if data == []:
            print('No categories saved')
        else:
            delete_index = input_int('Category number to delete', len(data))
            del data[delete_index-1]
            save_data(data)
            print('Category deleted')
        

    elif choice == 'q':
        # End the program.
        print('Goodbye')
        break



    else:
        # Print "invalid choice" message.
        print('Invalid choice')
