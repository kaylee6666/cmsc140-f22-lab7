import pandas as pd

# Import data
data = pd.read_csv("city_temperature.csv")

# Create another column to record the max temperature at the given region
data["MaxTemp"] = data.groupby(by="Region")["AvgTemperature"].transform(max)

# Filter days with max temperature given the region
result = data[data["AvgTemperature"] == data["MaxTemp"]]

# Remove the new column
result = result.drop("MaxTemp", axis="columns")

# Print out to a csv file
result.to_csv("city_maxtemp.csv", index=False)