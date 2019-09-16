if __name__ == '__main__':
    s = input()
    checks = {
        "alnum": False,
        "alpha": False,
        "digit": False,
        "lower": False,
        "upper": False
    }

    for char in list(s):
        if not checks["alnum"] and char.isalnum():
            checks["alnum"] = True

        if not checks["alpha"] and char.isalpha():
            checks["alpha"] = True

        if not checks["digit"] and char.isdigit():
            checks["digit"] = True

        if not checks["lower"] and char.islower():
            checks["lower"] = True

        if not checks["upper"] and char.isupper():
            checks["upper"] = True 

    keys = list(checks.keys())
    keys.sort()

    for key in keys:
        print(checks[key])
