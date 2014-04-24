import task
import database
import time
import subprocess

def main():
    while(True):
        task = database.load_next('db.db')
        if task:            
            print "Executing %s" % task.command
            try:
                output = subprocess.Popen(task.command.split(), 
                        stdout = subprocess.PIPE).communicate()[0]
                print "Finished %s" % task.command
                database.update_task('db.db', task_id=task.id, 
                                              executed=True, 
                                              correct=True)
            except Exception, why:
                print "Error executing %s" % task.command
                database.update_task('db.db', task_id=task.id, 
                                              executed=True, 
                                              correct=False)

        else:
            time.sleep(0.5)
        

if __name__ == '__main__':
    main()