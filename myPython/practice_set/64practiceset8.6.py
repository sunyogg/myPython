# 8.15 and 8.16
# 1)
import module
#importing every function from the 
tobeprinted = ['phone cover','buttons','pen','box','laptop case']
completedprint = []

module.printmodel(tobeprinted,completedprint)
module.showprintedmodel(completedprint)

#--------------------------------------------------------------------------------------------

# 2)
import module as m

tobeprinted = ['carrot','tomatos','capsicum','cabbage']
completed = []

m.printmodel(tobeprinted,completed)
m.showprintedmodel(completed)

#--------------------------------------------------------------------------------------------

# 3)
from module import *

tobeprinted = ['mango','apple','banana','strawberry']
completed = []

printmodel(tobeprinted,completed)
showprintedmodel(completed)

#--------------------------------------------------------------------------------------------

# 4)
from module import printmodel

tobeprinted = ['shark','dolphin','stingrey','whale']
completed = []

printmodel(tobeprinted,completed)

#--------------------------------------------------------------------------------------------

# 4.2)
from module import printmodel, showprintedmodel

tobeprinted = ['dog','cat','turtoise','rabbit']
completed = []

printmodel(tobeprinted,completed)
showprintedmodel(completed)

#--------------------------------------------------------------------------------------------
# 5)
from module import printmodel as pm 
from module import showprintedmodel as sm

tobeprinted = ['lion','tiger','cheetah','leopard']
completed = []

pm(tobeprinted,completed)
sm(completed)

#--------------------------------------------------------------------------------------------


