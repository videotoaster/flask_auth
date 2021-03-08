import json

class User:
    def __init__(self, username, session_id, password):
        self.username = username
        self.session_uuid = session_id
        self.password = password
        with open("users.json", "w") as database:
            json.dump({
                "username": username,
                "session_uuid": str(session_id),
                "password": password
                }
                , database)

    @staticmethod
    def get_user(uuid):
        if not uuid:
            return 
        with open("users.json", "r") as database:
            data = json.load(database)
            print(data)
            for user in data:
                print(user)
                if user['session_uuid'] == uuid:
                    return user