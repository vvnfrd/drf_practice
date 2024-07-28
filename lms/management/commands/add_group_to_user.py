from django.core.management import BaseCommand
from users.models import User
from django.contrib.auth.models import Group


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('user_email', type=str)
        parser.add_argument('group_name', type=str)

    def handle(self, *args, **options):
        # print(options['user_email'], options['group_name'])
        if User.objects.get(email=options['user_email']).groups.filter(name=options['group_name']).exists():
            print(f'Пользователь уже состоит в этой группе')
        else:
            if not User.objects.filter(email=options['user_email']).exists():
                print('Пользователя с такой почтой не существует')
            else:
                if not Group.objects.filter(name=options['group_name']).exists():
                    Group.objects.create(name=options['group_name'])
                    print(f'Создана новая группа {options["group_name"]}')
                group = Group.objects.get(name=options['group_name'])
                print(User.objects.get(email=options['user_email']).groups.add(group))
                if User.objects.get(email=options['user_email']).groups.filter(name=options['group_name']).exists():
                    print('Пользователь добавлен в группу!')