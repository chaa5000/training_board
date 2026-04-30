from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout # تأكد من وجود هذا السطر
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Project, Profile

# 1. الصفحة الرئيسية
def home(request):
    projects = Project.objects.all()
    return render(request, 'pages/index.html', {'projects': projects})

# 2. صفحة تفاصيل المشروع (محمية)
@login_required
def project_detail(request, pk):
    # نتحقق من موافقة المدير من خلال البروفايل
    if not request.user.profile.is_approved:
        return render(request, 'pages/waiting_approval.html')
    
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'pages/project_detail.html', {'project': project})

# 3. صفحة من نحن
def about(request):
    return render(request, 'pages/about.html')

# 4. صفحة اتصل بنا
def contact(request):
    return render(request, 'pages/contact.html')

# 5. دالة إنشاء حساب جديد (Signup)
def signup(request):
    context = {}
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        email = request.POST.get('email')
        username = request.POST.get('user')
        password = request.POST.get('pass')

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود مسبقاً.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مسجل بالفعل.")
        else:
            # إنشاء المستخدم
            user = User.objects.create_user(
                username=username, 
                email=email, 
                password=password,
                first_name=fname,
                last_name=lname
            )
            # إنشاء البروفايل
            Profile.objects.create(
                user=user,
                address=address,
                address2=address2,
                city=city,
                state=state,
                zip_code=zip_code
            )
            context['is_added'] = True
            messages.success(request, "تم إنشاء الحساب بنجاح! بانتظار موافقة المدير.")
            
    return render(request, 'registration/signup.html', context)

# 6. دالة تسجيل الخروج
def user_logout(request):
    logout(request) # دجانغو سيعرفها الآن بفضل الاستيراد في السطر رقم 3
    return redirect('home')