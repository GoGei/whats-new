from django.core.validators import RegexValidator

PhoneValidator = RegexValidator(regex=r'^([+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$',
                                message=(
                                    "Phone number must be entered in the format: '+380(99)-999-9999'."))
