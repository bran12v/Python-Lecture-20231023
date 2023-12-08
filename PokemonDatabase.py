
import requests

def get_pokemon_type(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(url, headers={"Accept": "application/json"})
    # print(response.json())
    for i in response.json()["types"]:
        print(i["type"]["name"])
    # return response.json()["types"] # This wasnt working previously but since I changed the headers, now it works

def main():
    # get_pokemon_type("gengar")
    while True:
        option = input("Would you like to look up a Pokemon's Type? (y or n) ")
        if option == "y":
            name = input("What is the name of the Pokemon? (lowercase) ")
            get_pokemon_type(name)
        elif option == "n": 
            print("Woe, okay, I guess you hate fun or something")
            break
        else:
            print("Try again buddy")
            continue

if __name__ == "__main__":
    main()