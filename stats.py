def number_of_words(contents):
        words = contents.split()
        num_words = len(words)
        return num_words

def number_of_characters(contents):
	contents = contents.lower()
	report = {}
	for characters in contents:
		if characters in report:
			report[characters] += 1
		else:
			report[characters] = 1
	return report

def sort_on(items):
	return items["num"]

def list_of_dicts(report):
	list = []
	for key, value in report.items():
		dict = {"char": key, "num": value}
		list.append(dict)
	return list


def get_sorted_char_list(report):
	results = list_of_dicts(report)
	results.sort(reverse=True, key=sort_on)
	return results
