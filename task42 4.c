cities = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

city_name = input("Enter a city name: ")

for country, city_list in cities.items():
    if city_name in city_list:
        print(f"{city_name} is in {country}")
        break
else:
    print("City not found in the database")
