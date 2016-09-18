import pandas
import matplotlib.pyplot as plt

def fahr_to_celsius(temp_fahr):
    """Convert Fahrenheit to Celsiuss
    
    Return Celsius conversion of input
    """
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius

def create_mosquitos_vs_tempC_plot(filename):
    """Create a png plot of mosquitos vs temp C
    
    Parameters
    ----------
    filename : string
        name of csv data file
    Returns
    -------
    mosquito_data : DataFrame
        Table with temp C column
    """
    
    # write processing here
    # load data
    print("Loading", filename)
    mosquitos_data = pandas.read_csv(filename)
    # convert celsius
    mosquitos_data["temperature_C"] = fahr_to_celsius(mosquitos_data["temperature"])
    # create the plot
    print("Plotting", filename)
    plt.plot(mosquitos_data["temperature_C"], mosquitos_data["mosquitos"], ".")
    # save the plot
    filename_png = filename[0:-4] + "_mosquitos_vs_tempC.png"
    plt.savefig(filename_png)
    print("Saving", filename_png)
    return mosquitos_data