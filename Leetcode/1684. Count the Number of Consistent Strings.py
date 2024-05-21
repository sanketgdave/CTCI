class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """

        # legit word count
        count = 0

        # allowed characters
        # words

        # all char of word must appear in allowed

        # dict for allowed
        # allowed_dict = dict(allowed, 0)
        allowed_set = set(allowed)
    
        # check each char in word such that it appears in allowed_dict or not
        for each_word in words:
            has_break_occured = False
            for each_char in each_word:
                # if each_char in allowed_set:
                #     pass
                # else:
                #     has_break_occured = True
                #     break

                if each_char not in allowed_set:
                    has_break_occured = True
                    break

            # check some how if break has happened or not
            # if has_break_occured:
            #     pass
            # else:
            #     count += 1

            if not has_break_occured:
                count += 1


        return count