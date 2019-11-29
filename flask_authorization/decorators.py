from functools import wraps
from flask import abort
from flask_login import current_user


def permission_required(permission):
    """Restrict a view to users with the given permission."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(403)
            if permission not in current_user.get_permissions():
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator