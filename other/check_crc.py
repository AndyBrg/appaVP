
def int_to_bytes(number: int) -> bytes:
    return number.to_bytes(
        length=(8 + (number + (number < 0)).bit_length()) // 8,
        byteorder='big', signed=True)

def check_crc(data: bytes) -> bool:
    package_len = 19 #Длина пакета 
    if len(data) == package_len:
        check_sum = 0
        for byte in range(package_len - 1):
            check_sum += data[byte]
        if data[-1:] == int_to_bytes(check_sum)[-1:]:
            return True
        else:
            return False
    else:
        return False
