# sasa-weather-tool
This program is part of a bigger project called [Shared Air/Shared Action](https://www.engg.ksu.edu/chsr/SA2%20Air%20Monitoring%20Project) - [Visit Repository](https://github.com/Shared-Air-Shared-Action)

##### USAGE
First, fork [stewartwatt's NOAA API](https://github.com/stewartwatts/noaahist) and copy-paste it to the same directory as this repository.

Edit the `sasa-weather-tool.sh` file according to the NOAA API to get data on the location and date desired [(Access Documentation here)](https://github.com/stewartwatts/noaahist/). The default is to run the historic data of the day before as this will be run daily and then displayed on a website. The sh file will get a CSV file with the hourly averages of the location requested and then run this python program will upload it to the postgres database.

Please refer to the NOAA API Documentation to gain knowledge on the fields available for download.

###### On your terminal
`chmod +x sasa-weather-tool.sh` <- Allow execution of the file

`sh sasa-weather-tool.sh` or `sasa-weather-tool.sh` 

##### DEPENDENCIES
datetime, pytz
