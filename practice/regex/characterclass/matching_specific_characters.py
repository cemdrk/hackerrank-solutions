
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][\.,]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
