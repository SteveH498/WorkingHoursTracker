import sys, argparse, sqlite3



def insert_timestamp(args):
    ''' Insert either startup or shutdown time stamp into sqlite database working_hours.db '''    
    is_startup = args.startup
    is_shutdown = args.shutdown
    is_startup_bin = 1
    # Determine whether this is a startup or shutdown execution and set the startup field accordingly
    if is_startup and is_shutdown:
        raise ValueError('Not possible to set --startup and --shutdown flag at once')
    elif is_startup:
        is_startup_bin = 1
    elif is_shutdown:
        is_startup_bin = 0
    else:
        raise ValueError('--startup or --shutdown flag must be set')
    
    # Insert time stamp into sqlite db
    conn = sqlite3.connect("working_hours.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS startups_shutdowns (timestamp TEXT, is_startup INTEGER)")
    c.execute("INSERT INTO startups_shutdowns VALUES (datetime('now'),?)", (is_startup_bin, ))
    
    # Save (commit) the changes
    conn.commit()
    conn.close()

def main(argv):
    parser = argparse.ArgumentParser(description="save startup or shutdown time stamps")    
    parser.add_argument("--startup", action="store_true", help="save startup time stamp")
    parser.add_argument("--shutdown", action="store_true", help="save shutdown time stamp")    
    args = parser.parse_args()
    # Insert time stamp
    insert_timestamp(args)       

if __name__ == '__main__':
    main(sys.argv[1:])

    
