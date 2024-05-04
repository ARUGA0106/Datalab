"""
Netflix! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.

Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry. Our friend has also been brushing up on their Python skills and has taken a first crack at a CSV file containing Netflix data. They believe that the average duration of movies has been declining. Using your friends initial research, you'll delve into the Netflix data to see if you can determine whether movie lengths are actually getting shorter and explain some of the contributing factors, if any.

You have been supplied with the dataset `netflix_data.csv` , along with the following table detailing the column names and descriptions. This data does contain null values and some outliers, but handling these is out of scope for the project. Feel free to experiment after submitting!
"""
## The data
### **netflix_data.csv**
| Column | Description |
|--------|-------------|
| `show_id` | The ID of the show |
| `type` | Type of show |
| `title` | Title of the show |
| `director` | Director of the show |
| `cast` | Cast of the show |
| `country` | Country of origin |
| `date_added` | Date added to Netflix |
| `release_year` | Year of Netflix release |
| `duration` | Duration of the show in minutes |
| `description` | Description of the show |
| `genre` | Show genre |



#importing pandas as pd
import pandas as pd
#importing matplotlib as plt
import matplotlib.pyplot as plt
# loading CSV file
netflix_df = pd.read_csv('netflix_data.csv', index_col = 0)
print(netflix_df)
#filtering the data to remove TV show
netflix_subset = netflix_df[netflix_df['type']=='movie']
print(netflix_subset)
# filtering the subsset to remove movies
import pandas as pd

# Load the CSV file
netflix_df = pd.read_csv('netflix_data.csv')

# Filter the data to remove TV shows
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

# Investigate and subset Netflix movie data
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

print(netflix_movies.head())
#Filter netflix_movies to find the movies that are strictly shorter than 60 minutes, saving the resulting DataFrame as short_movies;
short_movies = netflix_movies[netflix_movies['duration'] <60]
print(short_movies.head())
#Using a for loop and if/elif statements to iterate through the rows of netflix_movies and assign colors of my  choice to the four genre groups ("Children", "Documentaries", "Stand-Up", and "Other" for everything else), then saving the results in a colors list.
# Define color mappings for each genre group
color_mappings = {
    "Children": "blue",
    "Documentaries": "green",
    "Stand-Up": "orange"
}

# Initialize an empty list to store colors
colors = []

# Iterate through the rows of netflix_movies and assign colors based on genre
for index, row in netflix_movies.iterrows():
    genre = row['genre']
    if genre in color_mappings:
        colors.append(color_mappings[genre])
    else:
        colors.append("gray")  # Assign gray color for "Other" genres

# Printing the colors list to verify
print(colors)

#initializing matsploit figure and storing the result
import matplotlib.pyplot as plt

# Initialize matplotlib figure object
fig = plt.figure(figsize=(10, 6))

# Create scatter plot for movie duration by release year
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors, alpha=0.5)

# Add labels and title
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')

# Show the plot
plt.show()
