import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# load the dataset
df = pd.read_csv("data/shopping_behavior_updated.csv")



#Build a function that returns the Gender of the oldest person with loacation equal to Montana

def get_older(df):
    tmp = df[df.Age == df.Age.max()]
    res = tmp[tmp.Location == "Montana"].Gender.item()
    return res
    

print("The gender of the oldest person in Montana is")
print(get_older(df))


def get_avg_rev(df,gender,size="M"):
    
    tmp = df[df.Gender == gender]
    tmp = tmp[tmp.Size == size]
    
    return tmp["Review Rating"].mean()
    
    
print("MALE with S \t",get_avg_rev(df,"Male","S"))
print("MALE with M \t",get_avg_rev(df,"Male"))
print("MALE with L \t",get_avg_rev(df,"Male","L"))
print("MALE with XL\t",get_avg_rev(df,"Male","XL"))


plt.figure(figsize=(10,3))
plt.subplot(131)
plt.hist(df.Gender,color="blue")
plt.title("Gender hist")
plt.subplot(132)
plt.hist(df.Size,color="red")
plt.title("Size hist")
plt.subplot(133)
plt.title("Category hist")
a,b = np.unique(df.Category.to_numpy(),return_counts=True)
plt.bar([0,1,2,3],b,color="orange")
plt.xticks([0,1,2,3],a,rotation=25)
plt.savefig("myplot.pdf", bbox_inches = 'tight')
plt.show()


def build_dictionary(df):
    res = dict()
    for l in df.Location.unique():
        _,c = np.unique(df[df.Location == l]["Discount Applied"].to_numpy(),return_counts=True)

        res[l] = c[1]/sum(c)

    return res

res = build_dictionary(df)
print(res)


def most_commond_item(res):
    for i,j in res.items():
        if j<0.35:
            tmp = df[df.Location == i] 
            v,c = np.unique(tmp["Item Purchased"].to_numpy(),return_counts=True)
            
            print(v[np.argsort(c)])
            print(c[np.argsort(c)])
            print(c)
            
            print("The most common item in ",i," is ", v[np.argmax(c)])
            
most_commond_item(res)
