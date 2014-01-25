import json

suckersFile = 'suckers.json'

def serialize(data):
    return json.dumps(data) 

def deserialize(data):
    return json.loads(data)

def getFromFile(filename):
    try:
        fp = open(filename, 'r')
        result = fp.read()
        fp.close()
        return result
    except IOError:
        return False

def putInFile(data, filename):
    try:
        fp = open(filename, 'w')
        fp.write(data)
        fp.close
        return True
    except IOError:
        return False
