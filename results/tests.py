from django.test import TestCase

# Create your tests here.
def result(request):
    return render(request=request, template_name="main/result.html", context={})

