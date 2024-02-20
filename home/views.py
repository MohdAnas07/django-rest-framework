from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def index(request):
    courses = {
        'course_name':'Python',
        'learn':['flask','django','tornado','machine learning'],
        'course_provider':'Anas'
    }
    if request.method=='GET':
        print("YOU HIT A GET REQUEST!")
        return Response(courses)
    elif request.method =='POST':
        print("YOU HIT A POST REQUEST!")
        return Response(courses)