import argparse
import database


def main():
    parser = argparse.ArgumentParser(description='Insert a process in the queue.')

    parser.add_argument('command', type=str, nargs=1,
                       help='the complete command to execute')
    parser.add_argument('-p', dest='priority', type=int, default=1,#action='store_const',
                       help='priority to the command. Default: 1 (More priority)')

    args = parser.parse_args()
    database.Database().insert_task(args.command[0], args.priority)

if __name__ == '__main__':
    main()
