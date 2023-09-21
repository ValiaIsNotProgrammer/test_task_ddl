import pandas as pd
from sqlalchemy import create_engine

from config import *

url = "https://raw.githubusercontent.com/DenisPonizovkin/rc-task-back1/main/data.csv"
df = pd.read_csv(url, delimiter=';')

df = df.dropna(subset=['проект'])
df = df.fillna(0)

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

df.to_sql('data', engine, if_exists='replace', index=False)
engine.dispose()