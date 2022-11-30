from django.core.exceptions import ValidationError


def validate_file_size(image):
    if image.size > 2097152:
        raise ValidationError("Maximum size of profile picture is 2MB")
