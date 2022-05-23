import requests

# bearer = token from api twitter
# query = words to search
# max = max values to return #min value 10
def twitter_data(bearer,query,max):
    response = requests.get(f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results={max}&expansions=author_id,geo.place_id&place.fields=country,country_code,geo&user.fields=location",
                headers={
        "Accept": "application/json",
        "Authorization": bearer
    })

    return response.json()