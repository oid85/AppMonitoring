import time
import psutil


def do():
    process_name = "mstsc.exe"
    seconds = 0.0

    while True:
        try:
            interval = 15.0
            for proc in psutil.process_iter():
                name = proc.name()
                if name == process_name:
                    seconds = seconds + interval

            print(process_name, seconds/60, " мин.")
            time.sleep(interval)

        except Exception:
            print("Error...")


if __name__ == '__main__':
    do()
