# CSP

## Team Members

- Yahya Maleki Joobani
- Seyed Masih Sajadi
- Yasaman Bakhshi

## Initial settings

This part is taking place in main.py file, where `Halls` and `Groups`
are created. Input lines create these objects, as well as a list for halls
and a list for groups. These lines are used to create domains of
`Halls` as well as preferences of `Groups`

## Classes and Methods

### class `Hall`

This class has three attributes. The first and the second one are `hallNumber` and `hallName` which
are the `number` and the `name` of that `Hall` respectively. The third attribute
is `domain`, which is a list consisting of `Groups` that can be legally assigned to a `Hall`

### class `Group`

This class has three attributes. The first and the second one are `groupNumber` and `groupName` which
are the `number` and the `name` of that `Group` respectively. The third attribute
is `preference`, which is a list consisting of `Halls` that a `Group` tends to choose.

### class `Problem`

A class with many algorithms/methods

#### Important attributes

- `constraintPairsList` is a list of conflict pairs. ex: `Halls`
  H1 and H2 cannot have the same value.

- `hallsList` is the initial list of `Halls`.

- `groupsList` is the initial list of `Groups`.

#### Methods

##### `MRV`

`MRV` is a method that gets a list of `Halls` and returns the most constrained
one.

`Time complexity`: O(n) where n is the number of halls in hallList

`Space complexity` : O(1) ->because a single variable is needed to find min.

##### `LCV`

`LCV` is a method that gets the domain of the `Hall` which has been selected by `MRV`
and sorts its values based on the number of preferences they have, in descending order.

`Time complexity`: O(n\*log(n))

`Space complexity`: O(n) .

(Tim sort has been used by python's `sorted function`).

##### `forwardChecking`

`forwardChecking` is an algorithm that removes the value assigned to a `Hall`, from
its neighboring `Halls'` domains, during backtracking search.

`Time complexity` : O(m+n) where m is the length of constraintPairsList and n is the length of copiedHallsList.

`Space complexity`: O(m) where m is the length of constraintPairsList.

##### `answerGenerator`

`answerGenerator` produces an answer in the desired template.

`Time complexity`: O(n\*log(n))
`Space complexity`: O(n)

(Tim sort has been used by python's `sorted function`)

##### `backtracking`

`backtracking` is a recursive (DFS like) algorithm which uses `MRV`, `LCV` and `Forward checking`
in order to find an answer to the problem.

`Time complexity`: O(b^d) where d is maximum depth of the tree and b is the average branching factor.

`Space complexity`: O(db) where d is the maximum depth of the tree and b is the average branching factor.

### class `AC3`

Is a pre-processing method that limits the domain values of each variable before running the backtracking method.

#### Methods

We've implemented 2 methods for the AC3 algorithm.

##### `AC3`

AC3 starts by creating a queue of all the arcs in the CSP, where an arc is defined as a pair of variables connected by a constraint. The algorithm then removes inconsistent values from the domains of variables until either all the arcs are consistent or the queue is empty. If the queue is empty, it means that the problem has no solution.

`Time Complexity`: O(d^2 \* m) , d is the maximum size of a domain and
m is the number of constraints.

`Space Complexity`: O(n + m) , where n is the number of variables and
m is the number of constraints

##### `revise`

It enforces the consistency between two variables. It operates on a single constraint and removes all the inconsistent values from the domain of one variable. This is done by checking if there exists a value in the domain of one variable such that it satisfies the constraint with all values in the domain of the other variable. If no such value exists, then the value is removed from the domain of the first variable. The revise method is called for each constraint in the CSP and is used in algorithms such as AC3 to enforce arc consistency

`Time Complexity` : O(d)

`Space Complexity`: O(1)
