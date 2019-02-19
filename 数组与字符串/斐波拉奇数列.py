
class Feborlaqi():
    def method(self,n):
        f0 = 1
        f1 = 1
        for i in range(n-2):
            temp = f1
            f1 = f1 + f0
            f0 = temp

        return f1



if __name__ == '__main__':
    n = 5
    solute = Feborlaqi()
    print(solute.method(n))
