import pandas as pd

df = pd.read_csv('data\\fb-pages-food.nodes')
df.rename(columns={'id':'remove', 'name':'Label', 'new_id': "Id"},inplace=True)
df.drop('remove',axis=1,inplace=True)
df.sort_index(axis=1,inplace=True)
df.to_csv('csv\\fb-pages-food-nodes.csv',index=False)