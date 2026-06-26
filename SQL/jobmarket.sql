SELECT * FROM jobmarketingcampaignanalytics.`clean_job_market_dataset(sheet1)`;

#Total Candidates
select count(candidate_id) from `clean_job_market_dataset(sheet1)`;

#Total Job Roles
select count(distinct(job_role)) as Total_job_roles from `clean_job_market_dataset(sheet1)`;

#Total Cities
select count(distinct(city)) as Total_cities from `clean_job_market_dataset(sheet1)`;

#Total Source
select count(distinct(source)) as Total_sources from `clean_job_market_dataset(sheet1)`;

#Total Offer Status
select count(distinct(offer_status)) as Total_offer_status from `clean_job_market_dataset(sheet1)`;

#Total Candidates Per Job Roles
select job_role,count(candidate_id) as Total_candidates from `clean_job_market_dataset(sheet1)` group by job_role;

#Total Candidates per city
select city,count(candidate_id) as Total_candidates from `clean_job_market_dataset(sheet1)` group by city;

#Total Candidates on each source
select source,count(candidate_id) as Total_candidates from `clean_job_market_dataset(sheet1)` group by source;

#which candidate has highest experience year
select candidate_id,candidate_name,max(experience_years) as Highest_experience_candidate from `clean_job_market_dataset(sheet1)` group by candidate_id,candidate_name order by Highest_experience_candidate desc limit 1;

#which candidate has highest expected_salary
select candidate_id,candidate_name,max(expected_salary) as Highest_expected_salary_candidate from `clean_job_market_dataset(sheet1)` group by candidate_id,candidate_name order by Highest_expected_salary_candidate desc limit 1;

#which candidate has highest interview score
select candidate_id,candidate_name,max(interview_score) as Highest_interview_score from `clean_job_market_dataset(sheet1)` group by candidate_id,candidate_name order by Highest_interview_score desc limit 1;

#Total candidates who are offered in offered_status
select offer_status,count(candidate_id) as Total_candidates from `clean_job_market_dataset(sheet1)` group by offer_status having offer_status="Offered";

#Total job roles per city
select city,count(distinct(job_role)) as Total_job_roles from `clean_job_market_dataset(sheet1)` group by city;

#Total job roles on source
select source,count(job_role) as Total_job_roles from `clean_job_market_dataset(sheet1)` group by source;

#highest experience_years in job roles
select job_role,max(experience_years) as High_exp_job_role from `clean_job_market_dataset(sheet1)` group by job_role order by high_exp_job_role desc;

#average salary per job role
select job_role,avg(expected_salary) as average_salary from `clean_job_market_dataset(sheet1)` group by job_role;

#Lowest salary in job roles
select job_role,min(expected_salary) as minimum_salary from `clean_job_market_dataset(sheet1)` group by job_role;

#offer status reject on each job_role
select job_role,count(offer_status) as reject  from `clean_job_market_dataset(sheet1)` where offer_status="Rejected" group by job_role;

#average experience candidates in each city
select city,avg(experience_years) as average_experience_year from `clean_job_market_dataset(sheet1)` group by city;

#which  city has highest salary 
select city,max(expected_salary) as highest_salary from `clean_job_market_dataset(sheet1)` group by city order by highest_salary desc;

#which city has highest pending status
select city,count(offer_status) as highest_pending_offer_status from `clean_job_market_dataset(sheet1)` where offer_status="Pending" group by city order by highest_pending_offer_status desc;

#which source has highest expected salary for candidates
select source,max(expected_salary) as highest_expected_salary from `clean_job_market_dataset(sheet1)` group by source order by highest_expected_salary desc;

#which source has highest offered jobs for candidates
select source,count(offer_status) as highest_offered_offer_status from `clean_job_market_dataset(sheet1)` where offer_status="Offered" group by source order by highest_offered_offer_status desc;

#earliest and latest application date for jobs
select min(application_date) as earliest_application,max(application_date) as latest_application from `clean_job_market_dataset(sheet1)`;

#month vise applications
select monthname(application_date) as month, count(*) as total_application from `clean_job_market_dataset(sheet1)` group by month(application_date), monthname(application_date) order by month(application_date);

#job roles by number of opening
select job_role,count(job_role)as total_jobs,rank() over(order by count(*) desc) as job_rnk from `clean_job_market_dataset(sheet1)` group by job_role;

#top paying jobs in each city
select * from(select city,job_role,expected_salary,row_number() over(partition by city order by expected_salary desc)as rn from `clean_job_market_dataset(sheet1)`)t where rn=1;

#highest experience required per jobs
select * from(select job_role,experience_years,dense_rank() over(partition by job_role order by experience_years desc) as exp_rnk from `clean_job_market_dataset(sheet1)`)t where exp_rnk=1;

# overall second highest salary 
select * from(select expected_salary,dense_rank() over(order by expected_salary desc) as salary_rnk from `clean_job_market_dataset(sheet1)`)t where salary_rnk=2;

#offer conversation rate
select round(count(case when offer_status="Offered" then 1 End)*100/count(*),2) as offer_conversion_rate from `clean_job_market_dataset(sheet1)`;

#salary vs experience
SELECT experience_years,AVG(expected_salary) avg_salary FROM `clean_job_market_dataset(sheet1)` GROUP BY experience_years ORDER BY experience_years;

