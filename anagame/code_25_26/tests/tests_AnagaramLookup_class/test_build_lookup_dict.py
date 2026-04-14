import unittest
from valid_anagame_words import get_valid_word_list
from AnagramLookup import AnagramLookup


class TestBuildLookupDict(unittest.TestCase):
    def setUp(self):
        self.letters1 = ["a", "b", "e", "d", "l"]
        self.letters2 = ["r", "a", "t"]
        self.letters3 = ["p", "o", "o", "l"]
        self.letters4 = ["o", "o", "l", "p", "p", "e", "s", "t"]

    def test_0_type(self):
        """build_lookup_dict - return type should be a dictionary"""
        words = ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
        explorer = AnagramLookup(words, self.letters1)
        val = explorer.anagram_hash_table
        self.assertIsInstance(
            val, dict, "build_lookup_dict should return a dictionary")

    def test_1_basic_anagram_grouping(self):
        """build_lookup_dict - groups anagrams together correctly"""
        words = ["rat", "tar", "art", "bat", "tab"]
        explorer = AnagramLookup(words, self.letters2)
        hash_table = explorer.anagram_hash_table

        # Find the group containing "rat", "tar", "art"
        rat_group = None
        for group in hash_table.values():
            if "rat" in group:
                rat_group = set(group)
                break

        expected_rat_group = {"rat", "tar", "art"}
        self.assertEqual(rat_group, expected_rat_group,
                         f"Expected anagram group {expected_rat_group} but got {rat_group}")

    def test_2_multiple_anagram_groups(self):
        """build_lookup_dict - correctly handles multiple separate anagram groups"""
        words = ["abed", "bead", "stop", "pots", "tops", "opts"]
        explorer = AnagramLookup(
            words, ["a", "b", "e", "d", "s", "t", "o", "p"])
        hash_table = explorer.anagram_hash_table

        # Should have 2 groups: one with abed/bead, one with stop/pots/tops/opts
        group_sizes = [len(group) for group in hash_table.values()]
        group_sizes.sort()
        # abed group (2 words) and stop group (4 words)
        expected_sizes = [2, 4]
        self.assertEqual(group_sizes, expected_sizes,
                         f"Expected group sizes {expected_sizes} but got {group_sizes}")

    def test_3_empty_word_bank(self):
        """build_lookup_dict - handles empty word bank"""
        words = []
        explorer = AnagramLookup(words, self.letters1)
        hash_table = explorer.anagram_hash_table
        expected = {}
        self.assertEqual(hash_table, expected,
                         f"Expected empty dictionary but got {hash_table}")

    def test_4_all_words_accounted_for(self):
        """build_lookup_dict - ensures all words from word bank appear exactly once"""
        words = ["abed", "bead", "mouse", "rat", "tar", "art"]
        explorer = AnagramLookup(
            words, ["a", "b", "e", "d", "m", "o", "u", "s", "r", "t"])
        hash_table = explorer.anagram_hash_table

        # Collect all words from all groups
        all_words_in_table = set()
        for group in hash_table.values():
            all_words_in_table.update(group)

        expected_words = explorer.word_bank
        self.assertEqual(all_words_in_table, expected_words,
                         f"Words in hash table {all_words_in_table} don't match word bank {expected_words}")

    def test_5_integration_with_valid_word_list(self):
        """build_lookup_dict - integration with actual valid word list"""
        word_list = get_valid_word_list()
        explorer = AnagramLookup(word_list, self.letters4)
        hash_table = explorer.anagram_hash_table

        # Find groups containing known anagrams
        pool_group = None
        for group in hash_table.values():
            if "pool" in group:
                pool_group = set(group)
                break

        expected_anagrams = {"pool", "polo", "loop"}
        unexpected_anagrams = {"pools", "lop", "pol", "loo", "plop"}

        self.assertTrue(expected_anagrams.issubset(pool_group),
                        f"Expected {expected_anagrams} to be grouped together in {pool_group}")
        for word in unexpected_anagrams:
            self.assertNotIn(
                word, pool_group, f"Did not expect '{word}' to be in the pool anagram group")


if __name__ == "__main__":
    unittest.main()
