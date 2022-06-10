import gspread
from django.contrib import messages
from datetime import datetime
from django.shortcuts import redirect, render

def add_user(request):
    if request.method=="POST":
        try:
            fullname = request.POST['name']
            phone = request.POST['number']
            gs = gspread.service_account(filename='users.json')
            k = gs.open('Users').worksheet('user1')
            user = [fullname, phone, f"{datetime.now().strftime('%d-%m-%Y')}"]
            k.append_row(user)
            messages.success(request, "EduSpace Academiya admini tez orada siz bilan bog'lanadi")
        except:
            messages.error(request, "Muvaffaqiyatsiz urinish, iltimos qayta urinib ko'ring!")
        return redirect('social')
    return render(request,'social.html')
