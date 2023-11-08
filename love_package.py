# if some libraries need being installed, input their names in the `requirements.txt`, each (only the name of the package) in a new line as example in the file.
# import libraries here

class Fetcher:
    '''
    This is the representation of the object fetching data from Google Form using the API.
    '''
    def __init__(self):
        '''
        Initialize the Fetcher object.

        Input:

        Ouput: nothing.
        '''
        pass

    def fetch_data(self):
        '''
        This function returns the fetched data.

        Input:

        Output: fetched data (type list): containing all the fetched data.

        Modify:
        '''
        pass


class Volunteer:
    '''
    This is the representation of the volunteer. Each person has their own information and some method to clean their own data.
    '''
    def __init__(self, information):
        '''
        Initialize the Volunteer object.

        Input: information (type list/set/tuple): the information of each volunteer (suppose for now: each volunteer only submits the form once).

        Output: nothing.
        '''
        pass

    def clean(self):
        '''
        This method is to clean each form data.

        Input:

        Output: clean information (type list/set/tuple): the information that is clean.

        Modify: itself (or if we want to store both raw and clean data separately for later reference, this method can create new class attributes).
        '''
        pass


class FireBase:
    '''
    This is the representation of something to interact with Firebase database. This is neither a database nor storing any data.

    Some basic methods of the class may include create table, drop table, delete table, insert into, select, etc.
    '''
    def __init__(self):
        '''
        Initialize the object.

        Input:

        Output: nothing.

        Modify: create class attributes to interact with Firebase (typically if interacting with other kind of database, we will need self.connect, self.cursor).
        '''
        pass

    def store_data(self, data):
        '''
        This function executes the `insert` statement to stote the data.

        Input: data (type list): this is a list of list/set/tuple (or maybe a Pandas dataframe). The input is received from Volunteer().clean().

        Output: some message notifying that the data is successfully stored into the database or some error happens.

        Modify:
        '''
        pass