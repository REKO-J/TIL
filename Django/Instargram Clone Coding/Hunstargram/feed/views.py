from django.shortcuts import render

# Create your views here.
class Login(APIView):
    def get(self, request):
        return render(request, 'Hunstargram/login.html')

class Profile(APIView):
    def get(self, request):
        return render(request, 'Hunstargram/profile.html')