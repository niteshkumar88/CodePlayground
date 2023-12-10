import oracledb             # for oracle connectivity
import db_config            # fetching credentials from other file
import pandas as pd         # for sql results processing
from pandas import DataFrame

# Use the Oracle Instant Client to connect
oracledb.init_oracle_client()

# Connecting to the oracle database using oracledb
conn = oracledb.connect(user = db_config.username,
                        password = db_config.password,
                        dsn = db_config.dbserver)

# Storing a query
#sql = "Select * from employees"
sql = "SELECT EMPLOYEE_ID, COMMISSION_PCT, HIRE_DATE  FROM EMPLOYEES WHERE DEPARTMENT_ID=50"
#sql = "SELECT COMMISSION_PCT FROM EMPLOYEES WHERE DEPARTMENT_ID=50"
# Storing the query results in a pandas dataframe
df = pd.read_sql(sql, conn)

# Printing the results
print(df)