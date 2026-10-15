import math
import time
from random import choice
import requests
import wifi

# Fetch signups
HAVEN_EVENT_LOCATION = "london" # the best haven :D
def fetch_signups():
    data = requests.get("https://haven.hackclub.com/api/signups").json()
    for event in data["events"]:
        if event["slug"] == HAVEN_EVENT_LOCATION:
            return int(event["signups"])


# Event time functions
def calculate_time_to_event():
    rtc_list = list(rtc.datetime())
    rtc_list.append(0)
    time_tuple = rtc_list

    current_epoch = time.mktime(time_tuple)
    event_epoch = 1794642600  #  Nov 14, 2026 at 8:50:00 AM BST

    difference = event_epoch - current_epoch  # this is in seconds
    difference_days = math.floor(difference / 60 / 60 / 24)
    difference_hours = math.floor(difference / 60 / 60) - (difference_days * 24)

    return difference_days, difference_hours


def get_percentage_to_event():
    rtc_list = list(rtc.datetime())
    rtc_list.append(0)
    time_tuple = rtc_list

    booking_epoch = 1790328600  # Sep 25, 2026 at 10:30:00 AM BST
    current_epoch = time.mktime(time_tuple)
    event_epoch = 1794642600  # Nov 14, 2026 at 8:50:00 AM BST

    percentage = (current_epoch - booking_epoch) / (event_epoch - booking_epoch)
    return percentage

class ProgressBar:
    RADIUS = 4
    OUTLINE_THICKNESS = 2

    def __init__(self, top_left_corner_x, top_left_corner_y, width, height):
        self.fillable_width = width
        self.top_left_x = top_left_corner_x
        self.top_left_y = top_left_corner_y
        self.bar_height = height

        # Draw the filled white inside
        self.outline_fill = shape.rounded_rectangle(
            top_left_corner_x,
            top_left_corner_y,
            width,
            height,
            self.RADIUS,
        )
        # Draw the outline
        self.outline = self.outline_fill.stroke(self.OUTLINE_THICKNESS)

        # The actual progress bar
        self.bar_shape = shape.rectangle(
            top_left_corner_x,
            top_left_corner_y,
            0,
            self.bar_height,
        )

        # self.draw()

    def set_progress(self, progress):
        bar_width = self.fillable_width * progress
        self.bar_shape = shape.rounded_rectangle(
            self.top_left_x,
            self.top_left_y,
            bar_width,
            self.bar_height,
            self.RADIUS,
        )

    def draw(self):
        screen.pen = color.white
        screen.shape(self.outline_fill)

        screen.pen = color.black
        screen.shape(self.outline)

        screen.pen = color.black
        screen.shape(self.bar_shape)


time_bar = ProgressBar((screen.width - 200) / 2, 90, 200, 20)
signups_bar = ProgressBar((screen.width - 200) / 2, 135, 200, 20)

try:
    logo = image.load("/system/apps/haven_timeline/assets/logo.png")
except:
    logo = image.rectangle(5, 5, 5, 5)


wifi.connect()
while not wifi.is_connected():
    time.sleep(0.2)


def update():  # runs in a loop when the app is open
    badge.mode(FAST_UPDATE | NON_BLOCKING)

    screen.pen = color.white
    screen.clear()

    # Haven logo
    screen.blit(logo, vec2(50, 5))

    # Time text
    days, hours = calculate_time_to_event()
    screen.font = rom_font.nope
    screen.pen = color.black
    screen.text(f"{days} days, {hours} hours left!", 30, 75)

    # Time bar
    time_bar.set_progress(get_percentage_to_event())
    time_bar.draw()

    # Signups stuff
    wifi.connect()
    rtc.time_from_ntp()
    signups = fetch_signups()  # fetch the projects

    # Hackatime text
    screen.pen = color.black
    screen.text(f"{signups} / 200 signups", 30, 120)

    # Hackatime bar
    signups_bar.set_progress(signups / 200)
    signups_bar.draw()

    SLEEP_MINUTES = 30
    rtc.set_alarm(minutes=SLEEP_MINUTES)  # set an alarm to wake up after

    badge.update()
    wait_for_button_or_alarm(timeout=SLEEP_MINUTES * 60 * 1000)  # 600 seconds


def on_exit():
    rtc.clear_alarm()


run(update)
