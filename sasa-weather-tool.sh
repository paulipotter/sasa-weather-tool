
# Get today's date
today="$(date '+%Y%m%d')"
yesterday="$(date -d yesterday '+%Y%m%d')"

# Write the command and export it
echo "CHICAGO MIDWAY INTL ARPT | $yesterday | 60638 | TEMP,STP,SPD,DIR,PCP01" > noaa-reqs.txt
echo "Command Exported to noaa-reqs.txt"

# Run the NOAA API
../noaahist/noaahist.py --infile noaa-reqs.txt -p -m -o weather-info.csv

#Run python
