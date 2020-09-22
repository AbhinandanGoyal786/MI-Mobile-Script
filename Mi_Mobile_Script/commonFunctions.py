
def initdic(path):
    if path.split(".")[-1].lower().strip()=='json':
        import json
        f = open(path, )
        d = json.load(f)
        f.close()
    else:
        d = {}
        with open(path) as f:
            for line in f:
                (key, val) = line.split('==')
                d[key] = str(val).strip()
    return d


def writefile(path, txt):
    text_file = open(path, "w")
    n = text_file.write(txt)
    text_file.close()


def readfile(path):
    text_file = open(path, "r")
    n = text_file.read()
    text_file.close()
    return n


def reload(driver, url):
    driver.get(url=url)

if __name__ == "__main__":
    pass