from django.shortcuts import HTTP,render
from django.views.decorators.csrf import csrf_exempt
from .spam_model import is_spam
from django.contrib import messages
# Create your views here.
# from sklearn.externals import joblib
# reloadModel =joblib.load('static/spam_model.ipynb')

def Homepage(request):
    return render(request,"home.html")





@csrf_exempt
def SpamModel(request):
	#  form = ProductForm(request.POST or None)
	# if form.is_valid():
	# 	save_it = form.save(commit=False)
	# 	save_it.save()
 #    # print(request)
    # print("chlgya")
    # print(request.POST.dict())
    if request.method == "POST":
        temp={}
        temp['message']=request.POST.get('message')
        content={
        "msg":(is_spam(inp = [temp['message']]))  
        }

    return render(request,"SpamModel.html",content)




 #    form = ProductForm(request.POST or None)
	# if form.is_valid():
	# 	save_it = form.save(commit=False)
	# 	save_it.save()
	# 	messages.success(request, ' Thank You For Your Reaponse !!!!!')