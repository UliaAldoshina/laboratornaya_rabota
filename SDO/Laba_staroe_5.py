def read_lines(file_path, count):
    lines = []
    with open(file_path, "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            if i < count:
                lines.append(line.strip())
            else:
                break
    return lines
print(read_lines("test.txt", 2))
print(read_lines("test.txt", 3))
print(read_lines("test.txt", 5))