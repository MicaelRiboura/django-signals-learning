from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from core.models.employee_model import Employees
from core.models.shift_model import Shifts
from datetime import datetime

@receiver(post_save, sender=Employees)
def employee_created(sender, instance, created, **kwargs):
    if created:
        try:
            # Checa se turno está relacionado a um número inferior a 3 funcionários
            # Ordena por data do turno e obtém o primeiro objeto
            free_shift = Shifts.objects.annotate(employee_count=Count('employees_shift')) \
                .filter(employee_count__lt=3).order_by('shift_date').first()
        except (Shifts.DoesNotExists, IndexError, Exception,) as e:
            print('free_shift error: ', e)
            free_shift = None
        # Checa se turno vazio existe
        if free_shift:
            # Atribui funcionário ao turno vazio
            free_shift.employees_shift.add(instance.id)
        else:
            # Não foi encontrado turno livre
            # Procura o turno com a data mais recente e adiciona o objeto turno com: última data + 1 dia
            try:
                try:
                    latest_date = Shifts.objects.order_by('-shift_date').values('shift_date').first()
                    latest_date = latest_date['shift_date'] + datetime.timedelta(days=1)
                except (Shifts.DoesNotExist, IndexError, Exception) as e:
                    print('latest_date Error: ', e)
                    latest_date = None
                # Checa se há pelo menos um objeto no Banco de Dados
                if latest_date:
                    new_shift = Shifts.objects.create(shift_date=latest_date)
                    new_shift.save()
                    # Adiciona relação M2M
                    new_shift.employees_shift.add(instance.id)
                else:
                    # Não há nenhum turno no Banco, padronizando o input com a data atual
                    new_shift =  Shifts.objects.create()
                    new_shift.save()
                    new_shift.employees_shift.add(instance.id)

            except (Shifts.DoesNotExist, Exception) as e:
                print(e)


@receiver(pre_save, sender=Employees)
def wipe_expired_shifts(sender, **kwargs):
    current_date = datetime.date.today()
    try:
        Shifts.objects.filter(shift_date__lt=current_date).delete()
    except (Shifts.DoesNotExist, Exception) as e:
        print('Wipe redundant shifts Error: ', e)