from rest_framework.serializers import ValidationError

class VideoUrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        # reg = re.compile('youtube')
        tmp_val = dict(value).get(self.field)
        if not 'youtube' in tmp_val or 'youtu.be' in tmp_val:
            raise ValidationError('Поддерживаются ссылки только с youtube.com')