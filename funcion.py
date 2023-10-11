import mcstatus
import requests
import config


def initialization():
    global api
    global server_status
    global server_id
    # Initialize server id counter
    server_id = 0
    # Initialize HTTP API URL of go-cqhttp
    api = "http://" + config.api_ip + "/send_group_msg?group_id=" + config.group_id + "&message="
    server_status = list()
    # Test if go-cqhttp online
    try:
        requests.get("http://" + config.api_ip + "/get_login_info")
    except requests.exceptions.ConnectionError:
        print("Unable connect to go-cqhttp")
        exit()
    
    # Use a 2-D array to storage server information
    for i in config.server_list:
        server_status.append([i, "offline", "offline"])

def check_server(server_address):
    global api
    global server_status
    global server_id
    try:
        # Use config.timeout * 0.001 to turn measure unit into milliseconds
        mcstatus.JavaServer.lookup(server_address, config.timeout * 0.001).status()


    # Server offline
    except TimeoutError:
        server_status[server_id][1] = "offline"
        # Check if server status changed
        if server_status[server_id][1] != server_status[server_id][2]:
            send_message(server_address, "offline")

        server_status[server_id][2] = server_status[server_id][1]
        server_id = server_id + 1

        # Reset server id counter
        if server_id == len(config.server_list):
            server_id = 0


    # Server online
    else:
        print(server_status[server_id])
        # Check if server status changed
        if server_status[server_id][1] != server_status[server_id][2]:
            send_message(server_address, "online")

        server_status[server_id][2] = server_status[server_id][1]
        server_id = server_id + 1

        # Reset server id counter
        if server_id == len(config.server_list):
            server_id = 0


def send_message(server_address, message_type):
    global api
    if message_type == "online":
        try:
            print(config.online_massage.replace("~server~", server_address))
            requests.get(api + config.online_massage.replace("~server~", server_address))
        except requests.exceptions.ConnectionError:
            print("Unable send message")
    
    else:
        try:
            print(config.offline_massage.replace("~server~", server_address))
            requests.get(api + config.offline_massage.replace("~server~", server_address))
        except requests.exceptions.ConnectionError:
            print("Unable send message")
        
