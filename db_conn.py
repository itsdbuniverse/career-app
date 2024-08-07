import snowflake.connector
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
  

