df1 = xl("C2:O96")
df2 = xl("P1:T86",headers=True)
ss= "RND" 
newSKU = []
for i in range(len(df1)):
    if df1.iat[i, 1] == "Gold Weight":
        newSKU.append(i)
print(newSKU)
currStyle = 0

for i in range(len(df2)):
    if pd.isna(df2.at[i, "SKU"]) == False:
        
        # Determine the search range for current style
        start_idx = newSKU[currStyle]
        end_idx = newSKU[currStyle + 1] if currStyle < len(newSKU) - 1 else len(df1)
        totalSS=0
        for y in range(start_idx, end_idx):
            for x in range(len(df1.columns)):

                if df1.at[y, x] == ss:
                    currCell = df1.at[y, x]
                    
                    q=0
                    while currCell == ss:
                        
                        totalSS= totalSS + df1.at[y+q, x + 4]
                        currCell= df1.at[q+1, x]
                        q+=1
                        
                    df2.at[i, "SS"] = round(totalSS,2)

                if df1.at[y, x] == "(gms)":
                    df2.at[i, "GW"] = round(df1.at[y + 1, x],2)
                if df1.at[y, x] == "Sub-Total":
                    df2.at[i, "JEW COST"] = round(df1.at[y, x + 2],2)
                
    else:
        if currStyle == len(newSKU) - 1:
            break
        if i + 1 == len(df2):
            break
        if pd.isna(df2.at[i + 1, "SKU"]) == False:
            currStyle = currStyle + 1
            print(currStyle)
for i in range(len(df2)):
    for j in range(len(df2.columns)):
        if df2.iat[i,j] == None or pd.isna(df2.iat[i,j]):
            df2.iat[i,j]= ' '

print(currStyle)
print(df2)
