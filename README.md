# Database_Project
This Project's main goal is to hold the data of “Prisons in India” in a Database.
This Database holds information on all the prisons, including staff, budget, and income details of the prisons.
Holds personal details of the prisoners, illness details, released prisoner details, and the information surrounding the deaths of the prisoners.
Holds information on sections(laws and charges of the crimes) according to the Indian Penal Code(IPC).
Has statistical information on the number of prisoners in each state and year.
Holds gender and age-specific numbers based on different crimes.

#ER-Diagram of the database

<img width="899" alt="ER-Diagram_final_project" src="https://user-images.githubusercontent.com/113804196/202076015-60483a8c-1ec2-458a-98cc-c0f3e0f862ae.png">

# Web Application created using Streamlit Framework:
![UI](https://user-images.githubusercontent.com/113804196/202076301-2e50e2fc-1c09-4d45-9d12-23a17603f1b4.png)

# Prisons Database
Use Prisons Database by following the below steps.

Step 1: Install PostgreSQL in your local environment.
        Download Link: https://www.postgresql.org/download/

Step 2: Create a database and restore 'dbms_final_backup.tar' file 
        from the prisons_db_backup folder above. you will have the database online to work with.

# Web App
Access Web App using the following steps

Step 1: Download DBMS_project folder

Step 2: Open Command prompt and go to the file path of downloaded files in the local environment.

Step 3: Run pip install -r requirements.txt

Step 4: Open Connection.py file using visual studio app and update your postgresql credentials.

Step 5: Run pip install streamlit

Step 6: Run py -m streamlit run main.py

Step 7: You can access the web application and enter the details from the web to the database.


Dataset used for 'Prisons in India' database: https://www.kaggle.com/datasets/rajanand/prison-in-india?select=Jail+wise+population+of+prison+inmates.csv
