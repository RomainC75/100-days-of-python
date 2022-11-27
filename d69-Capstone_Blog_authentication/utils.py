from flask_login import current_user
from flask import redirect, request, url_for, abort
from functools import wraps

def admin_only(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and  current_user.id==1:
            return func(*args, **kwargs)
        return abort(404, description="not allowed!")
    return decorated_function
        
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if g.user is None:
#             return redirect(url_for('login', next=request.url))
#         return f(*args, **kwargs)
#     return decorated_function
