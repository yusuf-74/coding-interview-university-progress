# coding-interview-university-progress
I will log any progress in jwasham study plan repo here and I will add some notes for each topic.


# 1. Big (O) Notation 

**what is ***Big O Notation*** and what is ***Omega*** and ***Theta*** ?**

- **Big O Notation** is a mathematical Notation used to describe the limiting behavior of a function when the argument tends towards a particular value or infinity. It is commonly used in computer science to describe the time complexity of algorithms. In this context, it provides an upper bound on the number of operations required by an algorithm as a function of the input size.

  - **Big O Notation Mathematical exepression**

    O(g(n)) = { f(n): there exist positive constants c and n0
            such that 0 ≤ f(n) ≤ cg(n) for all n ≥ n0 }

  - ***Big O Notation Graph***
   <img src="https://cdn.programiz.com/sites/tutorial2program/files/big0.png" style = "width:400px" alt = "Figure for Big Oh Notation">

- **Omega Notation**, on the other hand, provides a lower bound on the running time of an algorithm. It is used to describe the best-case running time of an algorithm.

  - **Omega Notation Mathematical exepression**

    Ω(g(n)) = { f(n): there exist positive constants c and n0 
            such that 0 ≤ cg(n) ≤ f(n) for all n ≥ n0 }

  - ***Omega Notation Graph***
   <img src="https://cdn.programiz.com/sites/tutorial2program/files/omega.png" style = "width:400px" alt = "Figure for Big Oh Notation">

- **Theta Notation** is used to describe the tight bound on the running time of an algorithm. It provides both an upper and a lower bound on the running time of an algorithm. In other words, if a function is Θ(g(n)), then it is both O(g(n)) and Ω(g(n)).
 
  - **Theta Notation Mathematical exepression**

    Θ(g(n)) = { f(n): there exist positive constants c1, c2 and n0
            such that 0 ≤ c1g(n) ≤ f(n) ≤ c2g(n) for all n ≥ n0 }

  - ***Theta Notation Graph***
   <img src="https://cdn.programiz.com/sites/tutorial2program/files/theta.png" style = "width:400px" alt = "Figure for Big Oh Notation">

- **Big O Notation** measures the upper bound or worst-case scenario for the growth rate of a function. In the context of computer science and algorithm analysis, it is used to describe the maximum amount of time an algorithm takes to solve a problem as the input size grows.