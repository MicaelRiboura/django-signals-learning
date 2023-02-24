from django.dispatch import Signal, receiver
from datetime import datetime

def log_event(message):
    # Creates file 'log_event.log' in project root with append mode 'a'
    f = open('log_event.log', 'a')
    # Write current timestamp with user submitted message
    f.write(datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ' -- ' + message + '\n')
    f.close()

event_signal = Signal()

@receiver(event_signal)
def view_event_loggin(sender, **kwargs):
    print(sender, kwargs['message'])
    message = '{} - {}'.format(sender, kwargs['message'])
    log_event(message)