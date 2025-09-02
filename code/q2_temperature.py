import glob
import csv

# 1. Load all CSV files
files = glob.glob("assignment_files/temperatures/*.csv")

# Dictionary: station - list of all temps
station_data = {}

for fname in files:
    with open(fname, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            station = row[0].strip()
            temps = [t for t in row[5:] if t]  # monthly temps, ignore blanks
            temps = [float(t) for t in temps if t.lower() != "nan"]  # skip NaN

            if station not in station_data:
                station_data[station] = []

            station_data[station].extend(temps)

# 2. Calculate range (max - min) for each station
station_ranges = {}
for station, vals in station_data.items():
    if vals:  # make sure station has some data
        mx = max(vals)
        mn = min(vals)
        rg = mx - mn
        station_ranges[station] = (rg, mx, mn)

# 3. Find the station(s) with the largest range
largest_range = -1
winners = []
for st, (rg, mx, mn) in station_ranges.items():
    if rg > largest_range:
        largest_range = rg
        winners = [(st, rg, mx, mn)]
    elif abs(rg - largest_range) < 1e-9:  # tie
        winners.append((st, rg, mx, mn))

# 4. Save results to file
with open("assignment_files/largest_temp_range_station.txt", "w") as out:
    for st, rg, mx, mn in winners:
        out.write(f"{st}: Range {rg:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")

print("Saved results to assignment_files/largest_temp_range_station.txt")
            
            
            