from Model.baseTable import BaseTable


class InfoTable(BaseTable):
    def __init__(self, table, db="script/db_script.db"):
        super().__init__(table, db)

        self.create_sql = f""" CREATE TABLE IF NOT EXISTS `{self.table}`(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                detail TEXT
                );
        """




