def display_cities(first, second):
    """
    displays the two cities on a single line.
    """
    print(f"{first} -> {second}")

cities = ["Mexico City", "Phoenix, AZ", "Newport, CA"]
cities.append("Paris, France")
cities.append("Tokyo, Japan")


#for i in range(len(cities)):
    #print(f"{i + 1}. {cities[i]}")


#print(f"{cities[0]} -> {cities[1]}")       

display_cities(cities[0], cities[1])
display_cities(cities[1], cities[2])