from django.shortcuts import render, HttpResponse, redirect

def index(request):

    return render(request, 'goldapp/index.html')

def process(request):

    choice = request.POST['building']
    print(choice)
    if choice == 'farm':
        request.session['totalgold'] += random.randint(10, 20)
    elif choice == 'cave':
        request.session['totalgold'] += random.randint(5, 10)
    elif choice == 'house':
        request.session['totalgold'] += random.randint(2, 5)
    elif choice == 'casino':
        request.session['totalgold'] += random.randint(-50, 50)

    message = request.session['totalgold']
    


    return redirect("/")