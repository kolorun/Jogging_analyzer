#COMP.CS.100 The first Python program.
#Creator: Oloruntobiloba Kolawole
#Student id number: 050401219

""" I wrote this code and it will prompt the user to select number of days to be
analyzed as well as the km covered during those days then it would find the
average km ran and determine if it was low or high. If the user enters zero,
three times consecutively the program terminates."""

def main():
    no_of_days = int(input("Enter the number of days: "))
    sum = 0
    value_zero = 0
    previous = 1
    consecutive_days = True
    for X in range(1, no_of_days + 1):
        running_length = float(input("Enter day {} running length: ".format(X)))
        if previous == 0 and running_length == 0:
            value_zero += 1
        else:
            value_zero = 0
        sum += running_length
        previous = running_length
        if value_zero == 2:
            print(" ")
            print("You had too many consecutive lazy days!")
            consecutive_days = False
            break

    if consecutive_days:
        z = sum / no_of_days
        if z < 3:
            print(" ")
            print("Your running mean of {0:.2f} km was too low!".format(z))
        else:
            print(" ")
            print("You were persistent runner! With a mean of {0:.2f} km.".format(z))
if __name__ == "__main__":
    main()
