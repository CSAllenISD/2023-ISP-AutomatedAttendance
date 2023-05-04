class User:
    def __init__(self):
        self.name = ""
        self.ID = ""
        self.email = ""
        self.passwordhash = ""
        self.classes = []

    def __init__(self, name, email, ID, passwordhash):
        self.name = name
        self.ID = ID
        self.email = email
        self.passwordhash = passwordhash
        self.classes = []

    def __init__(self, name, email, ID, passwordhash, classes):
        self.name = name
        self.ID = ID
        self.email = email
        self.passwordhash = passwordhash
        self.classes = classes

    def create_database(self):
        db_filename = str(self.ID) + ".db"
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()

        # Create a table for each class period
        for period in self.classes:
            table_name = "period_" + str(period).replace(" ", "_")
            c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (stu_id INTEGER NOT NULL, stu_name TEXT NOT NULL, stu_attendance TEXT NOT NULL)")

        conn.commit()
        conn.close()
        print("Database and tables created successfully.")



exUser = User("John Doe", "johndoe@example.com", "123456789", "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d", ["Period 2", "Period 3", "Period 4"])
