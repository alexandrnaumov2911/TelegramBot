def unique_check(collection:iter):
    for index in range(len(collection)):
        if collection.count(collection[index]) > 1:
            return False
    return True

