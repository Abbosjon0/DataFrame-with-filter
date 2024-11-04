import pandas as pd
baza = {
    "ism": ["Ali", "Zarina", "Murod", "Sardor", "Gulnoza", "Bekzod", "Sevara", "Kamron", "Madina", "Dilshod"],
    "yosh": [15, 17, 16, 14, 13, 18, 17, 16, 15, 14],
    "jins": ["erkak", "ayol", "erkak", "erkak", "ayol", "erkak", "ayol", "erkak", "ayol", "erkak"],
    "maktab": ["22-maktab", "15-maktab", "12-maktab", "5-maktab", "7-maktab", "9-maktab", "6-maktab", "14-maktab", "10-maktab", "18-maktab"]
}
df=pd.DataFrame(baza)
#print(df)
#print("\n\n")
filter=df[(df["jins"]=="erkak") & (df["yosh"]>=15)]
#print(filter)

eng_katta_yosh = df["yosh"].max()
max=df[df["yosh"]==eng_katta_yosh]
print(max)