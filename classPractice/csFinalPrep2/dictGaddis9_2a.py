provinces=["Anhui", "Fuzhou","Gansu", "Guangdong","Guizhou"]
capitals=["Hefei","Fujian","Lanzhou","Guangzhou", "Guiyang"]

capitalOfProvinces={}
for i in range(len(provinces)):#remember, capitals[i] will give you capital of provinces[i].
    capitalOfProvinces[provinces[i]]=capitals[i]

