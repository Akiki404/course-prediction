from django.shortcuts import render, redirect
from .models import Record

# TO DO:::
# Install pandas & sklearn

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle



# Create your views here.
def index(request):
    return render(request, 'predictapp/index.html')


def database(request):
    records = Record.objects.all()
    return render(request, 'predictapp/db.html', {'records': records})


def predict(request):
    if request.method == 'POST':
        gender = int(request.POST.get('gender'))   
        grade = request.POST.get('grade')
        openness = int(request.POST.get('openness'))
        agreeableness = int(request.POST.get('agreeableness'))
        emotions = int(request.POST.get('emotions'))
        conscientiousness = int(request.POST.get('conscientiousness'))
        extraversion = int(request.POST.get('extraversion'))

    # TO DO:::
    # Switch case the grade to have numeric values
        if grade == 'A':
            grade = 80
        elif grade == 'A-':
            grade = 75    
        elif grade == 'B+':
            grade = 70
        elif grade == 'B':
            grade = 65
        elif grade == 'B-':
            grade = 60    
        elif grade == 'C+':
            grade = 55
        elif grade == 'C':
            grade = 50
        elif grade == 'C-':
            grade = 45        
        elif grade == 'D+':
            grade = 40
        elif grade == 'D':
            grade = 30
        elif grade == 'D-':
            grade = 20
        else:
            grade = 10

        # Load the model & unpickle
        with open('/home/code/Projects/ML/Course/courses_pickle', 'rb') as f:
            md = pickle.load(f)
    
            # Predict & return the results   
            course = md.predict([ [gender, grade, openness, agreeableness, emotions, conscientiousness, extraversion] ])[0] #Pass the values from the form
        
            record = Record(gender=gender, grade=grade, openness=openness, agreeableness=agreeableness, emotions=emotions, conscientiousness=conscientiousness, extraversion=extraversion, course=course)
            record.save()
        
        return render(request, 'predictapp/index.html',
            {
                'gender': gender,
                'grade': grade,
                'openness': openness,
                'agreeableness': agreeableness,
                'emotions': emotions,
                'conscientiousness': conscientiousness,
                'extraversion': extraversion,
                'course': course
            })
    return redirect('predictapp:index')    