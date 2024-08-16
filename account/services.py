from django.db import transaction
from .models import Account, Transaction

def transfer_funds(from_account_id, to_account_id, amount, description=None):
    try:
        with transaction.atomic():
            # Get the accounts
            from_account = Account.objects.get(id=from_account_id)
            to_account = Account.objects.get(id=to_account_id)

            if from_account.balance < amount:
                raise ValueError("Insufficient funds")

            # Deduct from sender account
            from_account.balance -= amount
            from_account.save()

            # Add to receiver account
            to_account.balance += amount
            to_account.save()

            # Record the transaction (optional)
            Transaction.objects.create(
                from_account=from_account,
                to_account=to_account,
                amount=amount,
                description=description
            )

    except Account.DoesNotExist:
        raise ValueError("Account not found")
    except Exception as e:
        # Handle other exceptions as needed
        raise e
