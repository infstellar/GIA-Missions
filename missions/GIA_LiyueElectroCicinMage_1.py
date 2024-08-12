from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [737.65, -998.59], 'end_position': [910.89, -1014.09], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [737.65, -998.59], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [853.33, -1020.75], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [910.89, -1014.09], 'special_key': None}], 'break_position': [[737.65, -998.59], [853.33, -1020.75], [910.89, -1014.09]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[910.5, -1011.0]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集璃月云来海萤术士'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集璃月云来海萤术士', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()
