if today is in range then use this location and zip
i=10
a=1
b=0.65
if [ "$a" != "$b" ] ; then
   case $i in
        1|2|5) echo "Not OK"; ;;
        9|10|12) echo "may be ok"; ;;
        *) echo "no clue - $i"; ;;
   esac;
fi

location=
today="$(date '+%Y%m%d')"
yesterday="$(date -d yesterday '+%Y%m%d')"
echo "$location | $yesterday | $zip | TEMP,STP,SPD,DIR,PCP01" > noaa-reqs.txt

./noaahist.py --infile noaa-reqs.txt -p -m
LasVegas|19710321|89109|TEMP,STP,SPD,DIR,PCP01' > reqs.txt
