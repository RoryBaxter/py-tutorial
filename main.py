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
        input("Hit enter when you are ready")
        print("Computers")
        return

class LessonTwo(Lesson):
    def play(self, u):
        pass
        
def boot():
    print("This is the Python programmning course!")
    u = User(input("What is your name (type it and hit enter): "))
    print("OK, " + u.name + ", welcome!")
    input("To start, hit enter")
    t = Tutorial(u)
    t.addLesson(LessonOne("Introduction"))
    t.run()

boot()
