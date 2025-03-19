def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not found"
        case 500:
            return "Internal server Error"
        case _:
            return "Unknown Status"
        
#Usage
print(http_status(200))     #ok
print(http_status(404))     #Not found
print(http_status(500))     #Internal server Error
print(http_status(403))     #Unknown Status