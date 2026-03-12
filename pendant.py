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
    centDia= df1.at[i, "CENTER DIA."]
    if centDia<.45:
        df1.at[i,"CHAIN SKU"]= 4801168
        df1.at[i,"CHAIN GW"]= 1.20
        df1.at[i,"CHAIN COST"]= 100
    elif centDia<.7:
        df1.at[i,"CHAIN SKU"]= 5055137
        df1.at[i,"CHAIN GW"]= 1.45
        df1.at[i,"CHAIN COST"]= 200
    else:
        df1.at[i,"CHAIN SKU"]= 5074553
        df1.at[i,"CHAIN GW"]= 2.45
        df1.at[i,"CHAIN COST"]= 300
    
    df1.at[i,"TOTAL GW"]=df1.at[i,"GW"]+df1.at[i,"CHAIN GW"]
    df1.at[i,"TOTAL JEW COST"]=df1.at[i,"JEW COST"]+df1.at[i,"CHAIN COST"]
    df1.at[i,"TOTAL COST"]=df1.at[i,"JEW COST"]+df1.at[i,"CHAIN COST"]+df1.at[i,"DIA COST"]
    

print(df1)
