# 🗒 Array

## N^2 Runtime Sorting Algorithms
First, let's make sure you understand all the common N^2 runtime sorting algorithms: Insertion Sort, Selection Sort and Bubble Sort. Watch these videos for a review of each:
- [Insertion Sort](https://www.youtube.com/watch?v=JU767SDMDvA)
- [Selection Sort](https://www.youtube.com/watch?v=g-PGLbMth_g&feature=youtu.be)
- [Bubble Sort](https://www.youtube.com/watch?v=xli_FI7CuzA)
  
Make sure you understand all the runtimes in the chart at the bottom of [this link](https://www.geeksforgeeks.org/comparison-among-bubble-sort-selection-sort-and-insertion-sort/#).

Finally, code up the solution to each approach [here](https://leetcode.com/problems/sort-an-array/).

## Binary Search
Binary search is one of the most common algorithmic patterns to learn. The purpose of binary search is to find items faster in a sorted collection. By leveraging binary search, you are able to reduce your search time from O(n) to O(logn).
1. Watch [this video](https://www.youtube.com/watch?v=P3YID7liBug) to learn the technique.
2. Then, code up your solution [here](https://leetcode.com/problems/binary-search/).
3. Finally, apply this technique to solving [this problem](https://leetcode.com/problems/first-bad-version/).

## Sliding Window & Two Pointers
Sliding window and two pointer techniques are names for a specific type of algorithm. When applied properly, these techniques are intended to reduce a nested loop O(n^2) approach to an O(n) algorithm by reducing the need for the nested loop. To do this, we need to store extra information that is updated as we traverse the array using a single pointer.

1. Watch [this video](https://www.youtube.com/watch?v=MK-NZ4hN7rs) to learn the approach and what types of problems benefit from this technique.
2. Apply that same approach to solve [this problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/).
3. Finally, see if you can figure how to solve [this problem](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/). At first glance, this problem may not seem like it has to do with sliding window at all. Can you figure out how it does?

## Merge Sort
Now, let's get into some of the more efficient O(nlogn) sort algorithms. These algorithms are significantly harder to follow than the previous algorithms. We recommend learning only one out of merge, quick, and heap unless you've exhausted the rest of this guide. Merge sort is a good one to learn because it also forces you to have a solid grasp of recursion.
1. Watch [this video](https://www.youtube.com/watch?v=4VqmGXwpLqc) for an overview of merge sort.
2. If this is the first time you're seeing this, [watch this video](https://www.youtube.com/watch?v=7h1s2SojIRw) for a more in depth walkthrough.
3. Finally, code up the solution [here](https://leetcode.com/problems/sort-an-array/).

## Quick Sort
Quicksort is another O(nlogn) relies on the concept of a "pivot".
1. Watch [this video](https://www.youtube.com/watch?v=Hoixgm4-P4M) for an overview of quick sort.
3. If this is the first time you're seeing this, watch [this video](https://www.youtube.com/watch?v=7h1s2SojIRw) for a more in depth walkthrough.
3. Finally, code up the solution [here](https://leetcode.com/problems/sort-an-array/).

<br>

# ⭕️ Node Data Structure
We are about to learn about a couple of data structures that are based on a Node class. At first glance, it feels like these data structures have very little to do with day to day engineering. So, before we dive into these structures, let's learn about why learning these does actually help improve you underlying engineering skills.

Watch [this video](https://www.youtube.com/watch?v=9SNZqQrQutA), where our founder Sophie Novati explains: _what's the point of studying node based data structures?!_

## 🔗 Linked List
Linked lists are the most simple type of Node data structure. Each Node in a linked list holds a value as well was a pointer to the next Node in the list. Watch the following video for an intro to the Linked List class.

Watch [this video](), where our founder Sophie Novati explains: _why Linked Lists are like scavenger hunts._

## Basic Linked List
1. Watch [this video](https://www.youtube.com/watch?v=WwfhLC16bis) to get an overview of the linked list data structure.
2. Read [this article](https://www.geeksforgeeks.org/programmers-approach-looking-array-vs-linked-list/) to learn the difference between an array and a linked list.
3. Watch [this video](https://www.youtube.com/watch?v=qauEA64G1Ds) to understand is its advantages (and disadvantages) compared to the array data structure.
4. If you are relatively new to the Linked List data structure, do the following problems as practice:
    - Practice creating the basic linked list [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/work-with-nodes-in-a-linked-list).
    - Practice removing an element from a linked list [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/remove-elements-from-a-linked-list).
    - Practice removing an element, given an index, from a linked list [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/remove-elements-from-a-linked-list-by-index).
    - Practice adding an element, given an index, from a linked list [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/add-elements-at-a-specific-index-in-a-linked-list).
    - Practice iterating through and searching for a value in a linked list [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/search-within-a-linked-list).
5. Solve [this problem](https://leetcode.com/problems/delete-node-in-a-linked-list/) on Leetcode to delete a node from a linked list.

## Detecting Cycles
A cycle in a linked list happens when a node's next pointer points to a node previously in the linked list. Cycle detection is a classic problem in linked lists. One of the classic methods to detect a cycle uses a two pointer technique, where one pointer is the "fast" pointer and the other is the "slow" one.

Watch [this video](https://www.youtube.com/watch?v=-YiQZi3mLq0) for an explanation of this approach. Note that this video refers to the "fast" pointer as the hare, and the "slow" pointer as the tortoise, but these are functionally equivalent.

## Intersection of Two Lists
Now, let's solve another classic problem with linked list — to find the intersection of two lists. You will be solving [this problem on Leetcode](https://leetcode.com/problems/intersection-of-two-linked-lists/).
1. Watch [this video](https://www.youtube.com/watch?v=_7byKXAhxyM) for a basic solution to the problem.
2. And [this one](https://www.youtube.com/watch?v=ycIMmSmkQbo) for a more clever approach.

## 🎄 Binary Tree
Binary trees are the next most simple type of Node data structure. They are almost identical to linked lists except that instead of one next pointer, each Node in a binary tree points to two other Nodes. While this seems like a small change, it makes the data structure a lot more difficult to iterate over.

### Basic Binary Tree
1. Watch [this video](https://www.youtube.com/watch?v=oSWTXtMglKE) to get an overview of the binary tree data structure.
2. Learn two different ways to traverse through a binary tree: BFS and DFS.
    - Read [this article](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/) to get an overview of the techniques.
    - Watch [this video](https://www.youtube.com/watch?v=9RHO6jU--GU) for a verbal explanation of the approaches.
    - Practice applying this technique by solving the problem [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/use-breadth-first-search-in-a-binary-search-tree).
3. If you are relatively new to the Binary Tree data structure, do the following problems as practice:
    - Read [this article](https://www.geeksforgeeks.org/count-full-nodes-binary-tree-iterative-recursive/) to learn how to count the nodes in a binary tree.
    - Read [this article](https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/) to learn how to get the height of a binary tree. Watch this [video](https://www.youtube.com/watch?v=_SiwrPXG9-g) for an explanation of the same algorithm.
    - Watch [this video](https://www.youtube.com/watch?v=Ut90klNN264) to see how to use a very similar technique to solve a different problem: to find the max value in a binary tree.
    - Practice inverting a binary tree [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/invert-a-binary-tree).

### Binary Search Tree
1. Watch [this video](https://www.youtube.com/watch?v=cySVml6e_Fc) to get an overview of the binary search tree data structure.
    - Practice adding a new element to a binary search tree [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/add-a-new-element-to-a-binary-search-tree).
2. Watch [this video](https://www.youtube.com/watch?v=zm83jPHZ-jA) to learn how to search in a binary search tree.
3. If you are relatively new to the Binary Search Tree data structure, do the following problems as practice:
    - Find the minimum and maximum value in a Binary Search Tree [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/find-the-minimum-and-maximum-value-in-a-binary-search-tree).
    - Check if an element exists in a Binary Search Tree [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/check-if-an-element-is-present-in-a-binary-search-tree).
    - Delete a leaf node in a Binary Search Tree [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/delete-a-leaf-node-in-a-binary-search-tree).
    - Delete a leaf node with just one child in a Binary Search Tree [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/delete-a-node-with-one-child-in-a-binary-search-tree).
    - Delete a leaf node with two children in a Binary Search Tree [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/delete-a-node-with-two-children-in-a-binary-search-tree).
4. Now, consider the problem you solved above where you found the maximum value in a binary tree. How would you solve this problem in a binary search tree? This solution should actually be much easier – think about why!
5. Watch [this video](https://www.youtube.com/watch?v=MILxfAbIhrE) to learn how to check if a binary tree is a valid binary search tree or not.
    - Practice this solution by solving the problem [here](https://www.freecodecamp.org/learn/coding-interview-prep/data-structures/check-if-tree-is-binary-search-tree).

### Balancing Binary Trees
Balancing a binary search tree is not just another algorithm. It's quite a hard one. Keeping a tree balanced also has extremely important implications for its runtime.
1. Watch [this video](https://www.youtube.com/watch?v=LU4fGD-fgJQ) for an overview of what balanced means and how to check if a binary tree is balanced or not.
2. Watch [this video](https://www.youtube.com/watch?v=1O5oaomE__M) to understand why this concept of balanced is important.

<br>

# #️⃣ Hashing
Hashing is one of the most fundamental concepts that make many of our primitive data structures work (sets / hash sets, dictionaries / hash tables). This section gets into some of the gnarly details of the hash function. Just as you don't need to understand how a microwave works to be able to use it, it is entirely possible to be an engineer using these sets / dictionaries without an understanding of the underlying technique that makes it possible, but understanding it will push you to understand things at a deeper level as an engineer.

## Understanding the Hash Function
1. Watch [this video](https://www.youtube.com/watch?v=KyUTuwz_b7Q) for a review of the dictionary / hash table data structure.
2. Hash functions are the core innovation that make hash tables possible, but not all hash functions are created equal. Watch [this video](https://www.youtube.com/watch?v=4ZJQ6ehmAsg) to get an understanding of what makes a good hash function.
3. It is possible for a hash function to output the same value for two different keys. That, in the context of a hash table, leads to a collision. Watch [this video](https://www.youtube.com/watch?v=zeMa9sg-VJM) to understand two of the most common strategies.
4. Watch [this video](https://www.youtube.com/watch?v=dxrLtf-Fybk) to learn a less common strategy called quadratic probing.
5. As you may know, the cost of lookup, insertion and deletion into a hash table is considered to be O(1). However, when we run out of space in a hash table, we have to do an expensive O(n) operation. So, how can the insertion be considered to be O(1)?
    1. First, watch [this video](https://www.youtube.com/watch?v=AA0KuKV3ARU) to understand what a resizing means.
    2. Then, watch [this video](https://www.youtube.com/watch?v=MTl8djZFWE0) understand what amortized runtime is.

<br>

# 🍱 Dynamic Programming
At a high level, dynamic programming is really about breaking a large problem into smaller problems, storing the answers to subproblems and then using the answers to subproblems to solve larger problems.

## 1) Fibonacci Sequence
1. Watch [this video](https://www.youtube.com/watch?v=vYquumk4nWw) to learn about this most classic simple dynamic programming problem.
2. Code up the solution [here](https://leetcode.com/problems/fibonacci-number/).

## 2) 0-1 Knapsack Problem
This is one of the most classic dynamic programming problems. It is an optimization problem where you're trying to optimize some value while limited by some constraint. Make sure you take the time to fully understand this on a theoretical level.
1. Watch [this video for](https://www.youtube.com/watch?v=8LusJS5-AGo) an overview of this problem.
2. Watch [this visualization](https://algorithm-visualizer.org/dynamic-programming/knapsack-problem) to see a step by step walkthrough of the problem as well as a sample coding up of the solution.

## 3) Making Change
This is another Dynamic Programming classic. This problem is often masked by some kind of story (like number of ways to get a football score), but actually comes up reasonably often in interviews. In this problem, you will figure out the minimum number of coins to make change adding up to a target value.
1. Watch [this video](https://www.youtube.com/watch?v=L27_JpN6Z1Q) to see a walkthrough of this problem.
2. Write up your own code [here](https://leetcode.com/problems/coin-change/).

## 4) Subset Sum
Subset sum is very similar to the coin change problem (adding a bunch of values to a target value). However, there are two key distinctions: you only have one of each value / "coin" and you just want to return true or false if the target sum can be made.
1. Watch [this video](https://www.youtube.com/watch?v=s6FhG--P7z0) to see a walkthrough of the approach
2. See if you can use that solution to solve this [slightly different problem](https://leetcode.com/problems/partition-equal-subset-sum/).

<br>

# 📚 Heap
Heaps are a very advanced data structure. In learning this data structure, you will want to learn how the data structure works and what types of problems it can solve. 

There are 0 problems that can be solved with a heap that cannot be solved in a simpler way. Heaps a data structure that purely optimizes the runtime of an existing solution, oftentimes from O(n) to O(logn). Complete the following steps to learn about this data structure.
1. Before understanding heap sort, [watch this](https://www.youtube.com/watch?v=t0Cq6tVNRBA) video to first learn the concept of a heap.
2. Now to see a practical application of heap, let's learn about heap sort.
    1. Watch [this video](https://www.youtube.com/watch?v=2DmK_H7IdTo&feature=youtu.be) first to get an overview of the technique.
    2. Now, watch [this video](https://www.youtube.com/watch?v=Q_eia3jC9Ts) for a detailed walkthrough. You may start at 39:00 if you understand the previous video.
    3. As usual, code up your solution [here](https://leetcode.com/problems/sort-an-array/).

<br>

# ፨ Graph
Before we go into graphs, we'd like to add a word of caution that for 99% of people reading this, we do not recommend reading any further. Graph data structures almost never come up in real interviews (except at a select few companies), and the blocker for most people in technical interviews is not being fluent at the simple stuff, not lack of knowledge of graphs. That being said, if you're interested, feel free to progress further.

## Intro to Graphs
1. Before we dive deep into all of the different graph algorithms, we recommend gaining a high level understanding of all the concepts by reading through [this doc](https://web.stanford.edu/class/cs97si/06-basic-graph-algorithms.pdf). Spend no more than 1 hour reading this.
2. Watch this video for an intro to the data structure. After you finish watching this, you should be able to answer these questions:
    - What is a directed graph vs. an undirected graph?
    - Is a tree a graph? Can you explain why?
    - What is an adjacency matrix?
    - What is a weighted graph?
3. Watch [this video](https://www.youtube.com/watch?v=gXgEDyodOJU) to learn how to traverse a graph using BFS and DFS (yes, the same BFS and DFS as in trees!).

## Topological Sort
One of the most classic things you want to do with a graph data structure is topological sort. Often times, you build a graph data structure for the sole purpose of applying topological sort on it.
1. Watch [this video](https://www.youtube.com/watch?v=ddTC4Zovtbc) to get an overview of the algorithm.
2. Then, read through [this article](https://www.interviewcake.com/concept/java/topological-sort#:~:text=The%20topological%20sort%20algorithm%20takes,is%20called%20a%20topological%20ordering.) to see another version of the code. Please copy and execute the code in your own environment.

## Minimum Spanning Tree
Watch the additional video on AlgoExpert if needed. A minimum spanning tree is a subset of a graph data structure that represents the cheapest set of edges that makes the graph still fully connected.

First, we'll learn about Kruskal's algorithm.
1. Before we can learn about Kruskal's algorithm, watch [this video](https://www.youtube.com/watch?v=ID00PMy0-vE) to learn about the concept of a Disjoint Set. Disjoint Set is a data structure that serves a very specific purpose. It is meant to make merging sets a very efficient operation.
2. Then, watch [this video](https://www.youtube.com/watch?v=fAuF0EuZVCk) about Kruskal's algorithm.

Next, we're going to review another famous algorithm for finding MST called Prim's. By the end of these videos, make sure you understand and can explain the difference between Kruskal's and Prim's.
1. Start with [this video](https://www.youtube.com/watch?v=cplfcGZmX7I) to understand an overview of the algorithm.
2. Continue on to [this video](https://www.youtube.com/watch?v=oP2-8ysT3QQ) for a deep dive.

## Dijkstra’s Algorithm
Dijkstra's Algorithm is one of the most famous graph algorithms. Watch [this video](https://www.youtube.com/watch?v=lAXZGERcDf4) to understand a bit more about it. For this algorithm, it's more important to understand it theoretically rather than necessarily be able to code it. You can optionally skip the coding part of the above video, and just make sure you understand how to walk through it.

After watching this video, you should be able to answer:
1. What is the purpose of Dijkstra's algorithm? What problem does it solve?
2. Why is it necessary to have a heap in the algorithm? What is the consequence if we don't have a heap? (hint: It has to do with runtime!)

## Bellman-Ford
OK, let's do one more famous graph algorithm. This one is called Bellman-Ford. It does the same thing as Dijkstra, but works a little differently. Watch [this video](https://www.youtube.com/watch?v=-mOEd_3gTK0) to get an overview.

When you're done with this algorithm, you should be able to answer the following:
1. What is the advantage to using Bellman Ford algorithm over Dijkstra?
2. What is a negative weight cycle?
3. How does Bellman-Ford deal detect a negative weight cycle?

<br>

# Practice
1. One of the tricky things about graph problems is that it's not always obvious when a problem is graph problem. This next problem reads like a normal problem but can be optimized using graph. Read [the prompt](https://leetcode.com/problems/alien-dictionary/), and try to think about which of the previous algorithms is relevant.
2. A lot of graph based algorithms have a lot of practical real world applications. Here is a [logistical problem](https://leetcode.com/problems/cheapest-flights-within-k-stops/), trying to find the cheapest flight within k stops, that relies on optimizing a path in a graph based data model. Which of the graph based algorithms might be helpful here?
