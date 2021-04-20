import numpy as np

__author__ = "zabik"


class Stochastic_matrix:
    def __init__(self, n, damping_factor = False):
        self.__matrix_binary = []
        self.__matrix_stochastic = []
        self.__n = n
        self.__values = []
        self.__damping_factor = damping_factor
        self.__names = []

    def one(self):
        print("Podawaj WIERSZE, po spacjach. Np.: $1 1 0 1\n")
        for _ in range(self.__n):
            self.__matrix_binary.append(list(map(float, input().split(" "))))
        self.__matrix_binary = np.array(self.__matrix_binary)
        self.__matrix_stochastic = self.__matrix_binary.copy()
        print(f"Twoja maciez binarna:\n{self.__matrix_binary}")
        self.calc_stochastic_matrix()

    def two(self):
        print("Podawaj WIERSZE, po spacjach. Np.: $1 1 0 1\nSeparator liczb zmmiennoprzecinkowych to kropka")
        for _ in range(self.__n):
            self.__matrix_stochastic.append(list(map(float, input().split(" "))))
        self.__matrix_stochastic = np.array(self.__matrix_stochastic)
        print(f"Twoja maciez stochastyczna:\n{self.__matrix_stochastic}")
        self.show_linear_equations()
        self.calc_values()

    def three(self):
        print("Jezeli dane polaczneie istnieje, podaj 1, w przeciwym wypadku, podaj 0\n")
        for i in range(self.__n):
            arr = []
            for j in range(self.__n):
                is_here = input(f"Czy istnieje polaczenie: D{j+1} -> D{i+1}? ")
                arr.append(float(is_here))
            self.__matrix_binary.append(arr)

        self.__matrix_binary = np.array(self.__matrix_binary)
        self.__matrix_stochastic = self.__matrix_binary.copy()
        print(f"Twoja maciez binarna:\n{self.__matrix_binary}")
        self.calc_stochastic_matrix()

    def calc_stochastic_matrix(self):
        for i in range(self.__n):
            arr = self.__matrix_binary[:, i].copy()
            size = sum(arr)
            if size != 0:
                self.__matrix_stochastic[:, i] = arr / size

        print(f"Twoja maciez stoachtyczna: \n{self.__matrix_stochastic}")
        self.show_linear_equations()
        self.calc_values()

    def show_linear_equations(self):
        self.__names = ["PR(D" + str(n + 1) + ")" for n in range(self.__n)]
        names_copy = self.__names.copy()
        print("Rownania liniowe:")
        for i, name in enumerate(self.__names):
            string_matrix = list(map(str, self.__matrix_stochastic[i, :]))
            added = ' + '.join([string_matrix[i] + name for i, name in enumerate(names_copy)])
            print(f"{name} = {added}")
        print(f"{' + '.join(names_copy)} = 1")


    def calc_values(self):
        self.__values = np.full(self.__n, 1/self.__n)
        in_loop = True
        while in_loop:
            print(f"Wartosci PageRank: {dict(zip(self.__names, self.__values))}\n")
            dec = input("Czy chcesz wykonac nastpene przejscie? [Y/N] ")
            if dec.upper() == "N":
                in_loop = False

            values = self.__values.copy()
            for i in range(self.__n):
                self.__values[i] = sum(self.__matrix_stochastic[i, :].copy() * values)


if __name__ == '__main__':
    dec = input("Podaj metode, z ktorej korzytasz:\n1.\tMaciez polaczen (same 1)\n2.\tMaciez stochatyczna"
          "\n3.\tPodawanie poszczegolnych polaczen wierzcholkow\n")
    n = input("Podaj wymiar maciezy\n")
    stochastic = Stochastic_matrix(int(n))
    if dec == '1':
        stochastic.one()
    elif dec == '2':
        stochastic.two()
    elif dec == '3':
        stochastic.three()