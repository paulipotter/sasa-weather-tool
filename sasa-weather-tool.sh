
pip-review --local --interactive

# Get today's date
today="$(date '+%Y%m%d')"
yesterday="$(date -d yesterday '+%Y%m%d')"

# Write the command and export it
echo '''CHICAGO MIDWAY INTL AIRPORT | 20170623
  | 41.7868, 87.7522 | DIR,SPD,GUS,CLG,SKC,
  L,M,H,VSB,TEMP,DEWP,SLP,ALT,STP,MAX,MIN,
  PCP01,PCP06,PCP24,PCPXX,SD''' > noaa-reqs.txt
echo "Command Exported to noaa-reqs.txt"

# Run the NOAA API
python ./noaahist/noaahist.py --infile noaa-reqs.txt -p -m -o weather-info.csv

#Run python
# python3 main.py
