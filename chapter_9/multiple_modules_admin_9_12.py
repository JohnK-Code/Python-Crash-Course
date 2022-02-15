#### TRY IT YOURSELF - Chapter 9 - Page 180 - Multiple Modules 
# Create Admin Instance using imported modules 
from multiple_modules_priv_admin_9_12 import Admin

john = Admin('kirsty', 'kelly', 32, 'test@test.com', 'glenrothes')
john.describe_user()
john.privileges.show_privileges()