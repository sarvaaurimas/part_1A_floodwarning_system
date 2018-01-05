# part_1A_floodwarning_system
The repository contains first year computing project for forecasting floods using real-time data from flood stations in the UK.

The project was written by me and my colleague S.L.Garcia and the files for fetching the data from the internet were built by our professors.

The project in a nutshell:

1)The data of every single UK flood station readings gets pulled from the internet.
2)The data undergoes some processing to make it easier to read and operate on.
3)Predictions of expected water levels are made using an extrapolated polyfit function from recent real-time data.
4)Each station is assigned a separate risk level: low, moderate, high or severe.

Programs written by me:
In the folder floodsystem there are modules that are used in the deliverable exercises:
- Geo.py contains various functions related to geographical data (Ex: sorts stations by distance from input coordinates or builds a list of stations that are within
  required distance of input coordinates taking into account the curvature of the earth)

- Analysis.py contains the polyfit function that is then used to make flood level predictions and the severity levels are assigned using the predicted values

In the main folder:

Map.py - an optional exercise that maps all the water stations used on google maps image and stores it as 'mymap.html'
Prediction_visualisation.py - plots both the recent water level data and the predicted water level value on the same graph.

Tasks:
1B - uses geo.stations_by_distance and prints a list of tuples (station name, town, distance) for the 10 closest and the 10 furthest stations 
     from the Cambridge city centre, (52.2053, 0.1218). 
1C - uses the function geo.stations_within_radius to build a list of stations within 10 km of the Cambridge city centre (coordinate (52.2053, 0.1218)). 
     Prints the names of the stations, listed in alphabetical order.

2F - for each of the 5 stations at which the current relative water level is greatest and for a time period extending back 2 days, 
     plots the level data and the best-fit polynomial of degree 12 against time. Shows the typical range low/high on the plot.
2G - Assigns the severity level for each station and prints out the stations that have "high" or "severe" flood risk.

The unit tests were written both by me and Samuel together. They test the various functions we created by inserting real or dummy data and checking 
if the output is correct.

Description of other modules and programs that were by both Samuel and me:
1D - Uses geo.rivers_with_station to print how many rivers have at least one monitoring station (Representative result: 843) and prints 
     the first 10 of these rivers in alphabetical order. It also uses geo.stations_by_river to print the names of the stations located on 
     the following rivers in alphabetical order:‘River Aire’, ‘River Cam’, ‘Thames’.
1E - prints the list of (number stations, river) tuples of 10 rivers that have the biggest number of monitoring stations
2A - sets the latest water level for all stations, and prints the latest levels at the stations
     ‘Bourton Dickler’, ‘Surfleet Sluice’, ‘Gaw Bridge’, ‘Hemingford’ and ‘Swindon’. 
2B - prints the name of each station at which the current relative level is over 0.8, with the relative level alongside the name.
2C - prints the names of the 10 stations at which the current relative level is highest, with the relative level beside each station name.
2D - fetches and prints the level history at the station ‘Cam’ over the past 2 days.
2F - plots the water levels over the past 10 days for the 5 stations at which the current relative water level is greatest.
