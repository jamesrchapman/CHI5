from django.shortcuts import render, redirect
from .forms import AptitudeTestForm

def aptitude_test(request):
    if request.method == 'POST':
        form = AptitudeTestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('thank_you')  # Redirect to a thank you page after form submission
    else:
        form = AptitudeTestForm()

    return render(request, 'aptitude_test.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')