# Getting Data
import requests
response=requests.get('https://cse6040.gatech.edu/datasets/groceries.csv')
groceries_file=response.text
print(groceries_file[0:106])

# Counting Frequency Of Combinations
from collections import defaultdict

def update_pair_counts (pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    
    assert type (pair_counts) is defaultdict
    itemset=list(itemset)
    for i in range(len(itemset)):
        for j in range(len(itemset)):
            if i !=j:
                pair_counts[(str(itemset[i]),str(itemset[j]))] +=1
    return(pair_counts)

# Counting Frequency Of Items

def update_item_counts(item_counts, itemset):
#
# YOUR CODE HERE
#
    itemset=list(itemset)
    for i in range(len(itemset)):
            item_counts[str(itemset[i])] +=1
    return(item_counts)

# Finding Association Strength

def filter_rules_by_conf_size (pair_counts, item_counts, threshold, size):
    rules = {} # (item_a, item_b) -> conf (item_a => item_b)
#
# YOUR CODE HERE
#
    keys1=list(pair_counts.keys())
    values1=list(pair_counts.values())
    values2=[]
    d3=dict()
    for i in range(len(keys1)):
        x=keys1[i]
        first,sec=x
        values2.append(int(values1[i])/item_counts[first])
        if values2[i]>=threshold and item_counts[first]>=size:
            d3={keys1[i]:values2[i]}
            rules.update(d3)
    
    return rules

# Final Code Putting Everything Together

x=list(groceries_file.split('\n'))
pair_counts=defaultdict(int)
item_counts=defaultdict(int)
for i in range(len(x)):
    y=x[i].split(',')
    update_pair_counts(pair_counts,y)
    update_item_counts(item_counts,y)
basket_rules=filter_rules_by_conf_size(pair_counts,item_counts,0.5, 10) # Parameters Flexible
print(basket_rules)
