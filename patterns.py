import math
from itertools import combinations

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
            temp = set()
            temp.add(item)
            possible_items.update({frozenset(temp): 0})

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
    rule_set=[]
    finished_rule_set=[]
    rules = {}
    for items in frequent_itemsets:
        for k in range(1, len(items[0])):
            temp = list(items[0])
            temp = list(combinations(temp, k))
            for combo in temp:
                condition = set(combo)
                effect = set(items[0]).difference(condition)
                rules.update({frozenset(condition): effect})
        rule_set.append(rules.copy())
        rules.clear()
    
    if metric == 'lift':
        index = 0
        for items in frequent_itemsets:
            for condition in rule_set[index].keys():
                support_A = 0
                support_B = 0
                
                for sets in itemsets:
                    if(sets.issuperset(condition)):
                        support_A += 1
                    if(sets.issuperset(rule_set[index][condition])):
                        support_B += 1
                
                support_A /= len(itemsets)
                support_B /= len(itemsets)

                #P(B|A)
                confidence = items[1]/support_A

                lift = confidence/support_B

                if(lift > metric_threshold):
                    finished_rule_set.append((set(condition), set(rule_set[index][condition]), lift))
            
            index += 1
    elif metric == 'all':
        index = 0
        for items in frequent_itemsets:
            for condition in rule_set[index].keys():
                support_A = 0
                support_B = 0
                
                for sets in itemsets:
                    if(sets.issuperset(condition)):
                        support_A += 1
                    if(sets.issuperset(rule_set[index][condition])):
                        support_B += 1
                
                support_A /= len(itemsets)
                support_B /= len(itemsets)
                
                #P(B|A)
                confidence_a = items[1]/support_A
                
                #P(A|B)
                confidence_b = items[1]/support_B

                alls = min(confidence_a, confidence_b)

                if(alls > metric_threshold):
                    finished_rule_set.append((set(condition), set(rule_set[index][condition]), alls))
            
            index += 1
    elif metric == 'max':
        index = 0
        for items in frequent_itemsets:
            for condition in rule_set[index].keys():
                support_A = 0
                support_B = 0
                
                for sets in itemsets:
                    if(sets.issuperset(condition)):
                        support_A += 1
                    if(sets.issuperset(rule_set[index][condition])):
                        support_B += 1
                
                support_A /= len(itemsets)
                support_B /= len(itemsets)
                
                #P(B|A)
                confidence_a = items[1]/support_A
                
                #P(A|B)
                confidence_b = items[1]/support_B

                maxs = max(confidence_a, confidence_b)

                if(maxs > metric_threshold):
                    finished_rule_set.append((set(condition), set(rule_set[index][condition]), maxs))
            
            index += 1
    elif metric == 'kulczynski':
        index = 0
        for items in frequent_itemsets:
            for condition in rule_set[index].keys():
                support_A = 0
                support_B = 0
                
                for sets in itemsets:
                    if(sets.issuperset(condition)):
                        support_A += 1
                    if(sets.issuperset(rule_set[index][condition])):
                        support_B += 1
                
                support_A /= len(itemsets)
                support_B /= len(itemsets)
                
                #P(B|A)
                confidence_a = items[1]/support_A
                
                #P(A|B)
                confidence_b = items[1]/support_B

                kul = (confidence_a + confidence_b) / 2

                if(kul > metric_threshold):
                    finished_rule_set.append((set(condition), set(rule_set[index][condition]), kul))
            
            index += 1
    elif metric == 'cosine':
        index = 0
        for items in frequent_itemsets:
            for condition in rule_set[index].keys():
                support_A = 0
                support_B = 0
                
                for sets in itemsets:
                    if(sets.issuperset(condition)):
                        support_A += 1
                    if(sets.issuperset(rule_set[index][condition])):
                        support_B += 1
                
                support_A /= len(itemsets)
                support_B /= len(itemsets)
                
                #P(B|A)
                confidence_a = items[1]/support_A
                
                #P(A|B)
                confidence_b = items[1]/support_B

                cosine = math.sqrt(confidence_a * confidence_b)

                if(cosine > metric_threshold):
                    finished_rule_set.append((set(condition), set(rule_set[index][condition]), cosine))
            
            index += 1

    # Should return a list of triples: condition, effect, metric value 
    # Each entry (c,e,m) represents a rule c => e, with the matric value m
    # Rules should only be included if m is greater than the given threshold.    
    # e.g. [(set(condition),set(effect),0.45), ...]
    return finished_rule_set
