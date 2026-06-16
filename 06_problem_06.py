# Create a list of 8 city names
cities = ["Delhi", "Mumbai", "Bhopal", "Indore",
          "Pune", "Jaipur", "Chennai", "Kolkata"]

# Print first 4 cities
print("First 4 cities:", cities[:4])

# Print last 4 cities
print("Last 4 cities:", cities[-4:])

# Add a new city at the end
cities.append("Hyderabad")
print("After adding a city:", cities)

# Remove the first city
cities.pop(0)
print("After removing first city:", cities)

# Convert list to tuple and print
cities_tuple = tuple(cities)
print("Tuple:", cities_tuple)