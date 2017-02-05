def test():
    value=input("Value here!") #eval is bad AND dangerous practice. Avoid using it.
    with open ("word-text.txt","r") as f:
        #At this point you can do one of two things:
        #1) read the entire file line by line
        #2) read the entire file into a list, and loop/iterate over that list
        #In this example, I'll read the file line by line:
        nice_strings = []
        for line in f:
            line = line.strip() #remove any extraneous whitespace from the line (e.g. spaces and newlines)
            nice_str_chars = []
            #At this point, you want to read EACH character in the line
            #N.B.: ord is the name of a built-in function. Use another name like `char` (below):
            for char in line:
                #Since you're in this loop, you are dealing with EACH individual character of each line
                #And, as you want to "shift" the character by some number of places
                #Python doesn't allow you to natively shift strings by arbitrary amounts,
                #so, the only way we can do so is to convert EACH character into its numeric representation.
                #In order to do so, you have to use the `ord` function which converts characters into
                #their respective integer representation.
                int_of_char = ord(char)
                #At this point, the character has been converted to it's integer equivalent
                #NOW, you can "shift" it. In other words, add the value to the `int_of_char`:
                int_of_char += value #update the value of the variable
                #At this point, the value has been modified, and the INTEGER value of the character has been
                #shifted. However, we don't want the shifted INTEGER value: we want the shifted CHARACTER value.
                #So, how do we convert integers to characters? Python has a builtin function called `chr` which
                #does exactly that.
                #So, let's convert the shifted INTEGER to a shifted CHARACTER using `chr`:
                nice_char = chr(int_of_char)
                #print it out the original and modified characters so you can see what's in the string (this step is optional)
                print char, '=>', nice_char
                #At this point we've successfully shifted the character. However, since this is just A character of the original
                #string, we need a way to save the updated characters as a string. There are a number of ways to do this.
                #For simplicity, we can use a list `nice_str_chars`:
                nice_str_chars.append(nice_char)
            #At this point we've looped over all the characters in ONE LINE, and we've calculated and stored the shifted
            #characters for that same line. However, since we've stored the characters in a list: `nice_str_chars`, we
            #have to convert it to a string. We can do that using the `join` method on an empty string, with 
            #`nice_str_chars` as the list (as we want to join the characters of the list into a string):
            nice_str = ''.join(nice_str_chars)
            #And, since you want to shift ALL the lines, you ought to append the corrected line to a list that can later be
            #returned:
            nice_strings.append(nice_str)
            #you can print it out if necessary:
            print line, '=>', nice_str, '\n'
        #At this point, you've successfully looped over the entire file, shifted all lines by a user entered integer amount,
        #now, all you have to do is return it, or do something else with them (i.e. write the updated strings to another file).
        #That part, I'll leave up to you.
        return nice_strings