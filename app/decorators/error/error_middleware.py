def error_middleware(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            return {"status": 500, "message": "Ocurrió un error en la aplicación.", "error": str(e)}, 500
    inner.__name__ = f.__name__
    return inner