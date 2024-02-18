import json
import random
import string
import os,sys

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

class NPC:
    character_json = None
    def __init__(self):
        json_file = open(DIR_PATH+"\BlankNPC.JSON")
        self.character_json = json.load(json_file)
        self.setRandomName()

    def getJSON(self):
        return self.character_json

    def __str__(self):
        return json.dumps(self.character_json)

    def setAbility(self, ability, mod):
        self.character_json['system']['abilities'][ability]['mod'] = mod

    def setAttributes(self, attribute, mod):
        if attribute == 'perception':
            self.setPerception(attribute, mod)
        else:
            self.character_json['system']['attributes'][attribute]['value'] = mod
            if attribute == "hp":
                self.character_json['system']['attributes'][attribute]['max'] = mod

    def setPerception(self, attribute, mod):
        self.character_json['system']['perception']['value'] = mod

    def setSaves(self, save, mod):
        self.character_json['system']['saves'][save]['value'] = mod

    def setLevel(self, level):
        if type(level) is str:
            level = int(level)
        self.character_json['system']['details']["level"]['value'] = level

    def setRandomName(self):
        self.character_json['name'] = ( ''.join(random.choice(string.ascii_lowercase) for i in range(10)) )

    def setAttackBonus(self, bonus):
        if type(bonus) is str:
            bonus = int(bonus)
        self.character_json['items'][0]['system']['bonus']['value'] = bonus

    def setDamage(self, damage):
        self.character_json['items'][0]['system']['damageRolls']['EgP3CZT4i6Fxt3Nq']['damage'] = damage

    def setSpeed(self, speed):
        if speed == "":
            return
        else:
            self.character_json['system']['attributes']['speed']['value'] = int(speed)

    def setSkill(self, skill, value):
        if skill == "":
            return
        skill_dict = None
        with open(DIR_PATH+"\ItemTemplates\SkillTemplate.JSON") as skill_template:
            to_json_string = ""
            for line in skill_template:
                to_json_string += line
            skill_dict = json.loads(to_json_string.replace("\n",""))
        skill_dict["name"] = skill
        skill_dict["system"]["mod"]["value"] = int(value)
        self.character_json['items'].append(skill_dict)

    def setSpellcasting(self, value_dc, value_attack):
        if value_dc == "":
            return
        spellcasting_dict = None
        with open(DIR_PATH+"\ItemTemplates\SpellcasterTemplate.JSON") as caster_template:
            to_json_string = ""
            for line in caster_template:
                to_json_string += line
            spellcasting_dict = json.loads(to_json_string.replace("\n",""))
        spellcasting_dict["system"]["spelldc"]["value"] = int(value_attack)
        spellcasting_dict["system"]["spelldc"]["dc"] = int(value_dc)
        self.character_json['items'].append(spellcasting_dict)
        
