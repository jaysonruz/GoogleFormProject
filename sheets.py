# 
# "Copy of Unimart Franchisee Application Form (Responses)"

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pandas as pd

#authentication part
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# sheet = client.open("Copy of Unimart Franchisee Application Form (Responses)").sheet1  # Open the spreadhseet
# Or, if you feel really lazy to extract that key, paste the entire spreadsheet’s url
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1H3sL9rt42Nznj_voUrNZFgM6BASmQp52qJZW6dcCeMA/edit#gid=1296598501').sheet1
# data = pd.DataFrame(sheet.get_all_records())
data = sheet.get_all_values()

col = sheet.col_values(5)

print(col,type(col))
# pprint(data)
print("name: ",data[-1][1])
print("phone: ",data[-1][4])
