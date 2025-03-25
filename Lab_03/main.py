from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation


def read_file(file_path):
    with open(file_path, "r") as f:
        for line in f:
            tmp = line.strip().split()
            if len(tmp) == 2:
                eq = Equation(int(tmp[0]), int(tmp[1]))
            elif len(tmp) == 3:
                eq = QuadraticEquation(int(tmp[0]), int(tmp[1]), int(tmp[2]))
            elif len(tmp) == 5:
                eq = BiQuadraticEquation(int(tmp[0]), int(tmp[2]), int(tmp[4]))

            print(eq.solve(), "--solutions:", eq.solutions_number())


if __name__ == '__main__':
    read_file('input01.txt')