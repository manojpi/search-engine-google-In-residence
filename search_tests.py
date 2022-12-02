from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)


    def test_keyword_to_titles(self):

        expected_empty_meatadata = {}
        self.assertEqual(keyword_to_titles([]), expected_empty_meatadata)

        random_metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, ['canadian', 'canada', 'lee', 'jazz', 'and', 'rock', 'singer', 'songwriter', 'also', 'known', 'hip', 'hop', 'musician', 'folk', 'pop', 'composer', 'drummer', 'player', 'rapper', 'john', 'don', 'guitarist', 'the', 'andrew', 'country', 'indie', 'charlie', 'alternative', 'paul', 'matt', 'james', 'blues', 'bassist', 'cellist', 'pianist', 'artist', 'marie', 'dance', 'winner', 'idol', 'mike', 'keyboardist', 'jason', 'music', 'tim', 'kim', 'soprano', 'kevin', 'martin', 'violinist', 'dan', 'blue', 'new', 'daniel', 'producer', 'punk', 'conductor', 'gospel', 'dave', 'big', 'band', 'george', 'brian', 'bill', 'classical', 'david', 'operatic', 'michael', 'film', 'jon', 'soul', 'billy', 'record', 'jim', 'member', 'broken', 'social', 'scene', 'musical', 'theatre', 'actress', 'actor', 'peter', 'ian', 'electronic', 'rhythm', 'taylor', 'vocalist', 'jesse', 'radio', 'personality', 'for', 'andy', 'former', 'solo', 'chris', 'ryan', 'mark', 'scott', 'kate', 'multi', 'formerly', 'mother', 'instrumentalist', 'johnson', 'white', 'smith']], ['French pop music', 'Mack Johnson', 1172208041, 5569, ['french', 'pop', 'music', 'the', 'france', 'and', 'radio']], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']], ['Noise (music)', 'jack johnson', 1194207604, 15641, ['noise', 'music', 'that', 'the', 'use', 'musical', 'this', 'made', 'and', 'sound', 'based', 'some', 'can', 'instruments', 'may', 'machine', 'sounds', 'audio', 'recordings', 'recording', 'other', 'produced', 'electronic', 'such', 'also', 'more', 'with', 'art', 'was', 'for', 'aesthetic', 'example', 'being', 'fluxus', 'artists', 'composition', 'early', 'young', 'rock', 'wave', 'industrial', 'works', 'his', 'from', 'one', 'not', 'signal', 'what', 'any', 'have', 'time', 'like', 'paul', 'hegarty', 'work', 'these', 'john', 'cage', 'which', 'all', 'japanese', 'genre', 'but', 'russolo', 'used', 'white', 'same', 'track', 'artist', 'first', 'had', 'found', 'called', 'created', 'paris', 'sirens', 'piece', 'using', 'percussion', 'tape', 'musique', 'concrète', 'group', 'recorded', 'various', '1960', 'album', 'cassette', 'ubuweb', 'com', 'ubu']]]
        expected_random_metadata = {'canadian': ['List of Canadian musicians'], 'canada': ['List of Canadian musicians'], 'lee': ['List of Canadian musicians'], 'jazz': ['List of Canadian musicians'], 'and': ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo', 'Noise (music)'], 'rock': ['List of Canadian musicians', 'Noise (music)'], 'singer': ['List of Canadian musicians'], 'songwriter': ['List of Canadian musicians'], 'also': ['List of Canadian musicians', 'Noise (music)'], 'known': ['List of Canadian musicians'], 'hip': ['List of Canadian musicians'], 'hop': ['List of Canadian musicians'], 'musician': ['List of Canadian musicians'], 'folk': ['List of Canadian musicians'], 'pop': ['List of Canadian musicians', 'French pop music'], 'composer': ['List of Canadian musicians'], 'drummer': ['List of Canadian musicians'], 'player': ['List of Canadian musicians', 'Edogawa, Tokyo'], 'rapper': ['List of Canadian musicians'], 'john': ['List of Canadian musicians', 'Noise (music)'], 'don': ['List of Canadian musicians'], 'guitarist': ['List of Canadian musicians'], 'the': ['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo', 'Noise (music)'], 'andrew': ['List of Canadian musicians'], 'country': ['List of Canadian musicians'], 'indie': ['List of Canadian musicians'], 'charlie': ['List of Canadian musicians'], 'alternative': ['List of Canadian musicians'], 'paul': ['List of Canadian musicians', 'Noise (music)'], 'matt': ['List of Canadian musicians'], 'james': ['List of Canadian musicians'], 'blues': ['List of Canadian musicians'], 'bassist': ['List of Canadian musicians'], 'cellist': ['List of Canadian musicians'], 'pianist': ['List of Canadian musicians'], 'artist': ['List of Canadian musicians', 'Noise (music)'], 'marie': ['List of Canadian musicians'], 'dance': ['List of Canadian musicians'], 'winner': ['List of Canadian musicians'], 'idol': ['List of Canadian musicians'], 'mike': ['List of Canadian musicians'], 'keyboardist': ['List of Canadian musicians'], 'jason': ['List of Canadian musicians'], 'music': ['List of Canadian musicians', 'French pop music', 'Noise (music)'], 'tim': ['List of Canadian musicians'], 'kim': ['List of Canadian musicians'], 'soprano': ['List of Canadian musicians'], 'kevin': ['List of Canadian musicians'], 'martin': ['List of Canadian musicians'], 'violinist': ['List of Canadian musicians'], 'dan': ['List of Canadian musicians'], 'blue': ['List of Canadian musicians'], 'new': ['List of Canadian musicians'], 'daniel': ['List of Canadian musicians'], 'producer': ['List of Canadian musicians'], 'punk': ['List of Canadian musicians'], 'conductor': ['List of Canadian musicians'], 'gospel': ['List of Canadian musicians'], 'dave': ['List of Canadian musicians'], 'big': ['List of Canadian musicians'], 'band': ['List of Canadian musicians'], 'george': ['List of Canadian musicians'], 'brian': ['List of Canadian musicians'], 'bill': ['List of Canadian musicians'], 'classical': ['List of Canadian musicians'], 'david': ['List of Canadian musicians'], 'operatic': ['List of Canadian musicians'], 'michael': ['List of Canadian musicians'], 'film': ['List of Canadian musicians'], 'jon': ['List of Canadian musicians'], 'soul': ['List of Canadian musicians'], 'billy': ['List of Canadian musicians'], 'record': ['List of Canadian musicians'], 'jim': ['List of Canadian musicians'], 'member': ['List of Canadian musicians'], 'broken': ['List of Canadian musicians'], 'social': ['List of Canadian musicians'], 'scene': ['List of Canadian musicians'], 'musical': ['List of Canadian musicians', 'Noise (music)'], 'theatre': ['List of Canadian musicians'], 'actress': ['List of Canadian musicians'], 'actor': ['List of Canadian musicians'], 'peter': ['List of Canadian musicians'], 'ian': ['List of Canadian musicians'], 'electronic': ['List of Canadian musicians', 'Noise (music)'], 'rhythm': ['List of Canadian musicians'], 'taylor': ['List of Canadian musicians'], 'vocalist': ['List of Canadian musicians'], 'jesse': ['List of Canadian musicians'], 'radio': ['List of Canadian musicians', 'French pop music'], 'personality': ['List of Canadian musicians'], 'for': ['List of Canadian musicians', 'Noise (music)'], 'andy': ['List of Canadian musicians'], 'former': ['List of Canadian musicians'], 'solo': ['List of Canadian musicians'], 'chris': ['List of Canadian musicians'], 'ryan': ['List of Canadian musicians'], 'mark': ['List of Canadian musicians'], 'scott': ['List of Canadian musicians'], 'kate': ['List of Canadian musicians'], 'multi': ['List of Canadian musicians'], 'formerly': ['List of Canadian musicians'], 'mother': ['List of Canadian musicians'], 'instrumentalist': ['List of Canadian musicians'], 'johnson': ['List of Canadian musicians'], 'white': ['List of Canadian musicians', 'Noise (music)'], 'smith': ['List of Canadian musicians'], 'french': ['French pop music'], 'france': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo', 'Noise (music)'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo'], 'noise': ['Noise (music)'], 'that': ['Noise (music)'], 'use': ['Noise (music)'], 'this': ['Noise (music)'], 'made': ['Noise (music)'], 'sound': ['Noise (music)'], 'based': ['Noise (music)'], 'some': ['Noise (music)'], 'can': ['Noise (music)'], 'instruments': ['Noise (music)'], 'may': ['Noise (music)'], 'machine': ['Noise (music)'], 'sounds': ['Noise (music)'], 'audio': ['Noise (music)'], 'recordings': ['Noise (music)'], 'recording': ['Noise (music)'], 'other': ['Noise (music)'], 'produced': ['Noise (music)'], 'such': ['Noise (music)'], 'more': ['Noise (music)'], 'art': ['Noise (music)'], 'was': ['Noise (music)'], 'aesthetic': ['Noise (music)'], 'example': ['Noise (music)'], 'being': ['Noise (music)'], 'fluxus': ['Noise (music)'], 'artists': ['Noise (music)'], 'composition': ['Noise (music)'], 'early': ['Noise (music)'], 'young': ['Noise (music)'], 'wave': ['Noise (music)'], 'industrial': ['Noise (music)'], 'works': ['Noise (music)'], 'his': ['Noise (music)'], 'from': ['Noise (music)'], 'one': ['Noise (music)'], 'not': ['Noise (music)'], 'signal': ['Noise (music)'], 'what': ['Noise (music)'], 'any': ['Noise (music)'], 'have': ['Noise (music)'], 'time': ['Noise (music)'], 'like': ['Noise (music)'], 'hegarty': ['Noise (music)'], 'work': ['Noise (music)'], 'these': ['Noise (music)'], 'cage': ['Noise (music)'], 'which': ['Noise (music)'], 'all': ['Noise (music)'], 'japanese': ['Noise (music)'], 'genre': ['Noise (music)'], 'but': ['Noise (music)'], 'russolo': ['Noise (music)'], 'used': ['Noise (music)'], 'same': ['Noise (music)'], 'track': ['Noise (music)'], 'first': ['Noise (music)'], 'had': ['Noise (music)'], 'found': ['Noise (music)'], 'called': ['Noise (music)'], 'created': ['Noise (music)'], 'paris': ['Noise (music)'], 'sirens': ['Noise (music)'], 'piece': ['Noise (music)'], 'using': ['Noise (music)'], 'percussion': ['Noise (music)'], 'tape': ['Noise (music)'], 'musique': ['Noise (music)'], 'concrète': ['Noise (music)'], 'group': ['Noise (music)'], 'recorded': ['Noise (music)'], 'various': ['Noise (music)'], '1960': ['Noise (music)'], 'album': ['Noise (music)'], 'cassette': ['Noise (music)'], 'ubuweb': ['Noise (music)'], 'com': ['Noise (music)'], 'ubu': ['Noise (music)']}
        self.assertEqual(keyword_to_titles(random_metadata), expected_random_metadata)

        no_keyword_metadata = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023, []]]
        expected_invalid_metadata = {}
        self.assertEqual(keyword_to_titles(no_keyword_metadata), expected_invalid_metadata)
    

    def test_title_to_info(self):

        expected_empty_metadata = {}
        self.assertEqual(title_to_info([]), expected_empty_metadata)

        no_author_metadata = [['List of Canadian musicians', 1181623340, 21023, ['canadian', 'canada', 'lee', 'jazz', 'and', 'rock', 'singer', 'songwriter', 'also', 'known', 'hip', 'hop', 'musician', 'folk', 'pop', 'composer', 'drummer', 'player', 'rapper', 'john', 'don', 'guitarist', 'the', 'andrew', 'country', 'indie', 'charlie', 'alternative', 'paul', 'matt', 'james', 'blues', 'bassist', 'cellist', 'pianist', 'artist', 'marie', 'dance', 'winner', 'idol', 'mike', 'keyboardist', 'jason', 'music', 'tim', 'kim', 'soprano', 'kevin', 'martin', 'violinist', 'dan', 'blue', 'new', 'daniel', 'producer', 'punk', 'conductor', 'gospel', 'dave', 'big', 'band', 'george', 'brian', 'bill', 'classical', 'david', 'operatic', 'michael', 'film', 'jon', 'soul', 'billy', 'record', 'jim', 'member', 'broken', 'social', 'scene', 'musical', 'theatre', 'actress', 'actor', 'peter', 'ian', 'electronic', 'rhythm', 'taylor', 'vocalist', 'jesse', 'radio', 'personality', 'for', 'andy', 'former', 'solo', 'chris', 'ryan', 'mark', 'scott', 'kate', 'multi', 'formerly', 'mother', 'instrumentalist', 'johnson', 'white', 'smith']]]
        expected_no_author_metadata = {}
        self.assertEqual(title_to_info(no_author_metadata), expected_empty_metadata)

        valid_metadata = [['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']]]
        expected_valid_metadata = {'Edogawa, Tokyo' : {'author': 'jack johnson', 'timestamp': 1222607041, 'length': 4526}}
        self.assertEqual(title_to_info(valid_metadata), expected_valid_metadata)


    def test_search(self):

        valid_keyword_to_titles = {'canada': ['List of Canadian musicians', 'Lights (musician)', 'Old-time music', 'Will Johnson (soccer)'], 'sun': ['Sun dog']}

        expected_empty_keyword = []
        self.assertEqual(search("", valid_keyword_to_titles), expected_empty_keyword)

        incorrect_case_keyword = "Canada"
        expected_incorrect_case_keyword = []
        self.assertEqual(search(incorrect_case_keyword, valid_keyword_to_titles), expected_incorrect_case_keyword)

        matching_case_keyword = "canada"
        expected_matching_case_keyword = ['List of Canadian musicians', 'Lights (musician)', 'Old-time music', 'Will Johnson (soccer)']
        self.assertEqual(search(matching_case_keyword, valid_keyword_to_titles), expected_matching_case_keyword)


    def test_article_length(self):

        valid_title_to_info = {'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}}
        valid_article_titles = ['Sun dog', 'List of Canadian musicians']

        negative_max_length = -10
        expected_negative_max_length = []
        self.assertEqual(article_length(negative_max_length, valid_article_titles, valid_title_to_info), expected_negative_max_length)

        valid_max_length = 19000
        expected_valid_max_length = ['Sun dog']
        self.assertEqual(article_length(valid_max_length, valid_article_titles, valid_title_to_info), expected_valid_max_length)

        less_than_min_length = 10000
        expected_less_than_min_length = []
        self.assertEqual(article_length(less_than_min_length, valid_article_titles, valid_title_to_info), expected_less_than_min_length)


    def test_key_by_author(self):

        valid_title_to_info = {'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}}
        valid_article_titles = ['Sun dog', 'List of Canadian musicians', 'Dalmatian (dog)']

        empty_article_title = []
        expected_empty_article_title = {}
        self.assertEqual(key_by_author(empty_article_title, valid_title_to_info), expected_empty_article_title)

        empty_title_to_info = {}
        expected_empty_title_to_info = {}
        self.assertEqual(key_by_author(valid_article_titles, empty_title_to_info), expected_empty_title_to_info)

        expected_valid_title_to_info = {'Mr Jake': ['Sun dog', 'Dalmatian (dog)'], 'Jack Johnson': ['List of Canadian musicians']}
        self.assertEqual(key_by_author(valid_article_titles, valid_title_to_info), expected_valid_title_to_info)


    def test_filter_to_author(self):

        valid_title_to_info = {'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}}
        valid_article_titles = ['Sun dog', 'List of Canadian musicians', 'Dalmatian (dog)']

        empty_author_name = ""
        expected_empty_author_name = []
        self.assertEqual(filter_to_author(empty_author_name, valid_article_titles, valid_title_to_info), expected_empty_author_name)

        incorrect_case_author_name = 'jack johnson'
        expected_incorrect_case_author_name = []
        self.assertEqual(filter_to_author(incorrect_case_author_name, valid_article_titles, valid_title_to_info), expected_incorrect_case_author_name)

        matching_case_author_name = 'Jack Johnson'
        expected_matching_case_author_name = ['List of Canadian musicians']
        self.assertEqual(filter_to_author(matching_case_author_name, valid_article_titles, valid_title_to_info), expected_matching_case_author_name)


    def test_filter_out(self):
        
        valid_keyword_to_titles = {'dog':['Black dog (ghost)', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', 'Sun dog'], 'canada': ['List of Canadian musicians', 'Lights (musician)', 'Old-time music', 'Will Johnson (soccer)']}
        valid_article_titles = ['Sun dog', 'List of Canadian musicians', 'Dalmatian (dog)']
        
        empty_keyword = ""
        expected_empty_keyword = ['Sun dog', 'List of Canadian musicians', 'Dalmatian (dog)']
        self.assertEqual(filter_out(empty_keyword, valid_article_titles, valid_keyword_to_titles), expected_empty_keyword)

        searched_keyword = "dog"
        dog_article_titles = ['Sun dog', 'Dalmatian (dog)']
        expected_dog_article_titles = []
        self.assertEqual(filter_out(searched_keyword, dog_article_titles, valid_keyword_to_titles), expected_dog_article_titles)

        valid_keyword = "canada"
        expected_valid_keyword = ['Sun dog', 'Dalmatian (dog)']
        self.assertEqual(filter_out(valid_keyword, valid_article_titles, valid_keyword_to_titles), expected_valid_keyword)

        case_sensetive_keyword = "Dog"
        expected_case_sensetive_keyword = ['Sun dog', 'List of Canadian musicians', 'Dalmatian (dog)']
        self.assertEqual(filter_out(case_sensetive_keyword, valid_article_titles, valid_keyword_to_titles), expected_case_sensetive_keyword)


    def test_articles_from_year(self):

        valid_title_to_info = {'Sun dog': {'author': 'Mr Jake', 'timestamp': 1208969289, 'length': 18050}, 'List of Canadian musicians': {'author': 'Jack Johnson', 'timestamp': 1181623340, 'length': 21023}, 'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}}
        valid_article_titles = ['Sun dog', 'List of Canadian musicians', 'Dalmatian (dog)']

        negative_year = -1980
        expected_negative_year = []
        self.assertEqual(articles_from_year(negative_year, valid_article_titles, valid_title_to_info), expected_negative_year)

        not_in_metadata_year = 1000
        expected_not_in_metadata_year = []
        self.assertEqual(articles_from_year(not_in_metadata_year, valid_article_titles, valid_title_to_info), expected_not_in_metadata_year)

        valid_year = 2008
        expected_valid_year = ['Sun dog', 'Dalmatian (dog)']
        self.assertEqual(articles_from_year(valid_year, valid_article_titles, valid_title_to_info), expected_valid_year)

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)
    

    @patch('builtins.input')
    def test_article_length_integration(self, input_mock):
        keyword = 'canada'
        advanced_option = 1
        advanced_response = 10000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Lights (musician)', 'Will Johnson (soccer)']\n"

        self.assertEqual(output, expected)
    

    @patch('builtins.input')
    def test_filter_to_author_integration(self, input_mock):
        keyword = 'dog'
        advanced_option = 3
        advanced_response = "Mr Jake"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Dalmatian (dog)', 'Sun dog']\n"

        self.assertEqual(output, expected)
    

    @patch('builtins.input')
    def test_filter_out_integration(self, input_mock):
        keyword = 'sun'
        advanced_option = 4
        advanced_response = "sun"

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)
    

    @patch('builtins.input')
    def test_search_integration(self, input_mock):
        keyword = 'soccer'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)
    

if __name__ == "__main__":
    main()