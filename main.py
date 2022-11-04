# Abel Vargas
# This is a program for teaching python to beginners

def basic_ops(num1, num2):
    print(f"{num1}**{num2}= " + str(num1 ** num2))  # num1^num2
    print(f"{num1}*{num2}= " + str(num1 * num2))  # num1 multiplied num2
    print(f"{num1}+{num2}= " + str(num1 + num2))  # num1 plus num1
    print(f"{num1}-{num2}= " + str(num1 - num2))  # num1 minus num2
    print(f"{num1}/{num2}= " + str(num1 / num2))  # num1 divided by num2
    print(f"{num1}//{num2}= " + str(num1 // num2))  # floor division
    print(f"{num1}%{num2}= " + str(num1 % num2))  # remainder of the numerical value
# this define function will be in option 2 and will calculate any whole number entered for num1 and num2

def basic_format(value):
    print(("Value changed: "), format(value, '.1f'))  # decimal number to the tenths decimal place
    print(("Value changed: "), format(value, '.2f'))  # decimal number to the hundredths place
    print(("Value changed: "), format(value, '.3f'))  # decimal number to the thousandths place
# this define function will be in option 3 and will show Pi outputted to the correct decimal place

def basic_boolean(num1, num2):
    print(f"The following statement {num1} == {num2} is", num1 == num2)  # num1 equal to num2
    print(f"The following statement {num1} > {num2} is", num1 > num2)  # num1 greater than num2
    print(f"The following statement {num1} < {num2} is", num1 < num2)  # num1 less than num2
    print(f"The following statement {num1} <= {num2} is", num1 <= num2)  # num1 less than or equal to num2
    print(f"The following statement {num1} >= {num2} is", num1 >= num2)  # num1 greater than or equal to num2
    print(f"The following statement {num1} != {num2} is", num1 != num2)  # num1 is not equal to num2
    # this define function will be in option 4 and will state whether the values entered are True or False
    #PRINT THE VALUES TO KNOW WHAT THE STATEMENT IS

def basic_d_format(value):
    print("Total cost is: $", format(value), sep='')
    print("Total cost is: $", format(value, '2d'), sep='')  # value displayed in second space
    print("Total cost is: $", format(value, '3d'), sep='')  # value displayed in third space
    print("Total cost is: $", format(value, '4d'), sep='')  # value displayed in fourth space
    print("Total cost is: $", format(value, '5d'), sep='')  # value displayed in fifth space
    print("Total cost is: $", format(value, '7d'), sep='')  # value displayed in sixth space
# this define function will be in option 5 and will result with the value creating space after the prompt and
# displaying the numerical value in the correct space

def using_if_else_operators(x,y):
    if (x < y):
        print(str(x)+" is less than "+str(y))
    else:
        print(str(x)+" is not less than "+str(y))
        if (x > y):
            print(str(x)+" is greater than "+str(y))
        else:
            print(str(x)+" is not greater than "+str(y))
            if (x == y):
                print(str(x)+" is equal to "+str(y))

def main_menu():
    print()
    print()
    print("1) Learn simple I/0 with 'end=' and 'sep='")
    print("2) Basic Operations")
    print("3) Formatting with 'f'")
    print("4) Boolean statements")
    print("5) Formatting with 'd'")
    print("6) using 'if' and 'else'")
    print("7) Using WHILE loops")
    print("8) Using FOR loops")
    print("9) Using AND function")
    print("Q) Type Q to quit and exit")



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi my name is , " + name)  # Press ⌘F8 to toggle the breakpoint.
    # The breakpoint comments were already there in PyCharm, just left there
    # for future reference. Didn't know what breakpoint was just yet  


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('Abel')
    print("Welcome to Python for Beginners Program")

    # displaying the user a few options to choose what they want to learn
    print("1) Learn simple I/0 with 'end=' and 'sep='")
    print("2) Basic Operations")
    print("3) Formatting with 'f'")
    print("4) Boolean statements")
    print("5) Formatting with 'd'")
    print("6) Using 'if' and 'else'")
    print("7) Using WHILE loops")
    print("8) Using FOR loops")
    print("9) Using AND function")
    print("Q) Type Q to quit and exit")
    selectOption = input("Please select one of the options:")
    while selectOption.lower() != "q":
        if selectOption == "1":
            # "if" function is telling the program what should happen under option 1 IF this option is chosen
            sentence = input("Type any sentence you want:")   # telling user to insert a sentence
            print("You typed: " + sentence)
            # prompt will be displayed along with sentence entered in previous line
            print("Using print() with end=!!!!")
            print(sentence, end='!!!!\n')
            # will output the sentence they typed with exclamation points at the end
            print("Using print() with sep=!!!!")
            print(sentence, "separating here!!!!", sep=' ')
            # will output the sentence they typed with a space between "sentence" and prompt
        elif selectOption == "2":
            x = int(input("Enter a number for x:"))
            y = int(input("Enter a number for y:"))
            # the user will have to insert an integer/whole number for x and Y
            print("using basic operations to calculate input variables")
            basic_ops(x, y)
            # running the define function that I have set up
        elif selectOption == "3":
            usingPie = input("Enter the value of Pi(3.14) to the thousandths place:")
            value = float(usingPie)  # telling program that number entered will not be whole but a decimal
            print("using format() with 'f'")
            basic_format(value)
            # running the define function that I have set up
        elif selectOption == "4":
            x = int(input("Insert any whole number:"))
            y = int(input("Insert any whole number:"))
            # allowing the user to type any whole number of their choosing
            print("outputting true and false statements")  # letting user know what will be displayed in output
            basic_boolean(x, y)
            # running the define function that I have set up
        elif selectOption == "5":
            number_of_items = int(input("Enter whole number:"))
            itemCost = int(input("Enter whole value:"))
            # will allow user to enter any whole number of their choosing
            price = number_of_items * itemCost
            # multiplying the whole numbers entered in previous lines
            print("using format() with 'd' and 'sep='")
            basic_d_format(price)
            # running the define function that i have set up
        elif selectOption == "6":
            x = int(input("Enter a whole number for x:"))
            y = int(input("Enter a whole number for y:"))
            using_if_else_operators(x,y)
        elif selectOption == "7":
            letterUse = input("Enter a letter that belongs in a-z:")
            while not letterUse.isalpha() or not letterUse.islower():
                letterUse = input("Enter a letter that belongs in a-z:")
                print("The WHILE loop will keep running until a lowercase is entered")
            print(letterUse)
        elif selectOption == "8":
            sentence = input("Enter one word or multiple words:")
            print("The FOR loop will print each letter of the word you entered with TAB space")
            words = sentence.split()
            for w in range(len(words)):
                word = words[w]
                for x in range(len(word)):
                    print(word[x], end="\t")
                print()
        elif selectOption == "9":
            value = int(input("Enter a positive or negative number number:"))
            if (value >= 0) and (value <= 100):
                print("The value you have entered is between 1 and 100")
            else:
                print("The you have entered is NOT between 1 and 100")

        main_menu()
        selectOption = input("Please select another option:")












# "elif" function is basically just saying that IF this option was selected 
# rather than another this is what the user should expect to see

#  Resources: w3schools.com, cloudxlab.com, learnpython.org
