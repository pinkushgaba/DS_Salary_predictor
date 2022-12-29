import glassdoor_scraper as gs
import pandas as pd
path = "D:/Projects/DS Salary predictor/DS_Salary_predictor/chromedriver"

df = gs.fetch_jobs('data scientist', 'Toronto', 1, path, 5)