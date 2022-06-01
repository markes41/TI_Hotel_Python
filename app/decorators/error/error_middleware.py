from functools import wraps

def error_middleware(f):
    @wraps(f)
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return {"status": 500, "message": "Ocurrió un error en la aplicación.", "error": str(e)}
    return inner