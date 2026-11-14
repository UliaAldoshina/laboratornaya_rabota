from datetime import datetime

def parse_datetime(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

print(parse_datetime("2024-01-15 10:30:00"))
print(parse_datetime("2023-12-31 23:59:59"))
print(parse_datetime("2000-06-01 00:00:00"))