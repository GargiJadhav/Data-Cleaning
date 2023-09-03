import pandas as pd

df = pd.read_csv("merged.csv")

print(df.shape)

print(df.columns)

df.drop(
    columns=[
        "Star_name.1","Distance.1","Mass.1","Radius.1","Luminosity",'Unnamed: 0','Unnamed: 6'
    ],inplace=True
)
print(df.columns)


df.to_csv("cleaned.csv")






