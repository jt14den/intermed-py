import analyze
import sys 

#filename = "a2_mosquito_data.csv"
#argv[0] our script filename
filename = sys.argv[1]

analyze2.create_mosquitos_vs_tempC_plot(filename)
