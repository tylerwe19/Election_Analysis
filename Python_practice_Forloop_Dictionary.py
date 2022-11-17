counties_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county,voters in counties_dict.items():
    print(f"{county} + county has {voters:,} registered voters.")

voting_data = [{'county':'Arapahoe','registered voters': 422829},
                    {'county':'Denver','registered voters':463353},
                    {'county':'Jefferson','registered voters':432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered voters']:,} registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
