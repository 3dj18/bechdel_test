from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import json

# bechdel_df = pd.read_csv('bechdel_all_movies.csv')
# imdb_movies = pd.read_csv('imdb_top_250_movies.csv')
#
# merged_left = pd.merge(left=imdb_movies, right=bechdel_df, how='left', left_on='imdb_id', right_on='imdbid')
# merged_left.to_csv('final_report.csv')

final = pd.read_csv('final_report.csv')
passing_movies = []
close_pass = []
one_pass = []
failed = []
missing = []

for ind in final.index:
    if final['rating_y'][ind] == 3.0:
        passing_movies.append(final['title'][ind])
    elif final['rating_y'][ind] == 2.0:
        close_pass.append(final['title'][ind])
    elif final['rating_y'][ind] ==1.0:
        one_pass.append(final['title'][ind])
    elif final['rating_y'][ind] ==0.0:
        failed.append(final['title'][ind])
    else:
        missing.append(final['movie_title'][ind])
print(f"How many passed: {len(passing_movies)}/250")
print(f"How many passed 2: {len(close_pass)}/250")
print(f"How many passed 1: {len(one_pass)}/250")
print(f"How many failed: {len(failed)}/250")
print(f"How many are missing: {len(missing)}/250")
for movie in missing:
    print(movie)

