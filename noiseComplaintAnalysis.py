import kaggle as kg
import numpy as np
import matplotlib.pyplot as plt

kg.api.authenticate()
kg.api.dataset_download_files(dataset='somesnm/partynyc', path='.', unzip=True, force=False)
kg.api.dataset_download_files(dataset='muonneutrino/new-york-city-census-data', path='.', unzip=True, force=False)

partyDt = {'names': ('created', 'closed', 'locType', 'zip', 'city', 'borough', 'lat', 'long'),
           'formats': ('U25', 'U25', 'U25', np.int, 'U25', 'U25', np.float, np.float)}

partyFile = "party_in_nyc.csv"
partyData = np.genfromtxt(partyFile, delimiter=',', dtype=partyDt, skip_header=1)

censusDt = {'names': ('cenTract', 'county', 'borough', 'totalPop', 'men', 'women', 'hispanic', 'white', 'black',
                      'native', 'asian', 'citizen', 'income', 'incomeErr', 'incomePerCap', 'incomePerCapErr', 'poverty',
                      'childPoverty', 'professional', 'service'),
            'formats': ('U20', 'U20', 'U20', np.int32, np.int32, np.int32, np.double, np.double, np.double, np.double,
                        np.double, np.int, np.double, np.double, np.double, np.double, np.double, np.double, np.double,
                        np.double)}

finalDt = {'names': ('borough', 'totalPop', 'men', 'women', 'hispanic', 'white', 'black', 'native', 'asian', 'citizen',
                     'income', 'incomePerCap', 'poverty', 'childPoverty', 'professional', 'service'),
           'formats': ('U20', np.int32, np.int32, np.int32, np.double, np.double, np.double, np.double, np.double,
                       np.int, np.double, np.double, np.double, np.double, np.double, np.double)}

censusFile = "nyc_census_tracts.csv"
censusData = np.genfromtxt(censusFile, delimiter=',', dtype=censusDt, skip_header=1)
# Removes empty data
mask = (np.isnan(censusData['hispanic']))
mask = (np.isnan(censusData['white']))
mask = (np.isnan(censusData['black']))
mask = (np.isnan(censusData['native']))
mask = (np.isnan(censusData['asian']))
mask = (np.isnan(censusData['income']))
mask = (np.isnan(censusData['incomeErr']))
mask = (np.isnan(censusData['incomePerCap']))
mask = (np.isnan(censusData['incomePerCapErr']))
mask = (np.isnan(censusData['poverty']))
mask = (np.isnan(censusData['childPoverty']))
mask = (np.isnan(censusData['professional']))
mask = (np.isnan(censusData['service']))
censusData = censusData[~mask]

# converts percentages to numbers to find percentages after data is combined
censusData['hispanic'] = (censusData['hispanic'] * censusData['totalPop'] / 100)
censusData['white'] *= censusData['totalPop'] / 100
censusData['black'] *= censusData['totalPop'] / 100
censusData['native'] *= censusData['totalPop'] / 100
censusData['asian'] *= censusData['totalPop'] / 100
censusData['poverty'] *= censusData['totalPop'] / 100
censusData['childPoverty'] *= censusData['totalPop'] / 100
censusData['professional'] *= censusData['totalPop'] / 100
censusData['service'] *= censusData['totalPop'] / 100

# removes rows with unpecified boroughs
partyData = partyData[partyData['borough'] != 'Unspecified']
censusData['borough'] = np.char.upper(censusData['borough'])

# borough names: ['BRONX' 'BROOKLYN' 'MANHATTAN' 'QUEENS' 'STATEN ISLAND']
bronx = censusData[censusData['borough'] == 'BRONX']
brooklyn = censusData[censusData['borough'] == 'BROOKLYN']
manhattan = censusData[censusData['borough'] == 'MANHATTAN']
queens = censusData[censusData['borough'] == 'QUEENS']
statenIsland = censusData[censusData['borough'] == 'STATEN ISLAND']

# grabs total pops of each borough
bronxTotalPop = np.sum(bronx['totalPop'])
brooklynTotalPop = np.sum(brooklyn['totalPop'])
manhattanTotalPop = np.sum(manhattan['totalPop'])
queensTotalPop = np.sum(queens['totalPop'])
statenIslandTotalPop = np.sum(statenIsland['totalPop'])

# number of men and women from each borough
# Men
bronxMen = np.sum(bronx['men'])
brooklynMen = np.sum(brooklyn['men'])
manhattanMen = np.sum(manhattan['men'])
queensMen = np.sum(queens['men'])
statenIslandMen = np.sum(statenIsland['men'])
# Women
bronxWomen = np.sum(bronx['women'])
brooklynWomen = np.sum(brooklyn['women'])
manhattanWomen = np.sum(manhattan['women'])
queensWomen = np.sum(queens['women'])
statenIslandWomen = np.sum(statenIsland['women'])

# race numbers
# Hispanic
bronxHispanic = np.sum(bronx['hispanic'])
brooklynHispanic = np.sum(brooklyn['hispanic'])
manhattanHispanic = np.sum(manhattan['hispanic'])
queensHispanic = np.sum(queens['hispanic'])
statenIslandHispanic = np.sum(statenIsland['hispanic'])

# White
bronxWhite = np.sum(bronx['white'])
brooklynWhite = np.sum(brooklyn['white'])
manhattanWhite = np.sum(manhattan['white'])
queensWhite = np.sum(queens['white'])
statenIslandWhite = np.sum(statenIsland['white'])

# Black
bronxBlack = np.sum(bronx['black'])
brooklynBlack = np.sum(brooklyn['black'])
manhattanBlack = np.sum(manhattan['black'])
queensBlack = np.sum(queens['black'])
statenIslandBlack = np.sum(statenIsland['black'])

# Native
bronxNative = np.sum(bronx['native'])
brooklynNative = np.sum(brooklyn['native'])
manhattanNative = np.sum(manhattan['native'])
queensNative = np.sum(queens['native'])
statenIslandNative = np.sum(statenIsland['native'])

# Asian
bronxwAsian = np.sum(bronx['asian'])
brooklynAsian = np.sum(brooklyn['asian'])
manhattanAsian = np.sum(manhattan['asian'])
queensAsian = np.sum(queens['asian'])
statenIslandAsian = np.sum(statenIsland['asian'])

# number of Citizens
bronxTotalCit = np.sum(bronx['citizen'])
brooklynTotalCit = np.sum(brooklyn['citizen'])
manhattanTotalCit = np.sum(manhattan['citizen'])
queensTotalCit = np.sum(queens['citizen'])
statenIslandTotalCit = np.sum(statenIsland['citizen'])

# Avg median household income
bronxAvgIncome = np.mean(bronx['income'])
brooklynAvgIncome = np.mean(brooklyn['income'])
manhattanAvgIncome = np.mean(manhattan['income'])
queensAvgIncome = np.mean(queens['income'])
statenIslandAvgIncome = np.mean(statenIsland['income'])

# AvgIncomePerCap
bronxAvgIncomePerCap = np.mean(bronx['incomePerCap'])
brooklynAvgIncomePerCap = np.mean(brooklyn['incomePerCap'])
manhattanAvgIncomePerCap = np.mean(manhattan['incomePerCap'])
queensAvgIncomePerCap = np.mean(queens['incomePerCap'])
statenIslandAvgIncomePerCap = np.mean(statenIsland['incomePerCap'])

# poverty
bronxAvgBelowPov = np.sum(bronx['poverty'])
brooklynAvgBelowPov = np.sum(brooklyn['poverty'])
manhattanAvgBelowPov = np.sum(manhattan['poverty'])
queensAvgBelowPov = np.sum(queens['poverty'])
statenIslandAvgBelowPov = np.sum(statenIsland['poverty'])

# child poverty
bronxAvgBelowChildPov = np.sum(bronx['childPoverty'])
brooklynAvgBelowChildPov = np.sum(brooklyn['childPoverty'])
manhattanAvgBelowChildPov = np.sum(manhattan['childPoverty'])
queensAvgBelowChildPov = np.sum(queens['childPoverty'])
statenIslandAvgBelowChildPov = np.sum(statenIsland['childPoverty'])

# proffesional
bronxProff = np.sum(bronx['professional'])
brooklynProff = np.sum(brooklyn['professional'])
manhattanProff = np.sum(manhattan['professional'])
queensProff = np.sum(queens['professional'])
statenIslandProff = np.sum(statenIsland['professional'])

# service
bronxServ = np.sum(bronx['service'])
brooklynServ = np.sum(brooklyn['service'])
manhattanServ = np.sum(manhattan['service'])
queensServ = np.sum(queens['service'])
statenIslandServ = np.sum(statenIsland['service'])

# combines bronx data
bronxFinal = np.array([("Bronx", bronxTotalPop, bronxMen, bronxWomen, np.round(bronxHispanic / bronxTotalPop * 100, 2),
                        np.round(bronxWhite / bronxTotalPop * 100, 2), np.round(bronxBlack / bronxTotalPop * 100, 2),
                        np.round(bronxNative / bronxTotalPop * 100, 2), np.round(bronxwAsian / bronxTotalPop * 100, 2),
                        bronxTotalCit, np.round(bronxAvgIncome, 2), np.round(bronxAvgIncomePerCap, 2),
                        np.round(bronxAvgBelowPov / bronxTotalPop * 100, 2),
                        np.round(bronxAvgBelowChildPov / bronxTotalPop * 100, 2),
                        np.round(bronxProff / bronxTotalPop * 100, 2),
                        np.round(bronxServ / bronxTotalPop * 100, 2))], dtype=finalDt)
# combines brooklyn data
brooklynFinal = np.array([("Brooklyn", brooklynTotalPop, brooklynMen, brooklynWomen,
                           np.round(brooklynHispanic / brooklynTotalPop * 100, 2),
                           np.round(brooklynWhite / brooklynTotalPop * 100, 2),
                           np.round(brooklynBlack / brooklynTotalPop * 100, 2),
                           np.round(brooklynNative / brooklynTotalPop * 100, 2),
                           np.round(brooklynAsian / brooklynTotalPop * 100, 2), brooklynTotalCit, brooklynAvgIncome,
                           brooklynAvgIncomePerCap, np.round(brooklynAvgBelowPov / brooklynTotalPop * 100, 2),
                           np.round(brooklynAvgBelowChildPov / brooklynTotalPop * 100, 2),
                           np.round(brooklynProff / brooklynTotalPop * 100, 2),
                           np.round(brooklynServ / brooklynTotalPop * 100, 2))], dtype=finalDt)
# combines manhattan data
manhattanFinal = np.array([("Manhattan", manhattanTotalPop, manhattanMen, manhattanWomen,
                            np.round(manhattanHispanic / manhattanTotalPop * 100, 2),
                            np.round(manhattanWhite / manhattanTotalPop * 100, 2),
                            np.round(manhattanBlack / manhattanTotalPop * 100, 2),
                            np.round(manhattanNative / manhattanTotalPop * 100, 2),
                            np.round(manhattanAsian / manhattanTotalPop * 100, 2), manhattanTotalCit,
                            np.round(manhattanAvgIncome, 2), np.round(manhattanAvgIncomePerCap, 2),
                            np.round(manhattanAvgBelowPov / manhattanTotalPop * 100, 2),
                            np.round(manhattanAvgBelowChildPov / manhattanTotalPop * 100, 2),
                            manhattanProff / manhattanTotalPop * 100, manhattanServ / manhattanTotalPop * 100)],
                          dtype=finalDt)
# combines queens data
queensFinal = np.array([("Queens", queensTotalPop, queensMen, queensWomen,
                         np.round(queensHispanic / queensTotalPop * 100, 2),
                         np.round(queensWhite / queensTotalPop * 100, 2),
                         np.round(queensBlack / queensTotalPop * 100, 2),
                         np.round(queensNative / queensTotalPop * 100, 2),
                         np.round(queensAsian / queensTotalPop * 100, 2), queensTotalCit, np.round(queensAvgIncome, 2),
                         np.round(queensAvgIncomePerCap, 2), np.round(queensAvgBelowPov / queensTotalPop * 100, 2),
                         np.round(queensAvgBelowChildPov / queensTotalPop * 100, 2),
                         np.round(queensProff / queensTotalPop * 100, 2),
                         np.round(queensServ / queensTotalPop * 100, 2))],
                       dtype=finalDt)
# combines statenIsland data
statenIslandFinal = np.array([("Staten Island", statenIslandTotalPop, statenIslandMen, statenIslandWomen,
                               np.round(statenIslandHispanic / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandWhite / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandBlack / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandNative / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandAsian / statenIslandTotalPop * 100, 2), statenIslandTotalCit,
                               np.round(statenIslandAvgIncome, 2), np.round(statenIslandAvgIncomePerCap, 2),
                               np.round(statenIslandAvgBelowPov / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandAvgBelowChildPov / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandProff / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandServ / statenIslandTotalPop * 100, 2))], dtype=finalDt)

# All unclosed calls
unclosedComplaints = partyData[(partyData['closed'] == '')]
bronxUnclosed = unclosedComplaints[unclosedComplaints['borough'] == 'BRONX']
brooklynUnclosed = unclosedComplaints[unclosedComplaints['borough'] == 'BROOKLYN']
manhattanUnclosed = unclosedComplaints[unclosedComplaints['borough'] == 'MANHATTAN']
queensUnclosed = unclosedComplaints[unclosedComplaints['borough'] == 'QUEENS']
statenIslandUnclosed = unclosedComplaints[unclosedComplaints['borough'] == 'STATEN ISLAND']

# Removes empty data
partyData = partyData[partyData['created'] != '']
partyData = partyData[partyData['closed'] != '']
partyData = partyData[partyData['city'] != '']
partyData = partyData[partyData['borough'] != '']

# complaints by borough
bronxComplaints = partyData[partyData['borough'] == 'BRONX']
brooklynComplaints = partyData[partyData['borough'] == 'BROOKLYN']
manhattanComplaints = partyData[partyData['borough'] == 'MANHATTAN']
queensComplaints = partyData[partyData['borough'] == 'QUEENS']
statenIslandComplaints = partyData[partyData['borough'] == 'STATEN ISLAND']
