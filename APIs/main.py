import requests

# Links to other APIs:
    # https://rapidapi.com/collection/list-of-free-apis
    # htps://github.com/public-apis/public-apis 

term_to_search = input("Enter a term to search the Urban Dictionary for:\n")
url = "https://unofficialurbandictionaryapi.com/api/search"

parameters = {"term":f"{term_to_search}"}

r = requests.get(url, params=parameters)
definitions_array = r.json()["data"]

for definition in definitions_array:
    print(definition["meaning"])
    print("===============================")