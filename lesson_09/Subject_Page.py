from sqlalchemy import create_engine, text


class Subjects:
    __scripts = {
        "select": text("select * from subject"),
        "select by title": text(
            "select * from subject where subject_title = :title"),
        "delete by title": text("delete from subject where \
                               subject_title =:title_to_delete"),
        "insert": text(
            "insert into subject (\"subject_title\") \
                values (:new_title)"),
        "update": text("update subject set subject_title =:upd_title \
                       where subject_title =:title_to_upd"),
        "count subject": text("select COUNT(*) from subject")
        }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        self.connect = self.db.connect()

    def get_list_subjects(self):
        transaction = self.connect.begin()
        rezult = self.connect.execute(self.__scripts["select"]).fetchall()
        transaction.commit()
        return rezult

    def get_subject(self, title):
        transaction = self.connect.begin()
        rezult = self.connect.execute(
            self.__scripts["select by title"], {"title": title})
        transaction.commit()
        return rezult

    def count_subjects(self):
        transaction = self.connect.begin()
        rezult = self.connect.execute(self.__scripts["count subject"]).scalar()
        transaction.commit()
        return rezult

    def delete_subject(self, my_title):
        transaction = self.connect.begin()
        self.connect.execute(
            self.__scripts["delete by title"], {"title_to_delete": my_title})
        transaction.commit()

    def insert_subject(self, title):
        transaction = self.connect.begin()
        rezult = self.connect.execute(
            self.__scripts["insert"], {"new_title": title})
        transaction.commit()
        return rezult

    def update_subject(self, title, my_title):
        transaction = self.connect.begin()
        param = {
            "title_to_upd": title,
            "upd_title": my_title
            }
        print(param)
        self.connect.execute(self.__scripts["update"], param)
        transaction.commit()
