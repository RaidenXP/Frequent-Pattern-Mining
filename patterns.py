import math

# DO NOT CHANGE THE FOLLOWING LINE
def apriori(itemsets, threshold):
    # DO NOT CHANGE THE PRECEDING LINE
    frequent = []
    previous_frequent = []
    possible_items = {}
    k = 2
    stop = False

    for sets in itemsets:
        for item in sets:
            possible_items.update({item: 0})

    while(not stop):
        for item in possible_items.keys():
            for sets in itemsets:
                if(sets.issuperset(item)):
                    possible_items[item] += 1
            
            support = possible_items[item] / len(itemsets)
            if(support >= threshold):
                frequent.append((item, support))
        
        possible_items.clear()

        for item in frequent:
            combo = set(item[0])
            for other_items in frequent:
                if item[0] != other_items[0]:
                    combo.update(other_items[0])
                    if len(combo) == k:
                        possible_items.update({frozenset(combo): 0})
                    combo.clear()
                    combo.update(set(item[0]))
        
        if len(frequent) != 0:
            previous_frequent = frequent.copy()
            frequent.clear()
            k += 1
        else:
            stop = True
    
    # Should return a list of pairs, where each pair consists of the frequent itemset and its support 
    # e.g. [(set(items), 0.7), (set(otheritems), 0.74), ...]
    return previous_frequent

    
# DO NOT CHANGE THE FOLLOWING LINE
def association_rules(itemsets, frequent_itemsets, metric, metric_threshold):
    # DO NOT CHANGE THE PRECEDING LINE
    
    # Should return a list of triples: condition, effect, metric value 
    # Each entry (c,e,m) represents a rule c => e, with the matric value m
    # Rules should only be included if m is greater than the given threshold.    
    # e.g. [(set(condition),set(effect),0.45), ...]
    return []
