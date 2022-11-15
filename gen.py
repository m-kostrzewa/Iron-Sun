#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader("."))
TMPL_FNAME = "MISS_TSN-IronSun.xml.tmpl"
OUT_FNAME = "MISS_TSN-IronSun.xml"

def render():

    topRightX, topRightZ = 0, 6401
    midtopRightX, midtopRightZ = 0, 29550
    midRightX, midRightZ = 0, 50000
    midbotRightX, midbotRightZ = 0, 70449
    botRightX, botRightZ = 0, 93598
    topLeftX, topLeftZ = 93288, 7231
    botLeftX, botLeftZ = 93288, 93183

    context = {
        "shuttles": [
            "Proteus", 
            "Theseus", 
            "Odysseus", 
            "Perseus", 
            "Dionysus", 
            "Icarus", 
            "Adonis", 
            "Invention",
        ],
        "cargoTypes": {
            0: "None",
            1: "Parts", 
            2: "Minerals", 
            3: "Gas",
        },
        "sites": {
            "HQ": {
                "desc": "Terran headquarters. Protect at all costs! Produces Parts.",
                "x": "93184.0",
                "y": "0.0",
                "z": "53425.0",
                "hullId": "1002",
                "type": "station",
                "constructionSiteName": "HQ Site",
                "constructionRequirements": {
                    0: 10, # dummy val for postinit 
                    1: 0,
                    2: 0,
                    3: 0,
                },
                "producesCargo": 1,
                "producesEvery": 5,
                "ports": {},
            },
            "Mineral processor": {
                "desc": "Mines Minerals.",
                "x": "53011.0",
                "y": "0.0",
                "z": "14290.0",
                "hullId": "1003",
                "type": "neutral",
                "constructionSiteName": "MP Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 0,
                    3: 0,
                },
                "producesCargo": 2,
                "producesEvery": 5,
                "ports": {},
            },
            "Mining rig A": {
                "requires_exist": ["Mineral processor"],
                "desc": "Speeds up mineral mining.",
                "x": "61627.0",
                "y": "0.0",
                "z": "10034.0",
                "hullId": "1601",
                "type": "neutral",
                "constructionSiteName": "MRA Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 2,
                "producesEvery": 5,
                "ports": {},
            },
            "Mining rig B": {
                "requires_exist": ["Mineral processor"],
                "desc": "Speeds up mineral mining.",
                "x": "44395.0",
                "y": "0.0",
                "z": "26955.0",
                "hullId": "1601",
                "type": "neutral",
                "constructionSiteName": "MRB Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 2,
                "producesEvery": 5,
                "ports": {},
            },
            "Gas refinery": {
                "desc": "Mines Gas.",
                "x": "52388.0",
                "y": "0.0",
                "z": "85916.0",
                "hullId": "1356",
                "type": "neutral",
                "constructionSiteName": "GR Site",
                "constructionRequirements": {
                    0: 0,
                    1: 2,
                    2: 2,
                    3: 0,
                },
                "producesCargo": 3,
                "producesEvery": 5,
                "ports": {},
            },
            "Gas collector A": {
                "requires_exist": ["Gas refinery"],
                "desc": "Speeds up gas collection.",
                "x": "45018.0",
                "y": "0.0",
                "z": "93391.0",
                "hullId": "1503",
                "type": "neutral",
                "constructionSiteName": "GCA Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 2,
                "producesEvery": 5,
                "ports": {},
            },
            "Gas collector B": {
                "requires_exist": ["Gas refinery"],
                "desc": "Speeds up gas collection.",
                "x": "60381.0",
                "y": "0.0",
                "z": "85916.0",
                "hullId": "1503",
                "type": "neutral",
                "constructionSiteName": "GCB Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 2,
                "producesEvery": 5,
                "ports": {},
            },
            "Shipyard": {
                "desc": "Produces allied fleets.",
                "x": "89654.0",
                "y": "0.0",
                "z": "47404.0",
                "hullId": "1053",
                "type": "neutral",
                "constructionSiteName": "SY Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "producesEvery": 5,
                "ports": {
                    2: {
                        "portName": "Light",
                        "var": "makeLightFleet",
                        "angle": "90",
                        "amountProduced": 1,
                    },
                    3: {
                        "portName": "Heavy",
                        "var": "makeHeavyFleet",
                        "angle": "270",
                        "amountProduced": 1,
                    }
                },
            },
            "Armory": {
                "desc": "Produces tactical ordnance: torpedoes, pshocks and EMPs.",
                "x": "89862.0",
                "y": "0.0",
                "z": "51557.0",
                "hullId": "1407",
                "type": "station",
                "constructionSiteName": "AR Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "producesEvery": 5,
                "ports": {
                    1: {
                        "portName": "Torpedo",
                        "var": "makeTorpedos",
                        "angle": "0",
                        "desc": "Adds 10 torpedos to station inventory in exchange for Parts.",
                    },
                    2: {
                        "portName": "PShock",
                        "var": "makePShocks",
                        "angle": "90",
                        "desc": "Adds 5 pshocks to station inventory in exchange for Minerals.",
                    },
                    3: {
                        "portName": "EMP",
                        "var": "makeEMPs",
                        "angle": "270",
                        "desc": "Adds 2 EMPs to station inventory in exchange for Gas.",
                    }
                },
            },
            "Nuclear lab": {
                "desc": "Produces nuke-based ordnance: mines and nukes.",
                "x": "92976.0",
                "y": "0.0",
                "z": "45743.0",
                "hullId": "1050",
                "type": "station",
                "constructionSiteName": "NL Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "producesEvery": 5,
                "ports": {
                    2: {
                        "portName": "Mine",
                        "var": "makeMines",
                        "angle": "90",
                        "desc": "Adds 2 mines to station inventory in exchange for Minerals.",
                    },
                    3: {
                        "portName": "Nuke",
                        "var": "makeNukes",
                        "angle": "270",
                        "desc": "Adds 2 nukes to station inventory in exchange for Gas.",
                    }
                },
            },
            "Research facility": {
                "desc": "May provide clues on how to defeat the Iron Sun.",
                "x": "95883.0",
                "y": "0.0",
                "z": "48235.0",
                "hullId": "1004",
                "type": "neutral",
                "constructionSiteName": "RS Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "Gravitational wave detector": {
                "requires_exist": ["Research facility"],
                "desc": "May provide clues on how to defeat the Iron Sun.",
                "x": "35052.0",
                "y": "0.0",
                "z": "66297.0",
                "hullId": "1410",
                "type": "neutral",
                "constructionSiteName": "GW Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "Neutrino detector": {
                "requires_exist": ["Research facility"],
                "desc": "May provide clues on how to defeat the Iron Sun.",
                "x": "27786.0",
                "y": "0.0",
                "z": "36712.0",
                "hullId": "1411",
                "type": "neutral",
                "constructionSiteName": "ND Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "Plasma drill": {
                "requires_exist": ["Research facility"],
                "desc": "May provide clues on how to defeat the Iron Sun.",
                "x": "0.0",
                "y": "0.0",
                "z": "0.0",
                "hullId": "1054",
                "type": "neutral",
                "constructionSiteName": "PD Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "Kugelblitz generator": {
                "requires_exist": ["Research facility", "Gravitational wave detector", "Neutrino detector", "Plasma drill"],
                "desc": "Creates a black hole from photon energy.",
                "x": "0.0",
                "y": "0.0",
                "z": "0.0",
                "hullId": "1055",
                "type": "neutral",
                "constructionSiteName": "KB Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "Sappers": {
                "desc": "Allows construction of weapon platforms.",
                "x": "96298.0",
                "y": "0.0",
                "z": "51141.0",
                "hullId": "1050",
                "type": "neutral",
                "constructionSiteName": "SA Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "WP1": {
                "requires_exist": ["Sappers"],
                "desc": "Weapons platform.",
                "x": "52284.0",
                "y": "0.0",
                "z": "83529.0",
                "hullId": "1052",
                "type": "neutral",
                "constructionSiteName": "WP1 Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "WP2": {
                "requires_exist": ["Sappers"],
                "desc": "Weapons platform.",
                "x": "45848.0",
                "y": "0.0",
                "z": "90795.0",
                "hullId": "1052",
                "type": "neutral",
                "constructionSiteName": "WP2 Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "WP3": {
                "requires_exist": ["Sappers"],
                "desc": "Weapons platform.",
                "x": "42319.0",
                "y": "0.0",
                "z": "27889.0",
                "hullId": "1052",
                "type": "neutral",
                "constructionSiteName": "WP3 Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "WP4": {
                "requires_exist": ["Sappers"],
                "desc": "Weapons platform.",
                "x": "50623.0",
                "y": "0.0",
                "z": "14913.0",
                "hullId": "1052",
                "type": "neutral",
                "constructionSiteName": "WP4 Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "WP5": {
                "requires_exist": ["Sappers"],
                "desc": "Weapons platform.",
                "x": "92769.0",
                "y": "0.0",
                "z": "41903.0",
                "hullId": "1052",
                "type": "neutral",
                "constructionSiteName": "WP5 Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "WP6": {
                "requires_exist": ["Sappers"],
                "desc": "Weapons platform.",
                "x": "85710.0",
                "y": "0.0",
                "z": "43356.0",
                "hullId": "1052",
                "type": "neutral",
                "constructionSiteName": "WP6 Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "WP7": {
                "requires_exist": ["Sappers"],
                "desc": "Weapons platform.",
                "x": "86333.0",
                "y": "0.0",
                "z": "54982.0",
                "hullId": "1052",
                "type": "neutral",
                "constructionSiteName": "WP7 Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "WP8": {
                "requires_exist": ["Sappers"],
                "desc": "Weapons platform.",
                "x": "93392.0",
                "y": "0.0",
                "z": "56228.0",
                "hullId": "1052",
                "type": "neutral",
                "constructionSiteName": "WP8 Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 1,
                    3: 0,
                },
                "producesCargo": 0,
                "ports": {}
            },
        },
        "tsnShipNames": ['Foxglove', 'Bantry', 'Calshot Castle', 'Gorgon', 'Egremont', 'Glorious', 'Church', 'Holcombe', 'Hereward', 'Appleby Castle', 'Hepatica', 'Bloom', 'Colchester', 'Kingcup', 'Polsham', 'Minehead', 'Polecat', 'Earl Roberts', 'Sartine', 'Glasgow', 'Whirlwind', 'Ufton', 'Dolphins Prize', 'Epinal', 'Dalswinton', 'Heythorp', 'Black', 'Aberfoyle', 'Ellinor', 'Diamond', 'Geranium', 'Gympie', 'Cordelia', 'Bourbonnaise', 'Diamantina', 'Alyssum', 'Indomitable', 'Poulmic', 'Porto', 'Woodcock', 'Deale Castle', 'Fubbs', 'England', 'Kilbride', 'Illustrious', 'Grandmere', 'Esperanza', 'Snaefell', 'Quainton', 'Quiberon', 'Token', 'Bangor', 'Hoverfly', 'Etna', 'Bedford Galley', 'Belfast', 'Quesnel', 'Zebra', 'Pinner', 'Hydrangea', 'Hecate', 'Goodall', 'Campaspe', 'Clavering Castle', 'Stoic', 'Bustler', 'Maplin', 'Arve Prince', 'Lonsdale', 'Capelin', 'Portia', 'Wrenn', 'Racoon', 'Carrere', 'Halifax', 'Gulnare', 'Durham', 'Dannemark', 'Kitchen', 'Abergavenny', 'Brutus', 'Don', 'Felicidade', 'Oryx', 'Tweed', 'Verity', 'Magic', 'Crocus', 'Monkshood', 'Chichester', 'New Zealand', 'Eltham', 'Whimbrel', 'Hazardous', 'Craufurd', 'Green Linnet', 'Whitley', 'Wilhelmina', 'Isabella', 'Calypso', 'Cromarty', 'Wanderer', 'Ursa', 'Penelope', 'Kestrel', 'Mayford', 'Kilmersdon', 'Fairy', 'Farndale', 'Aydon Castle', 'Woodpecker', 'Scarab', 'Frome', 'Latrobe', 'Niagara', 'President', 'Marguerite', 'Majestic', 'Clun Castle', 'Furieuse', 'Valkyrie', 'Brocklesby', 'Pluto', 'Cassius', 'Owners Goodwill', 'Ben Lomond', 'Auricula', 'Polacca', 'Axford', 'Trump', 'Amalthaea', 'Imogen', 'Paz', 'Investigator', 'Maryborough', 'Torrens', 'Inglis', 'Buttington', 'Scylla', 'Helverson', 'Jenny', 'Lizard', 'Patrician', 'Albert', 'Clydebank', 'Arbiter', 'Julius', 'Duke of Albany', 'Azov', 'Clitheroe Castle', 'Undaunted', 'Ladybird', 'Cardigan Bay', 'Ekins', 'Bickerton', 'Gawler', 'Curlew', 'Dictator', 'Kilfinny', 'Dennis', 'Infernal', 'Urania', 'Alaart', 'Termagent', 'Broomley', 'Lancaster', 'Arras', 'Mounsey', 'Maida', 'Georgeham', 'Malvern', 'Blackmore Lady', 'Westcott', 'Bienfaisant', 'Bruce', 'Gavotte', 'Hindustan', 'Quaker', 'Sovereign', 'Fernie', 'Black Joke', 'Atherstone', 'Abelia', 'Ruby', 'Alligator', 'Unrivalled', 'Torch', 'Sandown', 'Marlingford', 'Caraquet', 'Cobourg', 'Resolute', 'Honeysuckle', 'Prosperous', 'Frontenac', 'Bull', 'Galicia', 'Pandora', 'Pegasus', 'Port Antonio', 'Flintham', 'Cauvery', 'Iveston', 'Upas', 'Camperdown', 'Alfred', 'Bantum', 'Tenedos', 'Haughty', 'Alonzo', 'Edderton', 'Orilla', 'Kalgoorlie', 'Combustion', 'Stayner', 'Paramour', 'Viper', 'Ben-my-Chree', 'James', 'Courageux', 'Brearley', 'Guardian', 'Ceanothus', 'Clayoquot', 'Bedham', 'Vanguard', 'Greyhound', 'Demon', 'Blaxton', 'Floriston', 'Fortune', 'Quinte', 'Urgent', 'Stronghold', 'Penetang', 'Andromeda', 'Cutlass', 'Charlottetown', 'Abelard', 'Isis', 'Antelope', 'Walpole', 'Parramatta', 'Hydra', 'Ramisham', 'Shamrock', 'Margett', 'Ellinore', 'Cornerbrook', 'Grandmistress', 'Nepeta', 'Mingan', 'Minuet', 'Oakville', 'Hussar', 'Dartington', 'Furnace', 'Condamine', 'Panglima', 'Vigo', 'Galt', 'Liverpool', 'Seven Sisters', 'Dogstar', 'Starling', 'Galliot', 'Belliqueux', 'Trenchant', 'Bradford', 'Caunton', 'Cat', 'Messenger', 'Edmonton', 'Antagonist', 'Magnanime', 'Jerfalcon', 'Barrosa', 'Cobham', 'Clarbeston', 'Esquimalt', 'Goree', 'Dullisk Cove', 'Belzebub', 'Champlain', 'Clio', 'Brothers', 'Papillon', 'Regulus', 'Indignant', 'Herald', 'Caldecot Castle', 'Dromio', 'Holdernesse', 'Legion', 'Porpoise', 'Espion', 'Havant', 'Hygeia', 'Velox', 'Spikenard', 'Dundas', 'Kempton', 'Winchelsea', 'Harland', 'Thistle', 'Myosotis', 'Blade', 'Flame', 'Grebe', 'Dover Prize'],
        "hegShipNames": ['Cannon Blocker', 'Sunken Seaweed', 'Night Fighter', 'Happy Dog', 'Davy Jones', 'Buccaneers', 'Dead-Mans Raft', 'Chubb', 'Begonia', 'Yarra', 'Littleham', 'Una', 'Coltsfoot', 'Filthy', 'Scorn', 'Fearful Slave', 'Damned Night', 'Example', 'Insolent', 'Brave Titan', 'Fallen Hook', 'Astraea', 'White Wave', 'Shiverin’ Dragon', 'Cacophonous', 'Pirate', 'Dragon', 'Tally-Ho', 'Happy Sailor', 'Wicked Folly', 'Kilchreest', 'Embleton', 'Abandoned Barnacle', 'Return', 'Kistna', 'Britomart', 'Chatham Hulk', 'Prompt', 'Dark Shark', 'Mad', 'Vile', 'Angry', 'Tonnant', 'Carlotta', 'Golden Squid', 'Thunder Tide', 'Speedy Slug', 'Horrid', 'Infanta', 'Fallen Captain', 'Burton', 'Gold', 'Old James', 'Seas', 'Python', 'Nelson', 'Tainted', 'Doubloon', 'Grille', 'Corsair', 'Raven', 'Lost Lagoon', 'North', 'Servant', 'Camel', 'Sanguine', 'Deadly Squid', 'Royal Pearl', 'Fall', 'Old Scallywag', 'Bittersweet', 'Black', 'Dream Chaser', 'Red', 'Plague Storm', 'Abandoned', 'Pillager', 'Hungry Hangman', 'Treasure', 'Silent Killer', 'Old Sea Dog', 'Princess', 'Monowai', 'Aubretia', 'Soul Cairn', 'Wenslydale', 'Ogre', 'Marauders', 'Disgraced', 'Lightning', 'Barbaric Ghost', 'Nith', 'Tattoo', 'Howl', 'Old Barnacle', 'Prompt Prize', 'Durweston', 'Hangman', 'Servants', 'Hazard', 'Springer', 'Silent', 'Trumpeteer', 'Golden Eel', 'Tithonus', 'Stone Angel', 'Tainted Dragon', 'Delphinium', 'Night Wind', 'Rambler', 'Whitby', 'Executioners', 'Dishonorable', 'Grail', 'Confiance', 'Privateers', 'Slave', 'Fair Rhodian', 'Keren', 'Handy', 'Sea', 'Charles and Henry', 'Ganga', 'Torbay', 'Navarino', 'Murderers', 'Usk', 'Gold Coast', 'Otranto', 'Sea', 'Flight', 'Stinkin Skull', 'Irvine', 'Dead Bones', 'Oribi', 'Poseidon\'s Revenge', 'Pure Sirens', 'Lost King', 'Cadmus', 'Red Pirate', 'Rift', 'Ameer', 'Fowey', 'Aeolus', 'Kilmacrennan', 'Somme', 'Formidable', 'Canceaux', 'Spartan', 'Broken Slave', 'Blind', 'North Star', 'Mersey', 'Cursed', 'Wheatland', 'Swashbucklers', 'Dirty Dragon', 'Dodman Point', 'Slinger', 'Hurst Castle', 'Ruthless Raider', 'Gilia', 'Homicidal', 'Neptune’s Teeth', 'Pretty Coral', 'Hope', 'Squid Blaster', 'Dreaming Wave', 'Collins', 'New Pearl', 'Howling', 'Greed', 'Banshee', 'Ghostly Death', 'Beschermer', 'Old TIde', 'Hasty', 'Tainted Rose', 'Captains', 'Revenge Queen', 'Hateful', 'Ramsey', 'Fear', 'Serapis', 'Hades', 'Crimson', 'Halstarr', 'Caribbean', 'Cursed Raider', 'Vanilla Skyline', 'Lost Treasure', 'Plunder', 'Coriander', 'Eel', 'Sacrett', 'Murderous', 'Gambia', 'Inman', 'Sea of Terror', 'Pirates', 'Prize', 'Crofton', 'Damned', 'Privateer', 'Ben Nevis', 'Cottesmore', 'Shark', 'Buctouche', 'Red Wave', 'Independencia', 'Grief', 'Darsham', 'Vittoria', 'Glorioso', 'Firequeen', 'Cutlass', 'Broken', 'Torrington', 'Ledsham', 'Grand Serpent', 'Drunken James', 'Scurvy', 'Grenville', 'Puntoone', 'Poisonous Maid', 'Festering', 'Eclair', 'Harp', 'Insanity', 'Rude', 'Foul Serpent', 'Night', 'Bone Heart', 'Hangman’s Hollow', 'Brunei', 'Obedient', 'Red Hurricane', 'Rovers', 'Lost Soul', 'Ocean Curse', 'Penzance', 'Zest', 'Nisus', 'Nettle', 'Wager', 'Loyal Chancellor', 'Deceitful', 'Cromer', 'Seven Seas', 'Medina', 'Prestonian', 'Seven Seas of WIlliams', 'Bamborough Castle', 'Raider', 'Calendula', 'Murderer', 'Thunder Waves', 'Shadow Storm', 'Neptune', 'Ypres', 'Bream', 'Rising Ghost', 'Reindeer', 'Dream Stealer', 'Landrail', 'Sudden', 'Shadow', 'Progresso', 'Evil', 'Sceptre', 'Centaur', 'Sadness', 'Howl', 'Horror', 'Blood Lightening', 'Heliotrope', 'Happy', 'Jewel Serpent', 'Fearful', 'Amazon', 'Bloody Hangman', 'Moslem', 'Madness', 'Havannah', 'Seas', 'Terror', 'Saber', 'Guinea', 'Drunken Sailor', 'Nymph', 'Bigbury Bay', 'Devil’s Heart', 'Acheron', 'Kilfullert', 'Damp Queen', 'Tancred', 'Pimpernel', 'Chatham Double', 'Nereus', 'Flamingo', 'Ginger Snap', 'White Night', 'Serpent\'s Revenge', 'Greyhond', 'Mont Blanc', 'Kingsford', 'Corso', 'Sun Howler', 'Damned', 'Parret'],
        "caltronShipPrefixes": ['', '0x', '', '0b', '', '', '', '&', '', '*', '-', '', '', '', '', '', ''],
        "caltronShipInfixes": ['F', '_', 'B', 'V', 'L', 'add', 'nop', 'C', 'O', 'Y', 'M', 'mov', 'G', 'Z', 'U', '=>', 'mov', '_', 'Q', 'I', 'T', 'mul', '0', 'Y', '0', 'K', '5', 'H', 'P', 'I', 'X', 'S', 'fizz', 'H', 'P', '2', '6', 'N', 'R', 'buzz', '-', 'A', '-', 'D', '4', 'V', 'Z', '_', 'nop', '-', 'A', 'U', 'D', 'T', 'S', 'R', '4', '=>', 'O', 'N', '_', '1', 'J', '3', 'bar', 'J', '1', 'foo', '=>', '-', '_', 'L', '_', 'E', 'E', 'G', '-', 'C', 'X', '->', 'B', 'M', 'F', 'Q', '-'],
        "caltronShipSuffixes": ['', '++', '', '', '', '', '--', '', '()', '', ';', '[:]', '', '', '', ],
        "waves": [
            {
                "atDistance": 90000,
                "race": "TSN",
                "x": 4000,
                "y": "0.0",
                "z": midRightZ,
                "hulls": [1, 1, 2],
                "sideValue": 2,
            },
            {
                "hail": "Hello again, insects. We've devised a new test to see if you're worthy of ascension. Enjoy the encounter with Iron Sun!",
                "atDistance": 89900,
                "race": "Caltron",
                "spawnAt": "Iron Sun",
                "hulls": [7206, 7204, 7201],
                "sideValue": 1,
            },
            {
                "atDistance": 89800,
                "race": "Caltron",
                "x": midbotRightX,
                "y": "0.0",
                "z": midbotRightZ,
                "hulls": [7201, 7203],
                "sideValue": 1,
            },
            {
                "atDistance": 89700,
                "race": "Caltron",
                "x": midtopRightX,
                "y": "0.0",
                "z": midtopRightZ,
                "hulls": [7201, 7202, 7202],
                "sideValue": 1,
            },
        ],
    }


    with open(OUT_FNAME, 'w') as f:
        f.write(template_env.get_template(TMPL_FNAME).render(context))

def main():
    render()

if __name__ == "__main__":
    main()
