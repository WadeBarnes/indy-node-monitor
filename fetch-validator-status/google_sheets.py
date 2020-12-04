import gspread
from oauth2client.service_account import ServiceAccountCredentials

def gspread_authZ(gauth_json):
    # Google drive and Google sheets API setup
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(gauth_json + ".json", scope) # Set credentials using json file
        authD_client = gspread.authorize(creds) # Authorize json file
        return(authD_client)
    except:
        print("\033[1;31;40mUnable to athorize json! Make sure the Google API Credentials json file is in the root folder and name is correct.")
        print("Json name entered: " + gauth_json + ".\033[m")
        exit()


# Insert data in sheet
def gspread_append_sheet(authD_client, file_name, worksheet_name, row):
    try:
        sheet = authD_client.open(file_name).worksheet(worksheet_name) # Open sheet
        sheet.append_row(row, ) # Append sheet
    except:
        print("\033[1;31;40mUnable to upload data to sheet! Please check file and worksheet name and try again.")
        print("File name entered: " + file_name + ". Worksheet name entered: " + worksheet_name + ".\033[m")
        exit()