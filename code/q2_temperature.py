#Import the required modules
import glob
import csv

# Load all CSV files
files = glob.glob("assignment_files/temperatures/*.csv")

#Dictionary: station - list of all temps
station_data = {}

#Creating a list for all the temperature values for each season to belong
summer = []
autumn = []
winter = []
spring = []

#Create a loop that read every file ending in .csv
for fname in files:     
    with open(fname, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            station = row[0].strip()        #getting rid of unnecessary spaces in the town naame
            temps = [t for t in row[4:] if t]  # monthly temps, ignore blanks
            temps = [float(t) for t in temps if t.lower() != "nan"]  # skip NaN

            if station not in station_data:
                station_data[station] = []

            station_data[station].extend(temps)     #adding all the temperatures into the station_data dictionary

            summer.extend([row[4], row[5], row[15]])  #looping through so that the values in the index positions of the months corresponding to each season are added
            autumn.extend([row[6], row[7], row[8]])
            winter.extend([row[9], row[10], row[11]])
            spring.extend([row[12], row[13], row[14]])

  
# Question 2 part 1: Find the average temperature for all seasons across all years

season_temps = [summer, autumn, winter, spring]      #storing all the temperatures in a nested list
season_averages = []       #creating a list to store values for each season's average
for i in range(4):      #creating a loop that loops through the four seasons
    sum = 0     #intitial sum of temperatures set to 0
    for j in range(6270):       #creating a loop that loops through each temperture in each season's list, then dividing by 6270 to find a mean temperature
        sum = sum + float(season_temps[i][j])
    average = round(sum / 6270, 1)      #rounding average temperature to one decimal place
    season_averages.append(average)     #appending each season's average temp to season_average list
summer_average = season_averages[0]     #setting the index of the season_averages list equal to the corresponding month's average
autumn_average = season_averages[1]
winter_average = season_averages[2]
spring_average = season_averages[3]

#Save results to file
with open("assignment_files/average_temp.txt", "w") as out: #create a new file
    out.write(f"Summer: {season_averages[0]}°C \nAutumn: {season_averages[1]}°C \nWinter: {season_averages[2]}°C \nSpring: {season_averages[3]}°C \n")  #write the average temperatures on a new line for each
print("Saved results to assignment_files/average_temp.txt")     #print a verification that the process has been completed


# Question 2 part 2: Calculate range (max - min) for each station

station_ranges = {}
for station, vals in station_data.items():
    if vals:  # make sure station has some data
        mx = max(vals)
        mn = min(vals)
        rg = mx - mn
        station_ranges[station] = (rg, mx, mn)

#Find the station(s) with the largest range
largest_range = -1
winners = []
for st, (rg, mx, mn) in station_ranges.items():
    if rg > largest_range:
        largest_range = rg
        winners = [(st, rg, mx, mn)]
    elif abs(rg - largest_range) < 1e-9:  # tie
        winners.append((st, rg, mx, mn))

#Save results to file
with open("assignment_files/largest_temp_range_station.txt", "w") as out:
    for st, rg, mx, mn in winners:
        out.write(f"{st}: Range {rg:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")

print("Saved results to assignment_files/largest_temp_range_station.txt")


#Question 2 part 3: Finding the stations with the smallest and largest standard deviations

import statistics
#Calculate all standard deviations
standard_deviations = {k: None for k in station_data}       #creating a standard deviations dictionary which contains station names but no values assigned yet
for n in standard_deviations:
    standard_deviations[n] = round(statistics.stdev(station_data[n]), 1)        #assigning each station's standard deviation to the station name in the standard deviations dictionary

#Find the smallest and largest standard deviation
largest_stdev = {}      #creating a dictionary to contain town with largest standard deviation
for key in standard_deviations:     #loop which loops through every town
    if not largest_stdev:       #for the first town: if largest_stdev is empty
        largest_stdev["ADELAIDE-KENT-TOWN"] = standard_deviations["ADELAIDE-KENT-TOWN"] 
        lvalues =  largest_stdev["ADELAIDE-KENT-TOWN"]  #create a variable which stores the largest standard deviation value only
    elif standard_deviations[key] in largest_stdev: #for if the standard deviation is already in largest_stdev
        largest_stdev[station_data[key]] = lvalues  #add the station to the dictionary
        lvalues = next(iter(largest_stdev.values()))    
    elif standard_deviations[key] > lvalues:   
        largest_stdev.clear()           #if value of standard deviation is greater, clear largest_setdev and replace with the new key and value
        largest_stdev[key] =  standard_deviations[key]
        lvalues = next(iter(largest_stdev.values()))

smallest_stdev = {}          #creating a dictionary to contain town with largest standard deviation
for key in standard_deviations: #loop which loops through every town
    if not smallest_stdev:       #for the first town: if smallest_stdev is empty
        smallest_stdev["ADELAIDE-KENT-TOWN"] = standard_deviations["ADELAIDE-KENT-TOWN"]
        svalues =  smallest_stdev["ADELAIDE-KENT-TOWN"]  #create a variable which stores the smallest standard deviation value only
    elif standard_deviations[key] in smallest_stdev:       #for if the standard deviation is already in smallest_stdev
        smallest_stdev[station_data[key]] = svalues         #add the station to the dictionary
        svalues = next(iter(smallest_stdev.values()))
    elif standard_deviations[key] < svalues:
        smallest_stdev.clear()           #if value of standard deviation is smaller, clear smallest_setdev and replace with the new key and value
        smallest_stdev[key] =  standard_deviations[key]
        svalues = next(iter(smallest_stdev.values()))

smallest_stdev_town = next(iter(smallest_stdev))        #creat variables which store only the keys of the largest and smallest standard deviations
largest_stdev_town = next(iter(largest_stdev))

#Save results to file
with open("assignment_files/temperature_stability_stations.txt", "w") as out:
        out.write(f"Most Stable: Station {smallest_stdev_town}: Standard Deviation {svalues}°C\nMost Variable: Station {largest_stdev_town}: Standard Deviation {lvalues}°C")

print("Saved results to assignment_files/temperature_stability_stations.txt")



    

