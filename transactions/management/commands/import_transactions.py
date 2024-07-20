import json
from django.core.management.base import BaseCommand
from transactions.models import Transaction
from users.models import User
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Import transactions from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file to import')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as file:
            data = json.load(file)
            for item in data:
                user = User.objects.get(name=item['user'])
                Transaction.objects.create(
                    user=user,
                    date=parse_date(item['date']),
                    amount=item['amount'],
                    currency=item['currency'],
                    in_out=item['in_out'],
                    tag=item['tag']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported transactions'))
