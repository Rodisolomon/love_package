# if some libraries need being installed, input their names in the `requirements.txt`, each (only the name of the package) in a new line as example in the file.
# import libraries here
from typing import Optional
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import pandas as pd
import re

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

        Output: fetched data (panda dataframe): containing all the fetched data.

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
        return df


class Volunteer:
    '''
    This is the representation of the volunteer. Each person has their own information and some method to clean their own data.
    '''

    def __init__(self, dict):
        '''
        Initialize the Volunteer object with a DataFrame row.

        Input: row (pandas Series): A row from the DataFrame representing a volunteer's data.

        Output: nothing.
        '''
        self.name = dict['Name ']
        self.group = 0 if dict['Are you volunteering as an individual or with a group?'] == "Individual" else int(dict['If you are volunteering as a group, how many people are in your group?'])
        self.assembly = dict['Are you interested in driving for deliveries, assembling packages or both? '].lower().find('assembling') != -1
        self.driving = dict['Are you interested in driving for deliveries, assembling packages or both? '].lower().find('driving') != -1
        self.email = dict['Email Address ']
        self.phone = dict['Phone Number ']
        self.location = dict['Street Address/Neighborhood ']
        self.availability = dict['Specific Availability ']
        self.experience = dict['Have you volunteered with the Love Package Project before?'].lower() == 'yes'

    @classmethod
    def match_idx(cls, df, i):
        #doing text match return a list of idx in the order of init function
        first_row = df.iloc[0]
        second_row = df.iloc[i+1]

        # Creating key-value pairs and converting to a dictionary
        merged_dict = dict(zip(first_row, second_row))
        return merged_dict

            

    def clean(self):
        '''
        This method is to clean each form data.

        Input:

        Output: clean information (type list/set/tuple): the information that is clean.

        Modify: itself (or if we want to store both raw and clean data separately for later reference, this method can create new class attributes).
        '''
        # Remove non-numeric characters
        cleaned_number = re.sub(r'\D', '', self.phone)

        # Check if the number has 10 digits, then format
        if len(cleaned_number) == 10:
            return f"{cleaned_number[:3]}-{cleaned_number[3:6]}-{cleaned_number[6:]}"
        else:
            # Handle the case where the number is not 10 digits
            # You might want to return an error message or the original number
            return self.phone


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