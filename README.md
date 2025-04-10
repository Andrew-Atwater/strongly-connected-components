# strongly-connected-components
COS226 Assignment 5
Using Strongly Connected Components to Identify Coupling within Code

Overview

For this homework you are going to analyze the coupling of different classes that comprise a hypothetical computer
program. The program will be represented by a graph. Each node in the graph is a class. A directed edge exists
between two nodes if one class uses another. To accomplish this you will collapse the graph around strongly connected
components.

Learning Goals

Gain hands-on experience with graph representations and algorithms including adjacency lists and depth first search.

The Task

You will be given a text file with a graph in adjacency list format. Your program should read and parse the file and
construct an internal representation of the graph. The internal representation is up to you.
Each class has been given a single character code (e.g., A, B, etc.). Edges between classes represent one class making
use of another. For example, if B uses A in any way, such as storing a reference to an object of type A or calls one
of its methods, then the graph will have a directed edge going from A to B.
The goal is to collapse the graph such that sets of classes that form strongly connected components are collapsed
into a single node. This will allow us to better understand the dependencies within our code.
To accomplish this you must use the Strongly Connected Components algorithm in Section 20.5 of the textbook.
The resulting graph will be cycle free. See example below.

Input

Your program should prompt the user for the name of a file that contains the adjacency list. The prompt should be
short and to the point. It should not contain an elaborate menu or ask any other questions. It should not hard code
the name of the file, assume any file extensions or use absolute paths.

Output

Your program should output an adjacency matrix such that the cells in the matrix count the number of edges
between members of different strongly connected components. Row labels represent the from relationship and
columns represent the to relationship between nodes. The matrix should be formatted neatly, aligning rows and
columns. Columns should all be the same width. Use f-strings.
