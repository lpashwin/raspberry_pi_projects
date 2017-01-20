set datafile separator ","
set multiplot layout 2,2 title "Outputs from Raspberry Pi Sensehat Sensors \n"
plot 'output.txt' using 1:2 with lines
plot 'output.txt' using 1:3 with lines
plot 'output.txt' using 1:4 with lines
plot 'output.txt' using 1:5 with lines
