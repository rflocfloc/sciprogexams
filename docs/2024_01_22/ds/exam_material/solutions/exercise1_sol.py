import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt




def max_min_salary(data):
    min_s = data[data.salary == data.salary.min()]
    print("min salary:")
    print("\t category: ",min_s.job_category.item())
    print("\t location:",min_s.company_location.item())
    print("\t salary:   ",min_s.salary.item())
    
    min_s = data[data.salary == data.salary.max()]
    print("MAX salary:")
    print("\t category: ",min_s.job_category.item())
    print("\t location:",min_s.company_location.item())
    print("\t salary:   ",min_s.salary.item())
    



def get_exp_level(data,company_location,company_size):
    a = data[data.company_location == "Ireland"]
    a = a[a.company_size == "M"]
    
    return a[a.salary_in_usd == a.salary_in_usd.max()].experience_level.item()



def average_salary_over_time(data,work_setting="Remote",employee_residence="Canada"):
    
    d = data[data.work_setting == work_setting]
    d = d[d.employee_residence == employee_residence]
    
    res = dict()
    for y in d.work_year.unique():
        res[str(y)] = dict()
        tmp = d[d.work_year == y]
        
        for cat in tmp.job_category.unique():
            salary = tmp[tmp.job_category == cat]["salary_in_usd"].to_numpy()
            
            res[str(y)][cat] = [np.mean(salary),np.std(salary)]
    
    return res

def plot_jobs_category_over_time(data):
    job_categories = data['job_category'].unique()
    plt.figure(figsize=(12, 6))
    for category in job_categories:
        category_data = data[data['job_category'] == category]
        category_trend = category_data.groupby('work_year')['job_category'].count()
        plt.plot(category_trend, marker='o', label=category)

    plt.title('Job Trends Over Time by Job Category')
    plt.xlabel('Year')
    plt.ylabel('Number of Jobs')
    plt.legend(title='Job Category')#, loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.show()
    
# es 1
data = pd.read_csv("data/jobs_in_data.csv")


# es 2
max_min_salary(data)    


# es 3
get_exp_level(data,"Ireland","M")


# es 4
res = average_salary_over_time(data)
print(res)


# es 5  
# solution 1
with open("res_with_io.json", "w") as f:
    f.write(str(res))
# solution 2
with open('res_with_json.json', 'w') as f:
    json.dump(res, f,indent=4)


# es 6
plot_jobs_category_over_time(data)