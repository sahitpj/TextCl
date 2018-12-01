from utils import import_data, preprocess


filepath = 'data.txt'

data_as_lines, data_as_words = import_data(filepath)


print preprocess(data_as_words)