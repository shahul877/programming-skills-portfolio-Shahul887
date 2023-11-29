glossary = {
     "Variable": "A named storage location in the computer's memory, used to store and manipulate data during program execution.",
    "Function": "A reusable block of code that performs a specific task. Functions help in organizing code and promoting reusability.",
    "Loop": "A control flow statement that allows code to be repeatedly executed. Common types include 'for' loops and 'while' loops.",
    "Conditional Statement": "A programming construct that performs different actions based on whether a certain condition evaluates to true or false.",
    "Algorithm": "A step-by-step set of instructions or rules to solve a specific problem or accomplish a particular task in a finite amount of time.",
    "List": "An ordered collection of items. Lists are mutable, meaning their elements can be changed after creation.",
    "Tuple": "Similar to a list, but immutable. Once a tuple is created, its elements cannot be changed or modified.",
    "Dictionary": "A collection of key-value pairs. Dictionaries are unordered and can be used to store and retrieve data efficiently.",
    "Module": "A file containing Python definitions and statements. Modules allow code organization and reuse.",
    "Exception": "An error that occurs during the execution of a program. Exception handling allows the program to gracefully deal with errors.",
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
