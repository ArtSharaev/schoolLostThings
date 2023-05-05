import sqlite3
import os


class DB:
    def __init__(self, directory, db_name):
        self.directory = directory
        self.name = db_name

    def connect(self, text_for_execute: str, fetchall: bool = False,
                params: tuple = ()):
        with sqlite3.connect(self.directory + "/" + self.name) as conn:
            conn.cursor()
            if fetchall:
                try:
                    return conn.execute(text_for_execute, params).fetchall()
                except Exception:
                    print(text_for_execute)
            else:
                conn.execute(text_for_execute, params)
                conn.commit()

    def global_init(self):
        print(
            "Connecting to the database at " + '"' + self.directory +
            "/" + self.name + '"')
        if not os.path.exists(self.directory + "/" + self.name):
            with open(self.directory + "/" + self.name, "w+"):
                pass
            self.connect("""
                CREATE TABLE IF NOT EXISTS recordings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_id INTEGER NOT NULL,
                room_number VARCHAR(32) NOT NULL,
                building VARCHAR(8) NOT NULL,
                description VARCHAR(256),
                date DATETIME
            );""")

    def add_recording(self, image_id, room_number, building, description):
        self.connect("""INSERT INTO recordings(image_id, room_number, 
        building, description) VALUES(?, ?, ?, ?);
        """, params=(image_id, room_number, building, description))
        # site_id = self.connect("""
        #                 SELECT id FROM sites WHERE url=?
        #                 """, fetchall=True, params=(data["url"],))
        # if not site_id:
        #     site_id = self.connect("""
        #                     INSERT INTO sites(url) VALUES(?) RETURNING id;
        #                     """, fetchall=True, params=(data["url"],))
        # site_id = site_id[0][0]
        # # id запроса
        # req_type_id = self.connect("""
        #                 SELECT id FROM requests_types WHERE type = ?;
        #                 """, fetchall=True, params=(data["method"],))
        # if not req_type_id:
        #     print(f"Error unknown method: \"{data['method']}\"")
        #     return -1
        # self.connect("""
        #                 INSERT INTO requests(duration, status, site_id,
        #                  request_type_id, time) VALUES(?, ?, ?, ?, DATETIME("now", "+3 hours"));
        #                 """, params=(
        #     data["duration"], data["code"], site_id,
        #     req_type_id[0][0]))


if __name__ == "__main__":
    db = DB("../db", "lostthings.db")
    db.global_init()
