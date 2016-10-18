from model import Model
from controller import Controller
from view import View

test_model = Model('perf.txt','comp.txt')
test_view = View(test_model)
test_cont = Controller(test_model,test_view)

test_cont.main_menu()