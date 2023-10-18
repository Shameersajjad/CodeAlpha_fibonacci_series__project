# Here we can create a function of printing of the fibonacii series

# first of all we can create a fib function
def fib(n):

# here we can define a two variables of initialization
    a = 0
    b = 1
# now we can use the if statement to specify when user enter only one number than the one number is printed otherwise 
# two numbers are printed
    if n == 1:
        print(a)

    else:
        print(a)
        print(b)
    # now we can use the for loop to repeat the series
        for  i in range(2,n):
    # now we can use the third variable to specify the sum of a and b
            c = a+b
            a= b
            b= c

            print('\n',a+b)
# here we can call the user to enter number the he/her want to print the fibonacci series
n= int(input("Enter the number"))
fib(n)