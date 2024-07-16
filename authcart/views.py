from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import TokenGenerator, generate_token
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate, login, logout


# View for user signup
def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        
        # Check if passwords match
        if password != confirm_password:
            messages.warning(request, "Password is Not Matching")
            return render(request, 'signup.html')
        
        try:
            # Check if user with this email already exists
            if User.objects.get(username=email):
                messages.info(request, "E-mail already exists")
                return render(request, 'signup.html')
        except Exception as identifier:
            pass

        # Create a new user and mark them as inactive until activation
        user = User.objects.create_user(email, email, password)
        user.is_active = False
        user.save()
        
        # Prepare activation email with activation link
        email_subject = "Activate Your Account"
        message = render_to_string('activate.html', {
            'user': user,
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })

        # Send activation email to the user's email address
        email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
        email_message.send()
        
        messages.success(request, "Activate your Account by clicking the link in your mail")
        return redirect('/auth/login/')

    return render(request, "signup.html")


# View for activating user account
class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            # Decode uidb64 and get the user object
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        
        # Check if user is not None and token is valid
        if user is not None and generate_token.check_token(user, token):
            # Activate the user's account
            user.is_active = True
            user.save()
            messages.info(request, 'Account Activated Successfully')
            return redirect('/auth/login/')
        
        return render(request, 'activatefail.html')


# View for handling user login
def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']
        
        # Authenticate user credentials
        myuser = authenticate(username=username, password=userpassword)

        if myuser is not None:
            # If authentication is successful, log the user in
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/auth/login')
    
    return render(request, 'login.html')


# View for handling user logout
def handlelogout(request):
    logout(request)
    messages.info(request, "Logout Success")
    return redirect('/auth/login')


# View for requesting password reset email
class RequestResetEmailView(View):
    def get(self, request):
        return render(request, 'request-reset-email.html')
    
    def post(self, request):
        email = request.POST['email']
        user = User.objects.filter(email=email)
        
        if user.exists():
            # Prepare and send password reset email
            email_subject = '[Reset Your Password]'
            message = render_to_string('reset-user-password.html', {
                'domain': '127.0.0.1:8000',
                'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token': PasswordResetTokenGenerator().make_token(user[0])
            })

            email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
            email_message.send()

            messages.info(request, "WE HAVE SENT YOU AN EMAIL WITH INSTRUCTIONS ON HOW TO RESET THE PASSWORD")
            return render(request, 'request-reset-email.html')


# View for setting new password after reset
class SetNewPasswordView(View):
    def get(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token
        }
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.warning(request, "Password Reset Link is Invalid")
                return render(request, 'request-reset-email.html')

        except DjangoUnicodeDecodeError as identifier:
            pass

        return render(request, 'set-new-password.html', context)

    def post(self, request, uidb64, token):
        context = {
            'uidb64': uidb64,
            'token': token
        }
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        
        # Check if passwords match
        if password != confirm_password:
            messages.warning(request, "Password is Not Matching")
            return render(request, 'set-new-password.html', context)
        
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            
            # Set new password and save the user object
            user.set_password(password)
            user.save()
            
            messages.success(request, "Password Reset Success. Please Login with New Password")
            return redirect('/auth/login/')

        except DjangoUnicodeDecodeError as identifier:
            messages.error(request, "Something Went Wrong")
            return render(request, 'set-new-password.html', context)

        return render(request, 'set-new-password.html', context)

