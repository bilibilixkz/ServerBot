import funcion
import config
import time


funcion.initialization()

while True:
    for i in config.server_list:
        funcion.check_server(i)
    time.sleep(config.dalay)