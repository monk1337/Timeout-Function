from threading import Thread, Event
import time
when_stop=Event()
def time_out_function():
    i=0
    while True:
        i+=1
        print(i)
        time.sleep(1)

        if when_stop.is_set():
            break


if __name__ == '__main__':
    second_thread=Thread(target=time_out_function)
    second_thread.start()
    second_thread.join(timeout=5)

    when_stop.set()

    print("here you go")

