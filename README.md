[🔍 examples][examples] | [📖 documentation][documentation] | [📜 license][license] | [💡suggest silly ideas!][contact]  

# gapprox
a python toolkit to find the approximate function of any [graph][graph]  
instead of "find the graph of the function", youre flipping it: "find the function of the graph"

--- 
## 💾 installation
```shell
pip install gapprox
```
```shell
python -m pip install gapprox
```  
or get the source code:
```shell
git clone https://github.com/deftasparagusanaconda/gapprox
```
---
## 🔧 how to use

type `gapprox` in your terminal to launch a python interpreter with gapprox imported  
or do it manually in the python console:
```python
import gapprox as ga

mypoints = [1, 2, 4, -2, -4, 5], [1, 3, 3, -1, -5, 7]
line = ga.line(mypoints)

print(line)

# f(x) = 0.2 + 1.1333333333*x
```
```python
import gapprox as ga

mygraph = ga.API()

mygraph.paramgem = ga.paramgens.parabola.least_squares
mygraph.structgen = ga.structgens.polynomial
mygraph([2,3,6,5,4])

print(mygraph)
mygraph.plot()
```
check out more examples [here!][examples]

---
## ⚙️ how it works

### api
<p align="center">
        <img src="https://github.com/deftasparagusanaconda/gapprox/blob/main/documentation/diagrams/api.webp">
</p>

[converter](#converter) converts an expression from one form to another  
[analyzer][functional analysis] analyzes the input to generate parameters for an expression  
[optimizer](#optimizer) improves parameters by iterative [optimization][optimization]
[expression][expression] turns parameters into a math expression  
[converter](#converter) converts an expression from one form to another  

each component is optional. if you didnt set that component, the data simply passes through  
input and output are handled differently, depending on the interface  

### converter

<p align="center">
        <img height="250" src="https://github.com/deftasparagusanaconda/gapprox/blob/main/documentation/diagrams/converter.webp">
</p>

[parser][parsing] decodes string input into a callable function  
[sampler][sampling] samples a callable function into points  
[interpolator][interpolation] turns scattered points into a smooth function

the converter converts an expression from one form to another  
depending on input type and the desired output type, one or two components are chosen automatically  

as you parse string to function, you lose the ability to [differentiate/integrate](https://en.wikipedia.org/wiki/Differential_calculus) smoothly  
as you sample function to points, you lose the [smoothness][smoothness] of the function  
as you interpolate points to string, you add "fake" data which was not originally there  
string is the most favourable representation, so the api will try to preserve it

### optimizer

<p align="center">
        <img height="250" src="https://github.com/deftasparagusanaconda/gapprox/blob/main/documentation/diagrams/optimizer.webp">
</p>

[predictor][iterative method] finds the next best set of parameters to minimize error  
[expression][expression] turns parameters into a math expression  
[error][error analysis] calculates the difference between original input and approximation  

optimizer improves parameters by iterative [optimization][optimization]  
it holds its own configuration. this is done by making it an [object][object in cs]  
it runs until it reaches an end condition, such as time limit, iteration limit, ...  
it is also capable of multithreading/parallel processing  

---
## ⏳ coming soon ~
- DAG/expression trees  
- multi-objective analysis (and [pareto front](https://en.wikipedia.org/wiki/Pareto_front) presentation)
- webUI  
- GUI
- symbolic regression  
- complex numbers
- parametric function support  
- multiple-input multiple-output
- n-dimensional plotters  
- surface approximation  
- [many-to-many][relation types] relation approximation  
- point density evaluators  
- hypersonic blasters 🚀

in the far far future, ga will support multiple-input multiple-output approximation. for m inputs and n outputs, it runs n approximations of m-dimensional [manifolds][manifold] separately  
effectively, this turns it into a general-purpose prediction library, analogous to AI  
currently, ga only supports single-input single-output [many-to-one][relation types] functions. see [roadmap][roadmap] for details  

---
## 📔 you read all that?!?

this project is still budding 🌱 if you'd like to change something, add something, or suggest ideas—[come say hi!][contact]

with love, and a passion for maths ~  
\- [daa][contact] 🌸

[examples]: https://github.com/deftasparagusanaconda/gapprox/tree/main/examples/  
[documentation]: https://github.com/deftasparagusanaconda/gapprox/tree/main/documentation/  
[license]: https://github.com/deftasparagusanaconda/gapprox/tree/main/LICENSE  
[contact]: https://discordapp.com/users/608255432859058177
[roadmap]: <https://github.com/deftasparagusanaconda/gapprox/tree/main/documentation/personal rants/roadmap MIMO.txt>

[graph]: https://en.wikipedia.org/wiki/Graph_of_a_function  
[function]: https://en.wikipedia.org/wiki/Function_(mathematics)
[functional analysis]: https://en.wikipedia.org/wiki/Functional_analysis
[approximation]: https://en.wikipedia.org/wiki/Approximation_theory
[manifold]: https://en.wikipedia.org/wiki/Manifold
[smoothness]: https://en.wikipedia.org/wiki/Smoothness
[parsing]: https://en.wikipedia.org/wiki/Parsing
[sampling]: https://en.wikipedia.org/wiki/Sampling_(statistics)
[interpolation]: https://en.wikipedia.org/wiki/Interpolation
[optimization]: https://en.wikipedia.org/wiki/Mathematical_optimization
[iterative method]: https://en.wikipedia.org/wiki/Iterative_method
[expression]: https://en.wikipedia.org/wiki/Expression_(mathematics)
[error analysis]: https://en.wikipedia.org/wiki/Error_analysis_(mathematics)
[relation types]: https://en.wikipedia.org/wiki/Relation_(mathematics)#Combinations_of_properties
[object in cs]: https://en.wikipedia.org/wiki/Object_(computer_science)
