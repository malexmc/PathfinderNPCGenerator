import json
class CharacterTemplate():
    # template_name = None
    # abilities = {
    #                 "strength" : "High",
    #                 "constitution" : "High",
    #                 "dexterity" : "Low",
    #                 "intelligence" : "Low",
    #                 "wisdom" : "Low",
    #                 "charisma" : "Low"
    #             }
    # attributes = {
    #                 "armor_class" : "Low",
    #                 "hit_points" : "High",
    #                 "perception" : "Low"
    #              }
    
    # saves = {
    #                 "fortitude" : "High",
    #                 "reflex" : "Moderate",
    #                 "will" : "Low"
    #              }
    
    # attack_bonus = "High"
    # damage = "High"
    # speed = ""

    def __init__(self, template_json_path):
        self.abilities = {}
        self.attributes = {}
        self.saves = {}
        
        with open(template_json_path, 'r') as file_handle:
            json_file = json.load(file_handle)
            self.template_name = json_file["template_name"]
            self.abilities["strength"] = json_file["strength"]
            self.abilities["constitution"] = json_file["constitution"]
            self.abilities["dexterity"] = json_file["dexterity"]
            self.abilities["intelligence"] = json_file["intelligence"]
            self.abilities["wisdom"] = json_file["wisdom"]
            self.abilities["charisma"] = json_file["charisma"]
            self.attributes["armor_class"] = json_file["armor_class"]
            self.attributes["hit_points"] = json_file["hit_points"]
            self.attributes["perception"] = json_file["perception"]
            self.saves["fortitude"] = json_file["fortitude"]
            self.saves["reflex"] = json_file["reflex"]
            self.saves["will"] = json_file["will"]
            self.attack_bonus = json_file["attack_bonus"]
            self.damage = json_file["damage"]
            self.speed = json_file["speed"]
            self.skills = json_file["skills"]
            self.spell_dc = json_file["spell_dc"]
        
    def getTemplateAttributes():
        return ["perception", "strength", "constitution", "dexterity", "intelligence", "wisdom", "charisma", "armor_class", "fortitude", "reflex", "will", "hit_points", "attack_bonus", "damage", "speed"]