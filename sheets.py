import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_form_response(pnumber):
    #authentication part
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    # sheet = client.open("Copy of Unimart Franchisee Application Form (Responses)").sheet1  # Open the spreadhseet
    # Or, if you feel really lazy to extract that key, paste the entire spreadsheet’s url
    sheet_url='https://docs.google.com/spreadsheets/d/1H3sL9rt42Nznj_voUrNZFgM6BASmQp52qJZW6dcCeMA/edit#gid=1296598501'
    sheet = client.open_by_url(sheet_url).sheet1
    # data = sheet.get_all_values()
    phone_number_column= sheet.col_values(5)[1:]
    header = sheet.row_values(1)
    response_dict={}
    for i,number in enumerate(phone_number_column):
        if str(pnumber) == str(number):
            row = sheet.row_values(i+2)
            for head,body in zip(header,row):
                response_dict[head]=body
            return response_dict


if __name__=="__main__":
    print(get_form_response("9769966153"))