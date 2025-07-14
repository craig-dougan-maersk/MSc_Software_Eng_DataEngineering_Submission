import pandas as pd
#'''Import tld to country mapping export
#   From: https://gist.github.com/derlin/421d2bb55018a1538271227ff6b1299d'''

#'''https://gist.github.com/stevewithington/20a69c0b6d2ff846ea5d35e5fc47f26c'''
#country_and_code_df = pd.read_csv("https://gist.githubusercontent.com/stevewithington/20a69c0b6d2ff846ea5d35e5fc47f26c/raw/13716ceb2f22b5643ce5e7039643c86a0e0c6da6/country-and-continent-codes-list-csv.csv")
#print(country_and_code_df.head())

#tld_df = pd.read_csv("https://gist.githubusercontent.com/derlin/421d2bb55018a1538271227ff6b1299d/raw/3a131d47ca322a1d001f1f79333d924672194f36/country-codes-tlds.csv",skipinitialspace=True)

#print(tld_df.sample(10))

#tld_df.rename(columns={'country':'Country_Name'}, inplace=True)
#print(tld_df.head())
#combined_df = pd.merge(country_and_code_df, tld_df, how='left', on='Country_Name')
#print(f"tld   :{combined_df[combined_df['tld'].notna()].shape[0]}")
#print(f"no tld: {combined_df[combined_df['tld'].isna()]['Country_Name']}")
#print(f"total tld : {tld_df.shape[0]}")

cloud_regions = dict()

cloud_regions['gcp'] = pd.read_csv('https://raw.githubusercontent.com/dgl/cloud-regions/refs/heads/main/gcp/data.csv')
cloud_regions['azure'] = pd.read_csv('https://raw.githubusercontent.com/dgl/cloud-regions/refs/heads/main/azure/data.csv')
cloud_regions['aws'] = pd.read_csv('https://raw.githubusercontent.com/dgl/cloud-regions/refs/heads/main/aws/data.csv')

regions = [
    'US',
    'Asia',
    'Europe',
    'Africa',
    'Canada',
    'South America',
    'Middle East',
    'North America',
    'APAC',


]
for region in regions:
    cloud_regions['azure'].loc[cloud_regions['azure']['location_name'].str.contains(region, case=True, na=False),'global_region'] = region


cloud_regions['azure'].to_csv('azure_regions.csv')


our_world_df = pd.read_csv("https://ourworldindata.org/grapher/continents-according-to-our-world-in-data.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})
#print(our_world_df.head())

'''Data sources: Ember (2025)Energy Institute - Statistical Review of World Energy (2024) – with major processing by Our World in Data'''
# Fetch the data.
ember_carbon_intensity_df = pd.read_csv("https://ourworldindata.org/grapher/carbon-intensity-electricity.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

print(ember_carbon_intensity_df.sample(20))
