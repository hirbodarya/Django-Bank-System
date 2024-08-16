from django.db import models, transaction
from django.core.exceptions import ValidationError
from account.models import Account


class Transaction(models.Model):
    from_account = models.ForeignKey(Account, related_name='transactions_sent', on_delete=models.CASCADE)
    to_account = models.ForeignKey(Account, related_name='transactions_received', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add = True)
    description = models.TextField(blank = True, null = True)
    transaction_valid = models.BooleanField(default=True)
    
def Record(from_account, to_account, amount=0, description=None, valid=True):
    Transaction.objects.create(
        amount=amount,
        from_account=from_account,
        to_account=to_account,
        description=description,
        transaction_valid=valid
    )
    

def transfer_money(from_account_id, to_account_id, amount, description=None):
    try:
        with transaction.atomic():
            from_account = Account.objects.get(id=from_account_id)
            to_account = Account.objects.get(id=to_account_id)

            if from_account.balance < amount:
                raise ValidationError("Insufficient funds.")

            from_account.balance -= amount
            from_account.save()

            to_account.balance += amount
            to_account.save()

            Record(from_account, to_account, amount=amount, description=description)

    except ValidationError as e:
        Record(from_account, to_account, valid=False)
        raise e