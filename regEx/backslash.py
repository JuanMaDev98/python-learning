# Para poder buscar un backslash literalmente en un regex es necesario hacerlo de esta manera

import re

s = "balbla\la"
print(bool(re.search(r"\\", s))) 