from pyBook.models import User
import pyBook.utils.secrets as secrets

admin_salt = secrets.generate_salt()
admin_hash = secrets.hash_password("default", admin_salt)
admin_key = "65bf381f20cb704"

test_user = User("admin", "admin@fakeurl.com", 1,
                 "Admin", "User", "eng", admin_salt,
                 admin_hash, admin_key)
