class Seminar2_hw3:
    def main(self):
        a = 90
        b = 3
        if b != 0:
            print(a/b)

        self.printSum(23, 234)
        abc = [1, 2]
        if 3 < len(abc):
            abc[3] = 9

    def printSum(self, a, b):
        print(a + b)

seminar = Seminar2_hw3()
seminar.main()