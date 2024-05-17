import requests

url = "https://rawg-video-games-database.p.rapidapi.com/developers"

headers = {
	"X-RapidAPI-Key": "bb67c86bd3msh808468a8d4efcf3p1f309cjsndd3ff113e560",
	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())