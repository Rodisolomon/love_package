from love_package import *


fetcher = Fetcher()

firebase = FireBase()

# Fetch the data from the Google Form
data = fetcher.fetch_data()

# Clean the data of volunteer
clean_data = [Volunteer(datum).clean() for datum in data]

# Store clean data into the Firebase database
firebase.store_data(clean_data)