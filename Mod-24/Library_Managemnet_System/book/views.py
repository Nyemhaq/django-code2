from django.shortcuts import render,redirect, get_object_or_404
from .forms import signupForm,changeprofileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import BookModel
from borrow_transactions.forms import DepositForm
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

def user_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(req,req.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = name , password = user_pass)
            if user is not None:
                login(req,user)
                messages.success(req,"logged in successfully")
                return redirect("profile")
    else:
        form = AuthenticationForm()
    return render (req,'book/signup.html',{'form':form, 'type':'Login'})

@login_required
def profile(req):
    return render (req,'book/profile.html')

@login_required
def user_logout(req):
    logout(req)
    return redirect("login")
        
@login_required
def change_password(req):
    if req.method == "POST":
        form = PasswordChangeForm(req.user, data=req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Password Updated Successfully!')
            update_session_auth_hash(req,form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=req.user)
    return render (req,'book/change_pass.html',{'form':form})

def details(request, id):
    book = BookModel.objects.get(pk=id)
    return render(request, 'book/details.html', {'book': book})
    
@login_required
def buy_now(req,id):
    if req.method == 'POST':
        book = get_object_or_404(BookModel, pk=id)
        if book.total_copy > 0:
            price = book.borrowing_price
            balance = req.user.account.balance
            if balance >= price:
                req.user.account.balance -= price
                req.user.account.save()
                
                book.total_copy -= 1
                book.borrow_by.add(req.user)
                book.returned = False
                book.save()
            
                borrow_books = BookModel.objects.filter(borrow_by=req.user)
                messages.success(req,'Book Borrowed Successfully!')
                return render(req, "book/borrowed_books.html", {'borrow_books': borrow_books})
            
            else:
                messages.warning(req,'Out of Balance, Please Deposite!')
                return redirect("deposit_money")
            
        else:
            messages.warning(req,' Sorry! Book is not Available :( ')
            return redirect("home")
    else:
        return redirect("home")
    
def send_transaction_email(user, borrowed_books, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'borrowed_books': borrowed_books,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()
    
@login_required
def borrow_books(req):
    borrowed_books = BookModel.objects.filter(borrow_by=req.user)
    send_transaction_email(req.user,borrowed_books, "Borrowed Book Message", "book/borrow_book_email.html")
    return render(req, 'book/borrowed_books.html', {'borrowed_books': borrowed_books})

@login_required
def review(req, id):
    if req.method == 'POST':
        book = get_object_or_404(BookModel, pk=id)
        review = req.POST.get('review')
        if review:
            book.review = review
            book.save()
        
    return redirect('buy_now', id=req.user.id)

    
@login_required
def return_book(req,id):
    book = get_object_or_404(BookModel, pk=id)
    
    price = book.borrowing_price
    req.user.account.balance += price
    req.user.account.save()
    
    book.returned = True
    book.total_copy += 1
    book.save()
    
    messages.success(req,'Book Returned Successfully!')
    
    return redirect('borrow_books')

