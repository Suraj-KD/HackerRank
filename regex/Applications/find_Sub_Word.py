import  re

num_of_lines = int(input())
list_lines = list()
list_queries = list()
# Make list of statements 
for _ in range(num_of_lines):
    list_lines.append(input())
# Number of queries to find the  count    
num_of_queries = int(input())
# List of queries
for _ in range(num_of_queries):
    list_queries.append(input())
# Regex pattern to find the words from statements
Regex_pattern_line = re.compile(r'\W?\w+\W?')

for q in list_queries:
    count = 0
    # Regex to find the query match
    Regex_pattern_query = re.compile(r'\w+' + q + '\w+')
    for line in list_lines:
        word_list = re.findall(Regex_pattern_line, line)
        for word in word_list:
            if re.search(Regex_pattern_query, word):
                count += 1
    print(count)
