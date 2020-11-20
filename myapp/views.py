from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    return render(request,'myapp/login.html')
'''
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
            username = request.POST.get('usn')
            password = request.POST.get('password') 
            user = authenticate(username=username, password='Students@123')
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
            else:
                return redirect('student')
'''
def student(request):
    return render(request, 'myapp/student.html')

def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'myapp/home.html',{'img':img,'form':form})
