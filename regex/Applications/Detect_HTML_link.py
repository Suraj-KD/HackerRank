import re, sys
Regex_pattern_link = r'a.*?href="([^"]*)".*?>(.*?)</a>'
for i in sys.stdin.readlines()[1:]:
    splited_line = re.split('(<a.*?href="[^"]*".*?>.*?</a>)', i)
    for sub_line in splited_line:
        match = re.search(Regex_pattern_link, sub_line)
        if match:
            href = str(match.group(1))
            text = str(match.group(2))
            text = str(re.sub('<[^>]+>', '', text)).lstrip()
            print(href + ',' + text)
