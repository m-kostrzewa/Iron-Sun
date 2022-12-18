# Iron Sun

A mission for Artemis Spaceship Bridge Simulator v.2.8.1 (but may work on other versions).

There are two variants of this mission available: "normal" and "easy".

Normal mode is balanced for TSN RP community (~4 coordinated crews).

GM Console is available to tweak the scenario on the fly. If the GM buttons don't appear, use "G" hotkey when on GM screen.

You may wish to tweak the scenario to your liking. See [Modification](#Modification). 

![Screen 1](Screen1.png?raw=true "Map")
![Screen 2](Screen2.png?raw=true "Planet")
![Screen 3](Screen3.png?raw=true "Iron Sun")

## Outline

The ultimate Caltron weapon, Iron Sun, is headed towards Terra Noua.

Pirates and Hegemony, looking for opportunity to damage TSN in any way possible, ally with Caltron invaders.

Gather resources, construct stations, build fleets and ordnance, research the Caltron weapon and ultimately defeat the Iron Sun, before it reaches the planet!

## Installation

Requires TSN RP Mod File 3.1 installed (it provides additional assets), available [here](http://www.terranstellarnavy.net/tsn-expansion/).

* Place the MISS_TSN-IronSun.xml file under `Artemis\dat\Missions\MISS_TSN-IronSun` (e.g. `C:\Program Files (x86)\Artemis\dat\Missions\MISS_TSN-IronSun`).
* Place the MISS_TSN-IronSunEasy.xml file under `Artemis\dat\Missions\MISS_TSN-IronSunEasy` (e.g. `C:\Program Files (x86)\Artemis\dat\Missions\MISS_TSN-IronSunEasy`).


## Modification

You can tweak the scenario to your loking.

The easiest way is to modify the mission .xml file directly.

However, you can also modify template parameters in `gen.py`.

You may wish to remove/add/tweak the `waves` and `spawners` lists as described in the comments.
You can also lower construction resource requirements by modifying contents of `sites` list.

The .xml file is then regenerated using Python3 from Jinja2 template like so:

```
# Assuming you have Python3 installed

# Install jinja2 if you haven't already
pip3 install jinja2

# Regenerate the mission file!
python .\gen.py
```
