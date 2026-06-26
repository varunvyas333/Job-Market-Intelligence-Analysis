import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv("C:\\Users\\jeetv\\OneDrive\\Desktop\\data analyst projects\\job marketing campaign analytics\\Job_Market_All_Roles_Dirty_15000 1(Sheet1).csv")
print(df1.head())
print(df1.tail())
print(df1.describe())
print(df1.info())
print(df1.shape)
print(df1.isnull().sum())
df1["city"] = df1["city"].fillna("Baroda")
df1['expected_salary']=df1['expected_salary'].fillna(50000)
df1["interview_score"] = df1["interview_score"].fillna(60)
print(df1.isnull().sum())

print("Number of duplicate rows:", df1.duplicated().sum())
print("Removing duplicate rows...",df1.drop_duplicates(inplace=True))

df1["city"] = df1["city"].replace({
    "Ahemdabad": "Ahmedabad"
})

#city wise candidates
print(df1["city"].value_counts())

#source of the candidates
df=df1["source"].value_counts()
print(df)

#offered positions
df=(df1["offer_status"]=="Offered").sum()
print("Number of offered positions:", df)

#top job role
df=df1['job_role'].value_counts()
print(df)

#average salary by role
df=df1.groupby('job_role')['expected_salary'].mean().sort_values(ascending=False)
print("Average salary by role:")
print(df)

#top hiring cities
df= df1["city"].value_counts()
print("Number of candidates by city:")
print(df)

#average salary by city
df=df1.groupby('city')['expected_salary'].mean().sort_values(ascending=False)
print("Average salary by city:")
print(df)

#total candidates by source
df=df1.groupby('source')['candidate_id'].count().sort_values(ascending=False)
print("Total candidates by source:")
print(df)   

#total salary by ahmedabad city
df=df1[df1['city']=="Ahmedabad"]['expected_salary'].sum()
print("Total salary by Ahmedabad city:")
print(df)

#job role who is offered the most
df=df1[df1['offer_status']=="Offered"]['job_role'].value_counts().idxmax()
print("Job role who is offered the most:", df)

#job role who is offered the least
df=df1[df1['offer_status']=="Offered"]['job_role'].value_counts().idxmin()
print("Job role who is offered the least:", df)

#which job role has the highest salary
df=df1.groupby('job_role')['expected_salary'].max().sort_values(ascending=False).idxmax()
print("Job role with the highest salary:", df)

#which job role has the lowest salary
df=df1.groupby('job_role')['expected_salary'].min().sort_values(ascending=True).idxmin()
print("Job role with the lowest salary:", df)

#which candidate has the highest salary
df=df1.groupby('candidate_id')['expected_salary'].max().sort_values(ascending=False).idxmax()
print("Candidate with the highest salary:", df)

#which candidate has the lowest salary
df=df1.groupby('candidate_id')['expected_salary'].min().sort_values(ascending=True).idxmin()
print("Candidate with the lowest salary:", df)

#which candidate has highest experience years
df=df1.groupby('candidate_id')['experience_years'].max().sort_values(ascending=False).idxmax()
print("Candidate has highest experience is",df)

#which job role has highest rejected offer status
df=df1[df1['offer_status']=="Rejected"]["job_role"].value_counts()
print("rejected offer status by job role",df)

#which job role has highest offering status
df=df1[df1['offer_status']=="Offered"]["job_role"].value_counts()
print("highest offering status by job role",df)

#average interview score by job role
df=df1.groupby("job_role")["interview_score"].mean().sort_values(ascending=False)
print("average interview score by job role",df)

#top source by each role
df=df1.groupby("job_role")["source"].max().sort_values(ascending=False)
print("top source by each role",df)

df1.to_excel("clean_job_market_dataset.xlsx",index=False)

# 1. Source Wise Candidates
source_counts = df1["source"].value_counts()
plt.figure(figsize=(8,5))
plt.bar(source_counts.index, source_counts.values)
plt.title("Candidates by Source")
plt.xlabel("Source")
plt.ylabel("Number of Candidates")
plt.xticks(rotation=45)
plt.show()

# 2. Job Role Wise Candidates
role_counts = df1["job_role"].value_counts()
plt.figure(figsize=(10,5))
plt.bar(role_counts.index, role_counts.values)
plt.title("Candidates by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Number of Candidates")
plt.xticks(rotation=90)
plt.show()

# 3. Average Salary By Role
salary_role = (
    df1.groupby("job_role")["expected_salary"]
    .mean()
    .sort_values()
)
plt.figure(figsize=(10,6))
plt.barh(salary_role.index, salary_role.values)
plt.title("Average Salary By Role")
plt.xlabel("Average Salary")
plt.ylabel("Job Role")
plt.show()



# 4. Offer Status Distribution
offer_status = df1["offer_status"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    offer_status.values,
    labels=offer_status.index,
    autopct="%1.1f%%"
)
plt.title("Offer Status Distribution")
plt.show()


# 5. Offer Status By Source
pd.crosstab(
    df1["source"],
    df1["offer_status"]
).plot(
    kind="bar",
    stacked=True,
    figsize=(10,5)
)
plt.title("Offer Status by Source")
plt.xlabel("Source")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 6. Top Hiring Cities
city_counts = df1["city"].value_counts()

plt.figure(figsize=(8,5))
plt.bar(city_counts.index, city_counts.values)
plt.title("Candidates by City")
plt.xlabel("City")
plt.ylabel("Number of Candidates")
plt.show()

# 7. Average Interview Score
score = (
    df1.groupby("job_role")["interview_score"]
    .mean()
    .sort_values()
)
plt.figure(figsize=(10,6))
plt.barh(score.index, score.values)
plt.title("Average Interview Score by Role")
plt.xlabel("Average Score")
plt.ylabel("Job Role")
plt.show()

