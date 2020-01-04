from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from blog.models import *
import blog.func as func
from conf import *
# Create your views here.
# get blog_instance list
# get blog_instance destail
# get program_instance list
# get program_instance destail
# post leave_comment ip限制

def blog_instance_api(requests):
    blog_id = requests.GET.get('blog_id',"")
    categary = requests.GET.get('categary',"")
    type_categary = requests.GET.get('type_categary',"")
    if type_categary:
        res = []
        
        res.append({
            "name":"BUSINESS STORY",
            "data":list(blog_instance.objects.filter(categary="BUSINESS STORY").values("title","blog_img","author","id"))[:3]
        })
        res.append({
            "name":"STUDENT VOICE",
            "data":list(blog_instance.objects.filter(categary="STUDENT VOICE").values("title","blog_img","author","id"))[:3]
        })
        res.append({
            "name":"CULTURAL ADVENTURE",
            "data":list(blog_instance.objects.filter(categary="CULTURAL ADVENTURE").values("title","blog_img","author","id"))[:3]
        })
        for i in res:
            for j in i["data"]:
                j["blog_img"] = api_media + j["blog_img"]
        res[0]["desc"] = "INSPIRED FROM"
        res[1]["desc"] = "SPOTLIGHT ON"
        res[2]["desc"] = "HANDPICKED FROM"

        return JsonResponse({'status':'1','msg':'','data':res},content_type="application/json")  
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

            for j in res:
                j["blog_img"] = api_media + j["blog_img"]
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
            res["program_img"] = api_media + res["program_img"]
            return JsonResponse({'status':'1','msg':'','data':res},content_type="application/json")  
        except:
            return JsonResponse({'status':'0','msg':'','data':{}},content_type="application/json") 
    else:
        
        res = list(program_instance.objects.all().values())
        for j in res:
            j["program_img"] = api_media + j["program_img"]
    return JsonResponse({'status':'0','msg':'','data':res},content_type="application/json") 

def testimonials_instance_api(requests):
    res = list(testimonials_instance.objects.all().values())
    for j in res:
        j["img_src"] = api_media + j["img_src"]
    return JsonResponse({'status':'0','msg':'','data':res},content_type="application/json") 

def comment_api(requests):
    data_dict = dict(requests.GET.dict())
    ip_addr = func.get_client_ip(requests)
    # print(ip_addr)
    if func.cookie_limit(requests):
        try:
            # print(data_dict)
            if not func.check_email(data_dict["mail_addr"]):
                return JsonResponse({'status':'0','msg':'email'},content_type="application/json") 
            # if not func.check_phone(data_dict["phone"]):
            #     return JsonResponse({'status':'0','msg':'phone'},content_type="application/json")
            if func.check_null(data_dict["name"]):
                return JsonResponse({'status':'0','msg':'name'},content_type="application/json") 
            if func.check_null(data_dict["content"]):
                return JsonResponse({'status':'0','msg':'content'},content_type="application/json")
            leave_comment(**data_dict).save()
            return JsonResponse({'status':'1','msg':''},content_type="application/json") 
        except Exception as identifier:  
            return JsonResponse({'status':'0','msg':str(identifier)},content_type="application/json") 
    return JsonResponse({'status':'0','msg':'interval time'},content_type="application/json") 