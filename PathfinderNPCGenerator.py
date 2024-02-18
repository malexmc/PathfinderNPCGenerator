# Title: Pathfinder NPC Generator
# Author: Alex McClellan
# Description: Designing Pathfinder 2 NPCs from the templates listed in the book is mostly a matter of reference.
#              This script will do that reference for you and output the finished characters.


from NPC import NPC
from NPCTable import NPCTable
from CharacterTemplate import CharacterTemplate
from enum import Enum
import string
import random
import os,sys

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

class TableNames(Enum):
    ABILITY_MODIFIERS = 1,
    PERCEPTION = 2,
    AC = 3,
    HP = 4,
    SAVES = 5,
    ATTACK_BONUS = 6,
    DAMAGE = 7,
    SKILLS = 8,
    SPELL_DC = 9

def loadAllTables(tables):
    tables[TableNames.ABILITY_MODIFIERS] = NPCTable(DIR_PATH+"\AbilityModifiers.csv")
    tables[TableNames.PERCEPTION] = NPCTable(DIR_PATH+"\Perception.csv")
    tables[TableNames.AC] = NPCTable(DIR_PATH+"\AC.csv")
    tables[TableNames.HP] = NPCTable(DIR_PATH+"\HP.csv")
    tables[TableNames.SAVES] = NPCTable(DIR_PATH+"\SavingThrows.csv")
    tables[TableNames.ATTACK_BONUS] = NPCTable(DIR_PATH+"\AttackBonus.csv")
    tables[TableNames.DAMAGE] = NPCTable(DIR_PATH+"\Damage.csv")
    tables[TableNames.SKILLS] = NPCTable(DIR_PATH+"\Skills.csv")
    tables[TableNames.SPELL_DC] = NPCTable(DIR_PATH+"\SpellDC.csv")

def loadAllTemplates(templates, template_input_map):
    for key in template_input_map.keys():
        templates[template_input_map[key]] = CharacterTemplate(DIR_PATH+"\CharacterTemplates\%s.JSON" % key)

# Load all stat blocks
tables = {}
templates = {}
template_input_map = {}
filenames = []
for file in os.listdir(DIR_PATH+"\CharacterTemplates"):
    filenames.append(os.path.splitext(os.path.basename(file))[0])

TemplateNames = Enum('TemplateNames', [x.upper() for x in filenames])

for filename in filenames:
      template_input_map[filename] = getattr(TemplateNames, filename.upper())

loadAllTables(tables)
loadAllTemplates(templates, template_input_map)

# Ask which template is desired
    # Level
input_level = input("What level character should be made?\n  - ")
    # Template
template_string = "Which template?:\n  - "
for template in templates.keys():
    template_string += templates[template].template_name + "\n  - "
input_template = template_input_map[input(template_string + "-----\n  - ")]

# Apply Stat Blocks
template = templates[input_template]
npc = NPC()
npc.setLevel(input_level) # Level
for ability in template.abilities.keys(): # Abilities
    json_ability_name = ability[0:3]
    ability_value = tables[TableNames.ABILITY_MODIFIERS].getValueAtLevel(template.abilities[ability], input_level)
    npc.setAbility(json_ability_name, int(ability_value))

npc.setAttributes("perception", tables[TableNames.PERCEPTION].getValueAtLevel(template.attributes["perception"], input_level))
npc.setAttributes("ac", tables[TableNames.AC].getValueAtLevel(template.attributes["armor_class"], input_level))
npc.setAttributes("hp", tables[TableNames.HP].getValueAtLevel(template.attributes["hit_points"], input_level))

for save in template.saves.keys(): # Saves
    save_value = tables[TableNames.SAVES].getValueAtLevel(template.saves[save], input_level)
    npc.setSaves(save, int(save_value))
npc_JSON = npc.getJSON()

npc.setAttackBonus(tables[TableNames.ATTACK_BONUS].getValueAtLevel(template.attack_bonus, input_level))
npc.setDamage(tables[TableNames.DAMAGE].getValueAtLevel(template.damage, input_level))
npc.setSpeed(template.speed)
npc.setSpellcasting(
                    tables[TableNames.SPELL_DC].getValueAtLevel(template.spell_dc, input_level),
                    tables[TableNames.ATTACK_BONUS].getValueAtLevel(template.attack_bonus, input_level)
                    )

for skill in template.skills.keys(): #Skills
    skill_value = tables[TableNames.SKILLS].getValueAtLevel(template.skills[skill], input_level)
    npc.setSkill(skill[0].upper() + skill[1: ], skill_value)

# Write to file 
outfile = open(DIR_PATH+"\outfile.JSON", 'w')
outfile.write(str(npc))
