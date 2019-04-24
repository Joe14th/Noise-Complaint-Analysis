from noiseComplaintAnalysis import combinedCensusData
from noiseComplaintAnalysis import partyData
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------- BOROUGHS -------------------------------------------------
boroughs = ['BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']
bronx = partyData[partyData['borough'] == 'BRONX']
brooklyn = partyData[partyData['borough'] == 'BROOKLYN']
manhattan = partyData[partyData['borough'] == 'MANHATTAN']
queens = partyData[partyData['borough'] == 'BRONX']
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
# plt.subplot(132)

# # Borough: pie chart :Chey
# plt.subplot(133)

plt.show()

# -------------------------------- NYC CENSUS TRACT ---------------------------------------------
# # Men v Women: pie chart :Gabi
# plt.subplot(321)

# # Race: bar chart :Chey
# plt.subplot(322)

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

# # Types of Employment: bar chartx:Gabi
# plt.subplot(325)

# # Race (male & female) bar chart :Chey
# plt.subplot(326)

plt.show()

# -------------------------------- BOTH ---------------------------------------------
# Population of borough: plot :Chey

# Income v population per borough: box plot :Gabi

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
plt.scatter(counts1, len(counts1)*[poverty[0]], label='Bronx')
plt.scatter(counts2, len(counts2)*[poverty[1]], label='Brooklyn')
plt.scatter(counts3, len(counts3)*[poverty[2]], label='Manhattan')
plt.scatter(counts4, len(counts4)*[poverty[3]], label='Queens')
plt.scatter(counts5, len(counts5)*[poverty[4]], label='Staten Island')
plt.legend(title='Boroughs')
plt.xlabel("Number of Calls")
plt.ylabel("Poverty Levels")
plt.show()

# print(combinedCensusData[''])
# Heat map??

