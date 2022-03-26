def convert_IP(ip: str) -> str:
    return ".".join([bin(int(seg))[2:] for seg in ip.split(".")])

if __name__ == "__main__":
    ip = "132.172.23.209"
    print(convert_IP(ip))

