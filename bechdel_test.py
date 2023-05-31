from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import json

bechdel_results = requests.get("http://bechdeltest.com/api/v1/getAllMovies")
bechdel_data = bechdel_results.json()
bechdel_df = pd.json_normalize(bechdel_data)
bechdel_df.to_csv('bechdel_all_movies.csv')

# print("Starting")
# imdb_movies = pd.read_csv("imdb_top_250_movies.csv")
# bechdel_movie_titles = []
# print("read in imdb data")
# bechdel_movie_years = []
# bechdel_movie_score = []
# counter = 1
# list_len = len(imdb_movies['movie_title'])
# review = []
# for id in imdb_movies['imdb_id']:
#     print("Starting Bechdel requests")
#     print("Waiting on bechdel requests")
#     bechdel_result = requests.get(f"http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid={id}")
#     print("received bechdel requests")
#     if bechdel_result.status_code == 200:
#         bechdel_list_dict = bechdel_result.json()
#         if len(bechdel_list_dict) == 1:
#             bechdel_dict = bechdel_list_dict[0]
#             bechdel_movie_titles.append(bechdel_dict['title'])
#             bechdel_movie_score.append(bechdel_dict['rating'])
#             bechdel_movie_years.append(bechdel_dict['year'])
#             print(f"finished {counter}/{list_len}")
#         else:
#             review.append(bechdel_list_dict)
#         counter += 1
#     else:
#         raise TypeError(f"{bechdel_result.status_code}")
#
#
# bechdel_data = {
#     "movie_title": bechdel_movie_titles,
#     "bechdel_score": bechdel_movie_score,
#     "year_released": bechdel_movie_years
# }
# df = pd.DataFrame(data=bechdel_data)
# df.to_csv('bechdel_imdb_top_250_movies.cav')