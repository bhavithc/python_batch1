# Special file get executed when package is imported
# It's similar in spirit to a constructor.
# print("Loading package...")

# Import commonly used modules
# Instead of from math_utils.add import add
# 
# from .add import add
# from .subtract import subtract
#
# then
# from math_utils import add


# Package-level variables
# version = "1.0"
# print(math_utils.version)

# 4. Define public API
# 

print("Loading package...")

from .add import add
from .sub import sub


version = "1.2.3"

def foo():
    print("foo called")