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

user = User("John Doe", "johndoe@example.com", "123456789", "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d", ["Period 2", "Period 3", "Period 4"])
