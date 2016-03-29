## Polynomial Multiplication in 3 sub problems
This assignment shows what performance gains you can get from an algorithm by
dividing it into 3 sub problems rather than 4.

### Hi
My algorithms are contained in the Poly.py file. To test that the algorithms are
generating the same numbers run ```python test.py``` and compare the results.

#### Getting Data
The raw data collected from my algorithms are contained in outdiv.txt and outsimp.txt
for the divide and conquer and simple algorithms respectively. To collect data
all you have to do is run ```python simpleproblems.py``` or ```python divproblems.py```
and that will generate new data in the output text files mentioned earlier. I
also have a problems.py file which runs both the algorithms side by side but I
found that to be slower. If you do run that file, the output goes to out.txt.

#### Graph
If the graph in the report doesn't do it for you, you can generate it yourself
by installing matplotlib ```sudo apt-get install python-matplotlib``` and running
```python graph.py```.
