class Password:
    def __init__(self, service: str, username: str, password: str):
        self.service = service
        self.username = username
        self.password = password

    def __str__(self):
        return f"Service: {self.service}\nUsername: {self.username}\nPassword: {self.password}"

    def __reduce__(self):
        return self.__class__, (self.service, self.username, self.password)
