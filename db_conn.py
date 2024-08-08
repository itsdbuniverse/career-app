import snowflake.connector
import random

def query_runner(*,query):
  conn = snowflake.connector.connect(
    user= 'wproject889',
    password= 'Project@1234',
    account= 'vzjbhak-ns71761',
    warehouse= 'wipro_careers',
    database= 'wipro_careers',
    schema= 'wipro_careers',
    table= 'jobs'
    
    )
  if conn:
    cursor=conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results
  else:
    print("no connection")

def bring_data(query, params=None):
  conn = snowflake.connector.connect(
      user='wproject889',
      password='Project@1234',
      account='vzjbhak-ns71761',
      warehouse='wipro_careers',
      database='wipro_careers',
      schema='wipro_careers',
      table='jobs'
  )
  try:
      cursor = conn.cursor()
      cursor.execute(query, params)
      result_data = cursor.fetchall()
      return result_data
  except snowflake.connector.errors.DatabaseError as e:
      print(f"Database error: {e}")
      return None
  finally:
      cursor.close()
      conn.close()

def add_data_to_db(*,job_id, full_name, email, linkedin_url,education, work_experience, resume_url):
  print("::FUNC CALLED")
  conn = snowflake.connector.connect(
      user='wproject889',
      password='Project@1234',
      account='vzjbhak-ns71761',
      warehouse='wipro_careers',
      database='wipro_careers',
      schema='wipro_careers'
  )
  print("::DB CONNECTED::")
  try:
      id = str(random.randint(100, 999))
      cursor = conn.cursor()
      query = "INSERT INTO applications  VALUES (%s,%s, %s,%s,%s,%s,%s,%s)"
      cursor.execute(query, (id,job_id, full_name, email, linkedin_url, education, work_experience, resume_url))
      conn.commit()
      print("Data added to the database successfully.")
      
  except snowflake.connector.errors.DatabaseError as e:
      print(f"Database error: {e}")
  finally:
      cursor.close()
      conn.close()