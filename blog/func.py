import re 
import datetime

def get_client_ip(request):
    ip = "0.0.0.0"
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip

def cookie_limit(request):
    # increase count
    request.session["count"] = request.session.get("count", 0) + 1
    
    time_ = request.session.get("time", False)
    if not time_:
        request.session["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return True
    else:
        interval = int((datetime.datetime.now() - datetime.datetime.strptime(time_,"%Y-%m-%d %H:%M:%S")).seconds)
        print(interval,request.session["count"])
        if request.session["count"] > 10 and interval < 100:
            return False
        
        # 清零
        if interval > 100:
            request.session["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session["count"] = 0
            return True
    return True 
        
      
def check_email(str_arg):
    '''判断是否是邮箱'''
    str_1 = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
    if re.match(str_1, str(str_arg)):
        return True
    return False

def check_ok(str_arg):
    '''判断是否含有特殊字符'''
    if is_null(str(str_arg)):
        return False
    for i in str(str_arg):
        if i == "#" or i== "!" or i== "." or i=="\"" or i=="\'" or i=="?" or i=="$" or i=="&":
            return False,i
    return True,""

def check_phone(phone):  
    if re.match('^(13|14|15|18)[0-9]{9}$', phone):
        return True     
    else:  
        return False

def check_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def check_null(arg):
    '''判断是否为空'''
    str_arg = str(arg)
    if str_arg == "":
        return True
    if str_arg == False:
        return True
    if str_arg.isspace():
        return True
    if str_arg == None:
        return True
    return False

def check_phone(str_arg):
    '''判断是否为电话'''
    if len(str(str_arg)) != 11:
        return False
    for i in str(str_arg):
        if not check_number(i):
            return False
    return True

      
  
# Driver Code  
if __name__ == '__main__' :  
    # Enter the email  
    email = "ankitrai326@gmail.com"
      
    # calling run function  
    check(email) 
  
    email = "my.ownsite@ourearth.org"
    check(email) 
  
    email = "ankitrai326.com"
    check(email) 