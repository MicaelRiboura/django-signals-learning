from django.shortcuts import render
from .models import Employees
from .signals import event_signal
from django.http import HttpResponse

# Create your views here.
def test_logging(request):
    # Empty string
    message = ''
    try:
        # Create an object
        emp_inst = Employees.objects.create(first_name='user1',
                                            last_name='last_user',
                                            address='address',
                                            age=93)
        message += 'Employees object created: {} {}'.format(emp_inst.first_name, emp_inst.last_name)
    except (Employees.DoesNotExist, ValueError) as e:
        print('Error during employees creating occured: ', e)
        # Convert ValueError error to string for successful concatenation
        message += str(e)
        emp_inst = None
        pass

    event_signal.send(sender='View: test_logging', message=message, instance=emp_inst)
    return HttpResponse('bla')
