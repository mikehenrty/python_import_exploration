import test
from test import this as from_this
import test.this as test_this

print("--just test--")
print(test)

print("import test, then test.this")
print(test.this)

print("from test import this")
print(from_this)

print("imoprt this.test")
print(test_this)
