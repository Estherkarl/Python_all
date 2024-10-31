[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/dL3FRWXK)
# recursive_functions

# Task 1

## Recursion with return and instructions after return (non tail-recursive)
Create a function called harmonic_sum that requires an integer as an argument. The function will return the harmonic sum of the integer.

The harmonic sum is the sum of reciprocals of the positive integers. The harmonical sum of 2 is:
```python

1/1 + 1/2 = 1.5

The harmonic sum of 4 is:

1/1 + 1/2 + 1/3 + 1/4 = 2.083333333333333

Then, use the following test cases:

print(harmonic_sum(7))
print(harmonic_sum(4))
Your result should look like this:
2.5928571428571425
2.083333333333333
```

# Task 2

Write a recursive which will print the value of each child on each level with proper indentation.

example data set

```python
graph_data = {
    "node": 1,
    'value': 'node1',
    "neighbors": [
        {
            "node": 2, 
            "neighbors": [],
            'value': 'node2'
        },
        {
            "node": 3,
            'value': 'node3', 
            "neighbors": [
                {
                    "node": 4, "neighbors": [], 'value': 'node4'
                },
                {
                    "node": 5, "neighbors": [], 'value': 'node5'
                }
            ]
        }
    ]
}



result should look like this

Node: node1
  Node: node2
  Node: node3
    Node: node4
    Node: node5

```


# Task 3

Task 3:
Create a recursive function named count_pages that will count the amount of pages in a website. Takes a single argument as a list of pages, defined as dictionaries that may have two keys: title and pages.

The first is the title of the page and the second is another list with the same kind of dictionaries (again with title and, possibly, pages). The tree of pages has no depth limitations.

If a page dictionary has no key pages it means it has no further child pages, but all the pages, including those with children, count as a page.

You can use the following test case:

```python
test_data1 = [
    {
        "title": "Home",
        "pages": [
            {
                "title": "About",
                "pages": [
                    {
                        "title": "The company"
                    },
                    {
                        "title": "Our services"
                    },
                    {
                        "title": "Our products"
                    },
                    {
                        "title": "Our deliveries",
                        "pages": [
                            {
                                "title": "National"
                            },
                            {
                                "title": "International"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Shop",
                "pages": [
                    {
                        "title": "Browse all"
                    },
                    {
                        "title": "Categories"
                    }
                ]
            },
            {
                "title": "My account",
                "pages": [
                    {
                        "title": "Settings"
                    },
                    {
                        "title": "Edit profile"
                    },
                    {
                        "title": "My transactions"
                    }
                ]
            }
        ]
    }
]


print(count_pages(test_data1))
```

Your result should look like this:
```python
15
```

