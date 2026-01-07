from Back.database import db
from Back.Models.creature import Creature


class CreatureRepository:

    @staticmethod
    def create(name, max_hp, atm_hp, additional_info):
        creature = Creature(
            name=name,
            max_HP=max_hp,
            atm_HP=atm_hp,
            additional_info=additional_info
        )
        db.session.add(creature)
        db.session.commit()
        return creature

    @staticmethod
    def get_all():
        return Creature.query.all()

    @staticmethod
    def get_by_id(creature_id):
        return Creature.query.get(creature_id)

    @staticmethod
    def update(creature, max_hp=None, atm_hp=None, additional_info=None):
        if max_hp is not None:
            creature.max_HP = max_hp
        if atm_hp is not None:
            creature.atm_HP = atm_hp
        if additional_info is not None:
            creature.additional_info = additional_info

        db.session.commit()
        return creature

    @staticmethod
    def delete(creature):
        db.session.delete(creature)
        db.session.commit()
