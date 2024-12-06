

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from .models import *
import random as r


import matplotlib.pyplot as plt;
import numpy as np
import numpy
from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

# Create your views here.
def adminlogin(request):
    return render(request, 'admin.html')


def adminloginaction(request):
    userid=request.POST['aid']
    pwd=request.POST['pwd']
    print(userid, pwd,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if userid=='admin' and pwd=="admin":
        request.session['adminid']='admin'
        return render(request, 'adminhome.html')
    else:
        err='Your Login Data is wrong !!' 
        return render(request, 'admin.html',{'msg':err})


def adminhome(request):
    return render(request, 'adminhome.html')


def adminlogout(request):
    return render(request, 'admin.html')

def user(request):
    return render(request, 'user.html', {'b':False})

def usersignup(request):
    return render(request, 'user.html', {'b':True})

def usignupaction(request):
    if request.method == 'POST':
        email = request.POST['mail']

        d = company.objects.filter(email__exact=email).count()
        if d > 0:
            return render(request, 'user.html', {'msg': "Email Already Registered"})
        else:

            pass_word = request.POST['pass_word']
            phone = request.POST['phone']
            city = request.POST['city']
            name = request.POST['name']
            address = request.POST['addr']

            d = company(name=name, email=email, pass_word=pass_word, phone=phone,  city=city, stz='new', address=address)
            d.save()

        return render(request, 'user.html', {'msg': "Register Success, You can Login.."})

    else:
        return render(request, 'user.html')

def userloginaction(request):
    if request.method=='POST':
        uid=request.POST['mail']
        pass_word=request.POST['pass_word']
        d=company.objects.filter(email__exact=uid).filter(pass_word__exact=pass_word).filter(stz__exact='Activated').count()
        
        if d>0:
            d=company.objects.filter(email__exact=uid)
            request.session['email']=uid
            request.session['name']=d[0].name
         
         
            return render(request, 'user_home.html',{'data': d[0]})

        else:
            return render(request, 'user.html',{'msg':"Login Fail"})

    else:
        return render(request, 'user.html')
    


def userlogout(request):
    try:
        del request.session['email']
    except:
        pass
    return render(request, 'user.html')


def userhome(request):
    if "email" in request.session:
        email=request.session["email"]
        d=company.objects.filter(email__exact=email)
       
        return render(request, 'user_home.html',{'data': d[0]})

    else:
        return redirect('userlogout')


def feature_selection(request):
    if request.method == 'POST':

        file=request.POST['file']
        
        from .FeatureSelection import featureselection
        featureselection.calc(file)
        return render(request, 'feature_selection.html', {'b':True,'msg':'Feature Selection Completed '})

    else:
        return render(request, 'feature_selection.html')


def classification(request):
    return render(request, 'classification.html')

from .FeatureSelection2 import featureselection
def nbtrain(request):
    
    file=request.POST['file']  
    features=featureselection.calc(file)
     
    
    from .Training import Training
    sc = Training.train(2, features, file)

    performance.objects.filter(alg_name='Naive Bayes').delete()
    
    d = performance(alg_name='Naive Bayes', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()
    
    return render(request, 'classification.html', {'msg': "Naive Bayes Algorithm's training & testing completed"})


def dttrain(request):
    file=request.POST['file']  
    features=featureselection.calc(file)
    from .Training import Training
    sc = Training.train(4, features, file)
    performance.objects.filter(alg_name='Decision Tree').delete()
  
    d = performance(alg_name='Decision Tree', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()
    
    return render(request, 'classification.html', {'msg': "Decision Tree Algorithm's training & testing completed"})


def svmtrain(request):
    file=request.POST['file']  
    features=featureselection.calc(file)
    from .Training import Training
    sc = Training.train(3, features, file)
    performance.objects.filter(alg_name='SVM').delete()
  
    d = performance(alg_name='SVM', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()

    return render(request, 'classification.html', {'msg': "SVM Algorithm's training & testing completed"})



def rftrain(request):
    file=request.POST['file']  
    features=featureselection.calc(file)
    from .Training import Training
    sc = Training.train(1, features, file)
    performance.objects.filter(alg_name='Random Forest').delete()
    d = performance(alg_name='Random Forest', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])

    d.save()

    return render(request, 'classification.html', {'msg': "Random Forest Algorithm's training & testing completed"})


def lrtrain(request):
    file=request.POST['file']  
    features=featureselection.calc(file)
    from .Training import Training
    sc = Training.train(5, features, file)
    performance.objects.filter(alg_name='Logistic Regression').delete()
    d = performance(alg_name='Logistic Regression', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()

    return render(request, 'classification.html', {'msg': "Logistic Regression Algorithm's training & testing completed"})

def evaluation(request):
    from .Graphs import viewg
    
    d = performance.objects.all()
    val = dict({})
    for d1 in d:
        val[d1.alg_name] = d1.sc1
    viewg(val, 'accuracy.png', 'Accuracy')
    
    val = dict({})
    for d1 in d:
        val[d1.alg_name] = d1.sc2
    viewg(val, 'precision.png', 'Precision')
    
    val = dict({})
    for d1 in d:
        val[d1.alg_name] = d1.sc3
    viewg(val, 'recall.png', 'Recall')
    
    val = dict({})
    for d1 in d:
        val[d1.alg_name] = d1.sc4
    viewg(val, 'f1.png', 'F1 Score')
    
    return render(request, 'viewacc.html', {'data': d})



def newcompanies(request):
    if True:
        d=company.objects.filter(stz__exact='new')
        return render(request, 'newcompanies.html',{'data': d})


def viewcompanies(request):
    if True:
        d=company.objects.filter(stz__exact='Activated')
        return render(request, 'viewcompanies.html',{'data': d})



def accept(request):
    id = request.GET['id']
    company.objects.filter(email=id).update(stz='Activated')
    d = company.objects.filter(stz='new')
    return render(request, 'newcompanies.html', {'data': d})


def reject(request):
    id = request.GET['id']
    company.objects.filter(email=id).update(stz='Rejected')
    d = company.objects.filter(stz='new')
    return render(request, 'newcompanies.html', {'data': d})


def attrition(request):
    if request.method == 'POST':

        file=request.POST['file']

        from .FeatureSelection2 import featureselection
        features=featureselection.calc('Employee-Attrition.csv')
    
        from .Prediction import Prediction
        empid,res=Prediction.get(features, file)

        d=dict({})

        for i in range(len(empid)):
            d[empid[i]]=res[i]
        
        from .Freq import CountFrequency
        resdict=CountFrequency(res)

        from .Graphs import viewg
        viewg(resdict,'prediction.jpg','Prediction Result')
       
        return render(request, 'attritionres.html', {'data':d})

    else:
        return render(request, 'attrition.html')


def feedbackpost(request):
    if request.method == 'POST':

        file=request.POST['file']
        name=request.session['name']
        email=request.session['email']
        data=read_csv(file)

        import random
        fle=random.randint(9999, 99999)
        fle=str(fle)+".csv"

        d=feedback(name=name, email=email, file=fle)
        d.save()
        fle="Data//"+fle
        write_csv(fle, data)
        
        return render(request, 'feedbackpost.html', {'msg':'Data posted successfully !! '})
    else:
        return render(request, 'feedbackpost.html')

import csv
def read_csv(input_file):
    data = []
    with open(input_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def write_csv(output_file, data):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def viewfeedback(request):
    d=feedback.objects.all()
    return render(request, 'viewfeedback.html', {'data':d})
    
def viewdata(request):
    file=request.POST['file']
    csv_file_path = 'Data//'+file
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        csv_data = list(csv_reader)
    context = {'csv_data': csv_data}


    return render(request, 'view_csv.html', context)
    