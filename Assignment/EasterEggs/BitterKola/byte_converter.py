"""
byte_converter.py


"""
bytes = int(input("Enter Number of bytes: "))

kilo = bytes / 1024
mega = bytes / (1024 ** 2)
giga = bytes / (1024 ** 3)

print(f"{bytes} bytes in Kilobytes: {kilo}:.3fKB")
print(f"{bytes} bytes in MegaBytes: {mega:.3f}MB")
print(f"{bytes} bytes in Gigabytes: {giga:.3f}GB")
