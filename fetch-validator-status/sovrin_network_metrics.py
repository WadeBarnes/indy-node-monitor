from google_sheets import appendSheet
import datetime

def metrics(result, network_name):

    sheet_name = "Test Log"

    message = ""
    num_of_nodes = 0
    nodes_offline = 0
    time = datetime.datetime.now().strftime("%x %X") # formated to 12/03/20 21:27:49

    for node in result:
        num_of_nodes += 1
        print(node)
        if node["status"]["ok"] == False:
            nodes_offline += 1

    networkResilience = round((num_of_nodes)/3 + 1)

    # Could have a stepped warning system
    if nodes_offline >= networkResilience:
        message = "Network Resilience Danger!"

    row = [time, network_name, num_of_nodes, nodes_offline, networkResilience, message]

    print(row)
    appendSheet(sheet_name, row)
    print("Done!")