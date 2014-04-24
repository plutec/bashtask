import argparse
import task
import database
import time
import subprocess

def insert(command, priority=None):
    """
    We can use this method to insert a command in the queue without 
        use the terminal, for example, importing bashtask and using the method.
    """
    if not priority:
        priority = 1

    database.Database().insert_task(command, priority)


def main():    
    parser = argparse.ArgumentParser(description='Bashtask manager.')
    
    parser.add_argument('-c' , '--createdb', dest='create_db',
                        default=False, action='store_true',
                        help='to create empty database (Optional).')
    parser.add_argument('-cc' , '--cleandb', dest='clean_db',
                        default=False, action='store_true',
                        help='clean database (remove all entries).')
    parser.add_argument('-nr', '--notrun', dest='not_run', default=False,
                       help='to prevent run daemon.', action='store_true',)
    args = parser.parse_args()
    
    if args.create_db:
        print "Removing old database..."
        print "Creating empty database..."
        database.create_db()
    if args.clean_db:
        print "Cleaning database..."
        database.clean_db()
    if not args.not_run:
        print "Running bashtask daemon..."
        run()



def run():
    db = database.Database()
    while(True):
        task = db.load_next()
        if task:            
            print "Executing %s" % task.command
            try:
                output = subprocess.Popen(task.command.split(), 
                        stdout = subprocess.PIPE).communicate()[0]
                print "Finished %s" % task.command
                db.update_task(task_id=task.id, 
                               executed=True, 
                               correct=True)
            except Exception, why:
                print "Error executing %s" % task.command
                db.update_task(task_id=task.id, 
                               executed=True, 
                               correct=False)

        else:
            time.sleep(0.5)
        

if __name__ == '__main__':
    main()
