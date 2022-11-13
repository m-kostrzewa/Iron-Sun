#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader("."))
TMPL_FNAME = "MISS_TSN-IronSun.xml.tmpl"
OUT_FNAME = "MISS_TSN-IronSun.xml"

def render():
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
        },
        "tsnShipNames": ['Speedwell', 'Adventure Prize', 'Icarus', 'Coureuse', 'Truro', 'Marlingford', 'Daisy', 'Utmost', 'Karrakatta', 'Clarkia', 'Prosperity', 'Careful', 'Bamborough Castle', 'Carcass', 'Active', 'Vulture', 'Asturias', 'Fleche', 'Naseby', 'Burford', 'Cowichan', 'Adda', 'Vanoc', 'Valentine', 'Smilax', 'Bullhead', 'Belle Isle', 'Centaur', 'Pelargonium', 'Bahamas', 'Harman', 'Slothany', 'Alnwick Castle', 'Eastbourne', 'Urania', 'Grampus', 'Margett', 'Abraham', 'Toreador', 'Driver', 'Garland', 'Begum', 'Bream', 'Chambly', 'Dalrymple', 'Poole', 'Wahine', 'Georgeham', 'Garlies', 'Algiers', 'Andromache', 'Siskin', 'Mooltan', 'Goole', 'Coronation', 'Jaseur', 'Argon', 'Beehive', 'Dawlish', 'Bat', 'Linnet', 'Gadfly', 'Gold Coast', 'Comus', 'Abeille', 'Thyme', 'Emersham', 'Fredericton', 'Pearl Prize', 'Wyandra', 'Fairfield', 'Cheltenham', 'Bountiful', 'Emily', 'Perim', 'Thakeham', 'Slinger', 'Merry Hampton', 'Poppy', 'Spiraea', 'Ultor', 'Brantingham', 'Haerlem', 'Rosebay', 'Alyssum', 'Embleton', 'Ambuscade', 'Cowslip', 'Chequers', 'Infanta', 'Duckworth', 'Keren', 'Zenith', 'Glenroy', 'Bramble', 'Duddon', 'Acteon', 'Sharpshooter', 'Lewiston', 'Llandudno', 'Cyrene', 'Caicos', 'Meon', 'Mimico', 'Niement', 'Granby', 'Hoverfly', 'Honesty', 'Hunter', 'Glenelg', 'Nilam', 'Spark', 'Explorer', 'Lord Warden', 'Aveley', 'Indignant', 'Venerable', 'Ildefonso', 'Nimble', 'Cape Breton', 'Pouncer', 'Penlee Point', 'Launceston', 'Octavia', 'Chatham Double', 'Hubberston', 'Dubford', 'Postillion', 'Moro', 'Riviera', 'Yarnton', 'Obdurate', 'Penelope', 'Alphea', 'Moy', 'Fiji', 'Rye', 'Monkshood', 'Blean', 'Aquilon', 'Briton', 'Shoreham', 'Gaillarda', 'Afridi', 'Albuera', 'Caroline', 'Nith', 'Grana', 'Newfoundland', 'Censeur', 'Elven', 'Orquijo', 'Orby', 'Duchess of Norfolk', 'Torbay', 'Trent', 'Prompt', 'Poulmic', 'Cornwallis', 'Inscrutable', 'Vanguard', 'Ithuriel', 'Royalist', 'Blakeney', 'Grayfly', 'Lalmourn', 'Aphrodite', 'Eggesford', 'Lancaster', 'Endeavour', 'Artful', 'Seabear', 'Safety', 'Racehorse', 'Premier', 'Advantagia', 'Islip', 'Licorne', 'Burlington', 'Arundel', 'Pigot', 'Bombay', 'Jackton', 'Torch', 'Bloodhound', 'Dartmoor', 'Alerte', 'Duchess', 'Arromanches', 'Kaniere', 'Voyager', 'Flying Fox', 'Abigail', 'Dorsetshire', 'Pyramus', 'Beaulieu', 'Banterer', 'Modbury', 'Iris', 'Invermoriston', 'Engageante', 'Wasp', 'Ocean', 'Milfoil', 'Bellwort', 'Furieuse', 'Victorious', 'Abyssinia', 'Juste', 'Skylark', 'Maxton', 'Phosphorus', 'Iphigenia', 'Fox', 'Halsham', 'Mandate', 'Industry', 'Dacres', 'Fireball', 'Onondaga', 'Catherine', 'Camel', 'Alcestis', 'Grindall', 'Transfer', 'Tigress', 'Pesaquid', 'Sladen', 'Alpheus', 'Delight', 'Chediston', 'Paramour', 'Clinton', 'Arrow', 'Vengeance', 'Capelin', 'Quilliam', 'Kilbrittain', 'Itchen', 'Havant', 'Fountain', 'Glaisdale', 'Middlesbrough', 'Holcombe', 'Stevenstone', 'Kilcornie', 'Humber', 'Deane', 'Yarra', 'Aylmer', 'Conrad', 'Sluys', 'Battle', 'Wolverine', 'Moselle', 'Seraph', 'Kilbrachan', 'Crown Prize', 'Oudenarde', 'Owen Sound', 'Nelson', 'Tasman', 'Harland', 'Hannibal', 'Umpire', 'Glenarm', 'Oakham Castle', 'Regulus', 'Adventure', 'Drogheda', 'Conflagration', 'Hambledon', 'Conquestador', 'Basilisk', 'Epsom', 'Lockeport', 'Rhododendron', 'Armada', 'Theseus', 'Amboyna', 'Oshawa', 'Melville', 'Horseman', 'Fastnet', 'Georgetown', 'Bombay Castle', 'Dannemark', 'Spey', 'Glorieux', 'Chilton', 'Firme', 'Argus', 'Paluma', 'Norwich Castle', 'Carrick', 'Ant', 'Pirie', 'Biddeford', 'Ferret', 'Clown', 'Tresham', 'Haughty', 'Finwhale', 'Darsham', 'Robust', 'Piemontaise', 'Peacock', 'Botha', 'Legion', 'Bull'],
    }

    with open(OUT_FNAME, 'w') as f:
        f.write(template_env.get_template(TMPL_FNAME).render(context))

def main():
    render()

if __name__ == "__main__":
    main()
