from django.db.models.signals import pre_save, pre_delete, post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Transmitting, Warehouse


# if create warehouse object and warehouse with this product already exists, add count to existing warehouse
@receiver(pre_save, sender=Warehouse)
def update_or_create_warehouse(sender, instance, **kwargs):
    print('instance', instance.__dict__)
    print('kwargs', kwargs)
    print('sender', sender)
    if instance.pk is None:
        try:
            warehouse = Warehouse.objects.get(product=instance.product)
            print('before warehouse', warehouse.__dict__)

            warehouse.count += instance.count
            print('after warehouse', warehouse.__dict__)
            warehouse.save()
            # raise ValidationError('Omborda bunday mahsulot mavjud')
            print('Warehouse updated')

            # cancel creating new warehouse object by ValidationError
            raise ValidationError(f'Omborda {instance.product} mahsuloti mavjud yangi ombor yaratish mumkin emas')

        except Warehouse.DoesNotExist:
            pass


# create transmitting signal for updating warehouse
@receiver(pre_save, sender=Transmitting)
def update_warehouse(sender, instance, **kwargs):
    try:
        warehouse = Warehouse.objects.get(product=instance.product)
    except Warehouse.DoesNotExist:
        raise ValidationError('Mahsulot omborda mavjud emas')
    if warehouse.count < instance.count:
        raise ValidationError('Omborda yetarli mahsulot yo\'q')
    else:
        warehouse.count -= instance.count
        warehouse.save()
        print('Warehouse updated')


# delete transmitting signal for updating warehouse
@receiver(pre_delete, sender=Transmitting)
def delete_warehouse(sender, instance, **kwargs):
    try:
        warehouse = Warehouse.objects.get(product=instance.product)
    except Warehouse.DoesNotExist:
        raise ValidationError('Mahsulot omborda mavjud emas')
    warehouse.count += instance.count
    warehouse.save()
    print('Warehouse updated')
