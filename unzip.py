zipped = [("a", 1), ("b", 2)]
unzipped_object = zip(*zipped)
unzipped_list = list(unzipped_object)
print(unzipped_list)