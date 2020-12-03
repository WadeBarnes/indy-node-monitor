import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google drive and Google sheets API setup
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
try:
    SovrinNetworkStatus = ServiceAccountCredentials.from_json_keyfile_name("SovrinNetworkStatus.json", scope) # Set credentials using json file
    client = gspread.authorize(SovrinNetworkStatus) # Authorize json file
except:
    print("\033[1;31;40m Unable to athorize json! Json file is either missing or broken! Exiting... \033[m")
    raise


# Insert data in sheet
def appendSheet(sheet_name, row):
    sheet = client.open(sheet_name).sheet1 # Open sheet
    sheet.append_row(row, ) # Append sheet