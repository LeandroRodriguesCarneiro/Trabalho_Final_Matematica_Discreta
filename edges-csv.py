import pandas as pd

df = pd.read_csv('data\\fb-pages-food.edges')
df['Type'] = 'Undireted'
df.to_csv('csv\\fb-pages-food-edges.csv', index=False)