def check_age(age):
    if age<18:
        raise ValueError("not eligible!")
    return "eligible"
print(check_age(15))