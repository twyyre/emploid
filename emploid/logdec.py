
from emploid.constants import LOG_TO_DB
def decorator_wrapper(*args, **kwargs):
    print("args:", *args)
    print("kwargs:", **kwargs)
    exit()
    try:
        emp = args[0]
        
        try:
            #CREATE LOG FILE-------------------------------------------
            # emp.create_logs_directory = True
            # emp.log_path = "logs"
            # if(emp.create_logs_directory):
            #     year = datetime.datetime.now().year
            #     month = datetime.datetime.now().month
            #     day = datetime.datetime.now().day
            #     hour = datetime.datetime.now().hour
            #     minute = datetime.datetime.now().minute
            #     second = datetime.datetime.now().second
            #     log_filename = f"{emp.log_path}/internal_log {year}-{month}-{day}-{hour}-{minute}-{second}.log"

            #     tls.f_write(_filename=log_filename, _content="")
                
            #     logging.basicConfig(filename=log_filename, encoding='utf-8', format='%(asctime)s %(message)s', level=logger.INFO)
            #----------------------------------------------------------
            log_message = str(f"emploid started '{_func.__name__}'").replace("'", "\"")
            args_message = ""
            kwargs_message = ""
            
            if(len(args)):
                args_message = str(args).replace("'", "\"")
            else:
                args_message = 'NULL'
                
            if(len(kwargs)):
                kwargs_message = str(json.dumps(kwargs)).replace("'", "\"")
            else:
                kwargs_message = 'NULL'
            
            logger.info(log_message)
        except Exception as e:
            print("error when creating log:", e)
        
        if(LOG_TO_DB):
            try:
                query = f"""INSERT INTO logs (actionname, userid, message, fullerror, request, response, params, kwargs) VALUES ('{_func.__name__}', 'NULL', '{log_message}', 'NULL', 'NULL', 'NULL', '{args_message}', '{kwargs_message}');"""
                emp.query(_query=query)
            except Exception as e:
                print("could not save log to DB:", e)
            
        return _func(*args, **kwargs)
    
    except Exception as e:
        print("-----------------NORMAL ERROR-----------------")
        e = str(e).replace("'", "\"")
        print(e)
        
        if(LOG_TO_DB):
            try:
                emp.query(_query=f"""INSERT INTO logs (actionname, userid, message, fullerror, request, response, params, kwargs) VALUES ('{_func.__name__}', 'NULL', '-----------------NORMAL ERROR-----------------', '{e}', 'NULL', 'NULL', 'NULL', 'NULL');""")
            except:
                print("could not log normal error into database")
                print(e)

        print("-----------------LOG ERROR-----------------")
        logger.exception(e)
            
    return wrapper
#----------------------------------------------------------