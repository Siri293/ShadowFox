cities = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

same_country = False

for country, city_list in cities.items():
    if city1 in city_list and city2 in city_list:
        print(f"Both cities are in {country}")
        same_country = True
        break

if not same_country:
    print("They don't belong to the same country")
