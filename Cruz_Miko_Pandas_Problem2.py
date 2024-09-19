
#to gather the required output we first must load the main frame
df = pd.read_csv("cars.csv")
df

#utilizng the iloc function, we can gather the first five rows with an odd number of columns (including the index)
df.iloc[:5,1::2]

#to gather the 'Model' that contains a 'Mazda RX4' we can use the loc function to search for specific index in the mainframe
df.loc[df['Model'] == 'Mazda RX4']

# By utilizing the code from the previous problem, we can add more parameters to locate the specified value of 'cyl.'
df.loc[df['Model'] == 'Camaro Z28', ['Model', 'cyl']]

#tweaking the previous code to include the three cars using the .isin function and then adding an additional parameter 'gear' to locate the required output from the three cars
df.loc[df['Model'].isin(['Mazda RX4 Wag','Ford Pantera L', 'Honda Civic' ]),['Model','cyl','gear']]
