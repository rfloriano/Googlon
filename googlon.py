"""
    challenge's Google developer day 2011 Brasil
    
    @author: Rafael Floriano da Silva <rflorianobr@gmail.com>
    @date: 17/08/2011
    @last_update: 17/08/2011
    
    This module provides the fictional language Googlon of challenge
"""

class Googlon(object):
    """
    Googlon class provides all constants and methods to Googlon texts
    """
    
    FOO = list("gfzts")
    BAR = list("cbdhkjmlnqprwvx")
    ALPHABET = "twdcrzpsvhmklnfxqjbg"
    NUMBER_BASE = 20
    INDEX = lambda self, word: [ self.ALPHABET.index(char) for char in word ]

    def isBar(self, char):
        """
        isBar method to test if the char parameter is in constant BAR list
        
        @params:
            char: a character to test if is BAR constant
        @return:
            boolean
        """
        
        return (char in self.BAR)
        
    def isPreposition(self, word):
        """
        isPreposition method to test if a word has the last character in BAR
        and it not contains "m"
        
        @params:
            word: a word to test if it pass in preposition Googlon test
        @return:
            boolean
        """
        
        return (
            len(word) == 3 
            and self.isBar(word[-1])
            and not "m" in word
        )

    def isVerb(self, word):
        """
        isVerb method to test if the word has length greater or
        equal 7 and has the last character in BAR list
        
        @params:
            word: a word to test if it pass in verb Googlon test
        @return:
            boolean
        """
        
        return (
            len(word) >= 7 
            and self.isBar(word[-1])
        )

    def isVerbInFirstPerson(self, word):
        """
        isVerbInFirstPerson method to test if the word is a Googlon verb
        and has the first character in BAR list
        
        @params:
            word: a word to test if it pass in verb as first person Googlon test
        @return:
            boolean
        """
        
        return (
            self.isVerb(word)
            and self.isBar(word[0])
        )

    def isPrettyNumber(self, number):
        """
        isPrettyNumber method to test if the number is greater or
        equal 502344 and it is divisible by 4
        
        @params:
            number: a number to test if it pass in pretty number of Googlon test
        @return:
            boolean
        """
        
        return (
            number >= 502344 
            and not number % 4
        )
        
    def prepositions(self, text):
        """
        prepositions method to get a list of prepositions in the text
        
        @params:
            text: a text to get prepositions of Googlon
        @return:
            prep: list of prepositions in the text
        """
    
        prep = []
        for word in text.split():
            if self.isPreposition(word):
                prep.append(word)
        return prep

    def verbs(self, text):
        """
        verbs method to get list of verbs and first person verbs in the text
        
        @params:
            text: a text to get verbs and first person verbs of Googlon
        @return:
            prep: tuple of verbs and first person verbs
        """
    
        firstPerson = []
        verbs = []
        for word in text.split():
            if self.isVerb(word):
                verbs.append(word)
                if self.isVerbInFirstPerson(word):
                    firstPerson.append(word)
        return verbs, firstPerson

    def vocabulary(self, text):
        """
        vocabulary method to get unique words in the text and sort it
        
        @params:
            text: a text to get vocabulary of Googlon
        @return:
            text: a ordened text that contains all unique words of Googlon 
                  vocabulary
        """
    
        uniqueWords = list(
            set(text.split())
        )
        return " ".join(
            sorted(uniqueWords, key=self.INDEX)
        )

    def number(self, word):
        """
        number method to convert word into Googlon number
        
        @params:
            word: a word to convert to number in NUMBER_BASE (20) Googlon 
        @return:
            s: sum of all digits of a word as number
        """
    
        indexes = self.INDEX(word)
        s = 0
        for i in xrange(len(indexes)):
            s += indexes[i] * (self.NUMBER_BASE ** i)
        return s

    def distinctPrettyNumbers(self, text):
        """
        distinctPrettyNumbers method to get all distinct pretty numbers
        
        @params:
            text: text to transform in numbers
        @return:
            prettyNumbers: the unique pretty numbers of text
        """
    
        prettyNumbers = []
        for word in list(set(text.split())):
            number = self.number(word)
            if self.isPrettyNumber(number):
                prettyNumbers.append(number)
        return prettyNumbers
