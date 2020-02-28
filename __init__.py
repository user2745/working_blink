from mycroft import MycroftSkill, intent_file_handler
import subprocess

class HackerMan(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('man.hacker.intent')
    def handle_man_hacker(self, message):
        self.speak_dialog('man.hacker')
        subprocess.Popen(["sudo", "pwd"])
        subprocess.Popen (["sudo", "python3", "/opt/mycroft/skills/hacker-man-skill/blink.py"])
    
    @intent_file_handler('man.hacker.stop.intent')
    def handle_man_hacker_stop(self, message):
        self.speak_dialog('man.hacker.stop')
        subprocess.Popen(["sudo", "pwd"])
        subprocess.Popen (["sudo", "python3", "/opt/mycroft/skills/hacker-man-skill/blink.py"])


def create_skill():
    return HackerMan()

