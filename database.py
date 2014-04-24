import sqlite3
import task
import os


def clean_db():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
    c = conn.cursor()
    
    c.execute('DELETE FROM task')
    conn.commit()
    conn.close()


def create_db():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
    c = conn.cursor()

    c.execute('''CREATE TABLE task
                 (id INTEGER primary key AUTOINCREMENT,
                  date TEXT, 
                  command TEXT,
                  priority INTEGER, 
                  executed INTEGER,
                  correct INTEGER,
                  load INTEGER)''')
    conn.commit()
    conn.close()

def load_next():
    to_ret = list()
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
    c = conn.cursor()
    c.execute("SELECT * FROM task WHERE load=0 ORDER BY priority ASC LIMIT 1")
    task_obj = None
    for row in c.fetchall():
        task_obj = task.Task(command=row[2], priority=row[3])
        task_obj.id = row[0]
        c.execute("UPDATE task SET load=1 WHERE id=%d" % task_obj.id)
        conn.commit()
        #to_ret.append(task_obj)
    conn.close()
    return task_obj

def update_task(task_id, executed, correct):

    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
    c = conn.cursor()

    c.execute('''UPDATE task
                    SET 
                executed=%d, correct=%d
                    WHERE
                id=%d;''' % (executed, correct, task_id))

    conn.commit()
    conn.close()

def read_db(name):
    to_ret = list()
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
    c = conn.cursor()
    c.execute("SELECT * FROM task WHERE load=0")
    for row in c.fetchall():
        #print row
        task_obj = task.Task(command=row[2], priority=row[3])
        task_obj.id = row[0]
        c.execute("UPDATE task SET load=1 WHERE id=%d" % task_obj.id)
        conn.commit()
        to_ret.append(task_obj)
    conn.close()
    return to_ret

def insert_task(command, priority):
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
    c = conn.cursor()
    c.execute('''INSERT INTO task
                (date, command, priority, executed, correct, load)
                    VALUES
                (0, '%s', %d, 0, 1, 0);''' % (command, priority))
    conn.commit()
    conn.close()
