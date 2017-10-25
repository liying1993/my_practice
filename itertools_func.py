def vowel(c):
    return c.lowel() in 'aeiou'
list(filter(vowel, 'Asrdvark'))#['A' ,'a', 'a']

import itertools
list(itertools.filterfalse(vowel, 'Aardvark'))#['r', 'd' ,'v', 'r', 'k']

list(itertools.dropwhile(vowel, 'Aardvark'))#['r', 'd', 'v', 'a', 'r', 'k']

list(itertools.takewhile(vowel, 'Aardvark'))#['A','a']

list(itertools.compress('Aardvark', (1,0,1,1,0,1)))#['A', 'a', 'r', 'd']

list(itertools.islice('Aardvark', 4))#['A', 'a', 'r', 'd']

list(itertools.islice('Aardvark',4,7))#['v','a','r']

list(itertools.islice('Aardvark',1,7,2))#['a','d','a']
