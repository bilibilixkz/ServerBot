import mcstatus
import requests
import config


def initialization():
    global api
    global server_status
    global server_id
    server_id = 0
    api = "http://" + config.api_ip + "/send_group_msg?group_id=" + config.group_id + "&message="
    server_status = list()
    try:
        requests.get("http://127.0.0.1:5700/get_login_info")
    except requests.exceptions.ConnectionError:
        print("Unable connect to go-cqhttp")
        exit()
    
    for i in config.server_list:
        server_status.append([i, "offline", "offline"])

def check_server(server_address):
    global api
    global server_status
    global server_id
    try:
        mcstatus.JavaServer.lookup(server_address, config.timeout * 0.001).status()

    except TimeoutError:
        server_status[server_id][1] = "offline"
        if server_status[server_id][1] != server_status[server_id][2]:
            send_message(server_address, "offline")

        server_status[server_id][2] = server_status[server_id][1]
        server_id = server_id + 1

        if server_id == len(config.server_list):
            server_id = 0

    else:
        print(server_status[server_id])
        if server_status[server_id][1] != server_status[server_id][2]:
            send_message(server_address, "online")

        server_status[server_id][2] = server_status[server_id][1]
        server_id = server_id + 1
        if server_id == len(config.server_list):
            server_id = 0


def send_message(server_address, message_type):
    global api
    if message_type == "online":
        try:
            print(config.online_massage.replace("~server~", server_address))
            requests.get(api + config.online_massage.replace("~server~", server_address))
        except requests.exceptions.ConnectionError:
            print("Unable send message, do you shut down go-cqhttp accidentally?")
    
    else:
        try:
            print(config.offline_massage.replace("~server~", server_address))
            requests.get(api + config.offline_massage.replace("~server~", server_address))
        except requests.exceptions.ConnectionError:
            print("Unable send message, do you shut down go-cqhttp accidentally?")
        
