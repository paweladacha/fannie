# fannie

Simple yet very usefull implementation of partial function.

## contents
- intended use
- how it works?
- package contents

## intended use
Day-to-day use and protyping via interpreter, ipython or Jupyter notebook.

## how it works?
Simplest differences between this and *functools* implementation are mutable attributes '.f' (stores function) and '.p' (stores parameters|signature).
*(When it comes to "function" attribute, if it seems an overkill please look at [intended use](#intended_use).)*
More important difference lays in usage. Defined "variable placeholder" can be used to intuivelly and explicitlly point variable argument. In other words user can literally point with his finger wich argument should be variable.
Of course *keywords argument* solve this inconvenience but some built-in functions and methods (python 3.5) does not provide this feature. Also, when it comes to quick prototyping signatures sticked with 'key=value' parameters become are "too explicit".

### small extension
two @funcs defined in tools help in creation of more complex partials or "flows": *fan* and *pin*. They can be seen as two basic ways of connecting compenents in electric circuits:
fan - parallel
pin - sequential
Sequential "pin" uses the output of the previous call as an input to subsequent call.
Parallel "fan" calls all given functions with the same variable argument.


-----
## package contents:
- init
- core
- tools
<!-- sprawdzic -->
### core
defines partial class and "variable placeholder" constant

