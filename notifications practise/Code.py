import time
from plyer import notification
if __name__=='__main__':
    while True:
        notification.notify(
            title = "drink water ok?",
            message = "Do you wanna be a dehydrated bih?",
            timeout = 10
        )
        time.sleep(15)