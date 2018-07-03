'''
Stack Exchange is an information power-house, which contains libraries of crowdsourced problems (with answers) across a large number of topics which are as diverse as electronics, cooking , programming, etc.

We are greatly interested in crawling and scraping as many questions, as we can, from stack-exchange. This is an example of a question library page from stack-exchange.

Your task will be, to scrape the questions from each library page, in the order in which they are listed. You will be provided with the markup of question listing pages, from which you need to detect: 
(1) Identifier (2) Question text (which is on the Hyperlink to the question) (3) How long ago the question was asked.

The Markup in the Test Cases will be similar to the sample fragment shown below. Please note, that since this markup is real markup from the website, it is likely to contain some stray control and escape characters, unexpected whitespaces and newlines.

Output Format 
The output file should contain N lines, where N is the number of questions you have identified in the provided fragment.Each line contains the identifier, question text and (relative) time when the question was asked (with no leading or trailing spaces surrounding each section); separated by semi-colons. The information about the questions in the output file should match with the ordering in the original markup.

Sample Output:
80407;about power supply of operational amplifier;11 hours ago
80405;5V Regulator Power Dissipation;11 hours ago

Explanation:
The given markup fragment points to two questions on electronics.stackexchange.com (at the time the markup was noted). 
The first question has ID 80407, it is "about power supply of operational amplifier" and it was asked "11 hours ago" (relative to the time when this markup was noted). Search for these values in the given markup fragment to gain a better understanding of where we identified these values from. The second question has ID 80405, it is about "5V Regulator Power Dissipation", and it was asked "11 hours ago" (relative to the time when this markup was noted).
'''
import re, sys


if __name__ == '__main__':
    # Read all th input as one string
    fragment = sys.stdin.read()
    # Regex to find question_id
    Regex_pattern_id = re.compile(r'(id=\"question-summary-)(\d+)')
    # Regex to find Question text
    Regex_pattern_question = re.compile(r'(<a href=\"\/questions\/\d+.+?\">)(.+)(<\/a)')
    # Regex to find question's posting time
    Regex_pattern_date = re.compile(r'(class=\"relativetime\">)(.+)(<\/span>)')
    question_id = re.findall(Regex_pattern_id, fragment)
    question_text = re.findall(Regex_pattern_question, fragment)
    question_date = re.findall(Regex_pattern_date, fragment)
    for i in range(len(question_id)):
        print(question_id[i][1]+";"+question_text[i][1]+";"+question_date[i][1])
