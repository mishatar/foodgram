from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_even(value):
    if value.isnumeric():
        raise ValidationError(
            _('%(value)s is not a number!'),
            params={'value': value},
        )

def validate_mark(value):
    if not value.isalpha():
        raise ValidationError(
            _('%(value)s is not a marks!'),
            params={'value': value},
        )