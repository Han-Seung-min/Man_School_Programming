import sum_1

sum_1.sum_11(2, 3)


import p.sum_2

p.sum_2.sum_11(1, 2)


import p.ch.sum_3

p.ch.sum_3.sum_11(4,5)

import package01.sum_pa1

package01.sum_pa1.hello()
package01.sum_pa1.sum_11(1, 2)

from package01.sum_pa1 import hello

hello()

from package01 import sum_pa1

sum_pa1.hello()

from package01 import *

sum_pa1.hello()
sum_pa2.sum_11(3,4)



