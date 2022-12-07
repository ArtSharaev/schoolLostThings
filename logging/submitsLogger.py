class SubmitLogger:
    """Класс для отслеживания всех сабмитов пользователей"""
    def __init__(self, filepath="logging/submits.txt") -> None:
        self.filepath = filepath

    def update(self, message, time, room_number, filename) -> None:
        with open(self.filepath, "a") as file:
            file.write(f"\n{message.from_user.full_name} "
                       f"({message.from_user.username}) "
                       f"submitted at {time} UTC. Room number: {room_number}. "
                       f"Telegram id: {message.from_user.id}. "
                       f"Filename: {filename}")
