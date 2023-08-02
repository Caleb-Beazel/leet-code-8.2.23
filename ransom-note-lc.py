class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        list_note = list(ransom_note)
        list_mag = list(magazine)

        for letter in list_note:
            if letter in list_mag:
                list_mag.remove(letter)
            else:
                return False
        return True