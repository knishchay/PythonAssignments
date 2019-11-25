ob = [{'pId':'1','pName':'Watch', 'cost':'100','brand':'Titan','rating':'3',"discount":'20',"category":"Accessories"},
      {'pId':'2','pName':'Perfume','cost':'500','brand':'Titan','rating':'2',"discount":'10',"category":"Grooming"},
      {'pId':'3','pName':'Refrigerator','cost':'700','brand':'LG','rating':'4',"discount":'25',"category":"Home"},
      {'pId':'4','pName':'HarryPotter','cost':'400','brand':'Fiction','rating':'5',"discount":'15',"category":"Books"}
      
    ] 
  
def sorting(i):
        switcher={
                0:'cost',
                1:'rating',
                2:'discount',
                
            }
       
        sortCategory=switcher.get(i)
        sortType = int(input("Enter 1 if sort in ascending order"))
        if(sortType==1):
            ob.sort(key=lambda el: el[sortCategory])
            print(ob)

        else:
            ob.sort(key=lambda el: el[sortCategory],reverse=True)

            print(ob)
categor=int(input("Enter category: 0:cost, 1:rating, 2:discount"))
sorting(categor)

print("-----------------------------------------------------------")

brandName=input("Enter brand name")
newobj = filter(lambda el:el["brand"]==brandName,ob)
for i in newobj:
    print('{pName} {brand}'.format(**i))
    
print("--------------------------")
prodName=input("Enter product name")
newobj = filter(lambda el:el["pName"]==prodName,ob)
for i in newobj:
    print('{pName} {brand}'.format(**i))