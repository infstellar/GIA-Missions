from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [1308.39, -2487.34], 'end_position': [1007.21, -2021.28], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [1308.39, -2487.34], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [1162.97, -2215.36], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [974.4, -2090.46], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [1007.21, -2021.28], 'special_key': None}], 'break_position': [[1308.39, -2487.34], [1162.97, -2215.36], [974.4, -2090.46], [1007.21, -2021.28]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[1168.78, -2222.53], [1003.24, -2020.22]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '深渊法师-璃月瑶光滩2个'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '深渊法师-璃月瑶光滩2个', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

