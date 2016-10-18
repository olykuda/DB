from model import Model
class View:
    def __init__(self,model):
        self.model = model

    def view_main_menu(self):
        print """Select table:
    [1] View of performerers
	[2] View of compositions
	[3] Quit"""

    def view_performer_menu(self):
            print """Select a desired action:
    	[1] Add a performerer
    	[2] Remove a performerer
    	[3] Update a performerer
    	[4] Search performers (average time of compositions > 4 min)
    	[5] View the table
    	[6] Back to main menu
    	"""

    def view_composition_menu(self):
        print """Select a desired action:
    	[1] Add a composition
    	[2] Remove a composition
    	[3] Update a composition
    	[4] View the table
    	[5] Back to main menu"""

    def view_update_performer_menu(self):
        print """Select what do you want to change:
	[1] Id of performer
	[2] Name
	[3] Country
	[4] Back to performer menu"""

    def view_update_composition_menu(self):
        print """Select what do you want to change:
	[1] Id of composition
	[2] Name
	[3] Time
	[4] Back to composition menu"""

    def table_performer(self):
        print '{:->40}'.format('-')
        print '{:^40}'.format('P E R F O R M E R S')
        print '{:->40}'.format('-')
        print '{:>4} {:>20} {:>15}'.format('ID', 'NAME', 'COUNTRY')
        for per in self.model.get_performer_lst():
            print '{:4d} {:>20} {:>15}'.format(per['id'], per['name'], per['country'])

    def table_composition(self):
        print '{:->40}'.format('-')
        print 'C O M P O S I T I O N S'
        print '{:->40}'.format('-')
        print '{:>4} {:>20} {:>15} {:>15}'.format('ID', 'NAME', 'TIME', 'ID_OF_PERFORMER')
        for comp in self.model.get_composition_lst():
           print '{:>4} {:>20} {:>15} {:15d}'.format(comp['id'], comp['name'], comp['time'], comp['id_performer'])

    def table_result_search(self):
        print '{:->40}'.format('-')
        print 'LIST OF PERFORMERS (AVERAGE TIME OF COMPOSITIONS > 4 MINUTES)'
        print '{:->40}'.format('-')
        print '{:>4} {:>20} {:>15}'.format('ID', 'NAME', 'AVERAGE_TIME')
        for comp in self.model.search_performers():
            print '{:>4} {:>20} {:>15}'.format(comp['id'], comp['name'], comp['average_time'])

    def error_message(self,mess):
         print 'ERROR !!! ' + mess