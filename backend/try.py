from love_package import *

fetcher = Fetcher()
df = fetcher.fetch_data()
dic = Volunteer.match_idx(df, 0)
print(dic)
print(Volunteer(dic))