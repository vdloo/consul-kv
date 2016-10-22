from os.path import join


def loop_dictionary(dictionary, path='', callback=lambda path, k, v: None):
    """
    Loop the dictionary and perform the callback for each value
    :param dict dictionary: dictionary to loop for values
    :param str path: the depth in the dict joined by /
    :param func callback: the callback to perform for each value
    :return None:
    """
    for k, v in dictionary.items():
        if isinstance(v, dict):
            loop_dictionary(v, path=join(path, k), callback=callback)
        else:
            callback(path, k, v)


def map_dictionary(dictionary):
    """
    Map the
    :param dict dictionary: to flatten into a k/v mapping
    :return dict mapping: key value mapping
    """
    mapping = dict()

    def add_item_to_mapping(path, k, v):
        mapping.update({join(path, k): v})

    loop_dictionary(
        dictionary,
        callback=add_item_to_mapping
    )
    return mapping
