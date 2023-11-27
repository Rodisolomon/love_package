# if some libraries need being installed, input their names in the `requirements.txt`, each (only the name of the package) in a new line as example in the file.
# import libraries here
from typing import Optional
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import pandas as pd

class Fetcher:
    '''
    This is the representation of the object fetching data from Google Form using the API.
    reference: https://github.com/juampynr/google-spreadsheet-reader
    '''
    def __init__(self):
        '''
        Initialize the Fetcher object.

        Input:

        Ouput: nothing.
        '''
        self.SERVICE_ACCOUNT_FILE = "love-package-60637-ae5a77289b25.json"
        self.SPREADSHEET_ID = '11Gft4o2fr-IbD8PrOJ81TGjEERNXKE4YUogBHVONa6E'
        self.RANGE_NAME = 'Form Responses 1'
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']



    def fetch_data(self):
        '''
        This function returns the fetched data.

        Input:

        Output: fetched data (type list): containing all the fetched data.

        Modify:
        '''
        # Authenticate and create the service
        creds = Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        service = build('sheets', 'v4', credentials=creds)

        # Request data from the Sheet
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID, range=self.RANGE_NAME).execute()
        values = result.get('values', [])

        # Convert the data to a pandas DataFrame (optional)
        df = pd.DataFrame(values)
        print(df)


class Volunteer:
    '''
    This is the representation of the volunteer. Each person has their own information and some method to clean their own data.
    '''

    def __init__(self, 
            name: str, 
            group: Optional[str], 
            assembly: bool, 
            driving: bool, 
            email: str, 
            phone: str, 
            location: str, 
            availability: str,  
            experience: bool):
        '''
        Initialize the Volunteer object.

        Input: information (type list/set/tuple): the information of each volunteer (suppose for now: each volunteer only submits the form once).

        Output: nothing.
        '''
        self.name = name
        if group == "Individual":
            self.group = 0
        else:
            self.group = group
        # not sure how to parse assembly/driving, keep it a string for now
        self.assembly = assembly
        self.driving = driving
        self.email = email
        self.phone = phone
        self.location = location
        self.availability = availability
        if experience == "Yes":
            self.experience = 1
        else:
            self.experience = 0

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