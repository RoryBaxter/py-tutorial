import time
Try_And_Try_Again = False
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
        print("It is what is klnown as a high level programing leanguage.")
        time.sleep(1)
        print("This means that it is similar to English")
        time.sleep(1)
        print("Now the introduction has finished, hit enter to start learning th basics of programming")
        input("")
        return
# This is the second lesson
class LessonTwo(Lesson):
    def play(self, u):
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
# These while loops will enable the code to ceck that the user has typed the correct code
        while First_Sum != "2+3":
            if Try_And_Try_Again == False:
                print("Achievement Unlocked: Try and Try Again")
                Try_And_Try_Again = True
            print("Did you type in the correct sum. Make sure that you have the correc number of spaces. Remeber that the sum you need to type in is '2+3'")
            First_Sum = input("")
        print("5")
        print("Acheveiment unlocked: First Code")
        First_Code = True
        time.sleep(2)
        print("To contineue, hit enter")
        input("")
        print("Now let's try subtraction")
        time.sleep(2)
        print("Type in the sum '6-3'")
        Second_Sum = input("")
        while Second_Sum != "6-3":
            print("Did you type in the code correctly. Remeber that the code you need is '6-3'
            Second_Sum = input("")
        print("Hit enter to continue")
        input("")
        print("Now we are")
        
def boot():
    print("This is the Python programmning course!")
    u = User(input("What is your name (type it and hit enter): "))
    print("OK, " + u.name + ", welcome!")
    input("To start, hit enter.")
    t = Tutorial(u)
    t.addLesson(LessonOne("Introduction"))
    t.run()

boot()
