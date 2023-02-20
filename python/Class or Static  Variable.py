class Player:
    team_run = 0

    def __init__(self, run: object) -> object:
        self.run = run

    def hit_four(self):
        self.run += 4
        Player.team_run += 4

    def hit_six(self):
        self.run += 6
        Player.team_run += 6


sakib = Player(0)
tamim = Player(0)

sakib.hit_four()
tamim.hit_four()
sakib.hit_six()
tamim.hit_four()

print('Sakib',sakib.run)
print('Tamim',tamim.run)
print('Team Run',sakib.team_run)


print('-----------Example 2----------------')


class Student:
    count = 0

    def __init__(self,name,id):
        self.name = name
        self.id = id
        Student.count += 1

    def view(self):
        print('Name:',self.name,', ID:',self.id,',Student number:',Student.count)
    

s1 = Student('Bob', 1)
s2 = Student('Alic', 2)
s3 = Student('Mina', 3)

s1.view()

