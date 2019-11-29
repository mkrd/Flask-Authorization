# Flask-Authorization
Simple user authorization to use alongside with Flask-Login.

## Installation
```
pip3 install Flask-Authorization
```

## Usage
```python
from flask_Authorization import Authorize
authorize = Authorize()

# Initialize Extension
authorize.init_app(app)
```

For Flask-Authorization to work properly, your user models needs to implement a function called `get_permissions()` that returns a list of permissions. You can define any permissions you like, but `"ROOT", "ADMIN", "USER"` are recommended.
Flask-Authorization will check if the current user has the required permissions on routes decorated with the `@flask_authorization.permission_required(permission)` decorator.