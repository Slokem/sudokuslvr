import numpy as np

class Grid :

    def __init__(self):
        self.list =[]

    def add_blob(self, list):
        '''
        take as an input a list of 81 numbers corresponding to a full grid and
        return a blob string object than can be printed
        '''
        self.list = list
        blob = ""
        for i in range(9):
            blob+="||\n"
            if i%3 == 0:
                blob+="="*29+"\n"
            for j in range(9):
                if j%3 == 0:
                    blob+="|| "
                blob+= str(self.list[i*9+j])+" "
        blob+="||"+"\n"+"="*29
        self.blob = blob
        return self

    def print_blob(self):
        print(self.blob)
        return self
