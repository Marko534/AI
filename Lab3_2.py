from constraint import *


def constraint_size(*list):
    count = {"T1": 0, "T2": 0, "T3": 0, "T4": 0}
    for term in list:
        count[term] += 1
    ret = True
    for value in count.values():
        ret = ret and value <= 4
    return ret

# def check_

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
    variables = dict()
    i = 1
    for key in papers.keys():
        variables[i] = papers[key]
        i += 1

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(constraint_size, variables)

    results = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    print(results);
    [print(f"Paper{key} ({variables[key]}): {results[key]}") for key in results.keys()]
