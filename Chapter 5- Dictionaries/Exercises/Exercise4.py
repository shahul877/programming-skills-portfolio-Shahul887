rivers = {
    'Nile': 'Egypt',
    'Yangtze River': 'China',
    'Mississippi River': 'United States',
    }

for river, country in rivers.items():
    print(f"The {river} flows through {country}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country}")
