# Django: Validator
from django.core.validators import RegexValidator
from django.contrib.auth.validators import ASCIIUsernameValidator

username_validator = RegexValidator(r'[a-zA-Z-_\d+\.]+')

