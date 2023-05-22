Certainly! Here's a basic Django view and template setup for hosting the Aptitude test and gathering the data. Please note that this is a simplified example to give you a starting point, and you may need to customize it further based on your specific requirements:

**views.py:**
```python
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
```

**forms.py:**
```python
from django import forms
from .models import AptitudeTestData

class AptitudeTestForm(forms.ModelForm):
    class Meta:
        model = AptitudeTestData
        fields = ['name', 'age', 'personality', 'intellectual_aptitude', 'love_connection', 'esteem_social_contribution', 'intellectual_interest', 'simple_pleasures', 'physical_engagement']
```

**models.py:**
```python
from django.db import models

class AptitudeTestData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    personality = models.CharField(max_length=100)
    intellectual_aptitude = models.IntegerField()
    love_connection = models.IntegerField()
    esteem_social_contribution = models.IntegerField()
    intellectual_interest = models.IntegerField()
    simple_pleasures = models.IntegerField()
    physical_engagement = models.IntegerField()
```

**aptitude_test.html (template):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Aptitude Test</title>
</head>
<body>
    <h1>Aptitude Test</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

**thank_you.html (template):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Thank You</title>
</head>
<body>
    <h1>Thank You!</h1>
    <p>Thank you for completing the Aptitude Test.</p>
</body>
</html>
```

Make sure to set up your Django project properly with the necessary URLs and template configurations. This is a basic structure to get you started, and you can customize it further according to your needs.