from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from blog.models import *
import blog.func as func
# Create your views here.
# get blog_instance list
# get blog_instance destail
# get program_instance list
# get program_instance destail
# post leave_comment ip限制

def blog_instance_api(requests):
    blog_id = requests.GET.get('blog_id',"")
    categary = requests.GET.get('categary',"")
    if blog_id != "":
        try:
            res = blog_instance.objects.get(id=blog_id).__dict__
            del res["_state"]
            del res['push_time']
            return JsonResponse({'status':'1','msg':'','data':res},content_type="application/json")  
        except:
            return JsonResponse({'status':'0','msg':'','data':{}},content_type="application/json")  

    if categary != "":
        try:
            res = list(blog_instance.objects.filter(categary=categary).values())
            return JsonResponse({'status':'1','msg':'','data':res},content_type="application/json")  
        except:
            return JsonResponse({'status':'0','msg':'','data':[]},content_type="application/json")         
    return JsonResponse({'status':'0','msg':'','data':[]},content_type="application/json") 

def program_instance_api(requests):
    program_id = requests.GET.get('program_id',"")
    if program_id != "":
        try:
            res = program_instance.objects.get(id=program_id).__dict__
            del res["_state"]
            del res['push_time']
            return JsonResponse({'status':'1','msg':'','data':res},content_type="application/json")  
        except:
            return JsonResponse({'status':'0','msg':'','data':{}},content_type="application/json")        
    return JsonResponse({'status':'0','msg':'','data':[]},content_type="application/json") 

def comment_api(requests):
    data_dict = dict(requests.GET.dict())
    ip_addr = func.get_client_ip(requests)
    # print(ip_addr)
    if func.cookie_limit(requests):
        try:
            # print(data_dict)
            if not func.check_email(data_dict["mail_addr"]):
                return JsonResponse({'status':'0','msg':'email'},content_type="application/json") 
            if not func.check_phone(data_dict["phone"]):
                return JsonResponse({'status':'0','msg':'phone'},content_type="application/json")
            if func.check_null(data_dict["name"]):
                return JsonResponse({'status':'0','msg':'name'},content_type="application/json") 
            if func.check_null(data_dict["content"]):
                return JsonResponse({'status':'0','msg':'content'},content_type="application/json")
            leave_comment(**data_dict).save()
            return JsonResponse({'status':'1','msg':''},content_type="application/json") 
        except Exception as identifier:  
            return JsonResponse({'status':'0','msg':str(identifier)},content_type="application/json") 
    return JsonResponse({'status':'0','msg':'interval time'},content_type="application/json") 