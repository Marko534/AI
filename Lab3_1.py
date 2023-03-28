from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    # Марија слободни термини: 14:00-16:00, 18:00-19:00
    # Симона слободни термини: 13:00-15:00, 16:00-17:00, 19:00-20:00
    # Петар слободни термини: 12:00-14:00, 16:00-20:00
    problem.addVariable("Marija_prisustvo", (0, 1))
    problem.addVariable("Simona_prisustvo", (0, 1))
    problem.addVariable("Petar_prisustvo", (0, 1))
    problem.addVariable("vreme_sostanok", tuple(range(12, 20)))
    # ----------------------------------------------------
    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(lambda per, time: per == 1 and time in [14, 15, 18] or per == 0 and time not in [14, 15, 18],
                          ("Marija_prisustvo", "vreme_sostanok"))
    problem.addConstraint(
        lambda per, time: per == 1 and time in [13, 14, 16, 19],
        ("Simona_prisustvo", "vreme_sostanok"))
    problem.addConstraint(
        lambda per, time: per == 1 and time in [12, 13, 16, 17, 18, 19] or per == 0 and time not in [12, 13, 16, 17, 18,
                                                                                                     19],
        ("Petar_prisustvo", "vreme_sostanok"))
    # ----------------------------------------------------
    # print(problem.getSolutions())
    [print(solution) for solution in problem.getSolutions()]
