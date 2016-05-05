import sys, argparse, sqlite3, requests, time

def _insert_timestamp(args):
    ''' Insert either startup or shutdown time stamp into sqlite database working_hours.db '''    
    is_startup = args.startup
    is_shutdown = args.shutdown
    http_proxy = args.http_proxy
    https_proxy = args.https_proxy
    
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
    
    proxy = check_connection(http_proxy,https_proxy)
        
    if not proxy:
        return
                
    # Insert time stamp into sqlite db
    conn = sqlite3.connect("working_hours.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS startups_shutdowns_computer (date TEXT, time TEXT, is_startup INTEGER, proxy TEXT)")
    c.execute("INSERT INTO startups_shutdowns_computer VALUES (date('now','localtime'),time('now','localtime'),?,?)", (is_startup_bin, proxy,))
    
    # Save (commit) the changes
    conn.commit()
    conn.close()


def check_connection(http_proxy,https_proxy):
    proxies = {
        "http": http_proxy,
        "https": https_proxy,
    }    
    proxy = ""
    
    # Wait until internet connection is available
    start = time.time()
    while True:
        # Check for non-proxy environment
        try:
            requests.get("http://www.google.com")
            proxy = "None"
            break
        except:
            pass
        # Check for proxy environment
        try:
            requests.get("http://www.google.com", proxies=proxies)    
            proxy = proxies["http"]  
            break       
        except:
            pass
        
        end = time.time() - start
        if end > 300: #Timeout after 5 minutes
            print("Timeout")
            break       
    return proxy
    

def main(argv):
    parser = argparse.ArgumentParser(description="save startup or shutdown time stamps")    
    parser.add_argument("--startup", action="store_true", help="save startup time stamp")
    parser.add_argument("--shutdown", action="store_true", help="save shutdown time stamp")    
    parser.add_argument("--http_proxy", help="http proxy") 
    parser.add_argument("--https_proxy", help="https proxy") 
    args = parser.parse_args()
    # Insert time stamp
    _insert_timestamp(args)       

if __name__ == '__main__':
    main(sys.argv[1:])

    
