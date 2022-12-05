class SubmitLogger:
    def __init__(self, filepath="users_data/submits.txt") -> None:
        self.filepath = filepath

    def update(self, message, time, room_number) -> None:
        with open(self.filepath, "a") as file:
            file.write(f"{message.fullname} ({message.username}) "
                       f"submitted at {time}UTC. Room number: {room_number}. "
                       f"Telegram id: {message.id}")
