from DLC.DiTTS_FishAudio import DiTTS_FishAudioInstaller
from DLC.skills_attention import DiRailPunk, DiChirper, DiCrash
from DLC.skills_body import DiVitals, DiCPUTamaguchi
from LivinGrimoirePacket.LivinGrimoire import Brain, DiHelloWorld, DiSysOut


def add_DLC_skills(brain: Brain):


    # ╔══════════════════════════════════════════╗
    # ║                D E F A U L T             ║
    # ╚══════════════════════════════════════════╝
    brain.add_skill(DiCrash())
    #######
    # power#
    #######
    brain.add_skill(DiVitals())
    brain.add_skill(DiCPUTamaguchi())
    brain.add_skill(DiChirper())

    ###########
    # attention#
    ###########
    brain.add_skill(DiRailPunk())

    ############
    # continuity#
    ############

    ######
    # body#
    ######
    brain.chained(DiHelloWorld()).chained(DiSysOut())
    brain.add_skill(DiTTS_FishAudioInstaller(brain))