# 1. Write some text to file using Python, then read it as binary data
with open('file.txt', 'rb') as file:
    print(file.read())


# 2. Download manually some text file, add manually several splitting symbols to it (for instance ‘;;’), then read file
# contents, split it by symbols, find the length of each chunk.
def splitted_data():
    with open('file.txt', 'r') as file:
        file_data = file.read()
        splited_data = file_data.split(';')
        for data in splited_data:
            print(len(data))

splitted_data()


# 3. Write some 100000 characters(random symbols) to a file using Python, then read that file and check how many ‘a’ symbols it contains
def characters():
    file = open('text.txt', 'w')
    text = '''
    If you’ve used lower-level languages such as C or C++, you know that much of your work centers on implementing 
    objects—also known as data structures—to represent the components in your application’s domain. You need to lay 
    out memory structures, manage memory allocation, implement search and access routines, and so on. These chores 
    are about as tedious (and error-prone) as they sound, and they usually distract from your program’s real goals.
    In typical Python programs, most of this grunt work goes away. Because Python provides powerful object types as 
    an intrinsic part of the language, there’s usually no need to code object implementations before you start solving 
    problems. In fact, unless you have a need for special processing that built-in types don’t provide, you’re almost 
    always better off using a built-in object instead of implementing your own.
    As we just saw, the very meaning of the expression x * y in our simple times function depends completely upon the
    kinds of objects that x and y are—thus, the same function can perform multiplication in one instance and repetition 
    in another. Python leaves it up to the objects to do something reasonable for the syntax. Really, * is just a 
    dispatch mechanism that routes control to the objects being processed.
    This sort of type-dependent behavior is known as polymorphism, a term we first met in Chapter 4 that essentially 
    means that the meaning of an operation depends on the objects being operated upon. Because it’s a dynamically typed
    language, polymorphism runs rampant in Python. In fact, every operation is a polymorphic operation in Python: 
    printing, indexing, the * operator, and much more.
    This is deliberate, and it accounts for much of the language’s conciseness and flexibility. A single function, 
    for instance, can generally be applied to a whole category of object types automatically. As long as those objects 
    support the expected interface (a.k.a. protocol), the function can process them. That is, if the objects passed 
    into a function have the expected methods and expression operators, they are plug-and-play compat- ible with the 
    function’s logic.
    Even in our simple times function, this means that any two objects that support a * will work, no matter what they 
    may be, and no matter when they are coded. This function will work on two numbers (performing multiplication), or a 
    string and a number (per- forming repetition), or any other combination of objects supporting the expected 
    interface—even class-based objects we have not even coded yet.
    Moreover, if the objects passed in do not support this expected interface, Python will detect the error when the * 
    expression is run and raise an exception automatically. It’s therefore pointless to code error checking ourselves. 
    In fact, doing so would limit our function’s utility, as it would be restricted to work only on objects whose types 
    we test for.
    '''
    file.write(text)
    file.close()
    counter = 0

    for character in text:
        if 'a' in character:
            counter += 1
    print(counter)

characters()


# 4. Find which number starting from 1 to 1000000 can be divided to 56, to 23 and to 7.
def numbers():
    divisible_numbers = [i for i in range(1, 1000000) if i % 56 == 0 or i % 23 == 0 or i % 7 == 0]
    print(divisible_numbers)

numbers()

# 5. Read symbol from text file at some random position
with open('file.txt', 'r') as file:
    print(file.read(6))


# 6. Download a big text file manually, find if it contains text word (place manually)
def word_text():
    with open('file.txt', 'r') as file:
        if len(file.read()) > 1:
            return True
        return False