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
passing_movies_years = []
close_pass = []
close_pass_years = []
one_pass = []
one_pass_years = []
failed = []
failed_years = []
missing = []

for ind in final.index:
    if final['rating_y'][ind] == 3.0:
        passing_movies.append(final['title'][ind])
        passing_movies_years.append(int(final['year_x'][ind]))
    elif final['rating_y'][ind] == 2.0:
        close_pass.append(final['title'][ind])
        close_pass_years.append(int(final['year_x'][ind]))
    elif final['rating_y'][ind] ==1.0:
        one_pass.append(final['title'][ind])
        one_pass_years.append(int(final['year_x'][ind]))
    elif final['rating_y'][ind] ==0.0:
        failed.append(final['title'][ind])
        failed_years.append(int(final['year_x'][ind]))
    else:
        missing.append(final['movie_title'][ind])
print(f"How many passed: {len(passing_movies)}/250")
print(f"Average Years for passed: {sum(passing_movies_years)/len(passing_movies_years)}")
print(f"How many passed 2: {len(close_pass)}/250")
print(f"Average Years for passed 2: {sum(close_pass_years)/len(close_pass_years)}")
print(f"How many passed 1: {len(one_pass)}/250")
print(f"Average Years for passed 1: {sum(one_pass_years)/len(one_pass_years)}")
print(f"How many failed: {len(failed)}/250")
print(f"Average Years for failed: {sum(failed_years)/len(failed_years)}")
print(f"How many are missing: {len(missing)}/250")
for movie in failed:
    print(movie)

