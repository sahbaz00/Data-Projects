import pandas as pd
import geonamescache


data = {'Country': ['United States', 'Canada', 'Brazil', 'France', 'India']}
df = pd.DataFrame(data)

gc = geonamescache.GeonamesCache()
country_to_continent = {}

for country_code, country_info in gc.get_countries().items():
    country_name = country_info['name']
    continent = country_info['continentcode']
    country_to_continent[country_name] = continent

df['Continent'] = df['Country'].map(country_to_continent)