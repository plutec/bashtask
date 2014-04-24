import sqlite3
import task
import os

class Database(object):
    def __init__(self):
        """
        Constructor, create a connection
        """
        self.conn = sqlite3.connect(os.path.join(
                                        os.path.dirname(__file__), 'db.db'))
    def load_next(self):
        to_ret = list()
        #conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
        c = self.conn.cursor()
        c.execute("SELECT * FROM task WHERE load=0 ORDER BY priority ASC LIMIT 1")
        task_obj = None
        for row in c.fetchall():
            task_obj = task.Task(command=row[2], priority=row[3])
            task_obj.id = row[0]
            c.execute("UPDATE task SET load=1 WHERE id=%d" % task_obj.id)
            self.conn.commit()
            #to_ret.append(task_obj)
        #conn.close()
        return task_obj

    def insert_task(self, command, priority):
        c = self.conn.cursor()
        c.execute('''INSERT INTO task
                    (date, command, priority, executed, correct, load)
                        VALUES
                    (0, '%s', %d, 0, 1, 0);''' % (command, priority))
        self.conn.commit()

    def clean_db(self):
        """
        Remove all entries from the database
        """
        c = self.conn.cursor()
        c.execute('DELETE FROM task')
        self.conn.commit()

    def create_db(self):
        """
        Create a new database
        """
        c = self.conn.cursor()

        c.execute('''CREATE TABLE task
                     (id INTEGER primary key AUTOINCREMENT,
                      date TEXT, 
                      command TEXT,
                      priority INTEGER, 
                      executed INTEGER,
                      correct INTEGER,
                      load INTEGER)''')
        self.conn.commit()

    def update_task(self, task_id, executed, correct):
        c = self.conn.cursor()

        c.execute('''UPDATE task
                        SET 
                    executed=%d, correct=%d
                        WHERE
                    id=%d;''' % (executed, correct, task_id))

        self.conn.commit()
        

    def __del__(self):
        """
        Close the database connection
        """
        self.conn.close()
