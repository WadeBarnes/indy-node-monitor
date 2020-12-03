FROM bcgovimages/von-image:next-1

RUN pip install pynacl gspread oauth2client

ADD fetch_status.py .
ADD networks.json .
ADD sovrin_network_metrics.py . 
ADD google_sheets.py .
ADD SovrinNetworkStatus.json .

ENTRYPOINT ["bash", "-c", "python fetch_status.py $@", "--"]

 