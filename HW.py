d1={'welcome' :10,'to' :2,'my' :10,'class' :10}
print("Dictionary: ",str(d1))
n=int(input("Enter a number to check how many times its repeated: "))
frequency=0
for key in d1:
    if d1[key]==n:
        frequency=frequency+1
print("Frequency of your number is " + str(frequency))
