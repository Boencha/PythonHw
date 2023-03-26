
class Task1:

    def __init__(self, french, pianists, swimmers):
        self.french = french
        self.pianists = pianists
        self.swimmers = swimmers

    def special_students(self):
        swimmers_and_pianists = list(set(self.swimmers) & set(self.pianists))
        non_french_learners = list(set(swimmers_and_pianists) - set(self.french))
        return non_french_learners


class Task2:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def get_unique_list_1(self):
        if len(self.list_1) == 0:
            arr = []
        else:
            arr = set(self.list_1)
            arr = sorted(arr)
        return arr

    def get_unique_both_lists(self):
        if len(self.list_1) == 0 and len(self.list_2) == 0:
            arr = []
        else:
            arr = set(self.list_1) | set(self.list_2)
            arr = sorted(arr)
        return arr


class Task3:

    def __init__(self, films):
        self.films = films

    def get_results(self):
        films_dict = {}
        for film in self.films:
            if film in films_dict:
                films_dict[film] += 1
            else:
                films_dict[film] = 1

        films_sorted = sorted(films_dict.items(), key=lambda x: (-x[1], int(x[0])))
        result = {film: count for film, count in films_sorted}
        return result


class Task4:

    def __init__(self, text):
        self.text = text

    def word_counter(self):
        text = self.text.lower()
        for char in ",.!?":
            text = text.replace(char, "")
        counts = {}
        for word in text.split():
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        sorted_word_count = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        result = {word: count for word, count in sorted_word_count}
        return result



class Task5:

    def __init__(self, family):
        self.family = family


    def parents(self, name):
        return self.family.get(name, [])


    def grandparents(self, name):
        grandparents = []
        for parent in self.parents(name):
            grandparents.extend(self.parents(parent))
        return grandparents


    def siblings(self, name):
        siblings = []
        for person in self.family:
            if person != name and set(self.parents(person)) == set(self.parents(name)):
                siblings.append(person)
        return siblings


    def children(self, name):
        children = []
        for person in self.family:
            if name in self.parents(person):
                children.append(person)
        return children


    def grandchildren(self, name):
        grandchildren = []
        for child in self.children(name):
            grandchildren.extend(self.children(child))
        return grandchildren


