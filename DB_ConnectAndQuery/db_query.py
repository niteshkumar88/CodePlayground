import oracledb            # Importing to connect oracle database
import db_config       # to get the credentials from another files


# Python-oracledb's default Thin mode can connect to Oracle Database 12.1 or later.
# If you want to connect to Oracle Database 11.2 you need to enable Thick mode by calling
# oracledb.init_oracle_client() in your code.
# Use the Oracle Instant Client to connect
oracledb.init_oracle_client()

with oracledb.connect(user=db_config.username, password=db_config.password,
                      dsn=db_config.dbserver) as connection:
    with connection.cursor() as cursor:
        sql = """select * from EMPLOYEES"""
        for r in cursor.execute(sql):
            print(r)

# Below code is to write the sql query result set to a file
#sqlFile = "select * from EMPLOYEES"

# Run the SQL (sqlFile) on the connection (engine)
#pd.read_sql(sqlFile).to_csv('C:\Users\nites\Documents\Learnings\test.csv', header=True, index=False, sep='|')
