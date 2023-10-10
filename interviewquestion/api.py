  



from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import Student

class UserAPI(APIView):
    @login_required
    def get(self, request):
        students = Student.objects.all().values('username', 'branch', 'scholarship_eligibility')
        return Response(students)

    @login_required
    def post(self, request):
        user_data = request.data
        try:
            new_student = Student.objects.create(
                username=user_data.get('username'), 
                branch=user_data.get('branch'),
                scholarship_eligibility=user_data.get('scholarship_eligibility')
                address=user_data.get('address')
                branch=user_data.get('branch')

                )
            
            new_student.save()
            return Response({'message': 'Student registered successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        

    @login_required
    def delete(self, request):
        username_to_delete = request.data.get('username', None)
        if username_to_delete:
            try:
                
                student_to_delete = Student.objects.get(username=username_to_delete)
                student_to_delete.delete()
                return Response({'message': 'Student deleted successfully'})
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=404)
            except Exception as e:
                return Response({'error': str(e)}, status=500)
       

