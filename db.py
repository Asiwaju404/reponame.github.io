import psycopg2

import environ
env = environ.Env()
environ.Env.read_env()

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    port=5433,
    user='postgres',
    password=env('DBPASS'),
    database=env('DATABASE')
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the employee table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS hr_assist
            (id SERIAL PRIMARY KEY,
            employee TEXT NOT NULL,
            leave_request TEXT NOT NULL,
            start_date DATE,            
            due_date DATE,
            password_request TEXT NOT NULL,
            salary_review TEXT NOT NULL,
            peformance_review TEXT NOT NULL,
            travel_request TEXT NOT NULL,
            onboarding TEXT NOT NULL,
            priority INTEGER)''')

# Insert sample task into the employee table
cursor.execute("INSERT INTO hr_assist (employee, leave_request, start_date, due_date, password_request, salary_review, peformance_review, travel_request, onboarding, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               ('Adams Johnson', 'Appproved', '2023-05-01', '2023-05-03', 'Solved', 'Pending', 'Reviewed', 'Pending', 'Started', 1))
cursor.execute("INSERT INTO hr_assist (employee, leave_request, start_date, due_date, password_request, salary_review, peformance_review, travel_request, onboarding, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               ('Will Smith', 'Approved', '2023-05-03', '2023-05-05', 'Solved', 'Reviewed', 'Reviewed', 'Pending', 'Started', 2))
cursor.execute("INSERT INTO hr_assist (employee, leave_request, start_date, due_date, password_request, salary_review, peformance_review, travel_request, onboarding, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               ('Mich Asher', 'Approved', '2023-05-05', '2023-05-05', 'Solved', 'Pending', 'Reviewed', 'Pending', 'Started', 3))
cursor.execute("INSERT INTO hr_assist (employee, leave_request, start_date, due_date, password_request, salary_review, peformance_review, travel_request, onboarding, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               ('John Fang', 'Approved', '2023-05-08', '2023-05-05', 'Solved', 'Reviewed', 'Reviewed', 'Pending', 'Started', 4))
cursor.execute("INSERT INTO hr_assist (employee, leave_request, start_date, due_date, password_request, salary_review, peformance_review, travel_request, onboarding, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               ('Walter Simons', 'Not_Approved', '2023-05-10', '2023-05-05', 'Solved', 'Reviewed', 'Reviewed', 'Pending', 'Started', 5))
cursor.execute("INSERT INTO hr_assist (employee, leave_request, start_date, due_date, password_request, salary_review, peformance_review, travel_request, onboarding, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
               ('Cole John', 'Not_Approved', '2023-05-10', '2023-05-05', 'Solved', 'Pending', 'Reviewed', 'Pending', 'Started', 6))

# Commit the changes and close the connection
conn.commit()
conn.close()