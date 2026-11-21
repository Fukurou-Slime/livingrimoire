from DLC.RailPunk_Populators.boolean_populators import IfXThenY, IfISayXThenSayYSosu
from LG_SQLite_DB import SQLiteDictionaryDB
from LivinGrimoirePacket.AXPython import DailyEngager, PhraseInflector, Sarcophagus, DBAntiGlitch, \
    TimeGate, TimeUtils, Responder, DrawRndDigits, LGFIFO, TrgMinute, PercentDripper
from LivinGrimoirePacket.AlgParts import APHappy
from LivinGrimoirePacket.LivinGrimoire import Skill
from LivinGrimoirePacket.RailPunk import RailPunk


# test populators:



class DiRailPunk(Skill):
    def __init__(self, DB_name: str = ""):
        # to enable DB (per Railpunk skill give DB_name param some name)
        super().__init__()
        self.set_skill_type(2)  # continous skill
        self.faucet: DailyEngager = DailyEngager(span=10, times=3)  # faucet trigger to enable convo
        if len(DB_name)>0:
            self.bot: RailPunk = RailPunk(db=SQLiteDictionaryDB(DB_name))
        else:
            self.bot: RailPunk = RailPunk()  # chatbot engine
        self.filter: Sarcophagus = Sarcophagus()  # nono words filter
        self.filter_clear: set[str] = {"clear filter", "clear word filter", "clear sarcophagus"}
        # populators addition
        self.bot.add_populator(IfXThenY())  # example populators(modular deduction objects)
        self.bot.add_populator(IfISayXThenSayYSosu())
        # context reset
        self.idler: TimeGate = TimeGate(5)
        self.focus = False

    def input(self, ear: str, skin: str, eye: str):
        if DBAntiGlitch.starts_with_trigger(ear):
            return
        # on no input for N minutes reset context, save new learned input and deductions
        if ear:
            self.idler.openForPauseMinutes()
        elif self.idler.isClosed():
            self.bot.save_learned_data()
            self.bot.set_context("stand by")
            self.focus = False
            self.idler.openForPauseMinutes()
            return
        if not ear:
            return
        # focus mode replies with latest learned replies
        if ear == "focus":
            self.focus = True
            self.setSimpleAlg("focusing")
            return
        if self.filter.add_item_via_regex(ear):
            self.setSimpleAlg("ok i will not use that nono word")
            return
        if ear in self.filter_clear:
            self.filter.clear_items()
            self.setSimpleAlg("i am now ungovernable")
            return
        # stop convo abruptly
        if ear in ("stop", "shut up", "quiet"):
            self.faucet.stop()
            self.focus = False
            return
        temp = ear in ("hey", "lets talk")
        if not temp:
            self.bot.learn(ear)
        if self.faucet.poll(temp):
            if temp:
                self.setSimpleAlg("listening")
                return
            reply = self.get_reply(ear)  # reply gen
            if self.filter.shield(reply):
                self.setSimpleAlg("filtered")
                return
            if reply:
                self.setSimpleAlg(PhraseInflector.inflect_phrase(reply))


    def get_reply(self, ear: str)->str:
        if not self.focus:
            return self.bot.reply(ear)
        return self.bot.reply(ear,True)

    def skillNotes(self, param: str) -> str:
        if param == "notes":
            return "chatbot railpunk skill"
        if param == "triggers":
            return "on: hey / lets talk. off: stop / shut up / quiet"
        return "note unavailable"


class DiChirper(Skill):
    # chirps like a bird: autonomously at random or as a reply to other chirps (or predefined sounds)
    def __init__(self, chirps_per_hour: int = 3):
        super().__init__()
        self.dripper: PercentDripper = PercentDripper()

        # default chirps per hour
        self._chirpsPerHour = 2
        if 60 > chirps_per_hour > 0:
            self._chirpsPerHour = chirps_per_hour

        # triggers at minute 0 to refresh chirp schedule
        self._trgMinute: TrgMinute = TrgMinute()
        self._trgMinute.setMinute(0)

        # responder for reactive chirps
        self._responder1: Responder = Responder("hadouken", "hadoken")

        # random minute generator
        self._draw: DrawRndDigits = DrawRndDigits()
        self._chirpMinutes: LGFIFO = LGFIFO()

        # fill draw pool with minutes 1–59
        for i in range(1, 60):
            self._draw.addElement(i)

        # pick initial chirp minutes
        for i in range(0, chirps_per_hour):
            self._chirpMinutes.insert(self._draw.drawAndRemove())


    def setChirps(self, chirp_responder: Responder) -> 'DiChirper':
        # set sounds of chirp events
        self._responder1 = chirp_responder
        return self


    # Override
    def input(self, ear: str, skin: str, eye: str):
        # night? do not chirp
        if TimeUtils.partOfDay() == "night":
            return

        # reset chirp schedule every hour
        if self._trgMinute.trigger():
            self._chirpMinutes.clear()
            self._draw.reset()
            for i in range(0, self._chirpsPerHour):
                self._chirpMinutes.insert(self._draw.drawAndRemove())
            return

        # autonomous chirp
        now_minutes: int = TimeUtils.getMinutesAsInt()
        if self._chirpMinutes.contains(now_minutes):
            self._chirpMinutes.removeItem(now_minutes)
            self.algPartsFusion(4, APHappy(self._responder1.getAResponse()))
            return

        # reactive chirp (your added logic)
        if self._responder1.strContainsResponse(ear) and self.dripper.drip_below(50):
            self.setSimpleAlg(self._responder1.getAResponse())


    def skillNotes(self, param: str) -> str:
        if param == "notes":
            return "Randomly chirps several times an hour during the day. Will not occur during the night."
        elif param == "triggers":
            return f'Say {self._responder1.getAResponse()} to manually trigger a chirp.'
        return "note unavailable"


class DiCrash(Skill):
    def __init__(self):
        super().__init__()

    def input(self, ear: str, skin: str, eye: str):
        if ear == "crash":
            self.algPartsFusion(4)  # priority 4, but no AlgParts -> empty algorithm