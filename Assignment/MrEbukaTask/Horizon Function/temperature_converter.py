def converter(temperature, unit, threshold):
    if unit.lower() == "f":
        converted = (temperature * 9/5) + 32

    elif unit.lower() =="c":
        converted = (temperature * 9/5) + 32


    else:
        converted = (temperature * 9/5) + 32

    if converted < threshold:
        return "cold advisory"

    else:
        return "heat alert"


