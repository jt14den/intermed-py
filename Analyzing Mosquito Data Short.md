
start notebook inside 'mosquitos' folder


```python
import pandas
```

* interested in understanding the relationship b/t the weather and the number of mosquitos occuring during a particular year
* relationship at a particular site and whether or not it is consistent across sites
* data in csv files
* contains: single location data, rows holds single year info, mosiquito numbers and avg temps and rainfall 

year,temperature,rainfall,mosquitos  
2001,80,157,150  
2002,85,252,2177  
2003,86,154,153
## show file

### Learning objectives
* conduct variable assignment, looping, and conditionals in python
* use an external py library
* read tabular data from a file
* subset and perform analysis on data
* display simple graphs


```python
pandas.read_csv('A1_mosquito_data.csv')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2006</td>
      <td>75</td>
      <td>283</td>
      <td>237</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2007</td>
      <td>80</td>
      <td>214</td>
      <td>190</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2008</td>
      <td>85</td>
      <td>197</td>
      <td>181</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2009</td>
      <td>74</td>
      <td>231</td>
      <td>200</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2010</td>
      <td>74</td>
      <td>207</td>
      <td>184</td>
    </tr>
  </tbody>
</table>
</div>



* read_csv() function belongs to pandas library
* dot notation 



```python
data = pandas.read_csv('A1_mosquito_data.csv')
```


```python
print(data)
```

       year  temperature  rainfall  mosquitos
    0  2001           80       157        150
    1  2002           85       252        217
    2  2003           86       154        153
    3  2004           87       159        158
    4  2005           74       292        243
    5  2006           75       283        237
    6  2007           80       214        190
    7  2008           85       197        181
    8  2009           74       231        200
    9  2010           74       207        184



```python
data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2006</td>
      <td>75</td>
      <td>283</td>
      <td>237</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2007</td>
      <td>80</td>
      <td>214</td>
      <td>190</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2008</td>
      <td>85</td>
      <td>197</td>
      <td>181</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2009</td>
      <td>74</td>
      <td>231</td>
      <td>200</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2010</td>
      <td>74</td>
      <td>207</td>
      <td>184</td>
    </tr>
  </tbody>
</table>
</div>



* Once we have the data we can start playing with it.
* first let's ask what type of thing it is


```python
print(type(data))
```

    <class 'pandas.core.frame.DataFrame'>


* started in a data structure of DataFrame
* there are other data structures (remember numpy arrays from last class)
* we can select an individual column of data using it's name:


```python
print(data['year'])
```

    0    2001
    1    2002
    2    2003
    3    2004
    4    2005
    5    2006
    6    2007
    7    2008
    8    2009
    9    2010
    Name: year, dtype: int64


* or we can select several columns of data at once


```python
print(data[['rainfall', 'temperature']])
```

       rainfall  temperature
    0       157           80
    1       252           85
    2       154           86
    3       159           87
    4       292           74
    5       283           75
    6       214           80
    7       197           85
    8       231           74
    9       207           74


* we can subset rows using slices
* let's get first two rows


```python
print(data[0:2])
```

       year  temperature  rainfall  mosquitos
    0  2001           80       157        150
    1  2002           85       252        217


* remember python uses 0 based indexing
* starts at the first value and goes up to, but doesn't include the second value
* one thing we can't do with this syntax is directly as for data from a single row


```python
print(data['temperature'][data['year'] > 2005])
```

    5    75
    6    80
    7    85
    8    74
    9    74
    Name: temperature, dtype: int64


* data frames also know how to perform common math
* mean


```python
print(data.mean())
```

    year           2005.5
    temperature      80.0
    rainfall        214.6
    mosquitos       191.3
    dtype: float64



```python
print(data.max())
```

    year           2010
    temperature      87
    rainfall        292
    mosquitos       243
    dtype: int64



```python
print(data['temperature'].min())
```

    74



```python
print(data['mosquitos'][1:3].std())
```

    45.2548339959


## Challenge

Import the data from A2_mosquito_data.csv, create a new variable that holds a data frame with only the weather data, and print the means and standard deviations for the weather variables.


```python
data2 = pandas.read_csv('A2_mosquito_data.csv')
data2.head()
weather = data2[["temperature","rainfall"]]
print(data2.temperature.mean(), data2.temperature.std(), data2.rainfall.mean(), data2.rainfall.std())
```

    80.3921568627 6.13540033371 207.039215686 56.5603963156


## Loops

* we can loop over the data and perform operations
* remember loop structure:

```python
for item in list:
   do_something
```

* let's loop over temperatures and print out their values in degrees Celsius


```python
temps = data['temperature']
for temp_in_f in temps:
    temp_in_c = (temp_in_f - 32) * 5/9
    print(temp_in_c)
```

    26.6666666667
    29.4444444444
    30.0
    30.5555555556
    23.3333333333
    23.8888888889
    26.6666666667
    29.4444444444
    23.3333333333
    23.3333333333


## Modularization and Doc

** learning objectives**

* write code for ppl, not computers
* break programs into chunks 
* write functions
* document code

* write code for people not computers
* use meaniful variable names


```python
import pandas as pd

data = pd.read_csv('A2_mosquito_data.csv')
print(data.head())
```

       year  temperature  rainfall  mosquitos
    0  1960           82       200        180
    1  1961           70       227        194
    2  1962           89       231        207
    3  1963           74       114        121
    4  1964           78       147        140



```python
data['temperature'].plot(color="black", marker="*")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10ff26400>




![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_32_1.png)


* we can also set the index of the data frame


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
  </tbody>
</table>
</div>



* pandas has a concept of row index that you can set to what you want
* in this case, let's set our row index to `year`
* by default it will read in as the integer index


```python
data.set_index('year')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2001</th>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>75</td>
      <td>283</td>
      <td>237</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>80</td>
      <td>214</td>
      <td>190</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>85</td>
      <td>197</td>
      <td>181</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>74</td>
      <td>231</td>
      <td>200</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>74</td>
      <td>207</td>
      <td>184</td>
    </tr>
  </tbody>
</table>
</div>




```python
data
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2006</td>
      <td>75</td>
      <td>283</td>
      <td>237</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2007</td>
      <td>80</td>
      <td>214</td>
      <td>190</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2008</td>
      <td>85</td>
      <td>197</td>
      <td>181</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2009</td>
      <td>74</td>
      <td>231</td>
      <td>200</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2010</td>
      <td>74</td>
      <td>207</td>
      <td>184</td>
    </tr>
  </tbody>
</table>
</div>



* we can save that setting by overwriting our data


```python
data = data.set_index('year')
```


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2001</th>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['temperature'].plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x10ff64828>




![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_41_1.png)


* ah what happened to the x axes labels?  
* our index is not the right data type


```python
data.dtypes
```




    temperature    int64
    rainfall       int64
    mosquitos      int64
    dtype: object




```python
data.index
```




    Int64Index([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], dtype='int64', name='year')



* lets fix and rerun the plot making our index into a string


```python
data.index = data.index.map(str)
```


```python
data['temperature'].plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11051a668>




![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_47_1.png)


* one attribute of data frames is `dtypes` - tells us what our data types are

* Subsetting and filtering data frames
* let's see only temp greater than 80


```python
data[data["temperature"] > 80]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2002</th>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>85</td>
      <td>197</td>
      <td>181</td>
    </tr>
  </tbody>
</table>
</div>




```python
data[data["temperature"] > 80]["rainfall"]
```




    1    252
    2    154
    3    159
    7    197
    Name: rainfall, dtype: int64




```python
type(data)
```




    pandas.core.frame.DataFrame



### Challenge

>Select the mosiquitos where rainfall is less than 200


```python
data[data['rainfall'] < 200]['mosquitos']
```




    0    150
    2    153
    3    158
    7    181
    Name: mosquitos, dtype: int64



* this is equivalent statement:


```python
data['mosquitos'][data['rainfall'] < 200]
```




    2001    150
    2003    153
    2004    158
    2008    181
    Name: mosquitos, dtype: int64



* we can also get the max of that returned object


```python
data[data['rainfall'] < 200]['mosquitos'].max()
```




    181



**NOTE** - we can walk through this step by step

* we can also assign it to a variable for later


```python
mosquitos_with_low_rainfall = data['mosquitos'][data['rainfall'] < 200]
```


```python
type(mosquitos_with_low_rainfall)
```




    pandas.core.series.Series




```python
mosquitos_with_low_rainfall
```




    2001    150
    2003    153
    2004    158
    2008    181
    Name: mosquitos, dtype: int64




```python
mosquitos_with_low_rainfall.index
```




    Index(['2001', '2003', '2004', '2008'], dtype='object')




```python
data.plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x110614978>




![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_65_1.png)


## Functions

```python
def function_name(inputs):
    do stuff
    return output
```

* general form

## Challenge - function 

1. Write a function that converts temperature from Fahrenheit to Celcius and use it to replace

>```python
data['temperature'] = (data['temperature'] - 32) * 5 / 9.0
```

in our program.

```python
def fahr_to_celsius(temp_fahr):
    #your code here
    return temp_celsius
```


```python
def fahr_to_celsius(temp_fahr):
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius

print(fahr_to_celsius(32))
```

    0.0


* Documenting our functions. 
* Using function with pandas objects.


```python
def fahr_to_celsius(temp_fahr):
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius
```


```python
fahr_to_celsius(32)
```




    0.0




```python
fahr_to_celsius(212)
```




    100.0



* 
* let's comment our function


```python
#this is a comment
def fahr_to_celsius(temp_fahr):
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius
```


```python
"this is a string"
```




    'this is a string'




```python
#doesn't work
"a multiline 
string
"
```


      File "<ipython-input-24-316711d988ad>", line 2
        "a multiline
                     ^
    SyntaxError: EOL while scanning string literal



* a triple quote (single or double) will let us do a multi lined string


```python
multiline_string = ''' line one
line 2
one more
'''
```


```python
print(multiline_string)
```

     line one
    line 2
    one more
    



```python
#when we see the literal string we see the new line character
multiline_string
```




    ' line one\nline 2\none more\n'




```python
def fahr_to_celsius(temp_fahr):
    """Convert Fahrenheit to Celsiuss
    
    Return Celsius conversion of input
    """
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius
```


```python
# use a question after the function to get python help
fahr_to_celsius?
```

    Object `fahr_to_celsius` not found.



```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2001</th>
      <td>80</td>
      <td>157</td>
      <td>150</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>85</td>
      <td>252</td>
      <td>217</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>86</td>
      <td>154</td>
      <td>153</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>87</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>74</td>
      <td>292</td>
      <td>243</td>
    </tr>
  </tbody>
</table>
</div>



* now we have the have the function we can apply it to our data frame
* let's see how that looks and then save to the data frame itself 


```python
fahr_to_celsius(data['temperature'])
```




    0    26.666667
    1    29.444444
    2    30.000000
    3    30.555556
    4    23.333333
    5    23.888889
    6    26.666667
    7    29.444444
    8    23.333333
    9    23.333333
    Name: temperature, dtype: float64




```python
data["temperature_c"] = fahr_to_celsius(data['temperature'])
```


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
      <th>temperature_c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2001</td>
      <td>80</td>
      <td>157</td>
      <td>150</td>
      <td>26.666667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2002</td>
      <td>85</td>
      <td>252</td>
      <td>217</td>
      <td>29.444444</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2003</td>
      <td>86</td>
      <td>154</td>
      <td>153</td>
      <td>30.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004</td>
      <td>87</td>
      <td>159</td>
      <td>158</td>
      <td>30.555556</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005</td>
      <td>74</td>
      <td>292</td>
      <td>243</td>
      <td>23.333333</td>
    </tr>
  </tbody>
</table>
</div>



* yay we added a new column on our dataframe
* let's plot using that var and save our plot to the disk


```python
%matplotlib inline
```


```python
import matplotlib.pyplot as plt
```


```python
plt.plot?
```


```python
plt.plot(data['temperature_c'], data['mosquitos'], ".")
plt.savefig('A1_mosquito_data_mosquitos_vs_tempC.png')
```


![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_92_0.png)



```python
!ls *png
```

    A1_mosquito_data_mosquitos_vs_tempC.png


* ok, we've successfully added a column to our data frame and plotted values
* then we saved that image to the file system
* but remember: we have a number of files in that directory


```python
!ls -l *csv
```

    -rw-r--r--  1 jtdennis  2113415076   196 Feb  6 21:11 A1_mosquito_data.csv
    -rw-r--r--  1 jtdennis  2113415076   852 Feb  6 21:11 A2_mosquito_data.csv
    -rw-r--r--  1 jtdennis  2113415076  1837 Apr 27 10:31 A2_mosquito_data_C.csv
    -rw-r--r--  1 jtdennis  2113415076   827 Feb  6 21:11 A3_mosquito_data.csv
    -rw-r--r--  1 jtdennis  2113415076   823 Feb  6 21:11 B1_mosquito_data.csv
    -rw-r--r--  1 jtdennis  2113415076   852 Feb  6 21:11 B2_mosquito_data.csv


* what we want is to be able to read each of those files, plot and save the fig out
* problem is we don't want to have to specify the file name manually
* let's see if we can manipulate our csv filenames 


```python
a = "A1_mosquitos_data.csv"
```


```python
a
```




    'A1_mosquitos_data.csv'



* remember how we sliced off parts of strings earlier
* we can reuse that here


```python
a[0:-3] + "png"
```




    'A1_mosquitos_data.png'



* we can also concatenate our last part -- that tells us what we plotted


```python
a[0:-4] + "_mosquitos_vs_tempC.png"
```




    'A1_mosquitos_data_mosquitos_vs_tempC.png'



* we can do string replacement using the replace method


```python
a.replace(".csv", ".png")
```




    'A1_mosquitos_data.png'



**Let's put it all together with our conversion and plotting above into a couple of functions**


```python
def fahr_to_celsius(temp_fahr):
    temp_celsius = (temp_fahr- 32) * 5/9
    return temp_celsius
```


```python
%matplotlib inline
```

* It is often good to write out what you want the function to do step by step


```python
def creat_mosquitos_vs_tempC_plot(filename):
    # write out process here
    #load data
    #conert celsius
    #create the plot
    #save the plot
    pass
    
```

* Then just write out those operations 


```python
def create_mosquitos_vs_tempC_plot(filename):
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
    return filename_png
```


```python
name_of_png = create_mosquitos_vs_tempC_plot('A2_mosquito_data.csv')
```

    Loading A2_mosquito_data.csv
    Plotting A2_mosquito_data.csv
    Saving A2_mosquito_data_mosquitos_vs_tempC.png



![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_112_1.png)


* yay, we sucessfully created a function that takes a filename, reads in data, does a conversion, plots and then saves plot to the file


```python
print(name_of_png)
```

    A2_mosquito_data_mosquitos_vs_tempC.png



```python
create_mosquitos_vs_tempC_plot("B1_mosquito_data.csv")
```

    Loading B1_mosquito_data.csv
    Plotting B1_mosquito_data.csv
    Saving B1_mosquito_data_mosquitos_vs_tempC.png





    'B1_mosquito_data_mosquitos_vs_tempC.png'




![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_115_2.png)



```python
!ls *png
```

    A1_mosquito_data_mosquitos_vs_tempC.png B1_mosquito_data_mosquitos_vs_tempC.png
    A2_mosquito_data_mosquitos_vs_tempC.png


* now, how about instead of returning the new plot filename, let's return the data frame
* we just need to change the return value


```python
def create_mosquitos_vs_tempC_plot(filename):
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
```


```python
mosquito_data_A2 = create_mosquitos_vs_tempC_plot("A2_mosquito_data.csv")
```

    Loading A2_mosquito_data.csv
    Plotting A2_mosquito_data.csv
    Saving A2_mosquito_data_mosquitos_vs_tempC.png



![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_119_1.png)


* we can then save that new data out as csv


```python
mosquito_data_A2.to_csv("A2_mosquito_data_C.csv")
```


```python
mosquito_data_A2.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
      <th>temperature_C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>82</td>
      <td>200</td>
      <td>180</td>
      <td>27.777778</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>70</td>
      <td>227</td>
      <td>194</td>
      <td>21.111111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>89</td>
      <td>231</td>
      <td>207</td>
      <td>31.666667</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>74</td>
      <td>114</td>
      <td>121</td>
      <td>23.333333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>78</td>
      <td>147</td>
      <td>140</td>
      <td>25.555556</td>
    </tr>
  </tbody>
</table>
</div>




```python
!head A2_mosquito_data_C.csv
```

    ,year,temperature,rainfall,mosquitos,temperature_C
    0,1960,82,200,180,27.77777777777778
    1,1961,70,227,194,21.11111111111111
    2,1962,89,231,207,31.666666666666668
    3,1963,74,114,121,23.333333333333332
    4,1964,78,147,140,25.555555555555557
    5,1965,85,151,148,29.444444444444443
    6,1966,86,172,162,30.0
    7,1967,75,106,112,23.88888888888889
    8,1968,70,276,230,21.11111111111111


### Making a module

* Let's write a script! 
* We will turn our functions into a script and use in panadas like our `import` modules



```python
!ls *py
```

    analyze.py



```python
%matplotlib inline
```


```python
import analyze
```


```python
data = analyze.create_mosquitos_vs_tempC_plot("A2_mosquito_data.csv")
```

    Loading A2_mosquito_data.csv
    Plotting A2_mosquito_data.csv
    Saving A2_mosquito_data_mosquitos_vs_tempC.png



![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_128_1.png)



```python
print(data)
```

    A2_mosquito_data_mosquitos_vs_tempC.png


* notice that we added out earlier version of the plotting function to the file -- the one that returned the file
* edit the file and return mosquitos_data instead
* let's rerun the function call


```python
data = analyze.create_mosquitos_vs_tempC_plot("A2_mosquito_data.csv")
```

    Loading A2_mosquito_data.csv
    Plotting A2_mosquito_data.csv
    Saving A2_mosquito_data_mosquitos_vs_tempC.png



![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_131_1.png)



```python
print(data)
```

    A2_mosquito_data_mosquitos_vs_tempC.png


* doesn't work! 
* in juypter we have to explicitly 'reload' the module and this requies importing it from the importlib
* there's also `autoreload` extension 



```python
from importlib import reload
reload(analyze)
```




    <module 'analyze' from '/Users/jtdennis/workshops/intermed-py/analyze.py'>




```python
data = analyze.create_mosquitos_vs_tempC_plot("A2_mosquito_data.csv")
```

    Loading A2_mosquito_data.csv
    Plotting A2_mosquito_data.csv
    Saving A2_mosquito_data_mosquitos_vs_tempC.png



![png](Analyzing%20Mosquito%20Data%20Short_files/Analyzing%20Mosquito%20Data%20Short_135_1.png)



```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>temperature</th>
      <th>rainfall</th>
      <th>mosquitos</th>
      <th>temperature_C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1960</td>
      <td>82</td>
      <td>200</td>
      <td>180</td>
      <td>27.777778</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1961</td>
      <td>70</td>
      <td>227</td>
      <td>194</td>
      <td>21.111111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1962</td>
      <td>89</td>
      <td>231</td>
      <td>207</td>
      <td>31.666667</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1963</td>
      <td>74</td>
      <td>114</td>
      <td>121</td>
      <td>23.333333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1964</td>
      <td>78</td>
      <td>147</td>
      <td>140</td>
      <td>25.555556</td>
    </tr>
  </tbody>
</table>
</div>




```python
!ls *.png
```

    A1_mosquito_data_mosquitos_vs_tempC.png B1_mosquito_data_mosquitos_vs_tempC.png
    A2_mosquito_data_mosquitos_vs_tempC.png


**Last step -create a Python script that let's us run the above script from the command line**

1. Open another ext file
2. Call it run_analyze_script
3. Add the below to the file (using the cat command to print the file to the notebook)


```python
!cat run_analyze_script.py
```

    import analyze
    import sys 
    
    #filename = "a2_mosquito_data.csv"
    #argv[0] our script filename
    filename = sys.argv[1]
    
    analyze2.create_mosquitos_vs_tempC_plot(filename)


A note about the above: 

`sys.argv[1]` is the second element of the command line arguements - in this case the script filename is the first. So:
>python scriptname.py filename.csv 

sys.argv[0] is scriptname.py  
sys.argv[1] is filename.csv 

1. Lastly open a terminal console (cmd in win)
2. Go to the same directory of the file 
3. Type: `python run_analyze_script.py B1_mosquito_data.csv` in the command line and enter

* Yay! good job. 


```python

```
