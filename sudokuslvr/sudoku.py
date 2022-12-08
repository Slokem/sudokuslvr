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
        blob+="="*13+"\n"
        self.blob = blob
        return self

    def print_blob(self):
        print(self.blob)
        return self
