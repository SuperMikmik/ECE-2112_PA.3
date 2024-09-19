
#as per instruction, we must read the file provided
df = pd.read_csv("cars.csv")

#as specified, we must output the first five rows a (this is achieved through using the head function)
df.head()

#and as for the last 5 rows (we can utilize the tail function)
df.tail()
