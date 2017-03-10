import sys


class Skill:

    def __init__(self, name):
        self.name = name
        self.studied = False

    def study(self):
        self.studied = True


skills = []
ans = True
while ans:
    print ("""
    1.Add a Skill
    2.Show skills studied
    3.Show skills not studied
    4.View my learning progress
    5.Enter skill you have studied
    6.Exit
    """)
    ans = input("What would you like to do? ")
    ans = int(ans)
    if ans == 1:
        print("Add a skill")
        skill = input("Enter a skill: ")
        if skill:
            skills.append(Skill(skill))
    elif ans == 2:
        print("Show skills studied")
        studied_skills = [i for i in skills if i.studied]
        for n, skill in enumerate(studied_skills):
            print('{0} {1}'.format(n, skill.name))
    elif ans == 3:
        print("Show skills not studied")
        unstudied_skills = [i for i in skills if not i.studied]
        for n, skill in enumerate(unstudied_skills):
            print('{0} {1}'.format(n, skill.name))
    elif ans == 4:
        print("View My learning progress")
        studied = [i for i in skills if i.studied]
        for s in studied:
            print('You have studied {0}'.format(s.name))
        not_studied = [i for i in skills if not i.studied]
        for s in not_studied:
            print('You have not studied {0}'.format(s.name))
    elif ans == 5:
        name = input("Enter the name of a skill you have studied: ")
        if skill:
            input_skill = Skill(name)
            print(skills)
            print(input_skill)
            toupdate = [i for i in skills if i.name is input_skill.name]
            if len(toupdate):
                skills.remove(toupdate.pop())
                input_skill.study()
                skills.append(input_skill)
    elif ans == 6:
        print("Goodbye")
        sys.exit(0)
    else:
        print("Not Valid Choice Try again")