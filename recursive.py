#Task1

def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_sum(n - 1)

# Test cases
print(harmonic_sum(7))
print(harmonic_sum(4))




#Task2

def print_indented_nodes(node, level=0):
    print("  " * level + f"Node: {node['value']}")
    for neighbor in node["neighbors"]:
        print_indented_nodes(neighbor, level + 1)

# Example data set
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

# Result
print_indented_nodes(graph_data)


#Task3

def count_pages(pages):
    if not pages:
        return 0
    else:
        total_pages = len(pages)
        for page in pages:
            if 'pages' in page:
                total_pages += count_pages(page['pages'])
        return total_pages

# Test case
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

# Result
print(count_pages(test_data1))



