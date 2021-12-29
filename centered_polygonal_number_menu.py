


print("Welcome to the Centered Polygonal Number program!")
print("Here are your choices:")

#the main function
def main():
    #making a loop for rebaiting the program
    again = False
    while not again:
        # calling the choises function
        choices()

        # an input for the user to chose a choice
        choice = int(input("Enter your choice (1 - 4):"))

        # a while loop to make chore the user intered the right input
        while choice < 1 or choice > 4:
            choice = int(input("Invalid entry. Re-enter your choice (1 - 4):"))


        order = int(input("Enter an order number( >= 1):"))
        while order < 1:
            order = int(input("Invalid entry. Re-enter your order number (>=1):"))


        if choice == 1:
            x = 'centered triangular series'
        elif choice == 2:
            x = 'centered pentagonal series'
        elif choice == 3:
            x = 'centered heptagonal series'
        elif choice == 4:
            x = 'centered hendecagonal series'
            
        # print the answer 
        print("The number in position", order,"of the", x, "is:", end= " ")

        # calling the function depanding on the user choise 
        # writing an f elif statment 
        if choice == 1:
            print(centered_triangle(order))
        elif choice == 2:
            print(centered_pentagonal(order))
        elif choice == 3:
            print(centered_heptagonal(order))
        elif choice == 4:
            print(centered_hendecagonal(order))



        # ask the user if he want to run the program again
        yes_no = input("Would you like to run the program again? Enter yes or no:")
        string = yes_no.lower()
        
        # if else statment to run the program again or stop
        if yes_no == 'no':
            again = True
            print("Thanks for using the program! Goodbye!")
            continue
        else:
            print()
            again = False









# a function for the choices
def choices():
    print("1. Centered Triangular Number")
    print("2. Centered Pentagonal Number")
    print("3. Centered Heptagonal Number")
    print("4. Centered Hendecagonal Number")

# a function for the Centered Triangular Number
def centered_triangle(number):
    p_n = ((3 * (number ** 2)) + (3 * number) + 2) / (2)
    return int(p_n)
# a function for Centered Pentagonal Number
def centered_pentagonal(number):
    p_n = ((5 * (number ** 2)) + ( 5 * number) + 2) / (2)
    return int(p_n)
# a function for Centered Heptagonal Number
def centered_heptagonal(number):
    p_n = (( 7 * (number ** 2)) + ( 7 * number) + 2) / (2)
    return int(p_n)
# a function for Centered Hendecagonal Number
def centered_hendecagonal(number):
    p_n = ((11 * (number ** 2)) + ( 11 * number) + 2) / (2)
    return int(p_n)

# calling the main function
main()
