def main():
    list = ['a', 'b', 'c', 'd', 'e', 'f']
    values = []
    for i, m in enumerate(list):
        a = (f'[{i}_{m}]')
        values.append(a)
    return values

values = main()
for value in values:
    print(value)