list_strings = ['qtring_one','string_two','string_three','string_four','string_five']
for each_string in list_strings:
    print(each_string)

def string_printer(one_string):
    if (one_string.startswith('q')):
        print(one_string ,', q found')

string_printer('god bless you')

for each_string in list_strings:
    string_printer(each_string)

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
    for each_dictionary in dictionaries:
        if(each_dictionary["is_subscribed"] == True):
            new_list = each_dictionary
            print(new_list)

dictionary_printer(list_dictionaries)