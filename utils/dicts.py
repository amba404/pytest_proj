def get_val(collection: dict, key, default='git'):
    return collection.setdefault(key, default)