# The cost of Database Management System

#### -- Project Status: [Completed]

## Project Intro/Objective
Calculate the cost of Google Cloud storage (including storage cost and running queries cost)
Calculate the cost of in-house server storage
Show visual graphes for hybrid storage with different fraction of cloud/on-premises storage
The attached files include:
A sample input folder name: Gov dataset, insisting of:

governors_county.csv
governors_county_candidate.csv
governors_state.csv
house_candidate.csv
house_state.csv
The datasets with the same names are downloaded from: https://www.kaggle.com/unanimad/us-election-2020?select=senate_state.csv
The sample input files are those with 100 lines in each file.

Jupyter code file name: cost_analysis.ipynb, including 8 functions:

cloud_storage_cost(): user inputs the amount of storage (in GB), return the cost (in dollar) to store the dataset in one month on Google Cloud. The unit price is $0.023/GB/month
cloud_storage_cost1(x): same as cloud_storage_cost() but no user input
premises_storage_cost(): user inputs the amount of storage (in GB), return the cost (in dollar) to store the dataset in one month on premises. The unit price is $0.0427/GB/month
premises_storage_cost1(x): same as premises_storage_cost() but no user input
check_file_size(): given a folder or a file path, return the sum of the size of all files in that folder/file (in GB)
check_number(): given a parameter, return true if it is a number, return false if other.
hybrid_cost(): user inputs the amount of storage and fraction of amount stored in cloud. Returns the cost of hybrid database system.
hybrid_cost1(h_amount,frac): same as hybrid_cost() but no user input. The parameters are the amount of storage and fraction of amount stored in cloud.
hybrid_cost_list(h_amount1, frac_list =[]: return the cost of the hybrid system with any input fraction cloud/on-premises. The parameter is a list of fraction of cloud storage (eg: 0.5), the remaining portion is the on-premise storage
hybrid_premise_graph(storage_amount, frac_list1 = []): show a bar graph showing the cost of hybrid and on-premises database system with different fraction. The parameters are the storage amount in GB and a list of fraction of cloud storage.
To run the codes, just need to open jupyter lab, open file cost_analysis.ipynb, call the method with parameters and hit the run button (arrow sign)

SQL code file

Query_cost(): Calculates the queries total cost and execution time and returns the query, total cost, execution time. To exectue this query you are able to paste multiple queries and it will order it by the duration time. Put this function in your preferred query tool and create this function. Then to use this function you will need to execute SELECT * FROM query_cost( ARRAY["Your Query Goes Here"]) ORDER BY duration DESC, this will return a table with your query, cost, and exectution time.
Explain(): This is a in-build funtion in SQL that will return the cost of the query executed. To execute this query you will need to use a query tool that you prefer and execute "Explain "Your Query Goes Here"". This will return the query and the cost.

## Contributing DSWG Members
#### Team Members:

|Name     |  Slack Handle   | 
|---------|-----------------|
|Nghi Nguyen (https://github.com/hoangkhanhnghi04/my-repository)
|Rudra Gandhi
