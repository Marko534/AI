from constraint import *

# def check_count(list):
# for i in list:


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    # Poradi nekoja pricina raboti so strings samo do 9
    # variables = tuple(["1","2", "3","4","5","6","7","8","9","10","11","12","13"])

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    # problem.addConstraint()

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    print(result)
