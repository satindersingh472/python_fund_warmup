list_strings = ['qtring_one','string_two','string_three','string_four','string_five']

def string_printer(one_string):
    if (one_string.startswith('q')):
        print(one_string ,', q found')

for each_string in list_strings:
    string_printer(each_string)

string_printer('god bless you')


list_dictionaries = [
    {
        'username': 'satinder',
        'is_subscribed': True,
        'age': 27
    },
    {
        'username': 'sam',
        'is_subscribed': False,
        'age': 26
    },
    {
        'username': 'jag',
        'is_subscribed': True,
        'age': 55
    }
    ]

def dictionary_printer(dictionaries):
    new_list = []
    for each_dictionary in dictionaries:
        if(each_dictionary['is_subscribed'] == True):
            new_list.append(each_dictionary)
    return new_list

print(dictionary_printer(list_dictionaries))