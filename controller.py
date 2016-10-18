from model import Model
from view import View
import sys

class Controller:
    def __init__(self, model,view):
        self.model = model
        self.view = view

    def main_menu(self):
        choice = 0
        self.view.view_main_menu()
        while choice != 3:
            try:
                choice = int(raw_input("Your choice: "))
            except ValueError:
                self.view.error_message('Incorrect value')
            if choice == 1:
                self.view.table_performer()
                self.performer_menu()
            elif choice == 2:
                self.view.table_composition()
                self.composition_menu()
        if choice == 3:
            self.model.save_lst('perf.txt', 'comp.txt')
            sys.exit()

    def performer_menu(self):
        choice = 0
        while choice != 7:
            self.view.view_performer_menu()
            try:
                choice = int(raw_input("Your choice: "))
            except ValueError:
                self.view.error_message('Incorrect value')
            if choice == 1:
                try:
                    id = int(raw_input("id to add: "))
                    name = raw_input("name to add: ")
                    country = raw_input("country to add: ")
                    self.model.add_performer(id,name,country)
                except ValueError:
                    self.view.error_message('Incorrect value')
            elif choice == 2:
                try:
                    id = int(raw_input("id to remove: "))
                    self.model.del_performer(id)
                except ValueError:
                    self.view.error_message('Incorrect value')
            elif choice == 3:
                try:
                    id = int(raw_input("id to update: "))
                    self.update_performer_menu(id)
                except ValueError:
                    self.view.error_message('Incorrect value')
            elif choice == 4:
                self.model.search_performers()
                self.view.table_result_search()
            elif choice == 5:
                self.view.table_performer()
            elif choice == 6:
                self.main_menu()

    def composition_menu(self):
        choice = 0
        while choice != 6:
            self.view.view_composition_menu()
            try:
                choice = int(raw_input("Your choice: "))
            except ValueError:
                self.view.error_message('Incorrect value')
            if choice == 1:
                try:
                    id = int(input("id to add: "))
                    name = raw_input("name to add: ")
                    time = raw_input("time to add: ")
                    while not self.model.is_time_correct(time):
                        time = raw_input("time to add: ")
                    performer = raw_input("name of performer: ")
                    self.model.add_composition(id,name,time, performer)
                except ValueError:
                    self.view.error_message('Incorrect value')
            elif choice == 2:
                try:
                    id = int(input("id to remove: "))
                    self.model.del_composition(id)
                except ValueError:
                    self.view.error_message('Incorrect value')
            elif choice == 3:
                try:
                    id = int(raw_input("id to update: "))
                    self.update_composition_menu(id)
                except ValueError:
                    self.view.error_message('Incorrect value')
            elif choice == 4:
                self.view.table_composition()
            elif choice == 5:
                self.main_menu()

    def update_composition_menu(self, id):
        choice = 0
        if not self.model.is_comp_exist(id):
            return
        new_dict = {}

        while choice != 5:
            self.view.view_update_composition_menu()
            try:
                choice = int(raw_input('Your choice:'))
            except ValueError:
                self.view.error_message('Incorrect value')
            if choice == 1:
                new_dict['id'] = int(input('new id: '))
            elif choice == 2:
                new_dict['name'] = raw_input('new name: ')
            elif choice == 3:
                new_time = raw_input('new time: ')
                while not self.model.is_time_correct(new_time):
                    new_time = raw_input('new time: ')
            elif choice == 4:
                self.composition_menu()
            self.model.update_composition(id, new_dict)

    def update_performer_menu(self,id):
        choice = 0
        if not self.model.is_perf_exist(id):
            return
        new_dict = {}
        while choice != 5:
            self.view.view_update_performer_menu()
            try:
                choice = int(raw_input('Your choice:'))
            except ValueError:
                self.view.error_message('Incorrect value')
            if choice == 1:
                new_dict['id'] = int(input('new id: '))
            elif choice == 2:
                new_dict['name'] = raw_input('new name: ')
            elif choice == 3:
                new_dict['country'] = raw_input('new country: ')
            elif choice == 4:
                self.performer_menu()
            self.model.update_performer(id, new_dict)