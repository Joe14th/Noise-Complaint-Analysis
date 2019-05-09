import kaggle as kg
import numpy as np

kg.api.authenticate()
kg.api.dataset_download_files(dataset='somesnm/partynyc', path='.', unzip=True, force=False)
kg.api.dataset_download_files(dataset='muonneutrino/new-york-city-census-data', path='.', unzip=True, force=False)

partyDt = {'names': ('created', 'closed', 'locType', 'zip', 'city', 'borough', 'lat', 'long'),
           'formats': ('U25', 'U25', 'U25', np.int, 'U25', 'U25', np.float, np.float)}

partyFile = "party_in_nyc.csv"
partyData = np.genfromtxt(partyFile, delimiter=',', dtype=partyDt, skip_header=1)

censusDt = {'names': ('cenTract', 'county', 'borough', 'totalPop', 'men', 'women', 'hispanic', 'white', 'black',
                      'native', 'asian', 'citizen', 'income', 'incomeErr', 'incomePerCap', 'incomePerCapErr', 'poverty',
                      'childPoverty', 'professional', 'service', 'office', 'construction', 'production', 'drive',
                      'carpoop', 'transit', 'walk', 'otherTransp', 'workAtHome', 'meanCommute', 'employed',
                      'privateWork', 'publicWork', 'selfEmployed', 'familyWork', 'unemployment'),
            'formats': ('U20', 'U20', 'U20', np.int32, np.int32, np.int32, np.double, np.double, np.double, np.double,
                        np.double, np.int, np.int, np.double, np.double, np.double, np.double, np.double, np.double,
                        np.double, np.double, np.double, np.double, np.double, np.double, np.double, np.double,
                        np.double, np.double, np.double, np.double, np.double, np.double, np.double, np.double, np.double)}

finalDt = {'names': ('borough', 'totalPop', 'men', 'women', 'hispanic', 'white', 'black', 'native', 'asian', 'citizen',
                     'income', 'incomePerCap', 'poverty', 'childPoverty', 'professional', 'service', 'office',
                     'construction', 'production', 'drive', 'carpoop', 'transit', 'walk', 'otherTransp', 'workAtHome',
                     'meanCommute', 'employed', 'privateWork', 'publicWork', 'selfEmployed', 'familyWork',
                     'unemployment'),
           'formats': ('U20', np.int32, np.int32, np.int32, np.double, np.double, np.double, np.double, np.double,
                       np.int, np.int, np.double, np.double, np.double, np.double, np.double, np.double, np.double,
                       np.double, np.double, np.double, np.double, np.double, np.double, np.double, np.double,
                       np.double, np.double, np.double, np.double, np.double, np.double)}

censusFile = "nyc_census_tracts.csv"
censusData = np.genfromtxt(censusFile, delimiter=',', dtype=censusDt, skip_header=2)
#print(censusData['poverty'][:10])
# Removes empty data
mask = (np.isnan(censusData['hispanic']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['white']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['black']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['native']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['asian']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['income']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['incomeErr']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['incomePerCap']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['incomePerCapErr']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['poverty']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['childPoverty']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['professional']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['service']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['office']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['construction']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['production']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['drive']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['carpoop']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['transit']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['walk']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['otherTransp']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['workAtHome']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['meanCommute']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['employed']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['privateWork']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['publicWork']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['selfEmployed']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['familyWork']))
censusData = censusData[~mask]
mask = (np.isnan(censusData['unemployment']))
censusData = censusData[~mask]



# converts percentages to numbers to find percentages after data is combined
censusData['hispanic'] *= censusData['totalPop'] / 100
censusData['white'] *= censusData['totalPop'] / 100
censusData['black'] *= censusData['totalPop'] / 100
censusData['native'] *= censusData['totalPop'] / 100
censusData['asian'] *= censusData['totalPop'] / 100
censusData['poverty'] *= censusData['totalPop'] / 100
censusData['childPoverty'] *= censusData['totalPop'] / 100
censusData['professional'] *= censusData['totalPop'] / 100
censusData['service'] *= censusData['totalPop'] / 100

censusData['office'] *= censusData['totalPop'] / 100
censusData['construction'] *= censusData['totalPop'] / 100
censusData['production'] *= censusData['totalPop'] / 100
censusData['drive'] *= censusData['totalPop'] / 100
censusData['carpoop'] *= censusData['totalPop'] / 100
censusData['transit'] *= censusData['totalPop'] / 100
censusData['walk'] *= censusData['totalPop'] / 100
censusData['otherTransp'] *= censusData['totalPop'] / 100
censusData['workAtHome'] *= censusData['totalPop'] / 100
censusData['meanCommute'] *= censusData['totalPop'] / 100
censusData['employed'] *= censusData['totalPop'] / 100
censusData['privateWork'] *= censusData['totalPop'] / 100
censusData['publicWork'] *= censusData['totalPop'] / 100
censusData['selfEmployed'] *= censusData['totalPop'] / 100
censusData['familyWork'] *= censusData['totalPop'] / 100
censusData['unemployment'] *= censusData['totalPop'] / 100

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
bronxIncome = bronx['income']
brooklynAvgIncome = np.mean(brooklyn['income'])
brooklynIncome = brooklyn['income']
manhattanAvgIncome = np.mean(manhattan['income'])
manhattanIncome = manhattan['income']
queensAvgIncome = np.mean(queens['income'])
queensIncome = queens['income']
statenIslandAvgIncome = np.mean(statenIsland['income'])
statenIslandIncome = statenIsland['income']

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

# office
bronxOffice = np.sum(bronx['office'])
brooklynOffice = np.sum(brooklyn['office'])
manhattanOffice = np.sum(manhattan['office'])
queensOffice = np.sum(queens['office'])
statenIslandOffice = np.sum(statenIsland['office'])

# construction
bronxConstruction = np.sum(bronx['construction'])
brooklynConstruction = np.sum(brooklyn['construction'])
manhattanConstruction = np.sum(manhattan['construction'])
queensConstruction = np.sum(queens['construction'])
statenIslandConstruction = np.sum(statenIsland['construction'])

# production
bronxProduction = np.sum(bronx['production'])
brooklynProduction = np.sum(brooklyn['production'])
manhattanProduction = np.sum(manhattan['production'])
queensProduction = np.sum(queens['production'])
statenIslandProduction = np.sum(statenIsland['production'])

# drive
bronxDrive = np.sum(bronx['drive'])
brooklynDrive = np.sum(brooklyn['drive'])
manhattanDrive = np.sum(manhattan['drive'])
queensDrive = np.sum(queens['drive'])
statenIslandDrive = np.sum(statenIsland['drive'])

# carpoop
bronxCarpoop = np.sum(bronx['carpoop'])
brooklynCarpoop = np.sum(brooklyn['carpoop'])
manhattanCarpoop = np.sum(manhattan['carpoop'])
queensCarpoop = np.sum(queens['carpoop'])
statenIslandCarpoop = np.sum(statenIsland['carpoop'])

# transit
bronxTransit = np.sum(bronx['transit'])
brooklynTransit = np.sum(brooklyn['transit'])
manhattanTransit = np.sum(manhattan['transit'])
queensTransit = np.sum(queens['transit'])
statenIslandTransit = np.sum(statenIsland['transit'])

# walk
bronxWalk = np.sum(bronx['walk'])
brooklynWalk = np.sum(brooklyn['walk'])
manhattanWalk = np.sum(manhattan['walk'])
queensWalk = np.sum(queens['walk'])
statenIslandWalk = np.sum(statenIsland['walk'])

# otherTransp
bronxOtherTransp = np.sum(bronx['otherTransp'])
brooklynOtherTransp = np.sum(brooklyn['otherTransp'])
manhattanOtherTransp = np.sum(manhattan['otherTransp'])
queensOtherTransp = np.sum(queens['otherTransp'])
statenIslandOtherTransp = np.sum(statenIsland['otherTransp'])

# workAtHome
bronxWorkAtHome = np.sum(bronx['workAtHome'])
brooklynWorkAtHome = np.sum(brooklyn['workAtHome'])
manhattanWorkAtHome = np.sum(manhattan['workAtHome'])
queensWorkAtHome = np.sum(queens['workAtHome'])
statenIslandWorkAtHome = np.sum(statenIsland['workAtHome'])

# meanCommute
bronxMeanCommute = np.sum(bronx['meanCommute'])
brooklynMeanCommute = np.sum(brooklyn['meanCommute'])
manhattanMeanCommute = np.sum(manhattan['meanCommute'])
queensMeanCommute = np.sum(queens['meanCommute'])
statenIslandMeanCommute = np.sum(statenIsland['meanCommute'])

# employed
bronxEmployed = np.sum(bronx['employed'])
brooklynEmployed = np.sum(brooklyn['employed'])
manhattanEmployed = np.sum(manhattan['employed'])
queensEmployed = np.sum(queens['employed'])
statenIslandEmployed = np.sum(statenIsland['employed'])

# privateWork
bronxPrivateWork = np.sum(bronx['privateWork'])
brooklynPrivateWork = np.sum(brooklyn['privateWork'])
manhattanPrivateWork = np.sum(manhattan['privateWork'])
queensPrivateWork = np.sum(queens['privateWork'])
statenIslandPrivateWork = np.sum(statenIsland['privateWork'])

# publicWork
bronxPublicWork = np.sum(bronx['publicWork'])
brooklynPublicWork = np.sum(brooklyn['publicWork'])
manhattanPublicWork = np.sum(manhattan['publicWork'])
queensPublicWork = np.sum(queens['publicWork'])
statenIslandPublicWork = np.sum(statenIsland['publicWork'])

# selfEmployed
bronxSelfEmployed = np.sum(bronx['selfEmployed'])
brooklynSelfEmployed = np.sum(brooklyn['selfEmployed'])
manhattanSelfEmployed = np.sum(manhattan['selfEmployed'])
queensSelfEmployed = np.sum(queens['selfEmployed'])
statenIslandSelfEmployed = np.sum(statenIsland['selfEmployed'])

# familyWork
bronxFamilyWork = np.sum(bronx['familyWork'])
brooklynFamilyWork = np.sum(brooklyn['familyWork'])
manhattanFamilyWork = np.sum(manhattan['familyWork'])
queensFamilyWork = np.sum(queens['familyWork'])
statenIslandFamilyWork = np.sum(statenIsland['familyWork'])

# unemployment
bronxunEmployment = np.sum(bronx['unemployment'])
brooklynEmployment = np.sum(brooklyn['unemployment'])
manhattanEmployment = np.sum(manhattan['unemployment'])
queensEmployment = np.sum(queens['unemployment'])
statenIslandEmployment = np.sum(statenIsland['unemployment'])

# combines bronx data
bronxFinal = np.array([("Bronx", bronxTotalPop, bronxMen, bronxWomen, np.round(bronxHispanic / bronxTotalPop * 100, 2),
                        np.round(bronxWhite / bronxTotalPop * 100, 2), np.round(bronxBlack / bronxTotalPop * 100, 2),
                        np.round(bronxNative / bronxTotalPop * 100, 2), np.round(bronxwAsian / bronxTotalPop * 100, 2),
                        bronxTotalCit, bronxAvgIncome, np.round(bronxAvgIncomePerCap, 2),
                        np.round(bronxAvgBelowPov / bronxTotalPop * 100, 2),
                        np.round(bronxAvgBelowChildPov / bronxTotalPop * 100, 2),
                        np.round(bronxProff / bronxTotalPop * 100, 2),
                        np.round(bronxServ / bronxTotalPop * 100, 2),
                        np.round(bronxOffice / bronxTotalPop * 100, 2),
                        np.round(bronxConstruction / bronxTotalPop * 100, 2),
                        np.round(bronxProduction / bronxTotalPop * 100, 2),
                        np.round(bronxDrive / bronxTotalPop * 100, 2),
                        np.round(bronxCarpoop / bronxTotalPop * 100, 2),
                        np.round(bronxTransit / bronxTotalPop * 100, 2),
                        np.round(bronxWalk / bronxTotalPop * 100, 2),
                        np.round(bronxOtherTransp / bronxTotalPop * 100, 2),
                        np.round(bronxWorkAtHome / bronxTotalPop * 100, 2),
                        np.round(bronxMeanCommute / bronxTotalPop * 100, 2),
                        np.round(bronxEmployed / bronxTotalPop * 100, 2),
                        np.round(bronxPrivateWork / bronxTotalPop * 100, 2),
                        np.round(bronxPublicWork / bronxTotalPop * 100, 2),
                        np.round(bronxSelfEmployed / bronxTotalPop * 100, 2),
                        np.round(bronxFamilyWork / bronxTotalPop * 100, 2),
                        np.round(bronxunEmployment / bronxTotalPop * 100, 2))], dtype=finalDt)
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
                           np.round(brooklynServ / brooklynTotalPop * 100, 2),
                           np.round(brooklynOffice / brooklynTotalPop * 100, 2),
                           np.round(brooklynConstruction / brooklynTotalPop * 100, 2),
                           np.round(brooklynProduction / brooklynTotalPop * 100, 2),
                           np.round(brooklynDrive / brooklynTotalPop * 100, 2),
                           np.round(brooklynCarpoop / brooklynTotalPop * 100, 2),
                           np.round(brooklynTransit / brooklynTotalPop * 100, 2),
                           np.round(brooklynWalk / brooklynTotalPop * 100, 2),
                           np.round(brooklynOtherTransp / brooklynTotalPop * 100, 2),
                           np.round(brooklynWorkAtHome / brooklynTotalPop * 100, 2),
                           np.round(brooklynMeanCommute / brooklynTotalPop * 100, 2),
                           np.round(brooklynEmployed / brooklynTotalPop * 100, 2),
                           np.round(brooklynPrivateWork / brooklynTotalPop * 100, 2),
                           np.round(brooklynPublicWork / brooklynTotalPop * 100, 2),
                           np.round(brooklynSelfEmployed / brooklynTotalPop * 100, 2),
                           np.round(brooklynFamilyWork / brooklynTotalPop * 100, 2),
                           np.round(brooklynEmployment / brooklynTotalPop * 100, 2))], dtype=finalDt)
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
                            manhattanProff / manhattanTotalPop * 100, manhattanServ / manhattanTotalPop * 100,
                            np.round(manhattanOffice / manhattanTotalPop * 100, 2),
                            np.round(manhattanConstruction / manhattanTotalPop * 100, 2),
                            np.round(manhattanProduction / manhattanTotalPop * 100, 2),
                            np.round(manhattanDrive / manhattanTotalPop * 100, 2),
                            np.round(manhattanCarpoop / manhattanTotalPop * 100, 2),
                            np.round(manhattanTransit / manhattanTotalPop * 100, 2),
                            np.round(manhattanWalk / manhattanTotalPop * 100, 2),
                            np.round(manhattanOtherTransp / manhattanTotalPop * 100, 2),
                            np.round(manhattanWorkAtHome / manhattanTotalPop * 100, 2),
                            np.round(manhattanMeanCommute / manhattanTotalPop * 100, 2),
                            np.round(manhattanEmployed / manhattanTotalPop * 100, 2),
                            np.round(manhattanPrivateWork / manhattanTotalPop * 100, 2),
                            np.round(manhattanPublicWork / manhattanTotalPop * 100, 2),
                            np.round(manhattanSelfEmployed / manhattanTotalPop * 100, 2),
                            np.round(manhattanFamilyWork / manhattanTotalPop * 100, 2),
                            np.round(manhattanEmployment / manhattanTotalPop * 100, 2))],
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
                         np.round(queensServ / queensTotalPop * 100, 2),
                         np.round(queensOffice / queensTotalPop * 100, 2),
                         np.round(queensConstruction / queensTotalPop * 100, 2),
                         np.round(queensProduction / queensTotalPop * 100, 2),
                         np.round(queensDrive / queensTotalPop * 100, 2),
                         np.round(queensCarpoop / queensTotalPop * 100, 2),
                         np.round(queensTransit / queensTotalPop * 100, 2),
                         np.round(queensWalk / queensTotalPop * 100, 2),
                         np.round(queensOtherTransp / queensTotalPop * 100, 2),
                         np.round(queensWorkAtHome / queensTotalPop * 100, 2),
                         np.round(queensMeanCommute / queensTotalPop * 100, 2),
                         np.round(queensEmployed / queensTotalPop * 100, 2),
                         np.round(queensPrivateWork / queensTotalPop * 100, 2),
                         np.round(queensPublicWork / queensTotalPop * 100, 2),
                         np.round(queensSelfEmployed / queensTotalPop * 100, 2),
                         np.round(queensFamilyWork / queensTotalPop * 100, 2),
                         np.round(queensEmployment / queensTotalPop * 100, 2))],
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
                               np.round(statenIslandServ / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandOffice / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandConstruction / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandProduction / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandDrive / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandCarpoop / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandTransit / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandWalk / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandOtherTransp / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandWorkAtHome / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandMeanCommute / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandEmployed / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandPrivateWork / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandPublicWork / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandSelfEmployed / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandFamilyWork / statenIslandTotalPop * 100, 2),
                               np.round(statenIslandEmployment / statenIslandTotalPop * 100, 2),)], dtype=finalDt)

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

# combined census data
combinedCensusData = np.concatenate((bronxFinal, brooklynFinal, manhattanFinal, queensFinal, statenIslandFinal))

#print(combinedCensusData)
