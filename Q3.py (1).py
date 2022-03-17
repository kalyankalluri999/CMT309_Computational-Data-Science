

# Studnet ID: 21109714

def function_renamer(code):
    
    """
    Used "def" keyword function_renamer which takes input arguments: a multi line python code ('code') of type string.
 
    def - In Python def is a keyword used to build or define a function. A function is a logical unit of code containing a sequence of statements indented 
    under a name given using the “def” keyword.

    function_renamer - It is a function that takes as input a string "code" that represents the Python code. 
    It is typically a multi-line Python string. The function needs to return the tuple (d, newcode):

    It takes a piece of code as input, and finds every function name and replace it into its camel case in the code.
    
    Output:
    ---------    
    Returns a tuple t = (d,newcode) that consists of a nested dictionary "d" and a string named "newcode" which repersents the code with the 
    names of the functions replaced by their camel cases.
    The dictionary d composed of keys equal to the number of function's names founded in the code.
    Each key has three values. The hash code of its function before the transformation, its camel case and an all caps version of the unchanged function name. 
    ---------
   
    """
    import re

    # Here we are using a python built in package called "re" or "RegEx" or "Regular expersion" is a sequence of characters that forms a search pattern
    # When we start using package 're' we can start using regular expressions.

    d = {}
    #we called a variable 'd' with empty dicionary.
    
    functions_labels = re.findall(r'def\s*(\w+)\(.+', code)
    #Find the original function name established after the command 'def'.

    '''
    In the above code we used a variable called 'functions_labels' 
    re.findall - It is a part of "re" package and also it is a module used to search for “all” occurrences that match a given pattern. 
    '''
    for label in functions_labels :
        #Keeps function's names without any underscores or numbers before the first letter.
       
        names_with_underscores = re.findall(r'[^_*].+', label)
        #Finds every word from the list function_names. It works like spliting them in every underscores between them.
       
        split_names= re.findall(r'[a-zA-Z]+', label)
        #From the split_names we seperate the categories in which there are underscores between the words (len(spli_names)>1)
        #or there are no underscores between the words.

        #If the given name was split in at least one underscore the following procedure is followed: 
        if len(split_names)> 1:
            
            #Next, we implement the function title in every seperated word and then join them into a string.
            new_name= ''.join(x.title() for x in split_names)
           
            #In this step we join the changed names with the underscores in front of them if there were any.
            for ix in names_with_underscores :
                camelcase = re.sub(ix , new_name, label)
                
                #After we have created the camelcase names forms, we define a dictionary for each name with its hash code,
                #its camel case and its upper form. 
                d[label]= {"hash":hash(label), "camelcase":camelcase, "allcaps":label.upper()}
                
                #Finally we replace the old names with the camelcases into the code.
                code= re.sub(ix , new_name , code)
                
                '''
                re.sub() - The ‘re.sub’ is a module used to replace occurrences of a particular sub-string with another sub-string.
                
                '''
        
        #If the given name was not split in any underscores, we use 'upper' only in its first letter.
        else:
            new_name= label[0].upper() + label[1:]
            
            #Create the dictionary.
            d[label]= {"hash": hash(label), "camelcase":new_name, "allcaps":label.upper()}
            
            #Put the camelcases into the code replacing the old names.
            code= re.sub(label, new_name, code)
               
    newcode= code

    return (d,newcode)

#Studnet ID: 21109714