# haven timeline

<img width="1407" height="635" alt="Screenshot 2026-10-14 at 7 00 04 PM" src="https://github.com/user-attachments/assets/15c4710b-0a65-4a4f-9d80-491de86fe82d" />



## what
This project is a countdown to [Hack Club Haven](https://hack.club/havenldn)! It runs as an app on the Pimoroni Badger 2350 (an e-ink conference badge with battery power and WiFi).

Based on my [previous version](https://github.com/duckida/horizons_timeline) for Hack Club Horizons!

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
