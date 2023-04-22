# 🗒 Array

## N^2 runtime sorting algorithms

First, let's make sure you understand all the common N^2 runtime sorting algorithms: Insertion Sort, Selection Sort and Bubble Sort. Watch these videos for a review of each:

- [Insertion Sort](https://www.youtube.com/watch?v=JU767SDMDvA)
- [Selection Sort](https://www.youtube.com/watch?v=g-PGLbMth_g&feature=youtu.be)
- [Bubble Sort](https://www.youtube.com/watch?v=xli_FI7CuzA)
  
Make sure you understand all the runtimes in the chart at the bottom of [this link](https://www.geeksforgeeks.org/comparison-among-bubble-sort-selection-sort-and-insertion-sort/#).

Finally, code up the solution to each approach [here](https://leetcode.com/problems/sort-an-array/).

## Binary Search

Binary search is one of the most common algorithmic patterns to learn. The purpose of binary search is to find items faster in a sorted collection. By leveraging binary search, you are able to reduce your search time from O(n) to O(logn).

Watch [this video](https://www.youtube.com/watch?v=P3YID7liBug) to learn the technique.

Then, code up your solution [here](https://leetcode.com/problems/binary-search/).

Finally, apply this technique to solving [this problem](https://leetcode.com/problems/first-bad-version/).

## Sliding Window & Two Pointers

Sliding window and two pointer techniques are names for a specific type of algorithm. When applied properly, these techniques are intended to reduce a nested loop O(n^2) approach to an O(n) algorithm by reducing the need for the nested loop. To do this, we need to store extra information that is updated as we traverse the array using a single pointer.

1. Watch [this video]() to learn the approach and what types of problems benefit from this technique.
2. Apply that same approach to solve [this problem]().
3. Finally, see if you can figure how to solve [this problem](). At first glance, this problem may not seem like it has to do with sliding window at all. Can you figure out how it does?

## Merge Sort

Now, let's get into some of the more efficient O(nlogn) sort algorithms. These algorithms are significantly harder to follow than the previous algorithms. We recommend learning only one out of merge, quick and heap unless you've exhausted the rest of this guide. Merge sort is a good one to learn because it also forces you to have a solid grasp of recursion.

Watch [this video]() for an overview of merge sort.

If this is the first time you're seeing this, [watch this video]() for a more in depth walkthrough.

Finally, code up the solution [here]().

## Quick Sort

Quicksort is another O(nlogn) relies on the concept of a "pivot".

Watch [this video]() for an overview of quick sort.

If this is the first time you're seeing this, watch [this video]() for a more in depth walkthrough.

Finally, code up the solution [here]().

<br>

# ⭕️ Node Data Structure

We are about to learn about a couple of data structures that are based on a Node class. At first glance, it feels like these data structures have very little to do with day to day engineering. So, before we dive into these structures, let's learn about why learning these does actually help improve you underlying engineering skills.

Watch [this video](), where our founder Sophie Novati explains: _what's the point of studying node based data structures?!_

## 🔗 Linked List

Linked lists are the most simple type of Node data structure. Each Node in a linked list holds a value as well was a pointer to the next Node in the list. Watch the following video for an intro to the Linked List class.

Watch [this video](), where our founder Sophie Novati explains: _why Linked Lists are like scavenger hunts._

## Basic Linked List

1. Watch [this video]() to get an overview of the linked list data structure.
2. Read this article to learn the difference between an array and a linked list.
3. Watch this video to understand is its advantages (and disadvantages) compared to the array data structure.
4. If you are relatively new to the Linked List data structure, do the following problems as practice:
    - Practice creating the basic linked list here.
    - Practice removing an element from a linked list here.
    - Practice removing an element, given an index, from a linked list here.
    - Practice adding an element, given an index, from a linked list here.
    - Practice iterating through and searching for a value in a linked list here.
5. Solve this problem on Leetcode to delete a node from a linked list.

## Detecting Cycles

A cycle in a linked list happens when a node's next pointer points to a node previously in the linked list. Cycle detection is a classic problem in linked lists. One of the classic methods to detect a cycle uses a two pointer technique, where one pointer is the "fast" pointer and the other is the "slow" one.

Watch this video for an explanation of this approach. Note that this video refers to the "fast" pointer as the hare, and the "slow" pointer as the tortoise, but these are functionally equivalent.

Intersection of Two Lists

Now, let's solve another classic problem with linked list — to find the intersection of two lists. You will be solving this problem on Leetcode.

Watch this video for a basic solution to the problem.

And this one for a more clever approach.

## 🎄 Binary Tree

Binary trees are the next most simple type of Node data structure. They are almost identical to linked lists except that instead of one next pointer, each Node in a binary tree points to two other Nodes. While this seems like a small change, it makes the data structure a lot more difficult to iterate over.

### Basic Binary Tree

Watch this video to get an overview of the binary tree data structure.

Learn two different ways to traverse through a binary tree: BFS and DFS.

Read this article to get an overview of the techniques.

Watch this video for a verbal explanation of the approaches.

Practice applying this technique by solving the problem here.

If you are relatively new to the Binary Tree data structure, do the following problems as practice:

Read this article to learn how to count the nodes in a binary tree.

Read this article to learn how to get the height of a binary tree. Watch this video for an explanation of the same algorithm.

Watch this video to see how to use a very similar technique to solve a different problem: to find the max value in a binary tree.

Practice inverting a binary tree here.

### Binary Search Tree

Watch this video to get an overview of the binary search tree data structure.

Practice adding a new element to a binary search tree here.

Watch this video to learn how to search in a binary search tree.

If you are relatively new to the Binary Search Tree data structure, do the following problems as practice:

Find the minimum and maximum value in a Binary Search Tree here.

Check if an element exists in a Binary Search Tree here.

Delete a leaf node in a Binary Search Tree here.

Delete a leaf node with just one child in a Binary Search Tree here.

Delete a leaf node with two children in a Binary Search Tree here.

Now, consider the problem you solved above where you found the maximum value in a binary tree. How would you solve this problem in a binary search tree? This solution should actually be much easier – think about why!

Watch this video to learn how to check if a binary tree is a valid binary search tree or not.

Practice this solution by solving the problem here.

### Balancing Binary Trees

Balancing a binary search tree is not just another algorithm. It's quite a hard one. Keeping a tree balanced also has extremely important implications for its runtime.

Watch this video for an overview of what balanced means and how to check if a binary tree is balanced or not.

Watch this video to understand why this concept of balanced is important.

<br>

# #️⃣ Hashing

Hashing is one of the most fundamental concepts that make many of our primitive data structures work (sets / hash sets, dictionaries / hash tables). This section gets into some of the gnarly details of the hash function. Just as you don't need to understand how a microwave works to be able to use it, it is entirely possible to be an engineer using these sets / dictionaries without an understanding of the underlying technique that makes it possible, but understanding it will push you to understand things at a deeper level as an engineer.

## Understanding the Hash Function

Watch this video for a review of the dictionary / hash table data structure.

Hash functions are the core innovation that make hash tables possible, but not all hash functions are created equal. Watch this video to get an understanding of what makes a good hash function.

It is possible for a hash function to output the same value for two different keys. That, in the context of a hash table, leads to a collision. Watch this video to understand two of the most common strategies.

Watch this video to learn a less common strategy called quadratic probing.

As you may know, the cost of lookup, insertion and deletion into a hash table is considered to be O(1). However, when we run out of space in a hash table, we have to do an expensive O(n) operation. So, how can the insertion be considered to be O(1)?

First, watch this video to understand what a resizing means.

Then, watch this video understand what amortized runtime is.

<br>

# 🍱 Dynamic Programming

At a high level, dynamic programming is really about breaking a large problem into smaller problems, storing the answers to subproblems and then using the answers to subproblems to solve larger problems.

## 1) Fibonacci Sequence

Watch this video to learn about this most classic simple dynamic programming problem.

Code up the solution here.

## 2) 0-1 Knapsack Problem

This is one of the most classic dynamic programming problems. It is an optimization problem where you're trying to optimize some value while limited by some constraint. Make sure you take the time to fully understand this on a theoretical level.

Watch this video for an overview of this problem.

Watch this visualization to see a step by step walkthrough of the problem as well as a sample coding up of the solution.

## 3) Making Change

This is another Dynamic Programming classic. This problem is often masked by some kind of story (like number of ways to get a football score), but actually comes up reasonably often in interviews. In this problem, you will figure out the minimum number of coins to make change adding up to a target value.

Watch this video to see a walkthrough of this problem.

Write up your own code [here]().

## 4) Subset Sum

Subset sum is very similar to the coin change problem (adding a bunch of values to a target value). However, there are two key distinctions: you only have one of each value / "coin" and you just want to return true or false if the target sum can be made.

Watch [this video]() to see a walkthrough of the approach

See if you can use that solution to solve this [slightly different problem]().

<br>

# 📚 Heap

Heaps are a very advanced data structure. In learning this data structure, you will want to learn 1) how the data structure works and 2) what types of problems it can solve. We actually recommend learning 2) before 1). There are 0 problems that can be solved with a heap that cannot be solved in a simpler way. Heaps a data structure that purely optimizes the runtime of an existing solution, oftentimes from O(n) to O(logn). Complete the following steps to learn about this data structure.

1. Before understanding heap sort, watch this video to first learn the concept of a heap.
2. Now to see a practical application of heap, let's learn about heap sort.
    1. Watch this video first to get an overview of the technique.
    2. Now, watch this video for a detailed walkthrough. You may start at 39:00 if you understand the previous video.
    3. As usual, code up your solution here.

<br>

# ፨ Graph

Before we go into graphs, we'd like to add a word of caution that for 99% of people reading this, we do not recommend reading any further. Graph data structures almost never come up in real interviews (except at a select few companies), and the blocker for most people in technical interviews is not being fluent at the simple stuff, not lack of knowledge of graphs. That being said, if you're interested, feel free to progress further.

## Intro to Graphs

Before we dive deep into all of the different graph algorithms, we recommend gaining a high level understanding of all the concepts by reading through this doc. Spend no more than 1 hour reading this.

Watch this video for an intro to the data structure. After you finish watching this, you should be able to answer these questions:

What is a directed graph vs. an undirected graph?

Is a tree a graph? Can you explain why?

What is an adjacency matrix?

What is a weighted graph?

Watch this video to learn how to traverse a graph using BFS and DFS (yes, the same BFS and DFS as in trees!).

## Topological Sort

One of the most classic things you want to do with a graph data structure is topological sort. Often times, you build a graph data structure for the sole purpose of applying topological sort on it.

Watch this video to get an overview of the algorithm.

Then, read through this article to see another version of the code. Please copy and execute the code in your own environment.

## Minimum Spanning Tree

Watch the additional video on AlgoExpert if needed. A minimum spanning tree is a subset of a graph data structure that represents the cheapest set of edges that makes the graph still fully connected.

First, we'll learn about Kruskal's algorithm.

Before we can learn about Kruskal's algorithm, watch this video to learn about the concept of a Disjoint Set. Disjoint Set is a data structure that serves a very specific purpose. It is meant to make merging sets a very efficient operation.

Then, watch this video about Kruskal's algorithm.

Next, we're going to review another famous algorithm for finding MST called Prim's. By the end of these videos, make sure you understand and can explain the difference between Kruskal's and Prim's.

Start with this video to understand an overview of the algorithm.

Continue on to this video for a deep dive.

## Dijkstra’s Algorithm

Dijkstra's Algorithm is one of the most famous graph algorithms. Watch this video to understand a bit more about it. For this algorithm, it's more important to understand it theoretically rather than necessarily be able to code it. You can optionally skip the coding part of the above video, and just make sure you understand how to walk through it.

After watching this video, you should be able to answer:

What is the purpose of Dijkstra's algorithm? What problem does it solve?

Why is it necessary to have a heap in the algorithm? What is the consequence if we don't have a heap? (hint: It has to do with runtime!)

## Bellman-Ford

OK, let's do one more famous graph algorithm. This one is called Bellman-Ford. It does the same thing as Dijkstra, but works a little differently. Watch this video to get an overview.

When you're done with this algorithm, you should be able to answer the following:

What is the advantage to using Bellman Ford algorithm over Dijkstra?

What is a negative weight cycle?

How does Bellman-Ford deal detect a negative weight cycle?

<br>

# Practice

One of the tricky things about graph problems is that it's not always obvious when a problem is graph problem. This next problem reads like a normal problem but can be optimized using graph.  Read the prompt, and try to think about which of the previous algorithms is relevant.

A lot of graph based algorithms have a lot of practical real world applications. Here is a logistical problem, trying to find the cheapest flight within k stops, that relies on optimizing a path in a graph based data model. Which of the graph based algorithms might be helpful here?
