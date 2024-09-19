def main():
    filename = input('Enter a filename: ')
    file = open(filename, encoding='utf-8')
    # file is an object of _io.TextIOWrapper class
    # has these attributes:
    # 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines'

    content = file.read()
    file.close()

    print(content)

if __name__ == '__main__':
    main()
