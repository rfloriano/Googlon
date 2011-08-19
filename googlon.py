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

    INDEX = lambda self, word: [ self.alphabet.index(char) for char in word ]
    
    def __init__(self, foo, prepLength, prepLastCharIs, prepNotHas, verbLength, 
        verbGreaterOrEqual, verbLastCharIs, verbFirstCharIs, alphabet, pretty, 
        prettyDivisible, numberBase = 20):
        """
        On Googlon vocabulary we need to get a many parameters
        
        @params:
            foo: A string letters provideded by googlon
            prepLength: Length of preposition as integer
            prepLastCharIs: Type of last char preposition, such as: "Bar" or 
                            "Foo" as string
            prepNotHas: A char that a preposition can not contains a unique 
                        string I.E: "m".
            verbLength: Length of verb as integer
            verbGreaterOrEqual: True if the verbLength need be greater or equal
                                False if it onle grater
            verbLastCharIs: Type of last char verb, such as: "Bar" or 
                            "Foo" as string
            verbFirstCharIs: Type of first char verb, such as: "Bar" or 
                            "Foo" as string
            alphabet: the googlon alphabet as string
            pretty: A integer number as a first googlon's pretty number
            prettyDivisible: Integer that a pretty number should be divisible
            numberBase(optional): A number base of googlon's numbers as integer
                                  (default is 20)
        @returns:
            None
        """

        self.foo = foo
        self.bar = list(set(alphabet) - set(foo))
        self.prepLength = prepLength
        self.prepLastCharIs = prepLastCharIs
        self.prepNotHas = prepNotHas
        self.verbLength = verbLength
        if verbGreaterOrEqual:
            self.verbLength -= 1
        self.verbLastCharIs = verbLastCharIs
        self.verbFirstCharIs = verbFirstCharIs
        self.alphabet = alphabet
        self.numberBase = numberBase
        self.pretty = pretty
        self.prettyDivisible = prettyDivisible

    def isBar(self, char):
        """
        isBar method to test if the char parameter is in constant bar list
        
        @params:
            char: a character to test if is bar constant
        @return:
            boolean
        """
        
        return (char in self.bar)
        
    def isFoo(self, char):
        """
        isFoo method to test if the char parameter is in constant foo list
        
        @params:
            char: a character to test if is foo constant
        @return:
            boolean
        """
        
        return (char in self.foo)
        
    def isPreposition(self, word):
        """
        isPreposition method to test if a word has the last character in bar
        and it not contains "m"
        
        @params:
            word: a word to test if it pass in preposition Googlon test
        @return:
            boolean
        """
        
        return (
            len(word) == self.prepLength
            and eval("self.is"+self.prepLastCharIs+"(word[-1])")
            and not self.prepNotHas in word
        )

    def isVerb(self, word):
        """
        isVerb method to test if the word has length greater or
        equal 7 and has the last character in bar list
        
        @params:
            word: a word to test if it pass in verb Googlon test
        @return:
            boolean
        """
        
        return (
            len(word) > self.verbLength
            and eval("self.is"+self.verbLastCharIs+"(word[-1])")
        )

    def isVerbInFirstPerson(self, word):
        """
        isVerbInFirstPerson method to test if the word is a Googlon verb
        and has the first character in bar list
        
        @params:
            word: a word to test if it pass in verb as first person Googlon test
        @return:
            boolean
        """
        
        return (
            self.isVerb(word)
            and eval("self.is"+self.verbFirstCharIs+"(word[0])")
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
            number >= self.pretty 
            and not number % self.prettyDivisible
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
            word: a word to convert to number in numberBase (20) Googlon 
        @return:
            s: sum of all digits of a word as number
        """
    
        indexes = self.INDEX(word)
        s = 0
        for i in xrange(len(indexes)):
            s += indexes[i] * (self.numberBase ** i)
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
        
    def run(self, text):
        """
        Simple print features of a text
        
        @params:
            text: A text to be analysed
        @return:
            None
        """
        
        print "Text: ", text[:200]
        print "Prepositions in text: ", len(self.prepositions(text))
        verbs, firstPerson = self.verbs(text)
        print "Verbs in text: %s, these %s is in first person" % (len(verbs), len(firstPerson))
        print "Vocabulary ordened in text: ", self.vocabulary(text)
        print "Pretty numbers in text: ", len(self.distinctPrettyNumbers(text))
