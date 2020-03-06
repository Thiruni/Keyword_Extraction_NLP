import pandas as pd
testText = []

dataSet = pd.read_csv('venv/Data/News_Category_Description.csv', names=['ID', 'short_description'], header=1)
for text4 in dataSet["short_description"]:
    text4 = str(text4)
    testText.append(text4)
print("size of data", len(testText))

print(len(testText))

df = pd.DataFrame(testText, columns=['text'])
print(df)
df.to_csv('dataa2.csv')
