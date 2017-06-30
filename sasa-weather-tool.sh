if today is in range then use this location and zip

location=
today="$(date '+%Y%m%d')"
yesterday="$(date -d yesterday '+%Y%m%d')"
echo "$location | $yesterday | $zip | TEMP,STP,SPD,DIR,PCP01" > noaa-reqs.txt
