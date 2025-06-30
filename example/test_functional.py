import os
import json
from client import Game, check_has
import random

def test_1():
    username = str(random.randint(10000, 99999))
    game = Game(username)
    os.path.exists(f"./{username}.json")
    print("fichier du profil correctement créé")
    with open(f"./{username}.json", "r") as f:
        data = json.load(f)
    player_id = data["playerId"]
    profile = game.get(f"/player/{player_id}")
    print(f"argent de départ: {profile['money']}")
    sta = list(profile["stations"].keys())[0]
    game.buy_first_ship(sta)
    profile = game.get(f"/player/{player_id}")
    if len(profile["ships"]) > 0:
        print("Achat de vaisseau réussi")
    else:
        print("Échec: aucun vaisseau trouvé")
    profile = game.get(f"/player/{player_id}")
    print(f"Argent après achat du vaisseau: {profile['money']}")
    print("Transaction réussi et argent diminué")
    ship_id = profile["ships"][0]["id"]
    game.buy_first_mining_module("Miner", sta, ship_id)
    ship = game.get(f"/ship/{ship_id}")
    print("Achat du miner réussi")
    profile = game.get(f"/player/{player_id}")
    print(f"Argent après achat du miner: {profile['money']}")
    print("Transaction réussi et argent diminué")

def test_travel():
    username = str(random.randint(10000, 99999))
    if os.path.exists(f"./{username}.json"):
        os.remove(f"./{username}.json")
    game = Game(username)
    with open(f"./{username}.json", "r") as f:
        data = json.load(f)
    player_id = data["playerId"]
    profile = game.get(f"/player/{player_id}")
    sta = list(profile["stations"].keys())[0]
    game.buy_first_ship(sta)
    profile = game.get(f"/player/{player_id}")
    ship_id = profile["ships"][0]["id"]
    ship = game.get(f"/ship/{ship_id}")
    if not check_has(ship["crew"], "member_type", "Pilot"):
        game.hire_first_pilot(sta, ship_id)
    ship = game.get(f"/ship/{ship_id}")
    old_pos = ship["position"]
    new_pos = [old_pos[0] + 1, old_pos[1], old_pos[2]]
    game.travel(ship_id, new_pos)
    ship = game.get(f"/ship/{ship_id}")
    assert ship["position"] == new_pos
    print("Test travel avec pilote OK")



if __name__ == "__main__":
    test_1()
    print("=== Test 1 OK ===")
    test_travel()
    print("=== Test 2 OK ===")
