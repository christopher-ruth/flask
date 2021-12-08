import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'project',
    user = 'root',
    password = ''
)




mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS register(
        hospital_name VARCHAR(255) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(40) NOT NULL,
        confirm_password VARCHAR(40) NOT NULL,
        UNIQUE(email)
    );
    """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS login(
        email VARCHAR(100) NOT NULL,
        password VARCHAR(40) NOT NULL,
        UNIQUE(email)
    );
    """
)



mycursor.execute(
    """CREATE TABLE IF NOT EXISTS registed_patient(
        ID INT NOT NULL AUTO_INCREMENT,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        phone_number INT,
        email VARCHAR(100) NOT NULL,
        Blood_type VARCHAR(40) NOT NULL,
        genotype VARCHAR(40) NOT NULL,
        PRIMARY KEY(ID)
    );

    """
)