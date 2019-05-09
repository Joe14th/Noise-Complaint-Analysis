import matplotlib.pyplot as plt

from noiseComplaintAnalysis import *

# -------------------------------- BOROUGHS -------------------------------------------------
boroughs = ['BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']
bronx = partyData[partyData['borough'] == 'BRONX']
brooklyn = partyData[partyData['borough'] == 'BROOKLYN']
manhattan = partyData[partyData['borough'] == 'MANHATTAN']
queens = partyData[partyData['borough'] == 'QUEENS']
staten_island = partyData[partyData['borough'] == 'STATEN ISLAND']

# -------------------------------- PARTY IN NYC ---------------------------------------------
# Calls per day: plot : Jay
plt.subplot(131)
dates, counts = np.unique([x.split()[0] for x in partyData['created']], return_counts=True)
plt.plot(np.arange(len(counts)), counts)
plt.title("Calls Per Day")
plt.xlabel("Days")
plt.ylabel("Number of Calls")
xticks = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
months = [dates[x] for x in xticks]
plt.xticks(xticks, months, rotation=30)

# # Location types: bar chart: Gabi
plt.subplot(132)
location_types, loc_type_counts = np.unique([y.split()[0] for y in partyData['locType']], return_counts=True)
plt.bar(np.arange(len(loc_type_counts)), loc_type_counts, width=0.9, align='center', color='green')
plt.xticks(np.arange(len(location_types)), location_types, rotation=40, fontsize=7, )
plt.title("Location Types")
plt.xlabel("Locations")
# plt.ylabel("Calls Per Location")

# # Borough: pie chart :Chey
plt.subplot(133)
bronxCalls = np.unique(bronx)
bronxCount = bronxCalls.size
brookCalls = np.unique(brooklyn)
brookCount = brookCalls.size
manhattanCalls = np.unique(manhattan)
manCount = manhattanCalls.size
queensCalls = np.unique(queens)
queensCount = queensCalls.size
statenCalls = np.unique(staten_island)
statenCount = statenCalls.size
callPerBorough = [bronxCount, brookCount, manCount, queensCount, statenCount]
labels = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
colors = ['lightslategray', 'tomato', 'mediumblue', 'sandybrown', 'lightskyblue']
plt.pie(callPerBorough, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.title("Calls Per Borough")

plt.show()

# -------------------------------- NYC CENSUS TRACT ---------------------------------------------
# # Men v Women: pie chart :Gabi
plt.subplot(321)
men_pop = (bronxMen + brooklynMen + manhattanMen + queensMen + statenIslandMen)
wamen_pop = (bronxWomen + brooklynWomen + manhattanWomen + queensWomen + statenIslandWomen)
gender = [men_pop, wamen_pop]
labels = ['Men', 'Women']
plt.pie(gender, labels=labels, autopct='%1.1f%%')
plt.title("Men/Women NYC Population")

# # Race: bar chart :Chey
plt.subplot(322)
bronxHisp = combinedCensusData[0][4]
bronxWhite = combinedCensusData[0][5]
bronxBlack = combinedCensusData[0][6]
bronxNative = combinedCensusData[0][7]
bronxAsian = combinedCensusData[0][8]

brookHisp = combinedCensusData[1][4]
brookWhite = combinedCensusData[1][5]
brookBlack = combinedCensusData[1][6]
brookNative = combinedCensusData[1][7]
brookAsian = combinedCensusData[1][8]

manHisp = combinedCensusData[2][4]
manWhite = combinedCensusData[2][5]
manBlack = combinedCensusData[2][6]
manNative = combinedCensusData[2][7]
manAsian = combinedCensusData[2][8]

queensHisp = combinedCensusData[3][4]
queensWhite = combinedCensusData[3][5]
queensBlack = combinedCensusData[3][6]
queensNative = combinedCensusData[3][7]
queensAsian = combinedCensusData[3][8]

statenHisp = combinedCensusData[4][4]
statenWhite = combinedCensusData[4][5]
statenBlack = combinedCensusData[4][6]
statenNative = combinedCensusData[4][7]
statenAsian = combinedCensusData[4][8]

allHisp = [bronxHisp, brookHisp, manHisp, queensHisp, statenHisp]
allWhite = [bronxWhite, brookWhite, manWhite, queensWhite, statenWhite]
allBlack = [bronxBlack, brookBlack, manBlack, queensBlack, statenBlack]
allNative = [bronxNative, brookNative, manNative, queensNative, statenNative]
allAsian = [bronxAsian, brookAsian, manAsian, queensAsian, statenAsian]

xTicks = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
barWidth = .5
plt.bar(xTicks, allHisp, barWidth, label='Hispanic')
plt.bar(xTicks, allWhite, barWidth, bottom=allHisp, label='White')
plt.bar(xTicks, allBlack, barWidth, bottom=[i + j for i, j in zip(allHisp, allWhite)], label='Black')
plt.bar(xTicks, allNative, barWidth, bottom=[i + j + k for i, j, k in zip(allHisp, allWhite, allBlack)], label='Native')
plt.bar(xTicks, allAsian, barWidth,
        bottom=[i + j + k + l for i, j, k, l in zip(allHisp, allWhite, allBlack, allNative)],
        label='Asian')
plt.ylabel('Population-Thousands')
plt.xlabel('Boroughs')
plt.legend(loc=0)
plt.title('Calls by Race')

# Income: box plot:Jay
plt.subplot(323)
plt.title("Income")
plt.boxplot(combinedCensusData['income'], vert=False)

# # Employed v Unemployed: pie chart:Jay
plt.subplot(324)
plt.title("Employed v Unemployed")
employed = combinedCensusData[['employed', 'privateWork', 'publicWork', 'selfEmployed', 'familyWork']]
employed_sum = sum([sum(x) for x in employed])
unemployment_sum = combinedCensusData['unemployment'].sum()
plt.pie([employed_sum, unemployment_sum], labels=['employed', 'unemployed'], autopct='%1.2f%%')

# # Types of Employment: bar chart:Gabi
plt.subplot(325)
privateWork = bronxPrivateWork + brooklynPrivateWork + manhattanPrivateWork + queensPrivateWork + statenIslandPrivateWork
publicWork = bronxPublicWork + brooklynPublicWork + manhattanPublicWork + queensPublicWork + statenIslandPublicWork
selfEmployed = bronxSelfEmployed + brooklynSelfEmployed + manhattanSelfEmployed + queensSelfEmployed + statenIslandSelfEmployed
familyWork = bronxFamilyWork + brooklynFamilyWork + manhattanFamilyWork + queensFamilyWork + statenIslandFamilyWork
employ_type = [privateWork, publicWork, selfEmployed, familyWork]
print(employ_type)
plt.bar(np.arange(len(employ_type)), employ_type, width=0.9, align='center', color='green')
employ_type = ['Private Work', 'Public Work', 'Self Employed', 'Family Work']
plt.xticks(np.arange(len(employ_type)), employ_type, rotation=40, fontsize=7, )
plt.title("Types of Employment")
plt.ylabel("Population")

# # Race (male & female) bar chart :Chey
plt.subplot(326)
plt.title("Calls of Race and Gender")
bronxHisp = combinedCensusData[0][4]
bronxWhite = combinedCensusData[0][5]
bronxBlack = combinedCensusData[0][6]
bronxNative = combinedCensusData[0][7]
bronxAsian = combinedCensusData[0][8]
bronxWomen = [bronxAsian, bronxNative, bronxBlack, bronxWhite, bronxHisp]

brookHisp = combinedCensusData[1][4]
brookWhite = combinedCensusData[1][5]
brookBlack = combinedCensusData[1][6]
brookNative = combinedCensusData[1][7]
brookAsian = combinedCensusData[1][8]
brooklynWomen = [brookHisp, brookWhite, brookBlack, brookNative, brookAsian]

manHisp = combinedCensusData[2][4]
manWhite = combinedCensusData[2][5]
manBlack = combinedCensusData[2][6]
manNative = combinedCensusData[2][7]
manAsian = combinedCensusData[2][8]
manhattanWomen = [manHisp, manWhite, manBlack, manNative, manAsian]

queensHisp = combinedCensusData[3][4]
queensWhite = combinedCensusData[3][5]
queensBlack = combinedCensusData[3][6]
queensNative = combinedCensusData[3][7]
queensAsian = combinedCensusData[3][8]
queensWomen = [queensHisp, queensWhite, queensBlack, queensNative, queensAsian]

statenHisp = combinedCensusData[4][4]
statenWhite = combinedCensusData[4][5]
statenBlack = combinedCensusData[4][6]
statenNative = combinedCensusData[4][7]
statenAsian = combinedCensusData[4][8]
statenWomen = [statenHisp, statenWhite, statenBlack, statenNative, statenAsian]

xTicks = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
barWidth = .5
plt.bar(xTicks, bronxWomen, barWidth, label='Hispanic')
plt.bar(xTicks, brooklynWomen, barWidth, bottom=bronxWomen, label='White')
plt.bar(xTicks, manhattanWomen, barWidth, bottom=[i + j for i, j in zip(bronxWomen, brooklynWomen)], label='Black')
plt.bar(xTicks, queensWomen, barWidth, bottom=[i + j + k for i, j, k in zip(bronxWomen, brooklynWomen, manhattanWomen)],
        label='Native')
plt.bar(xTicks, statenWomen, barWidth,
        bottom=[i + j + k + l for i, j, k, l in zip(bronxWomen, brooklynWomen, manhattanWomen,
                                                    queensWomen)], label='Asian')

plt.ylabel('Population-Thousands')
plt.xlabel('Boroughs')
plt.legend(loc=0)

plt.show()

# -------------------------------- BOTH ---------------------------------------------
# Population of borough: plot :Chey
bronxPop = combinedCensusData[0][1]
brookPop = combinedCensusData[1][1]
manPop = combinedCensusData[2][1]
queensPop = combinedCensusData[3][1]
statenPop = combinedCensusData[4][1]
popsBorough = [bronxPop, brookPop, manPop, queensPop, statenPop]
yCoord = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
plt.barh(yCoord, popsBorough)
plt.xlabel('Population Size')
plt.title('Population Size by Borough')
plt.show()

# Income v population per borough: box plot :Gabi
plt.title("Income for Population")
plt.boxplot(combinedCensusData['income'], vert=False)
plt.show()

# Max and min of incoming calls per borough: bar chart like hw6 :Jay
min = []
max = []
counts1 = np.unique([x.split()[0] for x in bronx['created']], return_counts=True)[1]
min += [counts1.min()]
max += [counts1.max()]
counts2 = np.unique([x.split()[0] for x in brooklyn['created']], return_counts=True)[1]
min += [counts2.min()]
max += [counts2.max()]
counts3 = np.unique([x.split()[0] for x in manhattan['created']], return_counts=True)[1]
min += [counts3.min()]
max += [counts3.max()]
counts4 = np.unique([x.split()[0] for x in queens['created']], return_counts=True)[1]
min += [counts4.min()]
max += [counts4.max()]
counts5 = np.unique([x.split()[0] for x in staten_island['created']], return_counts=True)[1]
min += [counts5.min()]
max += [counts5.max()]
plt.title('Min and Max Number of Calls')
plt.bar(np.arange(1, 6), max, width=0.5, align='center', label='Max Calls')
plt.bar(np.arange(1, 6), min, width=0.3, align='center', label='Min Calls')
plt.legend()
plt.xticks(np.arange(1, 6), boroughs, rotation=30)
plt.xlabel('Boroughs')
plt.ylabel('Number of calls')
plt.show()

# Poverty and call correlation: scatter plot:Jay
poverty = combinedCensusData['poverty']
plt.title("Number of Calls and Poverty Levels")
plt.scatter(counts1, len(counts1) * [poverty[0]], label='Bronx')
plt.scatter(counts2, len(counts2) * [poverty[1]], label='Brooklyn')
plt.scatter(counts3, len(counts3) * [poverty[2]], label='Manhattan')
plt.scatter(counts4, len(counts4) * [poverty[3]], label='Queens')
plt.scatter(counts5, len(counts5) * [poverty[4]], label='Staten Island')
plt.legend(title='Boroughs')
plt.xlabel("Number of Calls")
plt.ylabel("Poverty Levels")
plt.show()

# print(combinedCensusData[''])
# Heat map??
