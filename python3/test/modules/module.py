from apt import Cache

def package_installed():
        
    cache = Cache()
    package = cache['apt']
    if package.is_installed:
        installed = True
        return installed
    if not package.is_installed:
        installed = False
        return installed

def hello():
    print("hello world")
