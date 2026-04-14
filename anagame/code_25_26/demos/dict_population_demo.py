# Dictionaries use a key-value lookup pairing
# Here, we have cities (strings) as keys, and their populations (int) as value
city_populations = {
    'New York': 8_336_817,
    'Los Angeles': 3_979_576,
    'Chicago': 2_693_976,
    'Houston': 2_320_268,
    'Phoenix': 1_680_992,
    'Philadelphia': 1_584_064,
    'San Antonio': 1_547_253,
    'San Diego': 1_423_851,
    'Dallas': 1_343_573,
    'San Jose': 1_021_795
}

print(city_populations['Chicago'])  # 2693976
print("Cities:", list(city_populations.keys()))
print("Populations", list(city_populations.values()))

# Loop over dictionary (keys are iterated)
for city in city_populations:
    print(city, city_populations[city])

# Adding a new entry
city_populations['Austin'] = 964_254
print(city_populations['Austin'])

# Removing an entry
city_populations.pop('Austin')

# Updating an existing value
city_populations['New York'] = 8_000_000
print(city_populations['New York'])

# Incrementing a value
city_populations['New York'] += 500
print(city_populations['New York'])
