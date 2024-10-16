import time
import psutil
import json
from datetime import datetime
import os


def do():
    process_name = "mstsc.exe"
    interval = 60

    while True:
        try:
            file_name = datetime.now().strftime('%d-%m-%Y') + '.json'

            if os.path.isfile(file_name):
                with open(file_name) as json_file:
                    data = json.load(json_file)

            else:
                data = {process_name: {"hours": 5, "minutes": 30}}

            for proc in psutil.process_iter():
                name = proc.name()
                if name == process_name:
                    hours = data[process_name]["hours"]
                    minutes = data[process_name]["minutes"]

                    minutes = minutes + 1

                    if minutes >= 60:
                        minutes = 0
                        hours = hours + 1

                    data[process_name]["hours"] = hours
                    data[process_name]["minutes"] = minutes

            with open(file_name, 'w') as outfile:
                json.dump(data, outfile)

            time.sleep(interval)

        except Exception as exception:
            print(exception)


if __name__ == '__main__':
    do()
