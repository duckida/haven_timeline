# haven timeline

## what
This project is a countdown to [Hack Club Haven](https://hack.club/havenldn)! It runs as an app on the Pimoroni Badger 2350 (an e-ink conference badge with battery power and WiFi).

It counts down days/hours until the event & shows the number of signups to the event pulled through the Haven signups API!

## why
i'm really excited for Haven, and wanted a quick way to check out how many people will show up & how much longer to go!

## installation guide
1. Download the repo & unzip
2. Put your badge in mass storage mode
3. Copy the `__init__.py`, `icon.png`, and `assets/` into a folder called `haven_timeline` in `/system/apps` on the badge (don't copy the whole repo folder as it contains large git history)
4. Change the Haven event slug in `__init__.py` under `HAVEN_EVENT_LOCATION` to yours (eg. `london`)
5. Ensure your badge has wifi configured in `secrets.py`
6. Eject the badge and open the app!

## AI declaration
I used AI only for debugging and research / calculations, all of the code was written by hand!
