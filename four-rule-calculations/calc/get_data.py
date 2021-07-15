import random
import numpy as np

class GetData:
    def __init__(self, sign):
        random.seed(1015)
        
        self.sign = sign
        self.res = list()
        self.label = list()


    def get_data(self):
        if self.sign == "+":
            for i in range(100):
                n1 = random.randrange(1, 100)
                n2 = random.randrange(1, 100)
                self.res.append([n1, n2])
                self.label.append(n1+n2)
            x, y = np.array(self.res), np.array(self.label)
            self.x = x.astype('float') / float(100*2)
            self.y = y.astype('float') / float(100*2)
            
            self.invert = lambda x : round(x*float(100*2))

            return self.x, self.y
        elif self.sign == "-":
            for i in range(100):
                n1 = random.randrange(1, 100)
                n2 = random.randrange(1, 100)
                self.res.append([n1, n2])
                self.label.append(n1-n2)
            x, y = np.array(self.res), np.array(self.label)
            self.x = (x.astype('float')+float(100)) / float(100*2)
            self.y = (y.astype('float')+float(100)) / float(100*2)
            
            self.invert = lambda x : round(x*float(100*2)-float(100))

            return self.x, self.y
        elif self.sign == "/":
            for i in range(100):
                n1 = random.randrange(1, 100)
                n2 = random.randrange(1, 100)
                self.res.append([n1, n2])
                self.label.append(n1/n2)
            x, y = np.array(self.res), np.array(self.label)
            self.x = (x.astype('float')*float(100)) / float(100*2)
            self.y = (y.astype('float')*float(100)) / float(100*2)

            self.invert = lambda x : (x*float(100*2) / float(100)) # round x

            return self.x, self.y
        elif self.sign == "*":
            for i in range(100):
                n1 = random.randrange(1, 100)
                n2 = random.randrange(1, 100)
                self.res.append([n1, n2])
                self.label.append(n1*n2)
            x, y = np.array(self.res), np.array(self.label)
            self.x = (x.astype('float')/float(100)) / float(100*2)
            self.y = (y.astype('float')/float(100)) / float(100*2)

            self.invert = lambda x : round(x*float(100*2) * float(100))

            return self.x, self.y
        else:
            import sys
            sys.exit(0)
