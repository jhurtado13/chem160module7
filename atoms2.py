names=["H", "He", "Li", "Be"]
masses=[1.008, 4.003, 6.491, 9.012]
Dict2={}
for i in range (len(names)):
    Dict2[names[i]]=masses[i]
print(Dict2)
print(Dict2["H"])
print("O" in Dict2)
