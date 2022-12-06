import pandas as pd
import numpy as np
import pyfpgrowth as fp


dict1 = {'id': [0, 1, 2, 3],
         'items': [["bramki", "ochraniacze"],
                   ["kij", "bramki", "ochraniacze", "kask"],
                   ["kask", "ochraniacze"],
                   ["kij", "ochraniacze", "kask"]]}

tranactionSet = pd.DataFrame(dict1)

patterns = fp.find_frequent_patterns(tranactionSet['items'], 1)
print(patterns)

rules = fp.generate_association_rules(patterns, 0.3)
print(rules)
