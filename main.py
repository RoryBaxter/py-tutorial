import time
class Tutorial:
    def __init__(self, user):
        self.lessons = []
        self.user = user
        
    def addLesson(self, l):
        self.lessons.append(l)

    def run(self):
        for i in self.lessons:
            print()
            print("Task: " + i.name)
            i.play(self.user)
            print("You completed the task!")
            print()
            print(self.user.name + "'s Achievements:")
            for stat in self.user.getStats():
                print(stat)

class User:
    def __init__(self, name):
        self.name = name
        self.stats = []
    
    def addStat(self, stat):
        self.stats.append(stat)

    def removeStat(self, stat):
        self.stats.remove(stat)

    def getStat(self, stat):
        self.stats[stat]

    def getStats(self):
        return self.stats
        
class Lesson:
    def __init__(self, name):
        self.name = name
        
    def play(self, u):
        raise NotImplementedError("Lesson did not implement method: play")

class LessonOne(Lesson):
    def play(self, u):
        print("Python is a programing language.")
        time.sleep(2)
        print("This means it is a way of telling the computer what to do.")
        time.sleep(1)
        input("Hit enter when you are ready")
        print("Python is used mostly for file sorting but can still be used for other tasks")
        time.sleep(2)
        print("It is what is known as a high level programing leanguage.")
        time.sleep(2)
        print("This means that it is similar to English")
        time.sleep(2)
        print("In Python, spaces matter a little, but not a lot")
        time.sleep(2)
        print("Now the introduction has finished, hit enter to start learning th basics of programming")
        input("")
        print("Achiement Unlock: Finished Introduction")
        Finished_Intro = True
        return
# This is the second lesson
class LessonTwo(Lesson):
    def play(self, u):
        Try_And_Try_Again = False
        print("To start off with you will learn about how Python can be used as a calucalator")
        time.sleep(2)
        print("Computers are just like giant calculaors")
        time.sleep(2)
        print("Pyton is a way to be able to access the computer's calulator abilities")
        time.sleep(2)
        print("Hit enter to continue")
        input("")
        print("Let's start with something simlpe. We'll do some adding with Python.")
        print("Enter the equation '2+3' ")
        First_Sum = input("")
        Done_F_S = False
# These while loops will enable the code to ceck that the user has typed the correct code
        if First_Sum.replace(" ", "") == "2+3":
            print ("5")
        else:
            while Done_F_S == False:
                if Try_And_Try_Again == False:
                    print("Achievement Unlocked: Try and Try Again")
                    u.addStat("Try and Try Again")
                    Try_And_Try_Again = True
                print("Did you type in the correct sum. Make sure that you have the correc number of spaces. Remeber that the sum you need to type in is '2+3'")
                First_Sum = input("")
                if First_Sum.replace(" ", "") == "2+3":
                    print("5")
                    Done_F_S = True
        print("Acheveiment unlocked: First Code")
        u.addStat("First Code")
        time.sleep(2)
        print("To contineue, hit enter")
        input("")
        print("Now let's try subtraction")
        time.sleep(2)
        print("Type in the sum '6-3'")
        Second_Sum = input("")
        while Second_Sum.replace(" ", "") != "6-3":
            print("Did you type in the code correctly. Remeber that the code you need is '6-3'")
            Second_Sum = input("")
        print("Well done, that works")
        print("Hit enter to continue")
        input("")
        print("Now we are going to do the same, but with multiplication")
        time.sleep(2)
        print("Try the sum which is normally written 2x4")
        Third_Sum = input("")
        if Third_Sum.replace(" ", "") == "2*4":
            print("Thats correct, how did you know what to do.")
        else:
            print("That dosen't work in Python")
        time.sleep(2)
        print("In Python, to do a multiplication sum, you have to use a astrix (*)")
        time.sleep(3)
        print("Yet's just try another.")
        print("Do the sum 5*3")
        New_Third_Sum = input("")
        while New_Third_Sum.replace(" ", "") != "5*3":
            print("Try that code again, remeber that it is '5*3'")
            New_Third_Sum = input("")
        print(15)
        print("Well done")
        time.sleep(2)
        print("Now let's do some division")
        time.sleep(2)
        print("Division is just like mulopiltlacation in Python in the sense that it does no use the tradioanal symbol.")
        time.sleep(5)
        print("In Python, the / is used for divsion")
        time.sleep(2)
        print("Try the sum 10/2")
        Fourth_Sum = input("")
        

class LessonFour(Lesson):
    def play(self, u):
        print("In this lesson we will talk about variables.")
        time.sleep(1)
        print("A variable is a special word that can be given a meaning")
        print("If you write the code 'myvar = 3', then you create a variable called myvar that actually means three")
        time.sleep(2)
        while True:
            print("Try to now create a variable called 'john' that equals 4")
            res = input()
            count = 0
            if res.replace(" ", "") == "john=4":
                if count == 2:
                    u.addStat("Third Time Lucky")
                print("Well done! john now equals 4!")
                u.addStat("Create a variable!")
                break
            else:
                print("I'm afraid that's wrong - try again")
                print("Remember not to capitalise the j in john")
                count += 1
        time.sleep(2)
        print()
        print("Of course, you don't have to call your variables john")
        print("The computer doesn't know that john is a name in real life")
        print("It just knows that 'john' is the name of the variable")
        time.sleep(2)
        print()
        print("Now let's try doing somthing with the variable.")
        print("Remember learning how to print somthing in the last lesson?")
        time.sleep(1)
        print("We can print variables too!")
        print("This is how:")
        print()
        print("var = \"Hello\"")
        print("print(var)")
        print()
        print("Can you guess what this would do?")
        input("Press enter when ready")
        print("Hello")
        print("It makes the word Hello appear!")
        time.sleep(1)
        print("Now you try! Make the variable 'spoon' be whatever you like...")
        print("...but remember to use '\"' around the text!")
        while True:
            var = input("spoon = ")
            if not var[0] == "\"" or not var[-1] == "\"":
                print("Remember to use speech marks around the text!")
            else:
                var = var.replace("\"", "")
                break
        print("Good job, " + u.name + "!")
        print("Now print out the variable!")
        while True:
            pr = input()
            if pr == "print(spoon)":
                print(var)
                print("Great Job!")
                u.addStat("Printing variables, like a pro!")
                break
            else:
                print("Not quite right!")
                print("You need to print out the variable spoon, remember not to use quotes around the word spoon")
        print("You have completed this lesson!")
        
def boot():
    print("This is the Python programmning course!")
    u = User(input("What is your name (type it and hit enter): "))
    print("OK, " + u.name + ", welcome!")
    cmd = input("To start, hit enter.")

    t = Tutorial(u)
    t.addLesson(LessonOne("Introduction"))
    t.addLesson(LessonTwo("Calculator Operations"))
    t.addLesson(LessonFour("Variables"))
    t.run()
    
boot()
