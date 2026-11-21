from __future__ import annotations
from datetime import datetime
from typing import Optional

from LivinGrimoirePacket.LivinGrimoire import *
from enum import Enum, auto
import calendar
import re
from math import sqrt
import random
import time
import datetime
from datetime import timedelta
from random import SystemRandom
from difflib import SequenceMatcher


# ╔════════════════════════════════════════════════════════════════════════╗
# ║ TABLE OF CONTENTS                                                      ║
# ╠════════════════════════════════════════════════════════════════════════╣
# ║ 1. STRING CONVERTERS                                                   ║
# ║ 2. UTILITY                                                             ║
# ║ 3. TRIGGERS                                                            ║
# ║ 4. SPECIAL SKILLS DEPENDENCIES                                         ║
# ║ 5. OUTPUT MANAGEMENT                                                   ║
# ║ 6. STATE MANAGEMENT                                                    ║
# ║ 7. LEARNABILITY                                                        ║
# ║ 8. MISCELLANEOUS                                                       ║
# ║ 9. UNDER USE                                                           ║
# ╚════════════════════════════════════════════════════════════════════════╝

# ╔══════════════════════════════════════════════════════════════════════╗
# ║     📜 TABLE OF CONTENTS — CLASS INDEX                               ║
# ╚══════════════════════════════════════════════════════════════════════╝

# ┌────────────────────────────┐
# │ 🧵 STRING CONVERTERS       │
# └────────────────────────────┘
# - AXFunnel
# - AXLMorseCode
# - AXNeuroSama
# - AXLHousing
# - AXLNeuroSama
# - AXStringSplit
# - PhraseInflector

# ┌────────────────────────────┐
# │ 🛠️ UTILITY                 │
# └────────────────────────────┘
# - TimeUtils
# - LGPointInt
# - distance (function)
# - LGPointFloat
# - enumRegexGrimoire
# - RegexUtil
# - CityMap
# - CityMapWithPublicTransport
# - StopWatch

# ┌────────────────────────────┐
# │ 🎯 TRIGGERS                │
# └────────────────────────────┘
# - MonthlyTrigger
# - CodeParser
# - TimeGate
# - LGFIFO
# - UniqueItemsPriorityQue
# - UniqueItemSizeLimitedPriorityQueue
# - RefreshQ
# - AnnoyedQ
# - TrgTolerance
# - AXCmdBreaker
# - AXContextCmd
# - AXInputWaiter
# - LGTypeConverter
# - DrawRnd
# - DrawRndDigits
# - AXPassword
# - TrgTime
# - Cron
# - AXStandBy
# - Cycler
# - TimeAccumulator
# - KeyWords
# - QuestionChecker
# - TrgMinute
# - TrgEveryNMinutes
# - OncePerDayGateV0
# - EveningGate
# - SimilarityScorer
# - TrueSprinkler
# - DailyEngager

# ┌──────────────────────────────────────────────┐
# │ 🧪 SPECIAL SKILLS DEPENDENCIES               │
# └──────────────────────────────────────────────┘
# - TimedMessages
# - AXLearnability
# - AlgorithmV2
# - SkillHubAlgDispenser
# - UniqueRandomGenerator
# - UniqueResponder
# - AXSkillBundle
# - AXGamification
# - Responder

# ┌────────────────────────────┐
# │ 🎛️ OUTPUT MANAGEMENT       │
# └────────────────────────────┘
# - LimUniqueResponder
# - WeightedResponder
# - PercentDripper
# - AXTimeContextResponder
# - Magic8Ball
# - Responder1Word

# ┌────────────────────────────┐
# │ 🧩 STATE MANAGEMENT        │
# └────────────────────────────┘
# - ButtonEngager
# - Differ

# ┌────────────────────────────┐
# │ 🧠 LEARNABILITY            │
# └────────────────────────────┘
# - SpiderSense
# - Strategy
# - Notes
# - Catche

# ┌────────────────────────────┐
# │ 🧿 MISCELLANEOUS           │
# └────────────────────────────┘
# - AXKeyValuePair
# - CombinatoricalUtils
# - AXNightRider

# ┌────────────────────────────┐
# │ 🚧 UNDER USE               │
# └────────────────────────────┘
# - DeepCopier
# - enumTimes
# - EmoDetectorCurious
# - EmoDetectorHappy
# - EmoDetectorStressed
# - Map
# - OutputDripper
# - getOrDefault (function)
# - DBAntiGlitch
# - Sarcophagus


# ╔════════════════════════════════════════════════════════════════════════╗
# ║                            STRING CONVERTERS                           ║
# ╚════════════════════════════════════════════════════════════════════════╝
# region STRING CONVERTERS

class AXFunnel:
    # funnel all sorts of strings to fewer or other strings
    def __init__(self, default: str = "default"):
        self.dic: dict[str, str] = {}
        self.default: str = default

    def setDefault(self, default: str):
        self.default = default

    def addKV(self, key: str, value: str) -> AXFunnel:
        # add key value pair
        self.dic[key] = value
        return self

    def addK(self, key: str) -> AXFunnel:
        # add key default pair
        self.dic[key] = self.default
        return self

    def funnel(self, key: str) -> str:
        # dictionary get or default(key)
        if key not in self.dic:
            return key
        return self.dic[key]

    def funnel_or_empty(self, key: str) -> str:
        # dictionary get or default("")
        if key not in self.dic:
            return ""
        return self.dic[key]


class AXLMorseCode:
    # A happy little Morse Code converter~! (◕‿◕✿)
    def __init__(self):
        self.morse_dict = {
            'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
            'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
            'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
            'M': '--',   'N': '-.',    'O': '---',   'P': '.--.',
            'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
            'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
            'Y': '-.--',  'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.',
            ' ': '/'
        }
        self.reverse_morse = {v: k for k, v in self.morse_dict.items()}

    def morse(self, text):
        # Converts text to Morse code! (◠‿◠)
        result = []
        for char in text.upper():
            if char in self.morse_dict:
                result.append(self.morse_dict[char])
        return ' '.join(result)

    def demorse(self, morse_code):
        # Converts Morse code back to text! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
        result = []
        for code in morse_code.split(' '):
            if code in self.reverse_morse:
                result.append(self.reverse_morse[code])
        return ''.join(result)


class AXNeuroSama:
    def __init__(self, rate: int):
        # the higher the rate the less likely to decorate outputs
        self._rate: int = rate
        self._nyaa: Responder = Responder(" heart", " heart", " wink", " heart heart heart")
        self._rnd: DrawRnd = DrawRnd()

    def decorate(self, output: str):
        if output == "":
            return output
        if self._rnd.getSimpleRNDNum(self._rate) == 0:
            return output + self._nyaa.getAResponse()
        return output


class AXLHousing:
    def decorate(self, str1: str) -> str:
        # override me
        return ""


class AXLNeuroSama(AXLHousing):
    def __init__(self):
        super().__init__()
        self._nyaa: AXNeuroSama = AXNeuroSama(3)

    def decorate(self, str1: str) -> str:
        return self._nyaa.decorate(str1)


class AXStringSplit:
    # may be used to prepare data before saving or after loading
    # the advantage is less data fields. for example: {skills: s1_s2_s3}
    def __init__(self):
        self._saparator: str = "_"

    def setSaparator(self, saparator: str):
        self._saparator = saparator

    def split(self, str1: str) -> list[str]:
        return str1.split(self._saparator)

    def stringBuilder(self, l1: list[str]) -> str:
        sTemp = self._saparator
        return sTemp.join(l1)


class PhraseInflector:
    # Maps for pronoun and verb inflection
    inflection_map = {
        "i": "you",
        "me": "you",
        "my": "your",
        "mine": "yours",
        "you": "i",  # Default inflection
        "your": "my",
        "yours": "mine",
        "am": "are",
        "are": "am",
        "was": "were",
        "were": "was",
        "i'd": "you would",
        "i've": "you have",
        "you've": "I have",
        "you'll": "I will"
    }

    @staticmethod
    def is_verb(word):
        verbs = {"am", "are", "was", "were", "have", "has", "had", "do", "does", "did"}
        return word in verbs

    @staticmethod
    def inflect_phrase(phrase):
        words = phrase.split()
        result = []

        for i, word in enumerate(words):
            lower_word = word.lower()
            inflected_word = word  # Default to original word

            # Check if word needs inflection
            if lower_word in PhraseInflector.inflection_map:
                inflected_word = PhraseInflector.inflection_map[lower_word]

                # Special case for "you"
                if lower_word == "you":
                    if i == len(words) - 1 or (i > 0 and PhraseInflector.is_verb(words[i - 1].lower())):
                        inflected_word = "me"
                    else:
                        inflected_word = "I"

            # Preserve capitalization
            if word[0].isupper():
                inflected_word = inflected_word.capitalize()

            result.append(inflected_word)

        return " ".join(result)


# endregion
# ╔════════════════════════════════════════════════════════════════════════╗
# ║                               UTILITY                                  ║
# ╚════════════════════════════════════════════════════════════════════════╝
# region UTILITY

class TimeUtils:
    week_days = {1: 'sunday',
                 2: 'monday',
                 3: 'tuesday',
                 4: 'wednesday',
                 5: 'thursday',
                 6: 'friday',
                 7: 'saturday',
                 }
    dayOfMonth = {1: "first of", 2: "second of", 3: "third of", 4: "fourth of", 5: "fifth of", 6: "sixth of",
                  7: "seventh of",
                  8: "eighth of", 9: "ninth of", 10: "tenth of", 11: "eleventh of", 12: "twelfth of",
                  13: "thirteenth of",
                  14: "fourteenth of", 15: "fifteenth of", 16: "sixteenth of", 17: "seventeenth of",
                  18: "eighteenth of",
                  19: "nineteenth of", 20: "twentieth of", 21: "twenty-first of", 22: "twenty-second of",
                  23: "twenty-third of",
                  24: "twenty-fourth of", 25: "twenty-fifth of", 26: "twenty-sixth of", 27: "twenty-seventh of",
                  28: "twenty-eighth of",
                  29: "twenty-ninth of", 30: "thirtieth of", 31: "thirty-first of"}

    @staticmethod
    def getCurrentTimeStamp() -> str:
        """This method returns the current time (hh:mm)"""
        right_now = datetime.datetime.now()
        temp_minute: int = right_now.minute
        tempstr: str
        if temp_minute < 10:
            tempstr = "0" + str(right_now.minute)
        else:
            tempstr = str(right_now.minute)
        return str(right_now.hour) + ":" + tempstr

    @staticmethod
    def getMonthAsInt() -> int:
        """This method returns the current month (MM)"""
        right_now = datetime.datetime.now()
        return right_now.month

    @staticmethod
    def getDayOfTheMonthAsInt() -> int:
        """This method returns the current day (dd)"""
        right_now = datetime.datetime.now()
        return right_now.day

    @staticmethod
    def getYearAsInt() -> int:
        """This method returns the current year (yyyy)"""
        right_now = datetime.datetime.now()
        return right_now.year

    @staticmethod
    def getDayAsInt() -> int:
        """This method returns the current day of the week (1, 2, ... 7)"""
        right_now = datetime.datetime.now()
        return right_now.isoweekday()

    @staticmethod
    def getMinutes() -> str:
        """This method returns the current minutes (mm)"""
        right_now = datetime.datetime.now()
        return str(right_now.minute)

    @staticmethod
    def getSeconds() -> str:
        """This method returns the current seconds (ss)"""
        right_now = datetime.datetime.now()
        return str(right_now.second)

    @staticmethod
    def getDayOfDWeek() -> str:
        """This method returns the current day of the week as a word (monday, ...)"""
        right_now = datetime.datetime.now()
        return calendar.day_name[right_now.weekday()]

    @staticmethod
    def translateMonthDay(day: int) -> str:
        """This method returns the current day of the month as a word (first_of, ...)"""
        return TimeUtils.dayOfMonth.get(day, "")

    @staticmethod
    def getSpecificTime(time_variable: enumTimes) -> str:
        """This method returns the current specific date in words (eleventh_of June 2021, ...)"""
        enum_temp = time_variable.name
        if enum_temp == "DATE":
            right_now = datetime.datetime.now()
            output = TimeUtils.translateMonthDay(right_now.day) + " " + calendar.month_name[
                right_now.month] + " " + str(
                right_now.year)
        elif enum_temp == "HOUR":
            output = str(datetime.datetime.now().hour)
        elif enum_temp == "SECONDS":
            output = str(datetime.datetime.now().second)
        elif enum_temp == "MINUTES":
            output = str(datetime.datetime.now().minute)
        elif enum_temp == "YEAR":
            output = str(datetime.datetime.now().year)
        else:
            output = ""
        return output

    @staticmethod
    def getSecondsAsInt() -> int:
        """This method returns the current seconds"""
        right_now = datetime.datetime.now()
        return right_now.second

    @staticmethod
    def getMinutesAsInt() -> int:
        """This method returns the current minutes"""
        right_now = datetime.datetime.now()
        return right_now.minute

    @staticmethod
    def getHoursAsInt() -> int:
        """This method returns the current hour"""
        right_now = datetime.datetime.now()
        return right_now.hour

    @staticmethod
    def getFutureInXMin(extra_minutes: int) -> str:
        """This method returns the date in x minutes"""
        right_now = datetime.datetime.now()
        final_time = right_now + datetime.timedelta(minutes=extra_minutes)
        s1: str = str(final_time)
        s1 = RegexUtil.extractEnumRegex(enumRegexGrimoire.simpleTimeStamp, s1)
        if s1[0] == '0':
            s1 = s1[1:]
        return s1

    @staticmethod
    def getPastInXMin(less_minutes: int) -> str:
        """This method returns the date x minutes before"""
        right_now = datetime.datetime.now()
        final_time = right_now - datetime.timedelta(minutes=less_minutes)
        s1: str = str(final_time)
        s1 = RegexUtil.extractEnumRegex(enumRegexGrimoire.simpleTimeStamp, s1)
        if s1[0] == '0':
            s1 = s1[1:]
        return s1

    @staticmethod
    def getFutureHour(startHour: int, addedHours: int) -> int:
        """This method returns the hour in x hours from the starting hour"""
        return (startHour + addedHours) % 24

    @staticmethod
    def getFutureFromXInYMin(to_add: int, start: str) -> str:
        """This method returns the time (hh:mm) in x minutes the starting time (hh:mm)"""
        values = start.split(":")
        times_to_add = (int(values[1]) + to_add) // 60
        new_minutes = (int(values[1]) + to_add) % 60
        new_time = str((int(values[0]) + times_to_add) % 24) + ":" + str(new_minutes)
        return new_time

    @staticmethod
    def timeInXMinutes(x: int) -> str:
        """This method returns the time (hh:mm) in x minutes"""
        right_now = datetime.datetime.now()
        final_time = right_now + datetime.timedelta(minutes=x)
        return f"{final_time.hour:02}:{final_time.minute:02}"

    @staticmethod
    def isDayTime() -> bool:
        """This method returns true if it's daytime (6-18)"""
        return 5 < datetime.datetime.now().hour < 19

    @staticmethod
    def smallToBig(*a) -> bool:
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                return False
        return True

    @staticmethod
    def partOfDay() -> str:
        """This method returns which part of the day it is (morning, ...)"""
        hour: int = TimeUtils.getHoursAsInt()
        if TimeUtils.smallToBig(5, hour, 12):
            return "morning"
        elif TimeUtils.smallToBig(11, hour, 17):
            return "afternoon"
        elif TimeUtils.smallToBig(16, hour, 21):
            return "evening"
        return "night"

    @staticmethod
    def convertToDay(number: int) -> str:
        """This method converts the week number to the weekday name"""
        return TimeUtils.week_days.get(number, "")

    @staticmethod
    def isNight() -> bool:
        """This method returns true if it's night (21-5)"""
        hour: int = TimeUtils.getHoursAsInt()
        return hour > 20 or hour < 6

    @staticmethod
    def getTomorrow() -> str:
        """This method returns tomorrow"""
        right_now = datetime.datetime.now()
        if right_now.weekday() == 6:
            return "sunday"
        return calendar.day_name[right_now.weekday() + 1]

    @staticmethod
    def getYesterday() -> str:
        """This method returns yesterday"""
        right_now = datetime.datetime.now()
        if right_now.weekday == 0:
            return "Sunday"
        return calendar.day_name[right_now.weekday() - 1]

    @staticmethod
    def getGMT() -> int:
        """This method returns the local GMT"""
        right_now = datetime.datetime.now()
        timezone = int(str(right_now.astimezone())[-6:-3])
        return timezone

    @staticmethod
    def getCurrentMonthName() -> str:
        month: int = TimeUtils.getMonthAsInt()
        match month:
            case 1:
                return "january"
            case 2:
                return "february"
            case 3:
                return "march"
            case 4:
                return "april"
            case 5:
                return "may"
            case 6:
                return "june"
            case 7:
                return "july"
            case 8:
                return "august"
            case 9:
                return "november"
            case 10:
                return "october"
            case 11:
                return "november"
            case 12:
                return "december"
        return ""

    @staticmethod
    def getCurrentMonthDay():
        return TimeUtils.dayOfMonth.get(TimeUtils.getDayOfTheMonthAsInt(), "")

    @staticmethod
    def getLocal() -> str:
        """This method returns the local time zone"""
        return f'{datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo}'

    @staticmethod
    def findDay(month: int, day: int, year: int) -> str:
        # get weekday from date
        if day > 31:
            return ""
        # april, june, sep, nov case:
        if day > 30:
            if (month == 4) or (month == 6) or (month == 9) or (month == 11):
                return ""
        # feb case:
        if month == 2:
            if TimeUtils.isLeapYear(year):
                if day > 29:
                    return ""
            if day > 28:
                return ""
        return datetime.date(year, month, day).strftime("%A").lower()

    @staticmethod
    def nxtDayOnDate(dayOfMonth: int) -> str:
        # get the weekday on the next dayOfMonth
        today: int = TimeUtils().getDayOfTheMonthAsInt()
        if today <= dayOfMonth:
            return TimeUtils.findDay(TimeUtils().getMonthAsInt(), dayOfMonth, TimeUtils().getYearAsInt())
        elif not (TimeUtils().getMonthAsInt() == 12):
            return TimeUtils.findDay(TimeUtils().getMonthAsInt() + 1, dayOfMonth, TimeUtils().getYearAsInt())
        return TimeUtils.findDay(1, dayOfMonth, TimeUtils().getYearAsInt() + 1)

    @staticmethod
    def isLeapYear(year: int):
        # divisible by 4
        isLeapyear: bool = year % 4 == 0
        # divisible by 4, not by 100, or divisible by 400
        return isLeapyear and (year % 100 != 0 or year % 400 == 0)


class LGPointInt:
    def __init__(self, x_init: int, y_init: int):
        self.x: int = x_init
        self.y: int = y_init

    def shift(self, x: int, y: int):
        self.x += x
        self.y += y

    def setPosition(self, x: int, y: int):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])


def distance(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


class LGPointFloat:
    def __init__(self, x_init: float, y_init: float):
        self.x: float = x_init
        self.y: float = y_init

    def shift(self, x: float, y: float):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    @staticmethod
    def distance(a, b):
        return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


class enumRegexGrimoire(Enum):
    email = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,6}"
    timeStamp = "[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}"
    simpleTimeStamp = "[0-9]{1,2}:[0-9]{1,2}"
    integer = "[-+]?[0-9]{1,13}"
    double_num = "[-+]?[0-9]*[.,][0-9]*"
    repeatedWord = "\\b([\\w\\s']+) \\1\\b"
    phone = "[0]\\d{9}"
    trackingID = "[A-Z]{2}[0-9]{9}[A-Z]{2}"
    IPV4 = "([0-9].){4}[0-9]*"
    domain = "[A-Za-z0-9.-]+\\.[A-Za-z]{2,6}"
    number = "\\d+(\\.\\d+)?"
    secondlessTimeStamp = "[0-9]{1,2}:[0-9]{1,2}"
    date = "[0-9]{1,4}/[0-9]{1,2}/[0-9]{1,2}"
    fullDate = "[0-9]{1,4}/[0-9]{1,2}/[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}"
    duplicatWord = "\\b(\\w+)\\b(?=.*\\b\\1\\b)"
    firstWord = "^\\w+"
    lastWord = "\\w+$"
    surname = "\\s+[^\\s]+"
    realNumber = "[-+]?[0-9]*[.,][0-9]*"  # -30.77 / 40.05
    numberStripper = "[^\\d]+"


''' REGEXUTIL CLASS'''


# returns expression of type theRegex from the string str2Check
class RegexUtil:
    @staticmethod
    def extractRegex(theRegex: str, str2Check: str) -> str:
        regexMatcher = re.search(theRegex, str2Check)
        if regexMatcher is not None:
            return regexMatcher.group(0).strip()
        return ""

    @staticmethod
    def extractEnumRegex(theRegex: enumRegexGrimoire, str2Check: str) -> str:
        # example usage:
        # print(regexUtil.extractEnumRegex(enumRegexGrimoire.domain,"the site is creamedcorn.com ok?"))
        regexMatcher = re.search(theRegex.value.__str__(), str2Check)
        if regexMatcher is not None:
            return regexMatcher.group(0).strip()
        return ""

    @staticmethod
    def extractAllRegexes(theRegex: str, str2Check: str) -> list[str]:
        p = re.compile(theRegex)
        return p.findall(str2Check)
        # mylist: list[str] = str2Check.split()
        # r = re.compile(theRegex)
        # l_final = list(filter(r.match, mylist))
        # return l_final

    @staticmethod
    def extractAllEnumRegexes(theRegex: enumRegexGrimoire, str2Check: str) -> list[str]:
        # return a list of all matches
        p = re.compile(theRegex.value.__str__())
        return p.findall(str2Check)

    @staticmethod
    def pointRegex(str2Check: str) -> LGPointInt:
        # "[-+]?[0-9]{1,13}(\\.[0-9]*)?" for double numbers
        theRegex: str = "[-+]?[0-9]{1,13}"
        result: LGPointInt = LGPointInt(0, 0)
        regexMatcher = re.search(theRegex, str2Check)
        if regexMatcher is not None:
            result.y = int(regexMatcher.group(0).strip())
        str2Check = str2Check[str2Check.index(f'{result.y}') + 1:len(str2Check)]
        phase2 = str2Check
        phase2 = RegexUtil.extractEnumRegex(enumRegexGrimoire.integer, phase2)
        if phase2 == "":
            return LGPointInt(result.y, 0)

        result.x = int(phase2)
        return LGPointInt(result.y, result.x)

    @staticmethod
    def afterWord(word: str, str2Check: str) -> str:
        # return a list of all matches
        theRegex = r"(?<=" + word + r")(.*)"
        regexMatcher = re.search(theRegex, str2Check)
        if regexMatcher is not None:
            return regexMatcher.group(0).strip()
        return ""


class CityMap:
    def __init__(self, n: int):
        self.streets: dict[str, deque[str]] = {}
        self.n: int = n
        self.lastInp:str = "standby"

    def add_street(self, current_street: str, new_street: str) -> None:
        if current_street not in self.streets:
            self.streets[current_street] = deque(maxlen=self.n)
        if len(new_street) == 0:
            return
        if new_street not in self.streets:
            self.streets[new_street] = deque(maxlen=self.n)

        self.streets[current_street].append(new_street)
        self.streets[new_street].append(current_street)

    def add_streets_from_string(self, current_street: str, streets_string: str) -> None:
        streets = streets_string.split('_')
        for street in streets:
            self.add_street(current_street, street)

    def learn(self, inp: str):
        if inp == self.lastInp:
            return
        self.add_street(self.lastInp, inp)
        self.lastInp = inp

    def find_path(self, start_street: str, goal_street: str, avoid_street: str, max_length: int = 4) -> list[str]:
        if start_street not in self.streets:
            return []
        queue: deque[tuple[str, list[str]]] = deque([(start_street, [start_street])])
        visited: set[str] = {start_street}
        while queue:
            current_street, path = queue.popleft()
            if len(path) > max_length:
                return []
            if current_street == goal_street:
                return path
            for neighbor in self.streets[current_street]:
                if neighbor not in visited and neighbor != avoid_street:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)
        return []

    def get_random_street(self, current_street: str) -> str:
        if current_street in self.streets and self.streets[current_street]:
            return random.choice(list(self.streets[current_street]))
        return ""

    def get_streets_string(self, street: str) -> str:
        if street in self.streets and self.streets[street]:
            return '_'.join(self.streets[street])
        return ""

    def get_first_street(self, current_street: str) -> str:
        if current_street in self.streets and self.streets[current_street]:
            return self.streets[current_street][0]
        return ""

    @staticmethod
    def create_city_map_from_path(path: list[str]) -> 'CityMap':
        new_city_map = CityMap(n=1)
        for i in range(len(path) - 1):
            new_city_map.add_street(path[i], path[i + 1])
        return new_city_map

    def find_path_with_must(self, start_street: str, goal_street: str, street_must: str, max_length: int = 4) -> list[
        str]:
        if start_street not in self.streets or street_must not in self.streets or goal_street not in self.streets:
            return []

        # Find path from start_street to street_must
        path_to_must = self.find_path(start_street, street_must, avoid_street="", max_length=max_length)
        if not path_to_must:
            return []

        # Find path from street_must to goal_street
        path_from_must = self.find_path(street_must, goal_street, avoid_street="", max_length=max_length)
        if not path_from_must:
            return []

        # Combine paths, ensuring street_must is not duplicated
        return path_to_must + path_from_must[1:]


class CityMapWithPublicTransport:
    def __init__(self, n: int):
        self.streets: dict[str, deque[str]] = {}  # Walking connections (street ↔ street or street ↔ bus stop)
        self.transport_lines: dict[str, list[str]] = {}  # Bus/train lines: {"Bus1": ["StopA", "StopB", ...]}
        self.n: int = n  # Max connections per street
        self.lastInp: str = "standby"

    def add_street(self, current_street: str, new_street: str) -> None:
        """Add a bidirectional walking connection between two streets (or a street and a bus stop)."""
        if current_street not in self.streets:
            self.streets[current_street] = deque(maxlen=self.n)
        if new_street not in self.streets:
            self.streets[new_street] = deque(maxlen=self.n)
        self.streets[current_street].append(new_street)
        self.streets[new_street].append(current_street)

    def add_transport_line(self, line_name: str, stops: list[str]) -> None:
        """Add a transport line (e.g., "Bus1" with stops ["StopA", "StopB"])."""
        self.transport_lines[line_name] = stops
        # Connect stops sequentially (bidirectional)
        for i in range(len(stops) - 1):
            self.add_street(stops[i], stops[i+1])

    def find_path(
        self,
        start: str,
        goal: str,
        avoid: Optional[str] = None,
        max_length: int = 4,
        use_transport: bool = True
    ) -> list[str]:
        """
        Finds a path using walking + transport (if enabled).
        Returns a list like ["StreetA", "StopX", "StopY", "StreetB"].
        """
        queue = deque([(start, [start], "walk")])  # (current, path, mode)
        visited = {(start, "walk")}  # Track (node, mode) to avoid loops

        while queue:
            current, path, mode = queue.popleft()

            if len(path) > max_length:
                continue  # Skip if path too long

            if current == goal:
                return path  # Found!

            # Explore walking neighbors (streets + adjacent bus stops)
            for neighbor in self.streets.get(current, []):
                if neighbor == avoid:
                    continue
                if (neighbor, "walk") not in visited:
                    visited.add((neighbor, "walk"))
                    queue.append((neighbor, path + [neighbor], "walk"))

            # Explore transport lines (if enabled and current is a stop)
            if use_transport:
                for line, stops in self.transport_lines.items():
                    if current in stops:
                        idx = stops.index(current)
                        # Next stop in line
                        if idx + 1 < len(stops):
                            next_stop = stops[idx + 1]
                            if (next_stop, line) not in visited:
                                visited.add((next_stop, line))
                                queue.append((next_stop, path + [next_stop], line))
                        # Previous stop in line (bidirectional)
                        if idx - 1 >= 0:
                            prev_stop = stops[idx - 1]
                            if (prev_stop, line) not in visited:
                                visited.add((prev_stop, line))
                                queue.append((prev_stop, path + [prev_stop], line))
        return []  # No path found


class StopWatch:
    """stop watch class with proper encapsulation"""

    def __init__(self):
        self._start_time = None
        self._paused_elapsed = 0.0
        self._is_paused = False
        self._is_running = False

    def start_timer(self):
        self._start_time = time.perf_counter()
        self._paused_elapsed = 0.0
        self._is_paused = False
        self._is_running = True

    def pause_timer(self):
        if self._is_running and not self._is_paused:
            self._paused_elapsed += time.perf_counter() - self._start_time
            self._is_paused = True

    def resume_timer(self):
        if self._is_running and self._is_paused:
            self._start_time = time.perf_counter()
            self._is_paused = False

    def reset_timer(self):
        self._is_running = False
        self._is_paused = False
        self._paused_elapsed = 0.0
        self._start_time = None

    def is_running(self):
        """Return True if timer is running (not paused and not stopped)."""
        return self._is_running

    def is_paused(self):
        """Return True if timer is paused."""
        return self._is_paused

    def get_current_seconds(self):
        """Get raw total seconds elapsed."""
        if not self._is_running:
            return 0

        if self._is_paused:
            return self._paused_elapsed

        return self._paused_elapsed + (time.perf_counter() - self._start_time)

    def get_time_elapsed(self):
        """Get formatted elapsed time as string."""
        total_seconds = self.get_current_seconds()

        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)

        parts = []
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        if seconds > 0 or not parts:
            parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")

        return " ".join(parts)


# endregion
# ╔════════════════════════════════════════════════════════════════════════╗
# ║                               TRIGGERS                                 ║
# ╚════════════════════════════════════════════════════════════════════════╝
# region TRIGGERS

class MonthlyTrigger:
    def __init__(self, day=1,hour=22,minute = 35):
        self.last_run_month = None
        self.d = day
        self.h = hour
        self.minute = minute

    def tick(self):
        now = datetime.datetime.now()

        # Check date + time
        if now.day == self.d and now.hour == self.h and now.minute == self.minute:
            # Ensure it runs only once per month
            if self.last_run_month != now.month:
                self.last_run_month = now.month
                return True
        return False


class CodeParser:
    @staticmethod
    def extract_code_number(s):
        match = re.fullmatch(r"code (\d+)", s)
        if match:
            return int(match.group(1))
        return -1


class TimeGate:
    # a gate that only opens x minutes after it has been set

    def __init__(self, minutes: int) -> None:
        self.pause = max(1, minutes)
        epsilon = datetime.timedelta(microseconds=100)
        now = datetime.datetime.now()
        self.openedGate: datetime.datetime = now - epsilon
        self.checkPoint: datetime.datetime = now

    def isClosed(self) -> bool:
        return self.openedGate < datetime.datetime.now()

    def isOpen(self) -> bool:
        return not self.isClosed()

    def open(self, minutes: int):
        self.openedGate = datetime.datetime.now() + datetime.timedelta(minutes=minutes)

    def open_for_n_seconds(self, seconds: int):
        self.openedGate = datetime.datetime.now() + datetime.timedelta(seconds=seconds)

    def openForPauseMinutes(self):
        self.openedGate = datetime.datetime.now() + datetime.timedelta(minutes=self.pause)

    def setPause(self, pause: int):
        if 0 < pause < 60:
            self.pause = pause

    def resetCheckPoint(self):
        self.checkPoint = datetime.datetime.now()

    def getRunTimeTimeDifInSecondes(self) -> int:
        diff: datetime.timedelta = self.checkPoint - datetime.datetime.now()
        return int(diff.total_seconds())

    def close(self):
        self.openedGate = datetime.datetime.now()


# A simple implementation of Priority Queue
# using Queue.

class LGFIFO:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    def peak(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def poll(self):
        if not len(self.queue) == 0:
            result0 = self.queue[0]
            del self.queue[0]
            return result0
        return None

    def size(self) -> int:
        return len(self.queue)

    def clear(self):
        self.queue.clear()

    def removeItem(self, item):
        if self.queue.__contains__(item):
            self.queue.remove(item)

    def getRNDElement(self):
        if self.isEmpty():
            return None
        else:
            return self.queue[random.randint(0, len(self.queue) - 1)]

    def contains(self, item) -> bool:
        return self.queue.__contains__(item)


class UniqueItemsPriorityQue(LGFIFO):
    # a priority queue without repeating elements
    # override
    def insert(self, data):
        if not self.queue.__contains__(data):
            self.queue.append(data)

    # override
    def peak(self) -> str:
        # returns string
        temp = super().peak()
        if temp is None:
            return ""
        return temp

    def strContainsResponse(self, item: str) -> bool:
        for response in self.queue:
            if len(response) == 0:
                continue
            if item.__contains__(response):
                return True
        return False


class UniqueItemSizeLimitedPriorityQueue(UniqueItemsPriorityQue):
    # items in the queue are unique and do not repeat
    # the size of the queue is limited
    # this cls can also be used to detect repeated elements (nagging or reruns)
    def __init__(self, limit: int):
        super().__init__()
        self._limit = limit

    def getLimit(self) -> int:
        return self._limit

    def setLimit(self, limit: int):
        self._limit = limit

    # override
    def insert(self, data):
        if super().size() == self._limit:
            super().poll()
        super().insert(data)

    # override
    def poll(self):
        # returns string
        temp = super().poll()
        if temp is None:
            return ""
        return temp

    # override
    def getRNDElement(self):
        temp = super().getRNDElement()
        if temp is None:
            return ""
        return temp

    def getAsList(self) -> list[str]:
        return self.queue


class RefreshQ(UniqueItemSizeLimitedPriorityQueue):
    def __init__(self, limit: int):
        super().__init__(limit)

    def removeItem(self, item: str):
        super().getAsList().remove(item)

    def insert(self, data):
        # FILO 1st in last out
        if super().contains(data):
            self.removeItem(data)
        super().insert(data)

    def stuff(self, data):
        # FILO 1st in last out
        if super().size() == self._limit:
            super().poll()
        self.queue.append(data)


class AnnoyedQ:

    def __init__(self, queLim: int):
        self._q1: RefreshQ = RefreshQ(queLim)
        self._q2: RefreshQ = RefreshQ(queLim)
        self._stuffedQue: RefreshQ = RefreshQ(queLim)

    def learn(self, ear: str):
        if self._q1.contains(ear):
            self._q2.insert(ear)
            self._stuffedQue.stuff(ear)
            return
        self._q1.insert(ear)

    def isAnnoyed(self, ear: str) -> bool:
        return self._q2.strContainsResponse(ear)

    def reset(self):
        # Insert unique throwaway strings to reset the state
        for i in range(self._q1.getLimit()):
            self.learn(f"throwaway_string_{i}")

    def AnnoyedLevel(self, ear: str, level: int) -> bool:
        return self._stuffedQue.queue.count(ear) > level


class TrgTolerance:
    # this boolean gate will return true till depletion or reset()
    def __init__(self, maxrepeats: int):
        self._maxrepeats: int = maxrepeats
        self._repeates: int = 0

    def setMaxRepeats(self, maxRepeats: int):
        self._maxrepeats = maxRepeats
        self.reset()

    def reset(self):
        # refill trigger
        self._repeates = self._maxrepeats

    def trigger(self) -> bool:
        # will return true till depletion or reset()
        self._repeates -= 1
        if self._repeates > 0:
            return True
        return False

    def disable(self):
        self._repeates = 0


class AXCmdBreaker:
    def __init__(self, conjuration: str):
        self.conjuration: str = conjuration

    def extractCmdParam(self, s1: str) -> str:
        if self.conjuration in s1:
            return s1.replace(self.conjuration, "").strip()
        return ""


class AXContextCmd:
    # engage on commands
    # when commands are engaged, context commands can also engage
    def __init__(self):
        self.commands: UniqueItemSizeLimitedPriorityQueue = UniqueItemSizeLimitedPriorityQueue(5)
        self.contextCommands: UniqueItemSizeLimitedPriorityQueue = UniqueItemSizeLimitedPriorityQueue(5)
        self.trgTolerance: bool = False

    def engageCommand(self, s1: str) -> bool:
        if len(s1) == 0:
            return False
        # active context
        if self.contextCommands.contains(s1):
            self.trgTolerance = True
            return True
        # exit context:
        if self.trgTolerance and not self.commands.contains(s1):
            self.trgTolerance = False
            return False
        return self.trgTolerance

    def engageCommandRetInt(self, s1: str) -> int:
        if len(s1) == 0:
            return 0
        # active context
        if self.contextCommands.contains(s1):
            self.trgTolerance = True
            return 1
        # exit context:
        if self.trgTolerance and not self.commands.contains(s1):
            self.trgTolerance = False
            return 0
        if self.trgTolerance:
            return 2
        return 0

    def disable(self):
        # context commands are disabled till next engagement with a command
        self.trgTolerance = False


class AXInputWaiter:
    # wait for any input
    def __init__(self, tolerance: int):
        self._trgTolerance: TrgTolerance = TrgTolerance(tolerance)
        self._trgTolerance.reset()

    def reset(self):
        self._trgTolerance.reset()

    def wait(self, s1: str) -> bool:
        # return true till any input detected or till x times of no input detection
        if not s1 == "":
            self._trgTolerance.disable()
            return False
        return self._trgTolerance.trigger()

    def setWait(self, timesToWait: int):
        self._trgTolerance.setMaxRepeats(timesToWait)


class LGTypeConverter:
    @staticmethod
    def convertToInt(v1: str) -> int:
        temp: str = RegexUtil.extractEnumRegex(enumRegexGrimoire.integer, v1)
        if temp == "":
            return 0
        return int(temp)

    @staticmethod
    def convertToDouble(v1: str) -> float:
        temp: str = RegexUtil.extractEnumRegex(enumRegexGrimoire.double_num, v1)
        if temp == "":
            return 0.0
        return float(temp)

    @staticmethod
    def convertToFloat(v1: str) -> float:
        temp: str = RegexUtil.extractEnumRegex(enumRegexGrimoire.double_num, v1)
        if temp == "":
            return 0
        return float(temp)

    @staticmethod
    def convertToFloatV2(v1: str, precision: int) -> float:
        # precision: how many numbers after the .
        temp: str = RegexUtil.extractEnumRegex(enumRegexGrimoire.double_num, v1)
        if temp == "":
            return 0
        return round(float(temp), precision)


class DrawRnd:
    # draw a random element, then take said element out
    def __init__(self, *values: str):
        self.strings: LGFIFO = LGFIFO()
        self._stringsSource: list[str] = []
        for i in range(0, len(values)):
            self.strings.insert(values[i])
            self._stringsSource.append(values[i])

    def addElement(self, element: str):
        self.strings.insert(element)
        self._stringsSource.append(element)

    def drawAndRemove(self) -> str:
        if len(self.strings.queue) == 0:
            return ""
        temp: str = self.strings.getRNDElement()
        self.strings.removeItem(temp)
        return temp

    def drawAsIntegerAndRemove(self) -> int:
        temp: str = self.strings.getRNDElement()
        if temp is None:
            return 0
        self.strings.removeItem(temp)
        return LGTypeConverter.convertToInt(temp)

    @staticmethod
    def getSimpleRNDNum(lim: int) -> int:
        return random.randint(0, lim)

    def reset(self):
        self.strings.clear()
        for t in self._stringsSource:
            self.strings.insert(t)

    def isEmptied(self) -> bool:
        return self.strings.size() == 0

    def renewableDraw(self) -> str:
        if len(self.strings.queue) == 0:
            self.reset()
        temp: str = self.strings.getRNDElement()
        self.strings.removeItem(temp)
        return temp


class DrawRndDigits:
    # draw a random integer, then take said element out
    def __init__(self, *values: int):
        self.strings: LGFIFO = LGFIFO()
        self._stringsSource: list[int] = []
        for i in range(0, len(values)):
            self.strings.insert(values[i])
            self._stringsSource.append(values[i])

    def addElement(self, element: int):
        self.strings.insert(element)
        self._stringsSource.append(element)

    def drawAndRemove(self) -> int:
        temp: int = self.strings.getRNDElement()
        self.strings.removeItem(temp)
        return temp

    @staticmethod
    def getSimpleRNDNum(lim: int) -> int:
        return random.randint(0, lim)

    def reset(self):
        self.strings.clear()
        for t in self._stringsSource:
            self.strings.insert(t)

    def isEmptied(self) -> bool:
        return self.strings.size() == 0

    def resetIfEmpty(self):
        if len(self.strings.queue) == 0:
            self.reset()

    def containsElement(self, element: int) -> bool:
        return self._stringsSource.__contains__(element)

    def CurrentlyContainsElement(self, element: int) -> bool:
        return self.strings.contains(element)

    def removeItem(self, element: int):
        if self.strings.contains(element):
            self.strings.removeItem(element)


class AXPassword:
    """ code # to open the gate
     while gate is open, code can be changed with: code new_number"""

    def __init__(self):
        self._isOpen: bool = False
        self._maxAttempts: int = 3
        self._loginAttempts = self._maxAttempts
        self._code = 0

    def codeUpdate(self, ear: str) -> bool:
        # while the gate is toggled on, the password code can be changed
        if not self._isOpen:
            return False
        if ear.__contains__("code"):
            temp: str = RegexUtil.extractEnumRegex(enumRegexGrimoire.integer, ear)
            if not temp == "":
                # if not temp.isEmpty
                self._code = int(temp)
                return True
        return False

    def openGate(self, ear: str):
        if ear.__contains__("code") and self._loginAttempts > 0:
            tempCode: str = RegexUtil.extractEnumRegex(enumRegexGrimoire.integer, ear)
            if not tempCode == "":
                code_x: int = int(tempCode)
                if code_x == self._code:
                    self._loginAttempts = self._maxAttempts
                    self._isOpen = True
                else:
                    self._loginAttempts -= 1

    def isOpen(self):
        return self._isOpen

    def resetAttempts(self):
        # should happen once a day or hour to prevent hacking
        self._loginAttempts = self._maxAttempts

    def getLoginAttempts(self):
        # return remaining login attempts
        return self._loginAttempts

    def closeGate(self):
        self._isOpen = False

    def closeGateV2(self, ear: str):
        if ear.__contains__("close"):
            self._isOpen = False

    def setMaxAttempts(self, maximum: int):
        self._maxAttempts = maximum

    def getCode(self) -> int:
        if self._isOpen:
            return self._code
        return -1

    def randomizeCode(self, lim: int, minimumLim: int):
        # event feature
        self._code = DrawRnd().getSimpleRNDNum(lim) + minimumLim

    def getCodeEvent(self) -> int:
        # event feature
        # get the code during weekly/monthly event after it has been randomized
        return self._code


class TrgTime:
    def __init__(self):
        super().__init__()
        self._t = "null"
        self._alarm: bool = True

    def setTime(self, v1: str):
        if v1.startswith("0"):
            v1 = v1[1:]
        self._t = RegexUtil.extractEnumRegex(enumRegexGrimoire.simpleTimeStamp, v1)

    def alarm(self) -> bool:
        now: str = TimeUtils.getCurrentTimeStamp()
        if self._alarm:
            if now == self._t:
                self._alarm = False
                return True
        if now != self._t:
            self._alarm = True
        return False


class Cron:
    # triggers true, limit times, after initial time, and every minutes interval
    # counter resets at initial time, assuming trigger method was run
    def __init__(self, startTime: str, minutes: int, limit: int):
        self._minutes: int = minutes  # minute interval between triggerings
        self._timeStamp = startTime
        self._initislTimeStamp = startTime
        self._trgTime: TrgTime = TrgTime()
        self._trgTime.setTime(startTime)
        self._counter: int = 0
        self._limit: int = limit
        if limit < 1:
            self._limit = 1

    def setMinutes(self, minutes: int):
        if minutes > -1:
            self._minutes = minutes

    def getLimit(self) -> int:
        return self._limit

    def setLimit(self, limit: int):
        if limit > 0:
            self._limit = limit

    def getCounter(self) -> int:
        return self._counter

    # override
    def trigger(self) -> bool:
        # delete counter = 0 if you don't want the trigger to work the next day
        if self._counter == self._limit:
            self._trgTime.setTime(self._initislTimeStamp)
            self._counter = 0
            return False
        if self._trgTime.alarm():
            self._timeStamp = TimeUtils.getFutureInXMin(self._minutes)
            self._trgTime.setTime(self._timeStamp)
            self._counter += 1
            return True
        return False

    def triggerWithoutRenewal(self) -> bool:
        if self._counter == self._limit:
            self._trgTime.setTime(self._initislTimeStamp)
            return False
        if self._trgTime.alarm():
            self._timeStamp = TimeUtils.getFutureInXMin(self._minutes)
            self._trgTime.setTime(self._timeStamp)
            self._counter += 1
            return True
        return False

    # override
    def reset(self):
        # manual trigger reset
        self._counter = 0

    def setStartTime(self, t1: str):
        self._initislTimeStamp = t1
        self._timeStamp = t1
        self._trgTime.setTime(t1)
        self._counter = 0

    def turnOff(self):
        self._counter = self._limit


class AXStandBy:
    def __init__(self, pause: int):
        self._tg:TimeGate = TimeGate(pause)
        self._tg.openForPauseMinutes()

    def standBy(self, ear: str) -> bool | None:
        # only returns true after pause minutes of no input
        if len(ear) > 0:
            # restart count
            self._tg.openForPauseMinutes()
            return False
        if self._tg.isClosed():
            # time out without input, stand by is true
            self._tg.openForPauseMinutes()
            return True
        return False


class Cycler:
    # cycles through numbers limit to 0 non-stop
    def __init__(self, limit: int):
        self.limit: int = limit
        self._cycler: int = limit

    def cycleCount(self) -> int:
        self._cycler -= 1
        if self._cycler < 0:
            self._cycler = self.limit
        return self._cycler

    def reset(self):
        self._cycler = self.limit

    def setToZero(self):
        self._cycler = 0

    def sync(self, n: int):
        if n < -1 or n > self.limit:
            return
        self._cycler = n

    def getMode(self) -> int:
        return self._cycler


class TimeAccumulator:
    # accumulator ++ each tick minutes interval
    def __init__(self, tick: int):
        # accumulation ticker
        self._timeGate: TimeGate = TimeGate(tick)
        self._accumulator: int = 0
        self._timeGate.openForPauseMinutes()

    def setTick(self, tick: int):
        self._timeGate.setPause(tick)

    def getAccumulator(self) -> int:
        return self._accumulator

    def reset(self):
        self._accumulator = 0

    def tick(self):
        if self._timeGate.isClosed():
            self._timeGate.openForPauseMinutes()
            self._accumulator += 1

    def decAccumulator(self):
        if self._accumulator > 0:
            self._accumulator -= 1


class KeyWords:
    def __init__(self, *keywords):
        # Initialize a set to store the keywords
        self.hash_set = set(keywords)

    # Method to add keywords to the hash_set
    def add_keyword(self, keyword):
        self.hash_set.add(keyword)

    # Extractor method
    def extractor(self, str1):
        for keyword in self.hash_set:
            if keyword in str1:
                return keyword  # Return the first matching keyword
        return ""  # Return empty string if no keyword matches

    # Excluder method
    def excluder(self, str1):
        for keyword in self.hash_set:
            if keyword in str1:
                return True  # Return True if a matching keyword is found
        return False  # Return False if no keyword matches

    def contains_keywords(self, param: str) ->bool:
        return self.hash_set.__contains__(param)


class QuestionChecker:
    QUESTION_WORDS = {
        "what", "who", "where", "when", "why", "how",
        "is", "are", "was", "were", "do", "does", "did",
        "can", "could", "would", "will", "shall", "should",
        "have", "has", "am", "may", "might"
    }

    @staticmethod
    def is_question(input_text):
        if not input_text or not input_text.strip():
            return False

        trimmed = input_text.strip().lower()

        # Check for question mark
        if trimmed.endswith("?"):
            return True

        # Extract the first word
        first_space = trimmed.find(' ')
        first_word = trimmed if first_space == -1 else trimmed[:first_space]

        # Check for contractions like "who's"
        if "'" in first_word:
            first_word = first_word.split("'")[0]

        # Check if the first word is a question word
        return first_word in QuestionChecker.QUESTION_WORDS


class TrgMinute:
    # trigger true at minute once per hour
    def __init__(self):
        super().__init__()
        self._hour1: int = -1
        self._minute: int = random.randint(0, 60)

    def setMinute(self, minute):
        if -1 < minute < 61:
            self._minute = minute

    # override
    def trigger(self) -> bool:
        temp_hour: int = TimeUtils.getHoursAsInt()
        if temp_hour != self._hour1:
            if TimeUtils.getMinutesAsInt() == self._minute:
                self._hour1 = temp_hour
                return True
        return False

    # override
    def reset(self):
        self._hour1 = -1


class TrgEveryNMinutes:
    def __init__(self, minutes):
        self.interval = timedelta(minutes=minutes)
        self.next_allowed = datetime.datetime.now()

    def trigger(self):
        now = datetime.datetime.now()
        if now >= self.next_allowed:
            self.next_allowed = now + self.interval
            return True
        return False


class OncePerDayGateV0:
    def __init__(self):
        self.last_yday = -1
        self.triggered_today = False

    def check(self, event_happened: bool) -> bool:
        # Fast integer day-of-year check
        yday = time.localtime().tm_yday

        # New day → reset
        if yday != self.last_yday:
            self.last_yday = yday
            self.triggered_today = False

        # If event happened and we haven't triggered today
        if event_happened and not self.triggered_today:
            self.triggered_today = True
            return True

        return False


class EveningGate:
    # ret true once at hour per each 24 hours
    def __init__(self, hour=19):
        self.hour = hour
        self._triggered_today = False
        self._current_day = None

    def trigger(self):
        now = datetime.datetime.now()
        today = now.date()

        if self._current_day != today:
            self._current_day = today
            self._triggered_today = False

        if now.hour == self.hour and not self._triggered_today:
            self._triggered_today = True
            return True

        return False


class SimilarityScorer:
    """
    Utility class for intent similarity scoring.
    """

    @staticmethod
    def similarity(a: str, b: str) -> int:
        """
        Intent similarity scoring.
        Returns integer between 0 and 100.
        0 = completely different. 100 = identical.
        """
        # Calculate the similarity ratio using SequenceMatcher
        weak_ratio: float = SequenceMatcher(None, a, b).ratio()

        # Multiply by 100 and convert to integer
        result: int = int(weak_ratio * 100)

        # Clamp the value to the range 0-100
        return max(0, min(100, result))


class TrueSprinkler:
    """
    Fires `count` times per day, at random minutes within [hour1:00, hour2:59].

    Each day's minutes are pre-rolled (self._slots) and consumed one by one
    as check() is called — so a given minute only triggers once, even if
    check() is called multiple times within that minute's window on a fast loop.
    """

    def __init__(self, count: int, hour1: int, hour2: int):
        self.count = max(0, count)                       # never negative
        self.hour1 = max(0, min(23, hour1))               # clamp to valid hour range
        self.hour2 = max(self.hour1, min(23, hour2))      # clamp + ensure hour2 >= hour1

        self._day = None                                 # date the current _slots belong to
        self._slots = set()                               # remaining trigger minutes (minute-of-day) for today

    def roll(self, from_min: int = 0):
        """
        Pick `count` random minutes (minute-of-day) inside [hour1:00, hour2:59],
        excluding anything before `from_min`.

        `from_min` matters on startup mid-window: if the program starts at,
        say, 14:30, we don't want to roll minutes at 14:00-14:29 that already
        passed and will never fire. On a normal day rollover we pass 0,
        since the whole window is still ahead.
        """
        start = max(self.hour1 * 60, from_min)            # window start, pulled forward if we're starting late
        end = (self.hour2 + 1) * 60                       # window end, exclusive (end of hour2)

        n = max(0, min(self.count, end - start))          # can't sample more slots than exist in the window
        self._slots = set(random.sample(range(start, end), n))

    def check(self, now: datetime = None) -> bool:
        """
        Call this periodically (e.g. once a minute). Returns True exactly once
        per rolled minute, if `now` falls on one.
        """
        now = now or datetime.now()
        m = now.hour * 60 + now.minute                    # current minute-of-day
        today = now.date()

        if today != self._day:                            # crossed into a new day (or first-ever call)
            first_run = self._day is None
            self._day = today
            # First run: skip minutes already passed today (avoid firing for the past).
            # Normal day rollover: reroll the full window, nothing's passed yet.
            self.roll(m if first_run else 0)

        if m in self._slots:
            self._slots.remove(m)                         # consume so it only fires once
            return True
        return False


class DailyEngager:
    """
    span:  minutes an engagement stays "true" once triggered
    times: how many times per day it can be engaged

    poll(trigger) is the per-cycle call: trigger=True spends a credit
    (free if a window is already open), then returns whether the window
    is open. A lapsed window never renews itself, only a new trigger
    does. The `times` counter resets when the calendar day changes.
    """

    def __init__(self, span: int, times: int):
        self.span = max(0, span)
        self.times = max(0, times)

        self._count = 0
        self._day = datetime.datetime.now().date()
        self._active_until = None  # type: datetime.datetime | None

    def _roll_day_if_needed(self):
        today = datetime.datetime.now().date()
        if today != self._day:
            self._day = today
            self._count = 0
            self._active_until = None

    def engage(self) -> bool:
        """Explicit credit spend. Don't call this every cycle, use poll()."""
        self._roll_day_if_needed()
        now = datetime.datetime.now()

        if self._active_until is not None and now < self._active_until:
            return True

        if self._count < self.times:
            self._count += 1
            self._active_until = now + datetime.timedelta(minutes=self.span)
            return True

        self._active_until = None
        return False

    def poll(self, trigger: bool = False) -> bool:
        """Safe per-cycle call. Only a trigger can consume a credit."""
        if trigger:
            self.engage()
        return self.is_active

    def stop(self):
        self._active_until = None

    @property
    def is_active(self) -> bool:
        """Peek at current state without consuming a use or re-engaging."""
        self._roll_day_if_needed()
        return self._active_until is not None and datetime.datetime.now() < self._active_until

    @property
    def remaining_today(self) -> int:
        self._roll_day_if_needed()
        return self.times - self._count


# endregion
# ╔════════════════════════════════════════════════════════════════════════╗
# ║                     SPECIAL SKILLS DEPENDENCIES                        ║
# ╚════════════════════════════════════════════════════════════════════════╝
# region DEPENDENCIES

class TimedMessages:
    """
        check for new messages if you get any input, and it feels like
        the code was waiting for you to tell you something.
        tm = TimedMessages()
        # Print the initial message status (should be False)
        print(tm.getMsg())
        # Add reminders
        tm.addMSG("remind me to work out at 1:24")
        tm.addMSG("remind me to drink water at 11:25")
        # Check if any reminders match the current time
        tm.tick()
        # make sure a fresh new message was loaded before using it
        print(tm.getMsg())
        # Get the last reminder message
        print(tm.getLastMSG())
        # tick each think cycle to load new reminders
        tm.tick()
        print(tm.getMsg()) # becomes true after .getLastMSG
        # Get the last reminder message again
        print(tm.getLastMSG())
    """

    def __init__(self) -> None:
        self.messages: dict[str, str] = {}
        self.lastMSG: str = "nothing"
        self.msg: bool = False

    def addMSG(self, ear: str) -> None:
        tempMSG: str = RegexUtil.extractRegex(r"(?<=remind me to).*?(?=at)", ear)
        if tempMSG:
            timeStamp: str = RegexUtil.extractEnumRegex(enumRegexGrimoire.simpleTimeStamp, ear)
            if timeStamp:
                self.messages[timeStamp] = tempMSG

    def addMSGV2(self, timeStamp: str, msg: str) -> None:
        self.messages[timeStamp] = msg

    def sprinkleMSG(self, msg: str, amount: int) -> None:
        for _ in range(amount):
            self.messages[self.generateRandomTimestamp()] = msg

    @staticmethod
    def generateRandomTimestamp() -> str:
        minutes: int = random.randint(0, 59)
        m = f"{minutes:02d}"
        hours: int = random.randint(0, 11)
        return f"{hours}:{m}"

    def clear(self):
        self.messages.clear()

    def tick(self) -> None:
        now: str = TimeUtils.getCurrentTimeStamp()
        if now in self.messages:
            if self.lastMSG != self.messages[now]:
                self.lastMSG = self.messages[now]
                self.msg = True

    def getLastMSG(self) -> str:
        self.msg = False
        return self.lastMSG

    def getMsg(self) -> bool:
        return self.msg


class AXLearnability:
    def __init__(self, tolerance):
        self.algSent = False
        # Problems that may result because of the last deployed algorithm:
        self.defcons = set()
        # Major chaotic problems that may result because of the last deployed algorithm:
        self.defcon5 = set()
        # Goals the last deployed algorithm aims to achieve:
        self.goals = set()
        # How many failures / problems till the algorithm needs to mutate (change)
        self.trgTolerance = TrgTolerance(tolerance)
        self.trgTolerance.reset()

    def pendAlg(self):
        # An algorithm has been deployed
        # Call this method when an algorithm is deployed (in a DiSkillV2 object)
        self.algSent = True
        self.trgTolerance.trigger()

    def pendAlgWithoutConfirmation(self):
        # An algorithm has been deployed
        self.algSent = True
        # No need to await for a thank you or check for goal manifestation:
        # self.trgTolerance.trigger()
        # Using this method instead of the default "pendAlg" is the same as
        # giving importance to the stick and not the carrot when learning
        # This method is mostly fitting workplace situations

    def mutateAlg(self, input1):
        # Recommendation to mutate the algorithm? true/false
        if not self.algSent:
            return False  # No alg sent => no reason to mutate
        if input1 in self.goals:
            self.trgTolerance.reset()
            self.algSent = False
            return False
        # Goal manifested; the sent algorithm is good => no need to mutate the alg
        if input1 in self.defcon5:
            self.trgTolerance.reset()
            self.algSent = False
            return True
        # ^ Something bad happened probably because of the sent alg
        # Recommend alg mutation
        if input1 in self.defcons:
            self.algSent = False
            mutate = not self.trgTolerance.trigger()
            if mutate:
                self.trgTolerance.reset()
            return mutate
        # ^ Negative result, mutate the alg if this occurs too much
        return False

    def mutateSkill(self, input1):
        # persistently tests feedback till definitive feedback, before deciding about recommending skill mutation.
        # Recommendation to mutate the algorithm? true/false
        if not self.algSent:
            return False  # No alg sent => no reason to mutate
        if input1 in self.goals:
            self.trgTolerance.reset()
            self.algSent = False
            return False
        # Goal manifested; the sent algorithm is good => no need to mutate the alg
        if input1 in self.defcon5:
            self.trgTolerance.reset()
            self.algSent = False
            return True
        # ^ Something bad happened probably because of the sent alg
        # Recommend alg mutation
        if input1 in self.defcons:
            mutate = not self.trgTolerance.trigger()
            if mutate:
                self.algSent = False
                self.trgTolerance.reset()
            return mutate
        # ^ Negative result, mutate the alg if this occurs too much
        return False

    def resetTolerance(self):
        # Use when you run code to change algorithms regardless of learnability
        self.trgTolerance.reset()


class AlgorithmV2:
    def __init__(self, priority, alg):
        self.priority = priority
        self.alg = alg

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority

    def get_alg(self):
        return self.alg

    def set_alg(self, alg):
        self.alg = alg


class SkillHubAlgDispenser:
    # super class to output an algorithm out of a selection of skills
    """
      engage the hub with dispenseAlg and return the value to outAlg attribute
      of the containing skill (which houses the skill hub)
      this module enables using a selection of 1 skill for triggers instead of having the triggers engage on multible skill
       the methode is ideal for learnability and behavioral modifications
       use a learnability auxiliary module as a condition to run an active skill shuffle or change methode
       (rndAlg , cycleAlg)
       moods can be used for specific cases to change behavior of the AGI, for example low energy state
       for that use (moodAlg)"""

    def __init__(self, *skillsParams: Skill):
        super().__init__()
        self._skills: list[Skill] = []
        self._activeSkill: int = 0
        self._tempN: Neuron = Neuron()
        self._kokoro = Kokoro(AbsDictionaryDB())
        for i in range(0, len(skillsParams)):
            skillsParams[i].setKokoro(self._kokoro)
            self._skills.append(skillsParams[i])

    def set_kokoro(self, kokoro):
        self._kokoro = kokoro
        for skill in self._skills:
            skill.setKokoro(self._kokoro)

    def addSkill(self, skill: Skill) -> SkillHubAlgDispenser:
        # builder pattern
        skill.setKokoro(self._kokoro)
        self._skills.append(skill)
        return self

    def dispenseAlgorithm(self, ear: str, skin: str, eye: str):
        # returns Algorithm? (or None)
        # return value to outAlg param of (external) summoner DiskillV2
        self._skills[self._activeSkill].input(ear, skin, eye)
        self._skills[self._activeSkill].output(self._tempN)
        for i in range(1, 6):
            temp: Algorithm = self._tempN.getAlg(i)
            if temp:
                return AlgorithmV2(i, temp)
        return None

    def randomizeActiveSkill(self):
        self._activeSkill = random.randint(0, len(self._skills) - 1)

    def setActiveSkillWithMood(self, mood: int):
        # mood integer represents active skill
        # different mood = different behavior
        if -1 < mood < len(self._skills) - 1:
            self._activeSkill = mood

    def cycleActiveSkill(self):
        # changes active skill
        # I recommend this method be triggered with a Learnability or SpiderSense object
        self._activeSkill += 1
        if self._activeSkill == len(self._skills):
            self._activeSkill = 0

    def getSize(self) -> int:
        return len(self._skills)

    def active_skill_ref(self) -> Skill:
        return self._skills[self._activeSkill]


class UniqueRandomGenerator:
    def __init__(self, n1: int):
        self.n1 = n1
        self.numbers = list(range(n1))
        self.remaining_numbers = []  # Declare here to avoid the error
        self.reset()

    def reset(self):
        self.remaining_numbers = self.numbers.copy()
        random.shuffle(self.remaining_numbers)

    def get_unique_random(self) -> int:
        if not self.remaining_numbers:
            self.reset()
        return self.remaining_numbers.pop()

class UniqueResponder:
    # simple random response dispenser
    def __init__(self, *replies: str):
        # Ensure replies is not empty to avoid range issues
        self.responses: list[str] = []
        self.urg: UniqueRandomGenerator = UniqueRandomGenerator(len(replies))
        for response in replies:
            self.responses.append(response)

    def getAResponse(self) -> str:
        if not self.responses:
            return ""
        return self.responses[self.urg.get_unique_random()]

    def responsesContainsStr(self, item: str) -> bool:
        return self.responses.__contains__(item)

    def strContainsResponse(self, item: str) -> bool:
        for response in self.responses:
            if len(response) == 0:
                continue
            if item.__contains__(response):
                return True
        return False

    def addResponse(self, s1: str):
        if not self.responses.__contains__(s1):
            self.responses.append(s1)
            self.urg: UniqueRandomGenerator = UniqueRandomGenerator(len(self.responses))


class AXSkillBundle:
    def __init__(self, *skills_params: Skill):
        self.skills: list[Skill] = []
        self.tempN: Neuron = Neuron()
        self.kokoro: Kokoro = Kokoro(AbsDictionaryDB())

        for skill in skills_params:
            skill.setKokoro(self.kokoro)
            self.skills.append(skill)

    def set_kokoro(self, kokoro):
        self.kokoro = kokoro
        for skill in self.skills:
            skill.setKokoro(self.kokoro)

    def add_skill(self, skill) -> AXSkillBundle:
        # Builder pattern
        skill.setKokoro(self.kokoro)
        self.skills.append(skill)
        return self

    def dispense_algorithm(self, ear, skin, eye):
        for skill in self.skills:
            skill.input(ear, skin, eye)
            skill.output(self.tempN)
            for j in range(1, 6):
                temp = self.tempN.getAlg(j)
                if temp:
                    return AlgorithmV2(j, temp)

        return None

    def get_size(self):
        return len(self.skills)


class AXGamification:
    # this auxiliary module can add fun to tasks, skills, and abilities simply by
    # tracking their usage, and maximum use count.
    def __init__(self):
        self._counter: int = 0
        self._max: int = 0

    def getCounter(self) -> int:
        return self._counter

    def getMax(self) -> int:
        return self._max

    def resetCount(self):
        self._counter = 0

    def resetAll(self):
        self._counter = 0
        self._max = 0

    def increment(self):
        self._counter += 1
        if self._counter > self._max:
            self._max = self._counter

    def incrementBy(self, n: int):
        self._counter += n
        if self._counter > self._max:
            self._max = self._counter

    def reward(self, cost: int) -> bool:
        # game grind points used for rewards
        # consumables, items or upgrades this makes games fun
        if cost < self._counter:
            self._counter -= cost
            return True
        return False

    def surplus(self, cost: int) -> bool:
        if cost < self._counter:
            return True
        return False


class Responder:
    # simple random response dispenser
    def __init__(self, *replies: str):
        self.responses: list[str] = []
        for response in replies:
            self.responses.append(response)

    def getAResponse(self) -> str:
        if not self.responses:
            return ""
        return self.responses[random.randint(0, len(self.responses) - 1)]

    def responsesContainsStr(self, item: str) -> bool:
        return self.responses.__contains__(item)

    def strContainsResponse(self, item: str) -> bool:
        for response in self.responses:
            if len(response) == 0:
                continue
            if item.__contains__(response):
                return True
        return False

    def addResponse(self, s1: str):
        self.responses.append(s1)


# endregion
# ╔════════════════════════════════════════════════════════════════════════╗
# ║                        OUTPUT MANAGEMENT                               ║
# ╚════════════════════════════════════════════════════════════════════════╝
# region OUTPUT MANAGEMENT


class LimUniqueResponder:
    def __init__(self, lim: int):
        self.responses: list[str] = []
        self.lim = lim
        self.urg = UniqueRandomGenerator(0)

    def get_a_response(self) -> str:
        if not self.responses:
            return ""
        return self.responses[self.urg.get_unique_random()]

    def responses_contains_str(self, item: str) -> bool:
        return item in self.responses

    def str_contains_response(self, item: str) -> bool:
        return any(response and response in item for response in self.responses)

    def add_response(self, s1: str) -> None:
        if s1 in self.responses:
            self.responses.remove(s1)
            self.responses.append(s1)
            return
        if len(self.responses) > self.lim - 1:
            self.responses.pop(0)
        else:
            self.urg = UniqueRandomGenerator(len(self.responses)+1)
        self.responses.append(s1)


    def add_responses(self, *replies: str) -> None:
        for value in replies:
            self.add_response(value)

    def get_savable_str(self) -> str:
        return "_".join(self.responses)

    def get_last_item(self) -> str:
        if not self.responses:
            return ""
        return self.responses[-1]

    def clone(self) -> LimUniqueResponder:
        cloned_responder = LimUniqueResponder(self.lim)  # Create a new instance with the same limit
        cloned_responder.responses = self.responses.copy()  # Copy the responses list
        cloned_responder.urg = UniqueRandomGenerator(
            len(cloned_responder.responses))  # Recreate the UniqueRandomGenerator
        return cloned_responder


class WeightedResponder:
    def __init__(self, lim: int) -> None:
        self.responses: list[str] = []
        self.lim: int = lim

    def get_a_response(self) -> str:
        size = len(self.responses)
        if size == 0:
            return ""

        weights: list[int] = [i + 1 for i in range(size)]
        total_weight: int = sum(weights)
        pick: int = SystemRandom().randint(0, total_weight - 1)

        cumulative = 0
        for i, weight in enumerate(weights):
            cumulative += weight
            if pick < cumulative:
                return self.responses[i]

        return self.responses[-1]

    def responses_contains_str(self, item: str) -> bool:
        return item in self.responses

    def str_contains_response(self, item: str) -> bool:
        for response in self.responses:
            if response and response in item:
                return True
        return False

    def add_response(self, s1: str) -> None:
        if s1 in self.responses:
            self.responses.remove(s1)
            self.responses.append(s1)
            return
        if len(self.responses) > self.lim - 1:
            self.responses.pop(0)
        self.responses.append(s1)

    def add_responses(self, *replies: str) -> None:
        for value in replies:
            self.add_response(value)

    def get_savable_str(self) -> str:
        return "_".join(self.responses)

    def get_last_item(self) -> str:
        return self.responses[-1] if self.responses else ""

    def clone_obj(self) -> 'WeightedResponder':
        cloned = WeightedResponder(self.lim)
        cloned.responses = self.responses.copy()
        return cloned


class PercentDripper:
    def __init__(self):
        self.__dr: DrawRnd = DrawRnd()
        self.__limis: int = 35

    def setLimit(self, limis):
        self.__limis = limis

    def drip(self) -> bool:
        return self.__dr.getSimpleRNDNum(100) < self.__limis

    def dripPlus(self, plus: int) -> bool:
        return self.__dr.getSimpleRNDNum(100) < self.__limis + plus

    def drip_below(self, value:int) -> bool:
        return self.__dr.getSimpleRNDNum(100) < value


class AXTimeContextResponder:
    # output reply based on the part of day as context
    def __init__(self):
        self.morning: Responder = Responder()
        self.afternoon: Responder = Responder()
        self.evening: Responder = Responder()
        self.night: Responder = Responder()
        self._responders: dict[str, Responder] = {"morning": self.morning, "afternoon": self.afternoon,
                                                  "evening": self.evening, "night": self.night}

    def respond(self) -> str:
        return self._responders[TimeUtils.partOfDay()].getAResponse()


class Magic8Ball:
    def __init__(self):
        self.__questions: Responder = Responder()
        self.__answers: Responder = Responder()
        # answers:
        # Affirmative answers
        self.__answers.addResponse("It is certain")
        self.__answers.addResponse("It is decidedly so")
        self.__answers.addResponse("Without a doubt")
        self.__answers.addResponse("Yes definitely")
        self.__answers.addResponse("You may rely on it")
        self.__answers.addResponse("As I see it, yes")
        self.__answers.addResponse("Most likely")
        self.__answers.addResponse("Outlook good")
        self.__answers.addResponse("Yes")
        self.__answers.addResponse("Signs point to yes")
        # Non – Committal answers
        self.__answers.addResponse("Reply hazy, try again")
        self.__answers.addResponse("Ask again later")
        self.__answers.addResponse("Better not tell you now")
        self.__answers.addResponse("Cannot predict now")
        self.__answers.addResponse("Concentrate and ask again")
        # Negative answers
        self.__answers.addResponse("Don’t count on it")
        self.__answers.addResponse("My reply is no")
        self.__answers.addResponse("My sources say no")
        self.__answers.addResponse("Outlook not so good")
        self.__answers.addResponse("Very doubtful")
        # questions:
        self.__questions = Responder("will i", "can i expect", "should i", "is it a good idea",
                                     "will it be a good idea for me to", "is it possible", "future hold",
                                     "will there be")

    def setQuestions(self, q: Responder):
        self.__questions = q

    def setAnswers(self, answers: Responder):
        self.__answers = answers

    def getQuestions(self) -> Responder:
        return self.__questions

    def getAnswers(self) -> Responder:
        return self.__answers

    def engage(self, ear: str) -> bool:
        if len(ear) == 0:
            return False
        if self.__questions.strContainsResponse(ear):
            return True
        return False

    def reply(self) -> str:
        return self.__answers.getAResponse()


class Responder1Word:
    # learns 1 word input
    # outputs learned recent words
    def __init__(self):
        self.q: UniqueItemSizeLimitedPriorityQueue = UniqueItemSizeLimitedPriorityQueue(5)
        self.q.insert("chi")
        self.q.insert("gaga")
        self.q.insert("gugu")
        self.q.insert("baby")

    def listen(self, ear: str):
        if not (ear.__contains__(" ") or ear == ""):
            self.q.insert(ear)

    def getAResponse(self) -> str:
        return self.q.getRNDElement()

    def contains(self, ear: str) -> bool:
        return self.q.contains(ear)

# endregion
# ╔════════════════════════════════════════════════════════════════════════╗
# ║                         STATE MANAGEMENT                               ║
# ╚════════════════════════════════════════════════════════════════════════╝
# region STATE MANAGEMENT

class ButtonEngager:
    """ detect if a button was pressed
     this class disables phisical button engagement while it remains being pressed"""

    def __init__(self):
        self._prev_state: bool = False

    def engage(self, btnState: bool) -> bool:
        # send true for pressed state
        if self._prev_state != btnState:
            self._prev_state = btnState
            if btnState:
                return True
        return False


class Differ:
    def __init__(self):
        self._powerLevel = 90
        self._difference = 0

    def getPowerLevel(self) -> int:
        return self._powerLevel

    def getPowerLVDifference(self) -> int:
        return self._difference

    def clearPowerLVDifference(self):
        self._difference = 0

    def samplePowerLV(self, pl: int):
        # pl is the current power level
        self._difference = pl - self._powerLevel
        self._powerLevel = pl


# endregion
# ╔════════════════════════════════════════════════════════════════════════╗
# ║                         LEARNABILITY                                   ║
# ╚════════════════════════════════════════════════════════════════════════╝
# region LEARNABILITY


class SpiderSense:
    # enables event prediction
    def __init__(self, lim: int):
        super().__init__()
        self._spiderSense: bool = False
        self._events: UniqueItemSizeLimitedPriorityQueue = UniqueItemSizeLimitedPriorityQueue(lim)
        self._alerts: UniqueItemSizeLimitedPriorityQueue = UniqueItemSizeLimitedPriorityQueue(lim)
        self._prev: str = "null"

    def addEvent(self, event: str):
        # builder pattern
        self._events.insert(event)
        return self

    """input param  can be run through an input filter prior to this function
     weather related data (sky state) only for example for weather events predictions"""

    """side note:
     use separate spider sense for data learned by hear say in contrast to actual experience
     as well as lies (false predictions)"""

    def learn(self, in1: str):
        if len(in1) == 0:
            return
        # simple prediction of an event from the events que :
        if self._alerts.contains(in1):
            self._spiderSense = True
            return
        # event has occured, remember what lead to it
        if self._events.contains(in1):
            self._alerts.insert(self._prev)
            return
        # nothing happend
        self._prev = in1

    def getSpiderSense(self) -> bool:
        # spider sense is tingling? event predicted?
        temp: bool = self._spiderSense
        self._spiderSense = False
        return temp

    def getAlertsShallowCopy(self):
        # return shallow copy of alerts list
        return self._alerts.queue

    def getAlertsClone(self) -> list[str]:
        # return deep copy of alerts list
        l_temp: list[str] = []
        for item in self._alerts.queue:
            l_temp.append(item)
        return l_temp

    def clearAlerts(self):
        """this can for example prevent war, because say once a month or a year you stop
         being on alert against a rival"""
        self._alerts.clear()

    def eventTriggered(self, in1:str) -> bool:
        return self._events.contains(in1)


class Strategy:
    def __init__(self, allStrategies: UniqueResponder, strategiesLim: int):
        # bank of all strategies. out of this pool active strategies are pulled
        self._allStrategies: UniqueResponder = allStrategies
        self._strategiesLim = strategiesLim
        # active strategic options
        self._activeStrategy: UniqueItemSizeLimitedPriorityQueue = UniqueItemSizeLimitedPriorityQueue(strategiesLim)
        for i in range(0, self._strategiesLim):
            self._activeStrategy.insert(self._allStrategies.getAResponse())

    def evolveStrategies(self):
        for i in range(0, self._strategiesLim):
            self._activeStrategy.insert(self._allStrategies.getAResponse())

    def getStrategy(self) -> str:
        return self._activeStrategy.getRNDElement()


class Notes:
    def __init__(self):
        self._log: list[str] = []
        self._index: int = 0

    def add(self, s1: str):
        if not s1 in self._log:
            self._log.append(s1)

    def clear(self):
        self._log.clear()

    def getNote(self) -> str:
        if len(self._log) == 0:
            return ""
        return self._log[self._index]

    def get_next_note(self) -> str:
        if len(self._log) == 0:
            return ""
        self._index += 1
        if self._index == len(self._log):
            self._index = 0
        return self._log[self._index]

    def get_note_list(self)->list[str]:
        return self._log

    def set_note_list(self, l1: list[str]):
        self._log = l1

    def remove_note(self, note: str):
        if note in self._log:
            self._log.remove(note)
            if len(self._log) == 0:
                self._index = 0
            elif self._index >= len(self._log):
                self._index = len(self._log) - 1


class Catche:
    # limited sized dictionary, used for short term memories
    def __init__(self, size: int):
        super().__init__()
        self._limit: int = size
        self._keys: UniqueItemSizeLimitedPriorityQueue = UniqueItemSizeLimitedPriorityQueue(size)
        self.d1: dict[str, str] = {}

    def insert(self, key: str, value: str):
        # update
        if self.d1.__contains__(key):
            self.d1[key] = value
            return
        # insert:
        if self._keys.size() == self._limit:
            temp = self._keys.peak()
            del self.d1[temp]
        self._keys.insert(key)
        self.d1[key] = value

    def clear(self):
        self._keys.clear()
        self.d1.clear()

    def read(self, key: str) -> str:
        if not self.d1.__contains__(key):
            return "null"
        return self.d1[key]


# endregion
# ╔════════════════════════════════════════════════════════════════════════╗
# ║                            MISCELLANEOUS                               ║
# ╚════════════════════════════════════════════════════════════════════════╝
# region MISC

class AXKeyValuePair:
    def __init__(self, key: str = "", value: str = "") -> None:
        self.key: str = key
        self.value: str = value

    def get_key(self) -> str:
        return self.key

    def set_key(self, key: str) -> None:
        self.key = key

    def get_value(self) -> str:
        return self.value

    def set_value(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"{self.key};{self.value}"


class CombinatoricalUtils:
    # combo related algorithmic tools
    def __init__(self):
        self.result: list[str] = []

    def _generatePermutations(self, lists: list[list[str]], result: list[str], depth: int, current: str):
        # this function has a private modifier (the "_" makes it so)
        if depth == len(lists):
            result.append(current)
            return
        for i in range(0, len(lists) + 1):
            self._generatePermutations(lists, result, depth + 1, current + lists[depth][i])

    def generatePermutations(self, lists: list[list[str]]):
        # generate all permutations between all string lists in lists, which is a list of lists of strings
        self.result = []
        self._generatePermutations(lists, self.result, 0, "")

    def generatePermutations_V2(self, *lists: list[list[str]]):
        # this is the varargs vertion of this function
        # example method call: cu.generatePermutations(l1,l2)
        temp_lists: list[list[str]] = []
        for i in range(0, len(lists)):
            temp_lists.append(lists[i])
        self.result = []
        self._generatePermutations(temp_lists, self.result, 0, "")


class AXNightRider:
    # night rider display simulation for LED lights count up than down
    def __init__(self, limit: int):
        self._mode: int = 0
        self._position: int = 0
        self._lim = 0
        if limit > 0:
            self._lim = limit
        self._direction = 1

    def setLim(self, lim: int):
        # number of LEDs
        self._lim = lim

    def setMode(self, mode: int):
        # room for more modes to be added
        if 10 > mode > -1:
            self._mode = mode

    def getPosition(self) -> int:
        match self._mode:
            case 0:
                self.mode0()
        return self._position

    def mode0(self):
        # clasic night rider display
        self._position += self._direction
        if self._direction < 1:
            if self._position < 1:
                self._position = 0
                self._direction = 1
        else:
            if self._position > self._lim - 1:
                self._position = self._lim
                self._direction = -1


# endregion
# ╔════════════════════════════════════════════════════════════════════════╗
# ║                            UNDER USE                                   ║
# ╚════════════════════════════════════════════════════════════════════════╝
# region underuse

class DeepCopier:
    @staticmethod
    def copyList(original: list[str]) -> list[str]:
        deepCopy: list[str] = []
        for item in original:
            deepCopy.append(item)
        return deepCopy

    @staticmethod
    def copyListOfInts(original: list[int]) -> list[int]:
        deepCopy: list[int] = []
        for item in original:
            deepCopy.append(item)
        return deepCopy


# the PlayGround cls is not a core class but very useful
class enumTimes(Enum):
    DATE = auto()
    DAY = auto()
    YEAR = auto()
    HOUR = auto()
    MINUTES = auto()
    SECONDS = auto()


class EmoDetectorCurious(Responder):
    def __init__(self):
        super().__init__("why", "where", "when", "how", "who", "which", "whose", "what")

    def isCurious(self, item: str):
        return self.strContainsResponse(item)


class EmoDetectorHappy(Responder):
    def __init__(self):
        super().__init__("good", "awesome", "great", "happy")

    def isHappy(self, item: str):
        return self.strContainsResponse(item)


class EmoDetectorStressed(Responder):
    def __init__(self):
        super().__init__("ouch", "help", "dough")

    def isStressed(self, item: str):
        return self.strContainsResponse(item)


class Map:
    def __init__(self):
        self._pointDescription: dict[str, str] = {}
        self._descriptionPoint: dict[str, str] = {}
        self._currentPosition: LGPointInt = LGPointInt(0, 0)

    def reset(self):
        # sleep location is considered (0,0) location
        self._currentPosition.reset()

    def moveBy(self, x: int, y: int):
        # shift current position
        self._currentPosition.shift(x, y)

    def moveTo(self, location: str):
        # use this when the AI is returning home
        if self._descriptionPoint.__contains__(location):
            value: str = self._descriptionPoint[location]
            p1 = RegexUtil.pointRegex(value)
            self._currentPosition.x = p1.x
            self._currentPosition.y = p1.y

    def write(self, description):
        # location name or item description will be
        # saved on the map on the current point position
        pointStr: str = self._currentPosition.__repr__()
        self._pointDescription[pointStr] = description
        self._descriptionPoint[description] = pointStr

    def read(self) -> str:
        # read place description
        temp: str = self._currentPosition.__repr__()
        if not self._pointDescription.__contains__(temp):
            return "null"
        return self._pointDescription[temp]

    def readPoint(self, p1: LGPointInt) -> str:
        # used for predition of upcoming locations
        # returns: what is the location name at point
        temp: str = p1.__repr__()
        if not self._pointDescription.__contains__(temp):
            return "null"
        return self._pointDescription[temp]

    def locationCoordinate(self, description):
        # get location coordinate
        if not self._descriptionPoint.__contains__(description):
            return "null"
        return self._descriptionPoint[description]


class OutputDripper(Cycler):
    # drips true once every limit times
    def __init__(self, limit: int):
        # set limit to 1 for on off effect
        super().__init__(limit)

    def drip(self) -> bool:
        return self.cycleCount() == 0

    def setLimit(self, lim: int):
        self.limit = lim


# class AXStrOrDefault:
def getOrDefault(str1: str, default1: str) -> str:
    return default1 if (str1 == "") else str1

class DBAntiGlitch:
    # prevents database hacks with livingrimoire naming convensions
    @staticmethod
    def starts_with_trigger(s: str) -> bool:
        return s.lower().startswith(("ah", "di", "da"))


class Sarcophagus:
    def __init__(self):
        """Initialize the sarcophagus with an empty set of shielded items."""
        self._shielded_items: set[str] = set()

    @property
    def shielded_items(self) -> set[str]:
        """Return a copy of the shielded items set (read-only access)."""
        return self._shielded_items.copy()

    def shield(self, input_str: str) -> bool:
        """
        Returns True if the input string contains any item from the shielded set.
        """
        for item in self._shielded_items:
            if item in input_str:
                return True
        return False

    def add_item(self, item: str):
        self._shielded_items.add(item)

    def add_item_via_regex(self, item: str) -> bool:
        pattern = r"do not say (\w+)"
        match = re.search(pattern, item, re.IGNORECASE)
        if match:
            actual_word = match.group(1)
            self._shielded_items.add(actual_word)
            return True
        return False

    def clear_items(self):
        """Clear all items from the shielded set."""
        self._shielded_items.clear()


# endregion