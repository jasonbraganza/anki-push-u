# anki-push-u

Tiny script to regularly notify you of cards due in your Anki deck, via Pushover.  
[Read more on related blog post](https://janusworx.com/anki-push-u)

Not yet ready for prime time.  
Still a wip

## You need

1. Anki Desktop
2. A functioning [Pushover account](https://pushover.net/)

## Instructions

1. Clone or download this repo to your machine
2. Create a new application or api token in your [Pushover account](https://pushover.net/)
3. Make a note of your Pushover User Key as well as your API Token/Key
4. Find out the path to your Anki Add-ons folder. (Tools -> Add-ons and then View Files in the window that appears)
5. Copy or move the pushover folder that into the Anki Add-ons folder.
6. Edit `__init__.py` and put in your details (your Pushover details and the interval at which, you’d like to be
   reminded in minutes) in the `SETUP` section of the file.
7. If Anki’s running, restart it. Anki will scan and pick up the add-on
8. As long as Anki’s running, you should get regular Pushover notifications