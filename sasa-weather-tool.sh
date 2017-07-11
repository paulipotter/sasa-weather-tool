sudo pip-review --local --auto
# Get today's date
today="$(date '+%Y%m%d')"
yesterday="$(date -d yesterday '+%Y%m%d')"

# Write the command and export it
echo '''14819|20130524|41.786,-87.752|DIR,SPD,GUS,CLG,SKC,L,M,H,VSB,TEMP,DEWP,SLP,ALT,STP,MAX,MIN,PCP01,PCP06,PCP24,PCPXX,SD''' > weather_requirements.txt
echo "Command Exported to weather_requirements.txt"

# Run the NOAA API
python ./noaahist.py --infile noaa-reqs.txt -p -m -o weather-info.csv
echo noaahist run finished
echo Running main.py
#Run python
python3 main.py
echo main.py run finished
