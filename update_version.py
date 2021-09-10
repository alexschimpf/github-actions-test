with open('version', 'r+') as f:
    version = int(f.read().strip())
    f.seek(0)
    f.write(str(version + 1) + '\n')
    f.truncate()
