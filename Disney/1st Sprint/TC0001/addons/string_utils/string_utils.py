from .actions import CompareTwoStrings, ConcatenateTwoStrings, ConvertStringToLowerCase, ConvertStringToNumber, ConvertStringToUpperCase, CountStrings, ExtractStringUsingRegex, FindLastSubstringIndexFromIndex, FindSubstringIndex, FindSubstringLastIndex, GetStringSubstring, InsertStringInIndex, IsStringEmpty, ReplaceSubstringFirstOcurrence, ReplaceSubstrings, ReplaceSubstringsWithRegex, SplitStringWithRegex, StringContains, StringLength, StringStartsWith, TransformCharacterAtIndex, TrimString


class StringUtils:
    @staticmethod
    def comparetwostrings(firstString: str, secondString: str, ignoreCase: bool, expectedResult: int) -> CompareTwoStrings:
        """Compares {{firstString}} with {{secondString}}.

        Compares two given strings lexicographically. Each character of both the strings is converted into a Unicode value for comparison..
        """
        return CompareTwoStrings(firstString, secondString, ignoreCase, expectedResult)

    @staticmethod
    def concatenatetwostrings(firstString: str, secondString: str) -> ConcatenateTwoStrings:
        """Concatenates {{firstString}} with {{secondString}}.

        Concatenates the second string to the end of the original string.
        """
        return ConcatenateTwoStrings(firstString, secondString)

    @staticmethod
    def convertstringtolowercase(inputString: str) -> ConvertStringToLowerCase:
        """Convert {{inputString}} to lowercase.

        Converts a given string to lowercase.
        """
        return ConvertStringToLowerCase(inputString)

    @staticmethod
    def convertstringtonumber(input: str) -> ConvertStringToNumber:
        """Remove none numeric characters from {{input}}."""
        return ConvertStringToNumber(input)

    @staticmethod
    def convertstringtouppercase(inputString: str) -> ConvertStringToUpperCase:
        """Converts {{inputString}} to uppercase.

        Converts a given string to uppercase.
        """
        return ConvertStringToUpperCase(inputString)

    @staticmethod
    def countstrings(inputString: str, delimiter: str) -> CountStrings:
        """Count how many strings are present in '{{inputString}}' with a given delimiter '{{delimiter}}'.

        Count how many strings are present in '{{inputString}}' with a given delimiter '{{delimiter}}'.
        """
        return CountStrings(inputString, delimiter)

    @staticmethod
    def extractstringusingregex(regex: str, input: str) -> ExtractStringUsingRegex:
        """Extract Sub-String from {{input}} using {{regex}}."""
        return ExtractStringUsingRegex(regex, input)

    @staticmethod
    def findlastsubstringindexfromindex(sourceString: str, subString: str, fromIndex: int) -> FindLastSubstringIndexFromIndex:
        """Get the index of the last occurrence of {{subString}}, searching backward starting from index {{fromIndex}}.

        Returns the index within source string of the last occurrence of specified substring, searching backward starting at the specified index.
        """
        return FindLastSubstringIndexFromIndex(sourceString, subString, fromIndex)

    @staticmethod
    def findsubstringindex(sourceString: str, subString: str, fromIndex: int) -> FindSubstringIndex:
        """Get the index of the first occurrence of {{substring}} in {{sourceString}}.

        Returns the index within source string of the first occurrence of specified substring.
        """
        return FindSubstringIndex(sourceString, subString, fromIndex)

    @staticmethod
    def findsubstringlastindex(sourceString: str, substring: str) -> FindSubstringLastIndex:
        """Get the last index of {{substring}} in {{sourceString}}.

        Returns the index within source string of the last occurrence of specified substring.
        """
        return FindSubstringLastIndex(sourceString, substring)

    @staticmethod
    def getstringsubstring(beginIndex: int, endIndex: int, inputString: str) -> GetStringSubstring:
        """Get substring of {{inputString}} from {{beginIndex}} to {{endIndex}}.

        Gets the substring from a string between start and end indexes.
        """
        return GetStringSubstring(beginIndex, endIndex, inputString)

    @staticmethod
    def insertstringinindex(inputString: str, index: int, stringToInsert: str) -> InsertStringInIndex:
        """Insert {{stringToInsert}} into {{inputString}} at {{index}}.

        Insert {{stringToInsert}} into {{inputString}} at {{index}}.
        """
        return InsertStringInIndex(inputString, index, stringToInsert)

    @staticmethod
    def isstringempty(string: str, expectedResult: bool) -> IsStringEmpty:
        """Checks if {{string}} is empty.

        Checks if a given string is empty.
        """
        return IsStringEmpty(string, expectedResult)

    @staticmethod
    def replacesubstringfirstocurrence(sourceString: str, regex: str, replacement: str) -> ReplaceSubstringFirstOcurrence:
        """Replace the first occurrence of {{regex}} with {{replacement}} in {{sourceString}}.

        Replaces the first substring of source string that match the given regular expression with the given replacement.
        """
        return ReplaceSubstringFirstOcurrence(sourceString, regex, replacement)

    @staticmethod
    def replacesubstrings(inputString: str, target: str, replacement: str) -> ReplaceSubstrings:
        """Replace all occurrences of {{target}} with {{replacement}} in {{inputString}}.

        Replaces all substrings in the input string.
        """
        return ReplaceSubstrings(inputString, target, replacement)

    @staticmethod
    def replacesubstringswithregex(sourceString: str, regex: str, replacement: str) -> ReplaceSubstringsWithRegex:
        """Replace all occurrences of {{regex}} with {{replacement}} in {{sourceString}}.

        Replaces all substrings of source string that match the given regular expression with the given replacement.
        """
        return ReplaceSubstringsWithRegex(sourceString, regex, replacement)

    @staticmethod
    def splitstringwithregex(sourceString: str, regex: str, limit: int, indexOfElement: str) -> SplitStringWithRegex:
        """Splits {{sourceString}} around matches of given regular expression {{regex}} limited by {{limit}}.

        Splits string around matches of given regular expression.
        """
        return SplitStringWithRegex(sourceString, regex, limit, indexOfElement)

    @staticmethod
    def stringcontains(inputString: str, substring: str, caseSensitive: bool, expectedResult: str) -> StringContains:
        """Is {{inputString}} contains {{substring}}?.

        Checks if the input string contains the given sequence.
        """
        return StringContains(inputString, substring, caseSensitive, expectedResult)

    @staticmethod
    def stringlength(inputString: str) -> StringLength:
        """Get the length of {{inputString}}.

        Returns the length of a given string.
        """
        return StringLength(inputString)

    @staticmethod
    def stringstartswith(sourceString: str, prefix: str, offset: int, expectedResult: bool) -> StringStartsWith:
        """Checks if {{sourceString}} starts with {{prefix}} starting from {{offset}}.

        Checks if string starts with given prefix.
        """
        return StringStartsWith(sourceString, prefix, offset, expectedResult)

    @staticmethod
    def transformcharacteratindex(input: str, lowerOrUpperCase: str, index: str) -> TransformCharacterAtIndex:
        """Change character at {{index}} to {{lowerOrUpperCase}}."""
        return TransformCharacterAtIndex(input, lowerOrUpperCase, index)

    @staticmethod
    def trimstring(sourceString: str) -> TrimString:
        """Trim {{sourceString}}.

        Returns new string after removing any leading and trailing whitespace.
        """
        return TrimString(sourceString)
