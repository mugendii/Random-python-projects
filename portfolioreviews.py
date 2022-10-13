#the dictionary

portfolioCollection = {'Sam': [56, 89, 34, 56, 99, 59, 99, 88, 100], 
                        'Peter': [99, 88, 100], 
                        'Adam': [99, 77, 88, 100, 23], 
                        'Jason': [56, 89, 34, 56, 99, 59, 99, 88, 100, 11, 91], 
                        'Spencer': [99, 88, 100], 
                        'Chris': [55, 66, 77, 88, 99, 100], 
                        'Dave': [45, 56, 57, 89, 98, 91, 92, 89], 
                        'Bob': [77, 76, 75, 89, 88, 87, 86], 
                        'Edwin': [100, 99, 99, 0] 
                    }

Sam_review = portfolioCollection['Sam']
print(Sam_review)
# finding the max & min value in the list
max_review = 0
for item in Sam_review:
    if item > max_review:
        max_review = item
print(max_review)

min_review = [0]
for item in Sam_review:
    if item <= min_review :
        min_review = item
print(min_review)


# for key, val in portfolioCollection.items():
#     print(key , val)
