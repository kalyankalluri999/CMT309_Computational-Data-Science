

# Studnet ID: 21109714

def pluralize(word):
    '''
     "def":- In Python def is a keyword used to build or define a function. A function is a logical unit of code containing a sequence of statements indented 
     under a name given using the “def” keyword.
     "pluraize":- This function Returns the singular or plural form of the word based on the input number, using an optional dictionary if supplied. 
    '''
    dict = {}
  # Called empty dictionary
    vowels = ['a','e','i','o','u']
   #Taken a variable vowels in a list.

    my_file = open("proper_nouns.txt.txt","r")
     # Used a variable my_file and we are using the funcion open() to open respective file passed in the program.
     # The 'r' states that the file should be opened in read mode 
     # If we are not loading data file properly we get an error "FileNotFoundError: [Errno 2] No such file or directory: 'proper_nouns.txt.txt'". so before
      processing with the code we have to make sure proper data file is loaded.

    content = my_file.read()
    # using function read we are reading the proper_nouns.txt file

    content_list = content.split("\n")
    # split() method is used for spliting a string into a list.
    my_file.close()
    #For closing the file
    
    #if empty string is passed
    if word == '':
        dict['plural'] =  ''
        dict['status'] = 'empty_string'
        return (dict)
    elif word.lower() in content_list:
        dict['plural'] =  word
        dict['status'] = 'proper_noun'
        return (dict)
    elif word[-3:].lower() == 'ies' or word[-2:].lower() == 'es' or word[-1:] == 's':
        dict['plural'] =  word
        dict['status'] = 'already_in_plural'
        return (dict)
    elif word[-1:].lower() in vowels:
        dict['plural'] = word + 's'
        dict['status'] = 'success'
        return (dict)
    elif word[-2:].lower() == 'sh' or word[-2:] == 'ch' or word[-1:] == 'z':
        dict['plural'] = word + 'es'
        dict['status'] = 'success'
        return (dict)
    elif word[-1:].lower() == 'f':
        dict['plural'] = word[:-1] + 'ves'
        dict['status'] = 'success'
        return (dict)
    elif word[-1:].lower() == 'y' and word[-2:-1].lower() not in vowels:
        dict['plural'] = word[:-1] + 'ies'
        dict['status'] = 'success'
        return(dict)
    else:
        dict['plural'] = word + 's'
        dict['status'] = 'success'
        return(dict) #retuning the dictionary as asked


pluralize('failure')
pluralize('food')
pluralize('Zulma')
pluralize('elf')
pluralize('computers')
pluralize('PCs')
pluralize('')

#Studnet ID: 21109714