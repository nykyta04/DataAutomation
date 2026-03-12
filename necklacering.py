df1= xl("A1:W123",headers=True)
df2= xl("Z1:AD123", headers=True)

for i in range(len(df1)):
    currSku= df1.at[i,"SKU"]
    for j in range(len(df2)):
        if df2.at[j,"SKU"]== currSku:
            breakIndex=j
    df1.at[i,"SS"]=df2.at[breakIndex,"SS"]
    df1.at[i,"GW"]=df2.at[breakIndex,"GW"]
    df1.at[i,"JEW COST"]=df2.at[breakIndex,"JEW COST"]
    df1.at[i,"TOTAL COST"]=df1.at[i,"JEW COST"]+df1.at[i,"DIA COST"]
    

print(df1)
