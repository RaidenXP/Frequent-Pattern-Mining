import pandas as pd
import patterns

def show_itemsets(itemsets):
    for itemset,support in itemsets:
        print(",".join(itemset), "%.2f"%(support))

def show_rules(rules):
    for condition,effect,metric in rules:
        print(",".join(condition), "=>", ",".join(effect), "%.2f"%(metric))

def analysis():
    steam_data = pd.read_csv('steam_games.csv')

    genres_set = []

    for instances in steam_data['genre']:
        if type(instances) != float:
            temp = instances.split(", ")
            genres_set.append(set(temp))
    
    common = patterns.apriori(genres_set, 0.15)
    show_itemsets(common)
    for metric in ["lift", "all", "max", "kulczynski", "cosine"]:
            rules = patterns.association_rules(genres_set, common, metric, 0.3)
            print(metric + ": ")
            show_rules(rules)
            print()

def main():
    analysis()

if __name__ == "__main__":
    main()