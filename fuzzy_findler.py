import re

def fuzzyfindler1(user_input, collection):
    suggestions = []
    pattern = ".*".join(user_input)
    regex =  re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append(match)
    return suggestions
def fuzzyfindler2(user_input,collection):
    suggestions = []
    pattern = ".*".join(user_input)
    for item in collection:
        match = re.search(pattern, item)
        if match:
            suggestions.append((match.start(), item))
    return [x for _, x in suggestions]

def fuzzyfindler3(user_input, collection):
    suggestions = []
    pattern = ".*?".join(user_input)
    for item in collection:
        match = re.search(pattern, item)
        if match:
            print(match.group())
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _,_,x in suggestions]
if __name__ == '__main__':
    collections = ['django_migrations.py', 'django_admin_log.py', 'main_generator.py', 'migrations.py', 'api_user.doc',
                   'user_group.doc', 'accounts.txt']
    print(fuzzyfindler3("djm", collections))
