from django.shortcuts import render
from .models import Guess
from .forms import GuessForm
import random
# Create your views here.
ram = random.randint(1,10)
def guess(request):
    message=''
    form = GuessForm()
    if request.method=='POST':
        form = GuessForm(request.POST)
        if form.is_valid():
            
            number = int(form.cleaned_data['number'])
            if number==ram:
                message=(' You have guessed the number.')
            elif number>ram:
                message='Guessed number is greater than the number.'
            elif number<ram:
                message='Guessed number is less than the number.'

    return render(request, 'guess.html', {'message':message, 'form':form})