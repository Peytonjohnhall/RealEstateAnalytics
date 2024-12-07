import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

# Function to plot the USA
def plot_usa():
    """Plots a focused map of the USA with improved visibility."""
    plt.figure(figsize=(12, 8))
    m = Basemap(
        projection="lcc",
        resolution="l",
        llcrnrlon=-125, llcrnrlat=23,  # Extend lower-left to include southern border
        urcrnrlon=-66, urcrnrlat=52,   # Extend upper-right to include northern border
        lat_0=38.5, lon_0=-97.5       # Central latitude and longitude
    )

    # Draw filled continents with land gray and ocean light blue
    m.drawmapboundary(fill_color='lightblue')  # Ocean color
    m.fillcontinents(color='lightgrey', lake_color='lightblue')  # Land and lakes

    # Draw US state boundaries
    m.drawstates()

    # Remove unnecessary country boundaries (Canada and Mexico details)
    m.drawcountries(linewidth=0.5, color="black")  # Draw only the outer USA boundary

    # Add a title
    plt.title("Focused Map of the USA", fontsize=16)

    # Display the map
    plt.show()

# Function to define city coordinates (stub)
def city_coordinates():
    """Stub for city coordinates function."""
    # stub
    """
    # create the variables and assign coordinates to each
    San_Fran_CA =
    LA_CA =
    Seattle_WA =
    San_Diego_CA =
    NY_NY =
    Chicago_IL =
	Dallas_TX =
	Boston_MA =
	Denver_CO =
	Phoenix_AZ =
	Miami_FL =
	Atlanta_GA =
	DC =
	Vegas_NV =
	Tampa_FL =
	Portland_OR =
	Charolette_NC =
	Detroit_MI =
	Minneapolis_MN =
	Cleveland_OH =
    """
    pass

# Load the CSV file into a pandas DataFrame
csv_file_path = "s_p_housing_data.csv"  # Ensure this file is in the same directory
housing_data = pd.read_csv(csv_file_path)

# Main method
def main():
    """Main function to call the plot_usa function."""
    plot_usa()

# Call the main method
if __name__ == "__main__":
    main()
