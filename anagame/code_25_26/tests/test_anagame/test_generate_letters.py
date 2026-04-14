import unittest
import random
import string
from anagame import generate_letters


class TestGenerateLetters(unittest.TestCase):
    def test_length_and_vowels(self):
        """generate_letters should return 7 lowercase letters and at least 3 vowels"""
        letters = generate_letters()
        self.assertEqual(len(letters), 7, "Expected 7 letters")
        for ch in letters:
            self.assertIn(ch, string.ascii_lowercase,
                          "Letters must be lowercase a-z")
        vowel_count = sum(1 for l in letters if l in "aeiou")
        self.assertGreaterEqual(vowel_count, 3, "At least 3 vowels required")

    def test_reproducible_with_seed(self):
        """Seeding random should make generate_letters deterministic"""
        random.seed(12345)
        a = generate_letters()
        random.seed(12345)
        b = generate_letters()
        self.assertEqual(
            a, b, "With the same random seed, outputs should be identical")

    def test_always_minimum_vowels_over_many_runs(self):
        """Run multiple times to ensure the vowel constraint is consistently enforced"""
        for _ in range(500):
            letters = generate_letters()
            vowel_count = sum(1 for l in letters if l in "aeiou")
            self.assertGreaterEqual(vowel_count, 3)

    def test_variety_across_runs(self):
        """Ensure randomness produces multiple distinct outputs across many runs"""
        seen = set()
        for _ in range(200):
            seen.add(tuple(generate_letters()))
        # Expect a reasonable number of distinct draws; threshold is conservative
        self.assertGreater(
            len(seen), 50, f"Expected >50 distinct letter sets, got {len(seen)}")

    def test_scrabble_distribution(self):
        """Check that letter frequencies roughly align with Scrabble distribution over many runs"""
        total_counts = {ch: 0 for ch in "abcdefghijklmnopqrstuvwxyz"}
        runs = 1000
        for _ in range(runs):
            letters = generate_letters()
            for l in letters:
                total_counts[l] += 1

        # Check a variety of letters to see if common letters appear more frequently
        self.assertGreater(total_counts['e'], 3*total_counts['z'],
                           "'e' should appear much more frequently than 'z'")
        self.assertGreater(total_counts['a'], 3*total_counts['q'],
                           "'a' should appear much more frequently than 'q'")
        self.assertGreater(total_counts['i'], 3*total_counts['j'],
                           "'i' should appear much more frequently than 'j'")
        self.assertGreater(total_counts['o'], 3*total_counts['p'],
                           "'o' should appear more frequently than 'p'")
        self.assertGreater(total_counts['u'], total_counts['y'],
                           "'u' should appear more frequently than 'y'")


if __name__ == "__main__":
    unittest.main()
