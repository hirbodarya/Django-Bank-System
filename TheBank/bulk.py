import random
from account.models import Account
from person.models import Person
from django.db import transaction


def generate_random_balance():
    return random.randint(100, 1000000000)


def create_random_accounts(num_records):
    persons = list(Person.objects.all())
    if not persons:
        raise ValueError("No Person records found. Cannot generate accounts.")

    last_account = Account.objects.order_by('-id').first()
    last_account = last_account.id if last_account else 0

    accounts = []
    for i in range(num_records):
        account_num = str(i+ last_account).zfill(16) 
        balance = generate_random_balance()
        owner = random.choice(persons)
        
        account = Account(
            account_number=account_num,
            balance=balance,
            owner=owner
        )
        
        accounts.append(account)
    
    with transaction.atomic():
        Account.objects.bulk_create(accounts)
