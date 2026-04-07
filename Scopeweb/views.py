from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Category,Courses,Registration,Country
from .forms import Registrationform,updateform,pass_updateform
import random
import ast

# Create your views here.
def index(request):
     email = request.session.get('email')
     value = request.COOKIES.get('key')
    #  if not value or not email:
        #   messages.warning(request, "you are not Logged in")
        #   return redirect('home')
     return render(request,'index.html')

def contact(request):
    email = request.session.get('email')
    value = request.COOKIES.get('key')
    if request.method=='POST':
         fname=request.POST.get('fname')
         sub=request.POST.get('lname')
         email=request.POST.get('email')
         msg=request.POST.get('msg')
         print("THE VALUES ARE",fname,sub,email,msg)
         mail=EmailMessage(f'Enquiry from {fname}-{sub} ',f'Dear Admin,\n {msg} \n  {fname} \n{email}','anurenjanapradeep02@gmail.com',['anurenjanapradeep02@gmail.com'])
         mail.send(fail_silently=False)
         try:
             messages.add_message(request,
                                 messages.INFO,"Message Sent !")
         except:
                messages.add_message(request,messages.WARNING,"Unable to Sent,Retry!")

    return render(request,'contact.html')
def about(request):
    email = request.session.get('email')
    value = request.COOKIES.get('key')
    return render(request,'about.html')
def courses(request):
    course1=Courses.objects.filter(category_name='Data Science, AI, & Data Analytics Courses')
    course2=Courses.objects.filter(category_name='Software Courses')
    course3=Courses.objects.filter(category_name='Networking, Server, Cloud, & DevOps Courses')
    course4=Courses.objects.filter(category_name='Software Testing Courses')
    course5=Courses.objects.filter(category_name='Other Courses')
    return render(request,'courses.html',{'course1':course1,'course2':course2,'course3':course3,'course4':course4,'course5':course5})



from django.core.mail import EmailMessage
def register(request):
    email = request.session.get('email')
    value = request.COOKIES.get('key')
    if request.method=='POST':
        form=Registrationform(request.POST,request.FILES)
        country = request.POST.get('country')
        state = request.POST.get('state')

            # update queryset dynamically
        # if country:
        #         form.fields['state'].queryset = State.objects.filter(country=country)

        # if state:
        #         form.fields['city'].queryset = City.objects.filter(state=state)
        if form.is_valid():
            fname=form.cleaned_data['full_name']
            pic=form.cleaned_data['photo']
            dob=form.cleaned_data['dob']
            gender=form.cleaned_data['gender']
            qualification=form.cleaned_data['educational_qualification']
            hoby=form.cleaned_data['hobbies']
            mb_no=form.cleaned_data['mobile_number']
            email=form.cleaned_data['email']
            gname=form.cleaned_data['guardian_name']
            goccu=form.cleaned_data['guardian_occu']
            gno=form.cleaned_data['guardian_mob']
            career=form.cleaned_data['career']
            mode=form.cleaned_data['mode']
            loc=form.cleaned_data['scope_location']
            time=form.cleaned_data['time']
            address=form.cleaned_data['address']
            country=form.cleaned_data['country']
            state=form.cleaned_data['state']
            city=form.cleaned_data['city']
            pin=form.cleaned_data['pin']
            mail=EmailMessage('Registration Status',f'Dear {fname}\n You have successfully registered.\n Kind Regards','anurenjanapradeep02@gmail.com',[email])
            mail.send()
            

            modelobj=Registration()
            modelobj.full_name=fname
            modelobj.photo=pic
            modelobj.date_of_birth=dob
            modelobj.gender=gender
            modelobj.educational_qualification=qualification
            modelobj.hobbies=hoby
            modelobj.mobile_no=mb_no
            modelobj.email=email
            
            modelobj.guardian_name=gname
            modelobj.guardian_occupation=goccu
            modelobj.guardian_phone=gno
            
           
            modelobj.training_mode=mode
            modelobj.location=loc
            modelobj.timing=time
            modelobj.address=address
            modelobj.country=country
            modelobj.state=state
            modelobj.city=city
            modelobj.pin_code=pin
            modelobj.save()
           # Get the course object
            course_obj = Courses.objects.get(course_name=career)

            # Add the selected course to ManyToMany field AFTER saving
            modelobj.choose_course.add(course_obj)
            try:
             messages.add_message(request,
                                 messages.INFO,"Registration Succesfull !")
            except:
                messages.add_message(request,messages.WARNING,"Registration Unsuccessfull !")

            # return redirect('home')
            return redirect('studentlogin')
            
        else:
            print(form.errors) 
            messages.add_message(request,messages.WARNING,"Please fill the Fields!")
              


    else:    
        form=Registrationform()
    return render(request,'Registrationform.html',{'form':form})

# def get_states(request):
#     country_name=request.GET.get('country')
#     states=State.objects.filter(country=country_name).values('state_name')
#     return JsonResponse({"states": list(states)})
# def get_city(request):
#     state_name=request.GET.get('state')
#     city=City.objects.filter(State__state_name=state_name).values('city_name')
#     return JsonResponse({"city":list(city)})

def login(request):
     if request.method=="POST":
          email=request.POST.get('email')
          password=request.POST.get('password')
          rem=request.POST.get('remember')
          form=Registration.objects.filter(email=email,password=password)
          
          if form.exists():
            form.update(remember_me=rem)
           
            request.session['email']=email
            if rem=='on':
                response=redirect("/dashboard")
                response.set_cookie('key',email,max_age=31536000)
                return response
            else:
                response=redirect("/dashboard")
                response.set_cookie('key',email,max_age=120)
                return response       
          else:
              messages.error(request, "Invalid Email or password ")    
     else:
            try:
                
                    print(request.session['email'])
                    del request.session['email']
                    response=render(request,'login.html')   
                    response.delete_cookie('key')   
                    return response
            except:
                pass        
     return render(request,'login.html')

def firstlogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = Registration.objects.filter(email=email)

        if user.exists():
            otp = random.randint(1000, 9999)
            subject = 'OTP for Verification'
            message = f'Dear User,\nThe OTP is {otp}'
            EmailMessage(subject, message, 'anurenjanapradeep02@gmail.com', [email]).send()

            user.update(otp_db=otp)

            messages.info(request, "OTP sent has been send to your Mail")
            response= redirect('/otpverify')
            response.set_cookie('key',otp,max_age=50)
            response.set_cookie('mailkey',email,max_age=200)
            return response
        else:
            messages.error(request, "Email not found")
            
    return render(request, 'firstlogin.html')

def verify_otp(request):
    if request.method=="POST":
        otp=request.POST.get('otp')
        
        verify=Registration.objects.filter(otp_db=otp)
        value=request.COOKIES.get('key')
        if value == None:
             messages.error(request, "OTP expired")
            
        else:
            if verify:
                return redirect('/setpassword')
            else:
                messages.error(request, "Invalid OTP")
        
              
    return render(request,'verifyotp.html')    

def resend_otp(request):
    email = request.COOKIES.get('mailkey')

    if email:
        new_otp = random.randint(1000, 9999)
        subject = "Resend OTP Code"
        message = f"Dear User,\nYour new OTP is {new_otp}"
        mail=EmailMessage(subject, message, 'anurenjanapradeep02@gmail.com', [email])
        mail.send()
        Registration.objects.filter(email=email).update(otp_db=new_otp)

        messages.info(request, "A new OTP has been sent to your email")
        
        response = redirect('/otpverify')
        response.set_cookie('key', new_otp, max_age=50)
        return response
    else:
        messages.warning(request,"Session has Expired")
        return redirect('/firstlogin')
    
           
def set_pass(request):
    if request.method == "POST":
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password == cpassword:
            email = request.COOKIES.get('mailkey')
            if not email:
                messages.error(request, "Session expired. Please login again.")
                return redirect('studentlogin')
            
            data = Registration.objects.filter(email=email)
            if data.exists():
                data.update(password=password, confirm_password=cpassword,existing_password=password)
                response = redirect('studentlogin')  # Redirect to login page
                response.delete_cookie('mailkey')    # Delete the cookie
                messages.success(request, "Password successfully updated")
                return response
            else:
                messages.error(request, "User not found")
        else:
            messages.error(request, "Passwords do not match")
    
    return render(request, 'pass.html')

def dashboard(request):
    email = request.session['email']
    value = request.COOKIES.get('key')

    if not value:
        messages.warning(request, "Session has Expired, Login again")
        return redirect('studentlogin')

    student = Registration.objects.get(email=email)
    course = student.choose_course.all()

    # ✅ FIX: convert string-list → actual list
    if student.timing:
        student.timing = ast.literal_eval(student.timing)
        
    if student.hobbies:
        student.hobbies = ast.literal_eval(student.hobbies)

    return render(request, "dashboard.html", {'data': student,'course':course})


def logout(request):
     try:
                
                    print(request.session['email'])
                    del request.session['email']
                    response=render(request,'login.html')   
                    response.delete_cookie('key')   
                    return response
     except:
                pass   


# profile updatte
def profile(request):
    email=request.session['email']
    value=request.COOKIES.get('key')
    if not value:
      
        messages.warning(request,"Session has Expired,Login again")
        return redirect('studentlogin')
    student = get_object_or_404(Registration, email=email)

    if request.method == "POST":
        form = updateform(request.POST, request.FILES)

        if form.is_valid():
            student.full_name = form.cleaned_data['full_name']
            if form.cleaned_data.get('photo'):
             student.photo = form.cleaned_data['photo']
            student.date_of_birth = form.cleaned_data['dob']
            student.gender = form.cleaned_data['gender']
            student.educational_qualification = form.cleaned_data['educational_qualification']
            student.hobbies = (form.cleaned_data['hobbies'])
            student.mobile_no = form.cleaned_data['mobile_number']
            student.email = form.cleaned_data['email']
            student.guardian_name = form.cleaned_data['guardian_name']
            student.guardian_occupation = form.cleaned_data['guardian_occu']
            student.guardian_phone = form.cleaned_data['guardian_mob']
            # student.choose_course = form.cleaned_data['career']
            student.training_mode = form.cleaned_data['mode']
            student.location = form.cleaned_data['scope_location']
            student.timing = (form.cleaned_data['time'])
            student.address = form.cleaned_data['address']
            student.country = form.cleaned_data['country']
            student.state = form.cleaned_data['state']
            student.city = form.cleaned_data['city']
            student.pin_code = form.cleaned_data['pin']
            

            student.save()
            
            # selected_courses = form.cleaned_data["career"]  # list of course names
            # course_objs = Courses.objects.filter(course_name__in=selected_courses)
            # student.choose_course.set(course_objs)  # replaces old values
            messages.success(request, "Profile Updated Successfully! Return to Profile")
            return redirect("profile")

    else:
        hobb_val=ast.literal_eval(student.hobbies) if student.hobbies else []
        timing_value = ast.literal_eval(student.timing) if student.timing else []
        # career_values = student.choose_course.values_list('course_name', flat=True)

        form = updateform(initial={
    'full_name': student.full_name,
    'photo':student.photo,
    'dob': student.date_of_birth,
    'gender': student.gender,
    'educational_qualification': student.educational_qualification,
    'hobbies': hobb_val,  
    'mobile_number': student.mobile_no,
    'email': student.email,
    'guardian_name': student.guardian_name,
    'guardian_occu': student.guardian_occupation,
    'guardian_mob': student.guardian_phone,
    # 'career': list(career_values),  
    'mode': student.training_mode,
    'scope_location': student.location,
    'time': timing_value,
    'address': student.address,
    'country': student.country,
    'state': student.state,
    'city': student.city,
    'pin': student.pin_code,
    
})
    return render(request, "profile.html", {'form': form, 'student': student})
# update password

def pass_update(request):
    if request.method == "POST":
       
        # email=request.session['email']
        value=request.COOKIES.get('key')
        if not value:
           
            return redirect('studentlogin')
        form = pass_updateform(request.POST)
        if form.is_valid():
            epass = form.cleaned_data['epassword']
            passw = form.cleaned_data['password']
            cpass = form.cleaned_data['cpassword']

            user = Registration.objects.filter(email=value,existing_password=epass).first()
            if user:
                if passw == cpass:
                    user.password = passw
                    user.confirm_password = cpass
                    user.existing_password = passw
                    user.save()
                    messages.success(request, "Password updated, please login again")
                    if request.session['email']:
                        try:
                            
                                
                                del request.session['email']
                                response=render(request,'login.html')   
                                response.delete_cookie('key')   
                                return response
                        except:
                            pass 
                else:
                    messages.error(request, "Passwords do not match")
            else:
                messages.error(request, "Existing password incorrect")
    else:
        form = pass_updateform()

    return render(request, 'password_up.html', {'data': form})


# course seach
def course_search(request):
    email=request.session['email']
    value=request.COOKIES.get('key')
    student=Registration.objects.get(email=email)
    if not value:
      
        messages.warning(request,"Session has Expired,Login again")
        return redirect('studentlogin')
    course1=Courses.objects.filter(category_name='Data Science, AI, & Data Analytics Courses')
    course2=Courses.objects.filter(category_name='Software Courses')
    course3=Courses.objects.filter(category_name='Networking, Server, Cloud, & DevOps Courses')
    course4=Courses.objects.filter(category_name='Software Testing Courses')
    course5=Courses.objects.filter(category_name='Other Courses')
    return render(request,'coursesearch.html',{'course1':course1,'course2':course2,'course3':course3,'course4':course4,'course5':course5})
   

# dashboard mycourse
def my_course(request):
    email = request.session.get('email')
    value = request.COOKIES.get('key')

    if not email or not value:
        messages.warning(request, "Session expired, Login again")
        return redirect('studentlogin')

    student = Registration.objects.get(email=email)
    
    # Fetch directly from M2M relationship
    course = student.choose_course.all()

    return render(request, 'mycourse.html', {'course': course})


# enroll
def enroll(request,id):
    email = request.session.get('email')
    value = request.COOKIES.get('key')
    if not value or not email:
        messages.warning(request, "Session expired, Login again")
        return redirect('studentlogin')
    print("retrived id",id)
    student=Registration.objects.get(email=email)
    course=Courses.objects.get(id=id) 
    print(course)   
    student.choose_course.add(course)    
    messages.success(request, "Course Added Successfully!")

    return redirect('my_course')

# unenroll
def cancelenroll(request,id):
    email = request.session.get('email')
    value = request.COOKIES.get('key')
    if not value or not email:
        messages.warning(request, "Session expired, Login again")
        return redirect('studentlogin')
    print("retrived id",id)
    student=Registration.objects.get(email=email)
    course=Courses.objects.get(id=id) 
    print(course)   
    student.choose_course.remove(course)    
    messages.success(request, "Course Removed !")

    return redirect('my_course')
