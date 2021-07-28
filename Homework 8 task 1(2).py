import re


def web_sorted(read_line):
    reg_ip = re.compile(r'^[\d.]+')
    reg_datetime = re.compile(r'[\d{2}]+[/][a-zA-Z0-9:+/]+[\s][+\d]+')
    reg_type = re.compile(r'\s[\"][A-Z]+\s+')
    reg_resource = re.compile(r'[/][\w_\-.]+[/][\w_\-.]+\s')
    reg_number = re.compile(r'\s\d{3}\s')
    reg_number2 = re.compile(r'\s\d+\s["]')

    reg_naim_datetime = reg_datetime.findall(read_line)
    reg_naim_ip = reg_ip.findall(read_line)
    reg_naim_type = reg_type.findall(read_line)
    reg_naim_resource = reg_resource.findall(read_line)
    reg_naim_number = reg_number.findall(read_line)
    reg_naim_number2 = reg_number2.findall(read_line)

    result = str(reg_naim_ip) + str(reg_naim_datetime) + str(reg_naim_type) + str(reg_naim_resource) + str(reg_naim_number) + str(reg_naim_number2)

    return result
