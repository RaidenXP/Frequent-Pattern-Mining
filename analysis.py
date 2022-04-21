from re import L
import pandas as pd
import patterns
import ast

def show_itemsets(itemsets):
    for itemset,support in itemsets:
        print(",".join(itemset), "%.2f"%(support))

def show_rules(rules):
    for condition,effect,metric in rules:
        print(",".join(condition), "=>", ",".join(effect), "%.2f"%(metric))

def analysis_genre():
    steam_data = pd.read_csv('steam_games.csv')

    genres_set = []

    for instances in steam_data['genre']:
        if type(instances) != float:
            temp = instances.split(", ")
            genres_set.append(set(temp))
    
    common = patterns.apriori(genres_set, 0.15)
    show_itemsets(common)
    print()
    for metric in ["lift", "all", "max", "kulczynski", "cosine"]:
            rules = patterns.association_rules(genres_set, common, metric, 0.3)
            print(metric + ": ")
            show_rules(rules)
            print()

def analysis_tags():
    steam_data = pd.read_csv('steam_games.csv')

    data = [item for (idx, item) in steam_data.iterrows()]

    instance_list = []

    for instance in data:
        instance_list.append(instance['tags'])

    tags_sets = []
    for sets in instance_list:
        temp = set(ast.literal_eval(sets))
        tags_sets.append(temp)

    common = patterns.apriori(tags_sets, 0.25)
    show_itemsets(common)
    print()
    for metric in ["lift", "all", "max", "kulczynski", "cosine"]:
            rules = patterns.association_rules(tags_sets, common, metric, 0.5)
            print(metric + ": ")
            show_rules(rules)
            print()

def analysis_tags_genres_developer():
    steam_data = pd.read_csv('steam_games.csv')

    master_set = []

    data = [item for (idx, item) in steam_data.iterrows()]
    
    for instance in data:
        temp = set()

        if type(instance['genre']) != float:
            genre_cat = instance['genre'].split(", ")
            temp.update(set(genre_cat))
        else:
            temp.update({'unknown'})
        
        tag_cat = set(ast.literal_eval(instance['tags']))
        temp.update(tag_cat)

        # doesn't seem like developers have any impact
        # if we wanted to recommend people games from certain
        # developers we just use that developer lol
        # not sure how we could recommend similar developers
        # maybe clustering

        # if type(instance['developer']) != float:
        #     developer_cat = set()
        #     developer_cat.add(instance['developer'])
        #     temp.update(developer_cat)
        # else:
        #     temp.update({'none'})
        
        master_set.append(temp)
    
    common = patterns.apriori(master_set, 0.1)
    show_itemsets(common)
    print()
    for metric in ["lift", "all", "max", "kulczynski", "cosine"]:
            rules = patterns.association_rules(master_set, common, metric, 0.1)
            print(metric + ": ")
            show_rules(rules)
            print()

        
def main():
    #analysis_genre()
    #analysis_tags()
    analysis_tags_genres_developer()

if __name__ == "__main__":
    main()