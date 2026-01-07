from Back.Repository.creature_repository import CreatureRepository


class CreatureService:

    @staticmethod
    def create_creature(name, max_hp, atm_hp, additional_info):
        return CreatureRepository.create(name, max_hp, atm_hp, additional_info)

    @staticmethod
    def get_all_creatures():
        return CreatureRepository.get_all()

    @staticmethod
    def get_creature_by_id(creature_id):
        return CreatureRepository.get_by_id(creature_id)

    @staticmethod
    def update_creature(creature_id, max_hp=None, atm_hp=None, additional_info=None):
        creature = CreatureRepository.get_by_id(creature_id)
        if not creature:
            return None
        return CreatureRepository.update(creature, max_hp, atm_hp, additional_info)

    @staticmethod
    def delete_creature(creature_id):
        creature = CreatureRepository.get_by_id(creature_id)
        if not creature:
            return False
        CreatureRepository.delete(creature)
        return True
