from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Contact
from django. contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Post,PostComment,Image
from.forms import ImageForm

# Create your views here.

def home(request):
    allposts=Post.objects.all()
    context ={'allposts':allposts}
    return render(request, "home.html",context)

def homeviews(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments =PostComment.objects.filter(post=post)
    context = {"post":post,"comments":comments,"user":request.user}
    return render(request, "homeviews.html",context)

def homeComment(request):
     if request.method=='POST':
        comment =request.POST.get("comment")
        user =request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        comment = PostComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been succesfully post")
     return redirect(f"/whispme/{post.slug}")

def contact(request):
    if request.method =='POST':
        name =request.POST['name']
        email = request.POST['email']
        phone =request.POST['phone']
        content= request.POST['content']
        contact = Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
        messages.success(request,"Your messages has sent successfully")
    return render(request, "contact.html")

def handleSignup(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        fname =request.POST['fname']
        lname =request.POST['lname']
        pass1 =request.POST['pass1']
        pass2 =request.POST['pass2']
        if pass1!=pass2:
            messages.warning(request,"your password didnt match")
            return redirect('/whispme')
        if not username.isalnum():
            messages.warning(request, "your username must contain letter and number")
            return redirect('/whispme')
            

        myuser =User.objects.create_user(username,email,pass1)
        myuser.first_name =fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been succesfully created")
        return redirect('/whispme')
    else:
        return HttpResponse("404 not found") 

def handleLogin(request):
        loginusername =request.POST['loginusername'] 
        loginpassword =request.POST['loginpassword'] 
        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect("/whispme")
        else:
            return HttpResponse("404 not found") 
        

def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect("/whispme")

def service (request):
    if request.method =="POST":
        form =ImageForm(data=request.POST, files =request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Your image has been upload succesfully")
            return render(request,"service.html")
    else:
        form = ImageForm()
        img =Image.objects.all()
        
    return render(request,"service.html",{'img':img,'form':form})

def about (request):
    return render(request,"about.html")
