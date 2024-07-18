import pandas as pd
data = pd.read_csv("../../crop-data-extraction-pandas/data/crop_information.csv")
pd.set_option('display.max_columns',10)
pd.set_option('display.max_rows',500)
ch=int(input("do you want to know the crop \n\n1 . Type of Soil you have \n\n2 .the session you are planting the crop "
      "\n\n Enter the option You like to SELECT :  "))
if ch == 1 :
    so = int(input("\n\n\n1. Alluvial soil\n2. Black soil\n3. Clay loam\n4. Laterite soil\n5. Loamy soil\n6. Sandy loam"
                   "\n\n Enter the option You like to SELECT :   "))
    s=('Alluvial soil','Black soil','Clay loam','Laterite soil','Loamy soil','Sandy loam')
    print(data[['Crop Name','Type','Best Soil','Best Season','Time']][data['Best Soil']==s[so-1]][0:])
elif ch == 2 :
    se = int(input("\n\n\n1. Kharif\n2. Rabi \n\n which season do you plan to plant the CROP (1 or 2) : "))
    s =('Kharif','Rabi')
    print(data[(data["Best Season"] == s[se-1])][['Crop Name','Type','Best Season','Best Soil','Time']])
else:
    print("noties: sorry,you have entered the wrong option!!")