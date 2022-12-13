import re
from django.core.exceptions import ValidationError


def hex_code_validator(code):
    if not re.search(r"#(([a-z]|[A-Z])|[0-9]){6}", code):
        raise ValidationError("Please input a valid hex code")
