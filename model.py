import pickle
from datetime import time
class Model:
    def __init__(self, perf_file, comp_file):#performer_lst=[], composition_lst=[]
        self.__performer_lst = list()
        self.__composition_lst = list()
        self.load_lst(perf_file, comp_file)
        #self.__performer_lst = performer_lst
        #self.__composition_lst = composition_lst

    # write to dump
    def load_lst(self,perf_file, comp_file):
        try:
            with open(perf_file, 'rb') as f1:
                self.__performer_lst = pickle.load(f1)
            f1.close()

            with open(comp_file, 'rb') as f2:
                self.__composition_lst = pickle.load(f2)
            f2.close()
        except:
            self.__performer_lst = list()
            self.__composition_lst = list()

    def save_lst(self,perf_file, comp_file):
        with open(perf_file, 'wb') as f1:
            pickle.dump(self.__performer_lst, f1)
        f1.close()

        with open(comp_file, 'wb') as f2:
            pickle.dump(self.__composition_lst, f2)
        f2.close()

    def get_composition_lst(self):
        return self.__composition_lst

    def get_performer_lst(self):
        return self.__performer_lst

    def __find(self, id, lst):
        for dict in lst:
            if dict['id'] == id:
                return dict
        return None

    def __is_exist(self, id, lst):
        if self.__find(id, lst) is not None:
            return True
        return False

    def add_performer(self, id, name, country):
        if not self.is_perf_exist(id):
            performer = {'id': id, 'name': name, 'country': country}
            self.__performer_lst.append(performer)
        else:
            raise Exception('Performer with such id is already exists')

    def del_performer(self, id):
        if self.is_perf_exist(id):
            tmp_per_lst = self.__performer_lst
            self.__performer_lst = []
            for dict in tmp_per_lst:
                if dict['id'] != id:
                    self.__performer_lst.append(dict)
                else:
                    tmp_comp_lst = self.__composition_lst
                    self.__composition_lst = []
                    for comp in tmp_comp_lst:
                        if comp['id_performer'] != id:
                            self.__composition_lst.append(comp)
        else:
            raise Exception('No such performer for removing')

    def add_composition(self, id, name, time, performer):
        tmp_dict = {}
        id_performer = -1
        for tmp_dict in self.__performer_lst:
            if tmp_dict['name'] == performer:
                id_performer = tmp_dict['id']
        if id_performer == -1:
            raise Exception('No such performer for adding composition')

        if not self.is_comp_exist(id):
            composition = {'id': id, 'name': name, 'time': time, 'id_performer': id_performer}
            self.__composition_lst.append(composition)
        else:
            raise Exception('Composition with such id is already exists')

    def del_composition(self, id):
        if self.is_comp_exist(id):
            tmp_comp_lst = self.__composition_lst
            self.__composition_lst = []
            for comp in tmp_comp_lst:
                if comp['id'] == id:
                    self.__composition_lst.append(comp)
        else: raise Exception('No such composition for removing')

    def update_performer(self, id, new_dict):
        tmp_dict = self.__find(id, self.__performer_lst)
        if tmp_dict is not None:
            tmp_dict.update(new_dict)
        else:
            raise Exception('No such performer to update')

    def update_composition(self, id, new_dict):
        tmp_dict = self.__find(id, self.__composition_lst)
        if tmp_dict is not None:
            tmp_dict.update(new_dict)
        raise Exception('No such composition to update')

    def __time_lst(self):
        tmp_per_lst = self.__performer_lst
        tmp_comp_lst = self.__composition_lst
        time = 0
        count = 0
        result_lst = []
        result_d = {}
        for per in tmp_per_lst:
            for comp in tmp_comp_lst:
                if comp['id_performer'] == per['id']:
                    result_d = {}
                    time += self.__time_in_seconds(comp['time'])
                    count += 1
            if count==0 :
                result_d['id'] = per['id']
                result_d['average_time'] = time/count
                result_d['name'] = per['name']
                result_lst.append(result_d)
            time = 0
            count = 0
        return result_lst

    def search_performers(self):
        result_per_lst = []
        for per in self.__time_lst():
            if per['average_time']>240:
                result_per_lst.append(per)
        return result_per_lst

    def is_time_correct(self,time):
        if ':' not in time:
            raise Exception('Incorrect time value')
        try:
            minutes = int(time.split(':')[0])
            seconds = int(time.split(':')[1])
        except ValueError:
            raise Exception('Incorrect time value')
        if minutes<0 or minutes>=60 or seconds<0 or minutes>=60:
            return False
        return True

    def __time_in_seconds(self,time):
        minutes = int(time.split(':')[0])
        seconds = int(time.split(':')[1])
        return minutes*60+seconds

    def is_comp_exist(self,id):
        return self.__is_exist(id,self.__composition_lst)
    def is_perf_exist(self,id):
        return self.__is_exist(id, self.__performer_lst)