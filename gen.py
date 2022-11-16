#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader("."))
TMPL_FNAME = "MISS_TSN-IronSun.xml.tmpl"
OUT_FNAME = "MISS_TSN-IronSun.xml"

def render():

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
                "onConstructedComms": "HQ online. Find a way to destroy Iron Sun before it obliterates Terra Noua! Also, defend us at the HQ.",
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
                "producesEvery": 60,
                "ports": {},
            },
            "Mineral processor": {
                "desc": "Mines Minerals.",
                "onConstructedComms": "Commencing mining operations.",
                "x": "53011.0",
                "y": "0.0",
                "z": "14290.0",
                "hullId": "1003",
                "type": "neutral",
                "constructionSiteName": "MP Site",
                "constructionRequirements": {
                    0: 0, # ignore
                    1: 1, # cost in Parts
                    2: 0, # cost in Minerals
                    3: 0, # cost in Gas
                },
                "producesCargo": 2,
                "producesEvery": "MineralMiningTime",
                "ports": {},
            },
            "Mining rig A": {
                "requires_exist": ["Mineral processor"],
                "desc": "Speeds up mineral mining.",
                "onConstructedComms": "Reporting for duty.",
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
                "ports": {},
            },
            "Mining rig B": {
                "requires_exist": ["Mineral processor"],
                "desc": "Speeds up mineral mining.",
                "onConstructedComms": "Ready!",
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
                "ports": {},
            },
            "Gas refinery": {
                "desc": "Mines Gas.",
                "onConstructedComms": "Pressure nominal.",
                "x": "52388.0",
                "y": "0.0",
                "z": "85916.0",
                "hullId": "1356",
                "type": "neutral",
                "constructionSiteName": "GR Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 2,
                    3: 0,
                },
                "producesCargo": 3,
                "producesEvery": "GasMiningTime",
                "ports": {},
            },
            "Gas collector A": {
                "requires_exist": ["Gas refinery"],
                "desc": "Online.",
                "x": "45018.0",
                "y": "0.0",
                "z": "93391.0",
                "hullId": "1503",
                "type": "neutral",
                "constructionSiteName": "GCA Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 2,
                    3: 0,
                },
                "ports": {},
            },
            "Gas collector B": {
                "requires_exist": ["Gas refinery"],
                "desc": "On station.",
                "x": "60381.0",
                "y": "0.0",
                "z": "85916.0",
                "hullId": "1503",
                "type": "neutral",
                "constructionSiteName": "GCB Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 2,
                    3: 0,
                },
                "ports": {},
            },
            "Shipyard": {
                "desc": "Produces allied fleets.",
                "onConstructedComms": "We are ready to construct light and heavy fleets for Minerals and Gas respectively.",
                "x": "89654.0",
                "y": "0.0",
                "z": "47404.0",
                "hullId": "1053",
                "type": "neutral",
                "constructionSiteName": "SY Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
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
                "onConstructedComms": "Bring us Parts, Minerals or Gas and we'll construct Torpedoes, PShocks and EMPs respectively.",
                "x": "89862.0",
                "y": "0.0",
                "z": "51557.0",
                "hullId": "1407",
                "type": "station",
                "constructionSiteName": "AR Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
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
                "onConstructedComms": "Nuclear fission byproducts let us prepare Mine and Nuke warheads for Minerals and Gas.",
                "x": "92976.0",
                "y": "0.0",
                "z": "45743.0",
                "hullId": "1050",
                "type": "station",
                "constructionSiteName": "NL Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
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
                "onConstructedComms": "We need more data! Construct gravitational waves detector, neutrino detector and plasma drill at designated coordinates.",
                "x": "95883.0",
                "y": "0.0",
                "z": "48235.0",
                "hullId": "1004",
                "type": "neutral",
                "constructionSiteName": "RS Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "Gravitational wave detector": {
                "requires_exist": ["Research facility"],
                "desc": "May provide clues on how to defeat the Iron Sun.",
                "onConstructedComms": "Analyzing Iron Sun gravitional wave footprint.",
                "x": "35052.0",
                "y": "0.0",
                "z": "66297.0",
                "hullId": "1410",
                "type": "neutral",
                "constructionSiteName": "GW Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 3,
                    3: 2,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "Neutrino detector": {
                "requires_exist": ["Research facility"],
                "desc": "May provide clues on how to defeat the Iron Sun.",
                "onConstructedComms": "We're detecting anti-neutrinos emanating from the Iron Sun.",
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
                    3: 3,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "Plasma drill": {
                "requires_exist": ["Research facility"],
                "desc": "May provide clues on how to defeat the Iron Sun.",
                "onConstructedComms": "Extracting Iron Sun surface sample.",
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
                "onConstructedComms": "Kugelblitz generator online.",
                "x": "0.0",
                "y": "0.0",
                "z": "0.0",
                "hullId": "1055",
                "type": "neutral",
                "constructionSiteName": "KB Site",
                "constructionRequirements": {
                    0: 0,
                    1: 0,
                    2: 1,
                    3: 3,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "Sappers": {
                "desc": "Allows construction of weapon platforms.",
                "onConstructedComms": "We have designated locations suitable for weapon platforms construction.",
                "x": "96298.0",
                "y": "0.0",
                "z": "51141.0",
                "hullId": "1050",
                "type": "neutral",
                "constructionSiteName": "SA Site",
                "constructionRequirements": {
                    0: 0,
                    1: 1,
                    2: 2,
                    3: 2,
                },
                "producesCargo": 0,
                "ports": {}
            },
            "WP1": {
                "requires_exist": ["Sappers"],
                "onConstructedComms": "Weapon platform online.",
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
                "onConstructedComms": "Weapon platform online.",
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
                "onConstructedComms": "Weapon platform online.",
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
                "onConstructedComms": "Weapon platform online.",
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
                "onConstructedComms": "Weapon platform online.",
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
                "onConstructedComms": "Weapon platform online.",
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
                "onConstructedComms": "Weapon platform online.",
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
                "onConstructedComms": "Weapon platform online.",
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
        "tsnShipNames": ['Guerriere', 'Kelly', 'Adroit', 'Orkney', 'Seabear', 'Statesman', 'Doon', 'Martial', 'York Castle', 'Decouverte', 'Mauritius', 'Orontes', 'Exeter', 'Halifax', 'Amfitrite', 'Kilmaine', 'Edmundston', 'Statice', 'Slinger', 'Buxton', 'Espoir', 'Nessus', 'Glenroy', 'Bodiam Castle', 'Etrusco', 'Medusa', 'Olympus', 'Strenuous', 'Daedalus', 'Amokura', 'Constance', 'Alynbank', 'Pollington', 'Benalla', 'Puck', 'Wessex', 'Pukaki', 'Spindrift', 'Mounts Bay', 'Cheriton', 'Epreuve', 'Prompte', 'Carhampton', 'Aboukir', 'Cornwallis', 'Gondwana', 'Kilcar', 'Niger', 'Nepeta', 'Teviot Bank', 'Crediton', 'Charles', 'Wolsey', 'Neza', 'Tedworth', 'Upholder', 'Plantagenet', 'Duchess of Norfolk', 'Carew Castle', 'Antagonist', 'Lockeport', 'Alpheus', 'Andromeda', 'Vulcan', 'George', 'Aphrodite', 'Badminton', 'Havick', 'Emperor', 'Aylmer', 'Albemarle', 'Friezland', 'Exmoor', 'Michael', 'Pevensey Castle', 'Paul', 'Clarence', 'Batman', 'Gorleston', 'Ledbury', 'Onslow', 'Eden', 'Alfred', 'Persian', 'Lewiston', 'Ballindery', 'Wishart', 'Brixham', 'Caroles', 'Redpole', 'Nyaden', 'Tenby', 'Puntoone', 'Flamborough', 'Linganbar', 'Yukon', 'Ascension', 'Goodson', 'Portsmouth', 'Unsparing', 'Kilmorey', 'Milne', 'Ettrick', 'Fairy', 'Hesper', 'Finch', 'Trinidad', 'Fritham', 'Seagull', 'Pomone', 'Panther', 'Elphinstone', 'James Galley', 'Kempthorne', 'Henrietta', 'Turpin', 'Marlborough', 'Spiteful', 'Bevington', 'Comeet', 'Drury', 'Moira', 'Norwich Castle', 'Tigress', 'Kincardine', 'Welshman', 'Nighthawk', 'Swindon', 'Borage', 'Ascot', 'Titania', 'Matchless', 'Phlegethon', 'Cardigan Bay', 'Mansfield', 'Orion', 'Slaney', 'Loosestrife', 'Unbridled', 'Kilburn', 'Podargus', 'Mediterranean', 'Zenobia', 'Burchett', 'Prestonian', 'Belle Isle', 'Aimable', 'Glengyle', 'Unite', 'Loyal Chancellor', 'Bouncer', 'Bellwort', 'Isle of Wight', 'Meynell', 'Cavalier', 'Thistle', 'Supreme', 'Cyclops', 'Bucephalus', 'Teviot', 'Oberon', 'Apollo', 'Dolphins Prize', 'Palinurus', 'Vidette', 'De Ruyter', 'Appleton', 'Viking', 'Aldenham', 'Eyderen', 'Sea Devil', 'Georgiana', 'Mutine', 'Sesame', 'Palm Tree', 'Triumph', 'Margate', 'Errant', 'Owners Adventure', 'David', 'Nile', 'Affray', 'Sovereign', 'Bilsthorpe', 'Adam & Eve', 'Sunfish', 'Dover Prize', 'Margett', 'Capilano', 'Cerf', 'Abelia', 'Dunwich', 'Deptford Prize', 'Hornby', 'Constitution', 'Battleaxe', 'Galliot', 'Chediston', 'Broadway', 'Cook', 'Carisbrooke Castle', 'Tweed', 'Carronade', 'Blake', 'Dover Castle', 'Audaciuex', 'Torbay', 'Satyr', 'Venturer', 'Fyen', 'Broaderschap', 'Allegiance', 'Highburton', 'Unrivalled', 'Torrington', 'Newcastle', 'Holcombe', 'Jubilant', 'Egremont Castle', 'Hyacinth', 'Newton', 'Valiant', 'Dunbar', 'Narcissus', 'Cherub', 'Lookout', 'Islip', 'Narbrough', 'Murray', 'Sabine', 'Sterlet', 'Wilton', 'Sladen', 'Chevreuil', 'Blackburn', 'Ranger', 'Excalibur', 'Lothian', 'Cambrian', 'Penn', 'Voltaire', 'Oakington', 'Sapphire', 'Dianella', 'Vetch', 'Henry Prize', 'Jellicoe', 'Matabele', 'Uganda', 'Decoy', 'Saladin', 'Gabriel', 'Otter', 'Bienfaisant', 'Oreste', 'Cicero', 'Prevost', 'Granby', 'Cawsand Bay', 'Bombay Castle', 'Tasman', 'Argenta', 'Owners Love', 'Parapet', 'Crafty', 'Glatton', 'Lasham', 'Badger', 'Cornel', 'Marne', 'Circassian', 'Elias', 'Menace', 'Mandate', 'Ivanhoe', 'Monitor', 'Sheerness', 'Redgauntlet', 'Hermes', 'Goodall', 'Meteor', 'Warwick', 'Explorer', 'Abundance', 'Dutiful', 'Sunflower', 'Bonito', 'Perseverance', 'Paladin', 'Cracker', 'Edgar', 'Grenada', 'Etna', 'Bedford Galley', 'Peterel', 'Mayford', 'Castor', 'Terrible', 'Geraldton', 'Caunton', 'Burnie', 'Peregrine', 'Anne Royal', 'Urania', 'Bottisham', 'Trumpeteer', 'Fleche', 'Hecate', 'Imaum', 'Omdurman'],
        "hegShipNames": ['Dirty Dragon', 'Vanilla Skyline', 'Rorqual', 'Gloire', 'Hawkins', 'Forester', 'Gayundah', 'Angel of Doom', 'Preston', 'Providence', 'Bluethroat', 'Golden Eel', 'Jervis', 'Epsom', 'Blood-Thirsty Rover', 'Trespasser', 'White Wave', 'Fearful', 'Malham', 'Manta', 'Thane', 'Christopher', 'Helicon', 'Boscawen', 'Murderer', 'Thisbe', 'Uncultured', 'Disgraced Anchor', 'Maesterland', 'Caribbean', 'Tide', 'Corrupted Skull', 'Plunderer', 'Scream Fire', 'Hellish', 'Baleine', 'Abbotsham', 'HellFish', 'Maryport', 'Killer', 'Elk', 'Crooked Star', 'Red Wave', 'Giles', 'Duncansby Head', 'Demir Hisar', 'Haydon', 'Advice Prize', 'Poisonous Maid', 'Beacon Hill', 'Fareham', 'Seven Seas of WIlliams', 'Pigeon', 'Thunder Tide', 'Deadly Squid', 'Night Blood', 'Rose', 'Dark Shark', 'Curse of Poseidon', 'Easton', 'Servants', 'Jewel Theif', 'Good', 'Christ', 'Hickleton', 'Saldhana', 'Lost Treasure', 'Night', 'Coaticook', 'Nova Scotia', 'Faulknor', 'Chasseur', 'Drunken Squid', 'Carrier', 'Tainted', 'Mermaid', 'Hardi', 'Tetcott', 'Uproar', 'Ghostly Death', 'Blairmore', 'Curragh', 'Moyola', 'Jolly Skull', 'Aeneas', 'Speedy', 'Sanguine', 'Dishonorable', 'Mayflower', 'Punjabi', 'Avon', 'Hestor', 'Ginger Snap', 'Petard', 'Comox', 'Impolite', 'Milfoil', 'Plague', 'Lagan', 'Jahangir', 'Deadly Destiny', 'Tiger', 'Sudden', 'Pirate’s Secret', 'Tainted Heart', 'Executioners', 'Fallen Hook', 'Nilam', 'Fawkner', 'Deale Castle', 'Abandoned', 'Kipling', 'Hateful', 'Bat', 'Petunia', 'Disgraceful', 'Grail', 'Captains', 'Revenge Queen', 'Night Fighter', 'Barbados', 'Redoubt', 'Night Soul', 'Damp Queen', 'Red', 'Ingonish', 'Princess', 'Broken Soul', 'Mystic Sirens', 'Servant', 'Amelia', 'Aubretia', 'Lost Lagoon', 'Lost Soul', 'Bloodthirsty', 'Poison', 'Serpent’s Cry', 'Demon', 'Cursed', 'Cicala', 'Golden', 'Neptune’s Teeth', 'Melbreak', 'Ulgy Kraken', 'Hungry Hangman', 'Canceaux', 'Pitcairn', 'Fallen Titan', 'Sea Ghost', 'Vicious', 'Hawthorn', 'Overyssel', 'Night', 'Claverhouse', 'Landguard', 'Hart', 'Engadine', 'Victory', 'Bloody', 'Old Sea Dog', 'Dream Stealer', 'Nusa', 'Dundalk', 'Madras', 'Hampton', 'Keats', 'Combatant', 'Resource', 'Marjoram', 'Artigo', 'Cambridge', 'Meredith', 'Executioner', 'Return', 'Plunder', 'Dusty Anchor', 'Arras', 'Shark', 'Plague Lagoon', 'Delphinen', 'Fear', 'Captain', 'Old Barnacle', 'Hellish Shark', 'Agate', 'Acertif', 'Hades', 'Euphrates', 'North Bay', 'Kilcolgan', 'Buccaneer', 'Barbaric Ghost', 'Joseph', 'Cursed Raider', 'Speedy Sun', 'Delhi', 'Windsor', 'Bearded', 'Sadness', 'Carnarvon Bay', 'Devils', 'Torch', 'Plunderers', 'Night Wind', 'Endymion', 'Brolga', 'Howling', 'Mad', 'Drunken Sailor', 'Terror', 'Frog', 'Corruption', 'Snake', 'Tetrarch', 'Wolverine', 'Fagons', 'Thetis', 'Alliance', 'Dolphin', 'Fallen Captain', 'Lanton', 'Charles and Henry', 'Golden Jewel', 'Lightning', 'Deceitful', 'Rancid', 'Whimbrel', 'Kilchvan', 'Seven Seas', 'Gael', 'Germoon Prize', 'Serpent’s Revenge', 'Disdain', "Lion's Whelp", 'Shah', 'Germaine', 'Ajdaha', 'Sun Howler', 'Sunken Seaweed', 'Bramber Castle', 'Moth', 'Tortola', 'Folkeston', 'Brune', 'Gawler', 'Firefly', 'Curacoa', 'New Pearl', 'Hurworth', 'Portleven', 'Chignecto', 'Mariana', 'Invention', 'Brayford', 'Inconstant', 'Devil’s Heart', 'Foul Serpent', 'Silent', 'Scream', 'Corrupted', 'Benjamin', 'Golden Rose', 'Lost Mayflower', 'Horrid', 'Sea of Terror', 'Thruster', 'Cruel', 'Soulless Dragon', 'Evil', 'Owen Glendower', 'Revenge', 'Radstock', 'Saber', 'Snap', 'Thunder Waves', 'Brenchley', 'Keppel', 'Estridge', 'Cavan', 'Toreador', 'Brave Titan', 'New Adventure', 'Tainted Dragon', 'Persimmon', 'Broken', 'Charlotte', 'Golden Squid', 'Droxford', 'Redmill', 'Mosquito', 'Kilbrittain', 'Diadem', 'Gulnare', 'Fredericton', 'Akbar', 'Braithwaite', 'Humberstone', 'Shadow Storm', 'Chester', 'Port Colborne', 'Sea Scout', 'Liberty', 'Blood Lightening', 'Upton', 'Blaze', 'Chepstow Castle', 'Unswerving', 'Halcyon', 'Burning Rose', 'Pirates', 'Camilla', 'Thule', 'Disgrace', 'Bellerophon', 'Oriole', 'Caicos', 'Franchise', 'Jewel Serpent', 'Verbena', 'Sick Walrus', 'Bastion', 'Eurotas', 'Celebes', 'Julian', 'Dampier', 'Sunken Whale', 'Colchester', 'Impregnable', 'Eagle', 'Stone Shark', 'Kite', 'Independencia', 'Dream Chaser', 'Red Pirate', 'Happy', 'Southwold', 'Cannon Blocker', 'Spur', 'Paradox', 'Botha', 'Guysborough', 'Pure Sirens', 'Festering', 'Portland Bill', 'Dilston', 'Biddeford', 'Fencer', 'Medina', 'Cyrus', 'Scorn', 'Curieux', 'Greed', 'Renascent', 'Rising', 'Poictiers', 'Delivery', 'Dazzling Pearl', 'Black', 'Silent Killer', 'Marauders', 'Willowherb', 'Popham', 'Aberfoyle', 'Jed', 'Disgraced', 'Astarte', 'Silent Raider', 'Montford', 'Sea', 'Lone Star', 'Tenedos', 'Milford', 'Fish Fryer', 'Spider', 'Courageux', 'Fallen Fish', 'Dacres', 'Dungeness', 'Scurvy Wave', 'Starwort', 'Insanity', 'Buccaneers', 'Red Hurricane', 'Gloriosa', 'Sun', 'Courbet', 'Tactician', 'Rambler', 'Bone Rattler', 'Barbaric Serpent', 'Lofoten', 'Pumba', 'Soul Cairn', 'Revenge', 'Minas', 'Mull', 'Discourteous', 'Amity', 'Rovers', 'Grand', 'Frobisher', 'Colombo', 'Anna', 'Belmont', 'Happy Dog', 'Shark Rider', 'Poisoned Arrow', 'Portreath', 'Plague Storm', 'Hornpipe', 'Peterhead', 'Speedy Slug', 'Cotswold', 'Adventure Prize', 'Barcross', 'Revenge Tide', 'Conflagration', 'Little', 'Siskin', 'Flying', 'Ossington', 'Crimson', 'Bathurst', 'Madness', 'Red Tsunami', 'Ranger', 'Wager', 'Fairlight', 'Doom', 'Cheviot', 'Bedouin', 'Murderers', 'Penelope', 'Dagger', 'Cadmus', 'Privateer', 'Grenade', 'Fortune', 'White', 'Ocean Curse', 'North', 'Bann', 'Old TIde', 'Raider', 'Scourge', 'Death Fire', 'Montbretia', 'Stinkin Plank', 'Voyager', 'Coward', 'Loyal', 'Jewel', 'Consort', 'Haughty', 'Wild Storm', 'Hellish Captain', 'Hannam', 'Wind Raider', 'Norwich', 'Swashbucklers', 'Trepassy', 'Trinity', 'Pirate', 'Hydra', 'Palma', 'Impulsive', 'Greenwich', 'Dirty', 'Fort Erie', 'Fife', 'Trailer', 'Ruthless Raider', 'Polruan', 'Neptune', 'Narbada', 'Glory Iv', 'Howl', 'Pillager', 'Adventure Galley', 'Wolf', 'Fearful Slave', 'Angry', 'Ben Meidie', 'Diver', 'Guelderland', 'Strumpet', 'Camel', 'Conquerante', 'Veronica', 'Suffolk', 'Keith', 'Courser', 'Walker', 'Bury', 'Bath', 'Ypres', 'Ellinor', 'Broken Slave', 'Raider', 'Jason', 'Murderous', 'Awake', 'Arab', 'Heron', 'Damnation', 'Sylph', 'Fearful Diamond', 'Rising Ghost', 'Unruly', 'Bear', 'Gold', 'Fortune', 'Glenelg', 'Kilham', 'Damned Night', 'Damned', 'Aeolus', 'Foam', 'Jewel of Atlantis', 'Echuca', 'Hespeler', 'Tavy', 'Disrespectful', 'Dark Soul', 'Vile', 'Dreaming Wave', 'Lisburne', 'Albrighton', 'Rusty Cannon', 'Mystic Sea', 'Moon Whisperer', 'Maryborough', 'Golden Mermaid', 'Mangy', 'Swordfish', 'Minnow', 'Galley', 'Old Scallywag', 'Treasure', 'Janus', 'England', 'Cacophonous', 'Bahamas', 'Snapdragon', 'Soggy Seaweed', 'Manchester', 'Blasted', 'Buccaneers', 'Dragon', 'Kilmuckridge', 'Pelican Prize', 'Bruizer', 'Fierce', 'Clitheroe Castle', 'Calendula', 'Squid Blaster', 'Wicked Folly', 'Leeds Castle', 'Plunder', 'Killers', 'Embleton', 'Happy Sailor', 'Port Mahon', 'Attacker', 'Durweston', 'Dragons', 'Adventure', 'Rift', 'Storm', 'Pillager', 'Paris', 'Drake', 'Delight', 'Pagham', 'Lust', 'Night of Doom', 'Squid', 'Malabar', 'Clumsy Sailor', 'Tuna', 'Old James', 'Falcon', 'Excellent', 'Anger', 'Cowra', 'Moorhen', 'Cutlass', 'Uppingham', 'Boreas', 'Truro', 'Damned', 'Black Posthorse', 'Galatea', 'Privateers', 'Dark Howler', 'Carnation', 'Cape Scott', 'Birmingham', 'Arundel', 'Upward', 'Stinkin Skull', 'Rockwood', 'Carrick', 'Howl', 'Grand Serpent', 'Desiree', 'Royal Pearl', 'Cursed Slave', 'Orwell', 'Most', 'Dead-Man’s Raft', 'Curse', 'Burning', 'Doubloon', 'Cuckmere', 'Burning Dragon', 'Blind', 'Cordelia', 'Shallow Mermaid', 'Cerberus', 'Jenny', 'Elusive', 'Cutter', 'Raglan', 'Savage', 'Oribi', 'Littleham', 'Alisma', 'Vivien', 'Fall', 'Davy Jones', 'Cameronia', 'Alacrity', 'Portia', 'Filthy', 'Mingan', 'Infanta', 'Dervish', 'Earl of Chatham', 'Secret', 'Hades', 'Tattoo', 'Laleston', 'Salamander', 'Clinton', 'King', 'Parker', 'Dorothea', 'Abergavenny', 'Dagger', 'Bloody Hangman', 'Shiverin’ Dragon', 'Peterman', 'Barbaric', 'Brevdrageren', 'Lost King', 'Hind', 'Pretty Coral', 'Odin', 'Pyrrhus', 'Scurvy', 'Transit', 'Sea', 'Cursed Hangman', 'Secret Dagger', 'Crown Malago', 'Heliotrope', 'Jolly Storm', 'Parret', 'Slave', 'Shadow', 'Seas', 'Balfour', 'Culloden', 'Ghost', 'Fiona', 'Black Pearl', 'Neptune’s Wave', 'Derrington', 'Lark', 'Rupert', 'Grenado', 'Dead Bones', 'Seas', 'Atlantis', 'Golden Cairn', 'Hangman', 'Tortuga', 'Hell-born', 'Bone Heart', 'Tainted Rose', 'Bellona', 'Kilby', 'Post', 'Pearl', 'Sheldrake', 'Vengeance', 'Eskimo', 'Celerity', 'Quadrille', 'Demon Sea-Dog', 'Drunken', 'Genoa', 'Bigbury Bay', 'Horror', 'Rusty Bell', 'Corsair', 'Norfolk', 'Amarylis', 'White Night', 'Knave', 'Bayfield', 'Lochinvar', 'Ortenzia', 'Poseidon’s Revenge', 'Bisham', 'Grief', 'Convulsion', 'Gift', 'Minoru', 'Eel', 'Cry', 'Eurus', 'Dainty', 'Ildefonso', 'Stone Angel', 'Chevron', 'Homicidal', 'Morris', 'Drunken James', 'Lost Screams of Peter', 'Lost Dreams', 'Manly', 'Hangman’s Hollow', 'Abandoned Barnacle', 'Tracker', 'Rude', 'Moon Raider', 'Death', 'Alfreda'],
        "caltronShipPrefixes": ['', '0x', '', '0b', '', '', '', '&', '', '*', '-', '', '', '', '', '', ''],
        "caltronShipInfixes": ['F', '_', 'B', 'V', 'L', 'add', 'nop', 'C', 'O', 'Y', 'M', 'mov', 'G', 'Z', 'U', '=>', 'mov', '_', 'Q', 'I', 'T', 'mul', '0', 'Y', '0', 'K', '5', 'H', 'P', 'I', 'X', 'S', 'fizz', 'H', 'P', '2', '6', 'N', 'R', 'buzz', '-', 'A', '-', 'D', '4', 'V', 'Z', '_', 'nop', '-', 'A', 'U', 'D', 'T', 'S', 'R', '4', '=>', 'O', 'N', '_', '1', 'J', '3', 'bar', 'J', '1', 'foo', '=>', '-', '_', 'L', '_', 'E', 'E', 'G', '-', 'C', 'X', '->', 'B', 'M', 'F', 'Q', '-'],
        "caltronShipSuffixes": ['', '++', '', '', '', '', '--', '', '()', '', ';', '[:]', '', '', '', ],
        "waves": [
            {
                "atDistance": 90000,  # Distance between Iron Sun and Terra noua at which the wave "triggers"
                "nameList": "TSN",    # This simply defines from which name list to name the new ships
                "x": 4000,            # X,Y,Z positions of the newly spawned fleet. Alternatively, provide "spawnAt" (see usage below).
                "y": "0.0",
                "z": midRightZ,
                "hulls": [1, 1, 2],   # List of hull types to spawn. NOTE there are limits: max 3 TSN, max 4 Caltron, max 7 Hegemony/Pirate hulls per wave.
                "sideValue": 2,       # 2 - friendly; 1 - enemy.
            },
            {
                "hail": "Hello again, meatbags. Behold, our ultimate weapon, the Iron Sun!",
                "atDistance": 89900,
                "nameList": "Caltron",
                "spawnAt": "Iron Sun",
                "hulls": [7206, 7204, 7201],
                "sideValue": 1,
            },
            {
                "atDistance": 89800,
                "nameList": "Caltron",
                "x": midbotRightX,
                "y": "0.0",
                "z": midbotRightZ,
                "hulls": [7201, 7203],
                "sideValue": 1,
            },
            {
                "atDistance": 89700,
                "nameList": "Caltron",
                "x": midtopRightX,
                "y": "0.0",
                "z": midtopRightZ,
                "hulls": [7201, 7202, 7202],
                "sideValue": 1,
            },

            {
                "hail": "Let's invite some of your old friends, the Kraliens, to the party.",
                "atDistance": 75300,
                "nameList": "Hegemony",
                "x": topLeftX,
                "y": "0.0",
                "z": topLeftZ,
                "overrideName": "Antenna A", # Override automatic naming of ships so that we can add custom behaviour to this ship.
                "hulls": [1353],
                "sideValue": 1,
            },
            {
                "atDistance": 75200,
                "nameList": "Hegemony",
                "spawnAt": "Antenna A",
                "hulls": [2000, 2000, 2001, 2001, 2002, 2100],
                "sideValue": 1,
            },
            {
                "atDistance": 75100,
                "nameList": "Hegemony",
                "spawnAt": "Antenna A",
                "hulls": [2000, 2000, 2001, 2001, 2002, 2100],
                "sideValue": 1,
            },

            {
                "hail": "The Ximni are here too.",
                "atDistance": 67200,
                "nameList": "Hegemony",
                "x": midtopRightX,
                "y": "0.0",
                "z": midtopRightZ,
                "hulls": [7504, 7502],
                "sideValue": 1,
            },
            {
                "atDistance": 67100,
                "nameList": "Hegemony",
                "x": midbotRightX,
                "y": "0.0",
                "z": midbotRightZ,
                "hulls": [7506, 7502],
                "sideValue": 1,
            },

            {
                "hail": "Looks like the Kraliens called for help of their Hegemony allies.",
                "atDistance": 50300,
                "nameList": "Hegemony",
                "x": botLeftX,
                "y": "0.0",
                "z": botLeftZ,
                "overrideName": "Antenna B",
                "hulls": [1353],
                "sideValue": 1,
            },
            {
                "atDistance": 50200,
                "nameList": "Hegemony",
                "spawnAt": "Antenna B",
                "hulls": [3002, 3002, 3100],
                "sideValue": 1,
            },
            {
                "atDistance": 50100,
                "nameList": "Hegemony",
                "spawnAt": "Antenna B",
                "hulls": [3001, 3001, 3001],
                "sideValue": 1,
            },

            {
                "hail": "Im enjoying this.",
                "atDistance": 40200,
                "nameList": "Hegemony",
                "x": topLeftX,
                "y": "0.0",
                "z": topLeftZ,
                "hulls": [5000, 5002],
                "sideValue": 1,
            },
            {
                "atDistance": 40100,
                "nameList": "Hegemony",
                "x": botLeftX,
                "y": "0.0",
                "z": botLeftZ,
                "hulls": [5001, 5000],
                "sideValue": 1,
            },

            {
                "hail": "We didn't invite Torgoths, but they must have scented your blood!",
                "atDistance": 30200,
                "nameList": "Hegemony",
                "x": botRightX,
                "y": "0.0",
                "z": botRightZ,
                "overrideName": "Antenna C",
                "hulls": [1353],
                "sideValue": 1,
            },
            {
                "atDistance": 30100,
                "nameList": "Hegemony",
                "spawnAt": "Antenna C",
                "hulls": [4002, 4100],
                "sideValue": 1,
            },

            {
                "hail": "Can you feel the end?",
                "atDistance": 20200,
                "nameList": "Hegemony",
                "x": topLeftX,
                "y": "0.0",
                "z": topLeftZ,
                "hulls": [5000, 5000, 5000],
                "sideValue": 1,
            },
            {
                "atDistance": 20100,
                "nameList": "Hegemony",
                "x": botLeftX,
                "y": "0.0",
                "z": botLeftZ,
                "hulls": [5001, 5002],
                "sideValue": 1,
            },
        ],
        "spawners": {
            "Antenna A": {
                "commsFromHQ": "We're reading Kralien slingshot jump signatures!",
                "every": 60*4,                              # Hulls will be spawned every this amount of seconds
                "nameList": "Hegemony",                     # See 'waves'
                "hulls": [2000, 2000, 2001, 2002, 2100],    # See 'waves'
                "sideValue": 1,                             # see 'waves'
            },
            "Antenna B": {
                "commsFromHQ": "Incoming jump signatures, Arvonian configuration!",
                "every": 60*4,
                "nameList": "Hegemony",
                "hulls": [3001, 3001, 3002],
                "sideValue": 1,
            },
            "Antenna C": {
                "commsFromHQ": "Torgoth fleet just entered the system!",
                "every": 60*4,
                "nameList": "Hegemony",
                "hulls": [4000, 4000, 4001],
                "sideValue": 1,
            },
            "Asteroid Base": {
                "commsFromHQ": "We're reading a pirate raiding party on long range scanners!",
                "every": 60*4,
                "nameList": "Hegemony",
                "hulls": [7300, 7300, 7301],
                "sideValue": 1,
            },
            "Iron Sun": {
                "commsFromHQ": "Seismic activity on the Iron Star... More Caltrons!",
                "every": 60*5,
                "nameList": "Caltron",
                "hulls": [7201, 7202, 7201, 7205],
                "sideValue": 1,
            }
        }
    }


    with open(OUT_FNAME, 'w') as f:
        f.write(template_env.get_template(TMPL_FNAME).render(context))

def main():
    render()

if __name__ == "__main__":
    main()
