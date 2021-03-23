import csv
import socket
from datetime import datetime

# Checks whether connection to an given address is available
# address: Specifies address to establish connection to (default Google DNS-Server)
# port: Specifies the port of connection
# timeout: Sets timeout for trying to connect in seconds
def connection_available(address="8.8.8.8",port=53,timeout=3):

    try:
        sock = socket.create_connection((address,port),timeout=timeout)
        return True
    except:
        return False

# Runs endlessly checking connection. On lost_connection writes start and end of
# outages to file.
def log_downtime(treshold=60):

    while True:
        connection_lost=False
        start_time = datetime.now()
        while not connection_available():
            end_time = datetime.now()
            connection_lost=True
            duration=(end_time-start_time).total_seconds()

        if connection_lost and duration>treshold:
            with open('outages.txt','w+') as file:
                writer = csv.writer(file)
                writer.writerow([start_time,end_time,duration])

log_downtime()
