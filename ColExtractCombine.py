import pandas as pd
import os


path = os.path.dirname(os.path.realpath(__file__)) # Assigns the directory path to path

os.chdir(path) # changes working direcotory to path

flist = os.listdir(path) # Creates a list of file names in the directory

video_list = []

ratings_combined = pd.DataFrame()

for f in flist:
    if f.endswith(".csv"):
        rating_df = pd.read_csv(f)
        colnames = list(rating_df.columns.values)
        rating_colname = colnames[1]
        video_list.append(rating_colname)
                
        rating_df = rating_df[rating_colname]
        rating_df = rating_df.to_frame()
        ratings_combined = pd.concat([ratings_combined, rating_df], axis=1)

video_list = pd.DataFrame(video_list)
print(video_list)

video_list.to_csv("video_name_list.csv", header=False)
ratings_combined.to_csv("ratings_combined.csv", header=True)