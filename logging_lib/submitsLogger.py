import os


class SubmitLogger:
    """Класс для отслеживания всех сабмитов пользователей"""
    def __init__(self, filepath="logging_lib/submits.txt") -> None:
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                pass

    def update(self, message, time, room_number, filename) -> None:
        with open(self.filepath, "a") as file:
            file.write(f"\n{message.from_user.full_name} "
                       f"({message.from_user.username}) "
                       f"submitted at {time} UTC. Room number: {room_number}. "
                       f"Telegram id: {message.from_user.id}. "
                       f"Filename: {filename}")
