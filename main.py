import argparse
import task
import database
import time
import subprocess

def insert(command, priority=None):
    if not priority:
        priority = 1

    database.insert_task('db.db', command, priority)


def main():    
    parser = argparse.ArgumentParser(description='Bashtask manager.')
    #parser.add_argument('command', type=str, nargs=1,
    #                   help='the complete command to execute')
    parser.add_argument('-c' , '--createdb', dest='create_db',
                        default=False, action='store_true',
                        help='to create empty database (Optional).')
    parser.add_argument('-nr', '--notrun', dest='not_run', default=False,
                       help='to prevent run daemon.', action='store_true',)
    args = parser.parse_args()
    
    if args.create_db:
        print "Removing old database..."
        print "Creating empty database"
        database.create_db(name='db.db')
    if not args.not_run:
        run()



def run():
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