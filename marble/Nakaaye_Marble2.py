"""
Control Flow
Conditional Statements(if-elif-else)
"""
"""
    if condition1:
        print('True') # Code lock is only executed if condition1 is true
    elif condition:
        print ('True) #code block is only executed if condition2 is true
    else:
        print('False') #code block is only executed if all conditions are false
"""

age=9
if age<18:
            print("You are underage please")

elif age>=18 and age<=65:
            print("You are adult")

else:
     print("You are a senior citizen")

     #Loops
     #Loops(for, while)

"""
     for i in sequence:(Can only execute that code for each item in the sequence)
            #Loop through(Iterate over sequences)
     """
cars= ["Tesla", "Jeep", "Ford", "Toyota", "BMW"]
for car in cars:
    print(car) 
        
    fruits=["Mangoes", "Apples", "Oranges", "Bananas"]
for fruit in fruits:
    print(fruit)

    for i in range(1,10):
        print (i)

    #while loop
fruits=["Mangoes", "Apples", "Oranges", "Bananas"]

fruit_count=0
while fruit_count< len(fruits):
    print(fruits[fruit_count])
    fruit_count += 1

#Example3
    x=0

    while x>5:
        print(x)
        x+=1

phones=("Samsung", "Iphone", "Tecno", "Huawei", "Itel")
phones_count=0
while phones_count<len(phones):
        print(phones[phones_count])
        phones_count += 1

        phones.append("Infinix")

        for phone in phones:
                print(phone) 

    #Break and Continue statements
    #Break Statement

for number in range(1, 10):
            if number == 5:
                    break
            print(number)

for number in range(1, 10):
            if number == 5:
                    continue
            print(number)
    
fruits=['Mangoes', 'Apples', 'Oranges', 'Bananas']
for fruit in fruits:
        if fruit=='Oranges':
                break
                print(fruit)


#Exception handling(try, exception, finally)
"""
try block: 
except:
finally:
    """

# try:
#         x=10/0

# except ZeroDivisionError:
#         print("Error: Division by Zero")

# finally:
#     print("This is always executed")


    #Example5
    #Dict is a dictionry {}

    # emotion= {
    #        'happy': "I'm glad to hear your happy.",
    #        'sad': "I'm sorry to hear your sad.",
    #        'angry': "Take a deep breath",
    #        'fearful': "Feel at home",
    #        'disgusted': "That's so unfortunate",
    # }

    #Prompt the user to enter their emotions

    # user_emotion= input("How are you feeling today?")

    #convert the user input
#     user_emotion= user_emotion.lower()

#     if user_emotion in emotion:
#            print(emotion[user_emotion])

#     else:
#            print("I'm sorry, i don't understand your emotions")

# print("Student's Mental Health Program")
# x= input("On a rate of 1-10, How are you feeling?")
# print(x)
emotion={
    1: 'Share some happiness',
    2: 'Hope all is well',
    3:'Everything is gonna be alright',
    4: 'You have a right to be sad for a cause',
    5: 'Guess now your feeling alright',
    6: 'Breath deeply to calm down',
    7: 'You are superb and just know we here for you',
    8: "Not bad, let's make it to 10",
    9:'Yah everything seems fine now',
    10: 'You look gorgeous in the 10/10 mood.'
}
emoti= input("Rate how your feeling today on a scale of 1-10?")
try:
    emoti= int(emoti)
except ValueError as error:
    print("ValueError: ", error)
    print("Please enter a number between 1-10.")
    exit()

    if emoti in emotion:
        print(emotion[emoti])





    


