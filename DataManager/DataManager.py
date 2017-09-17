# coding : utf-8

class DataManager(object):

    def __init__(self):
        self.datas=[]

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_data(self):
        for i in self.datas:
            print(i)

    def get_data(self):
        return self.datas
