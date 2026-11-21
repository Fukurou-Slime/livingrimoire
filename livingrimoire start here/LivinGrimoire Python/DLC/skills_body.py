import time

import psutil

from LivinGrimoirePacket.AXPython import TrgEveryNMinutes
from LivinGrimoirePacket.AlgParts import APSad
from LivinGrimoirePacket.LivinGrimoire import Skill


class DiVitals(Skill):
    def __init__(self):
        super().__init__()
        self.ticker = TrgEveryNMinutes(5)
        self.trigger_phrases = [
            "vitals", "system check", "diagnostics",
            "how are you running"
        ]
        self.last_user_check = 0
        self.cooldown_seconds = 3

    # -----------------------------
    # INTERNAL HELPERS
    # -----------------------------
    @staticmethod
    def get_vitals():
        cpu = psutil.cpu_percent(interval=None)  # non-blocking
        mem = psutil.virtual_memory().percent
        return cpu, mem

    @staticmethod
    def format_report(cpu, mem, tone):
        return (
            f"Vitals check complete.\n"
            f"CPU Usage: {cpu}%\n"
            f"Memory Usage: {mem}%\n"
            f"{tone}"
        )

    def user_triggered(self, ear):
        return self.trigger_phrases.__contains__(ear)

    # -----------------------------
    # MAIN INPUT LOGIC
    # -----------------------------
    def input(self, ear, skin, eye):
        # --- PERIODIC CHECK ---
        if self.ticker.trigger():
            cpu, mem = DiVitals.get_vitals()
            if cpu > 80 or mem > 90:
                tone = "warning Running hot"
                self.setVerbatimAlg(4, self.format_report(cpu, mem, tone))
            return

        # --- USER TRIGGER CHECK ---
        if not self.user_triggered(ear):
            return

        # --- COOLDOWN ---
        now = time.time()
        if now - self.last_user_check < self.cooldown_seconds:
            return
        self.last_user_check = now

        # --- ACTIVE REPORT ---
        cpu, mem = self.get_vitals()
        if cpu > 80 or mem > 90:
            tone = "warning Running hot"
        else:
            tone = "no issues detected"

        self.setVerbatimAlg(4, DiVitals.format_report(cpu, mem, tone))

    # -----------------------------
    # METADATA
    # -----------------------------
    def skillNotes(self, param):
        if param == "notes":
            return "Reads real-time system vitals and returns a personality-infused health report"
        elif param == "triggers":
            return ", ".join(self.trigger_phrases)
        return "Self-diagnostic reporting skill"


class DiCPUTamaguchi(Skill):
    def __init__(self):
        super().__init__()
        self.ticker = TrgEveryNMinutes(25)  # every 5 minutes she checks battery
        self.plugged = False

    def manifest(self):
        self.plugged = self.is_plugged_ret_bool()

    def input(self, ear, skin, eye):
        is_plugged = self.is_plugged_ret_bool()
        if not is_plugged == self.plugged:
            # gotten unplugged
            bat = self.get_battery_percentageInt()
            if not is_plugged:
                if bat < 80:
                    self.setSimpleAlg(f'hey i am still eating')
                else:
                    self.setSimpleAlg(f'battery at {bat} percent and unplugged')
            else:
                # gotten plugged
                if bat < 80:
                    self.setSimpleAlg(f'peanut butter jelly time')
                else:
                    self.setSimpleAlg(f'battery at {bat} percent and plugged')
            self.plugged = is_plugged
            return

        # -------------------------
        # PERIODIC HUNGER CHECK
        # -------------------------
        if self.ticker.trigger():
            battery = self.get_battery_percentageInt()
            if battery != -1 and battery < 50 and not self.is_battery_plugged():
                # She is hungry
                self.setVerbatimAlg(4, "i am so hungry")
            return

        # -------------------------
        # USER COMMANDS
        # -------------------------
        match ear:
            case "battery":
                self.setSimpleAlg(self.get_battery_percentage())

            case "are you eating":
                self.setSimpleAlg(self.isPlugged())

            case "are you hungry":
                hunger: int = self.get_battery_percentageInt()
                if hunger == 100:
                    self.setSimpleAlg(f"no I am full")
                elif hunger> 90:
                    self.setSimpleAlg(f"I am pretty full")
                elif hunger > 50:
                    self.setSimpleAlg(f"I am missing{100 - hunger}%")
                else:
                    self.algPartsFusion(4, APSad("i am so hungry"))

            case "cpu usage":
                self.setSimpleAlg(self.get_cpu_usage())

    # -------------------------
    # BATTERY HELPERS
    # -------------------------
    @staticmethod
    def get_battery_percentage():
        battery = psutil.sensors_battery()
        if battery is None:
            return "No battery found."
        return f"Battery Percentage: {battery.percent}%"

    @staticmethod
    def isPlugged():
        battery = psutil.sensors_battery()
        if battery is None:
            return "No battery found."
        return f"**Power plugged in**: {battery.power_plugged}"

    @staticmethod
    def is_plugged_ret_bool() -> bool:
        battery = psutil.sensors_battery()
        if battery is None:
            return False
        return battery.power_plugged

    @staticmethod
    def is_battery_plugged() -> bool:
        battery_info = psutil.sensors_battery()
        if battery_info is None:
            return False  # No battery found
        return battery_info.power_plugged

    @staticmethod
    def get_battery_percentageInt() -> int:
        battery = psutil.sensors_battery()
        if battery is None:
            return -1
        return battery.percent

    @staticmethod
    def get_cpu_usage():
        """
        Returns the current system-wide CPU usage percentage.
        """
        return f"{psutil.cpu_percent()}"

    def skillNotes(self, param: str) -> str:
        if param == "notes":
            return "hardware states reading"
        elif param == "triggers":
            return "'battery', 'are you hungry', CPU usage'"
        return "note unavailable"