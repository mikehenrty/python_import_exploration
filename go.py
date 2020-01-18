import test
from test import this as from_this
import test.this as test_this

print("\n-- import test--")
print(test)

print("\n-- import test, then test.this")
print(test.this)

print("\n-- from test import this")
print(from_this)

print("\n-- import this.test")
print(test_this)
