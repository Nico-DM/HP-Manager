from flask import Blueprint, request, jsonify
from Back.Service.creature_service import CreatureService

creature_bp = Blueprint("creature_bp", __name__)


@creature_bp.route("/", methods=["POST"])
def create_creature():
    data = request.get_json()

    creature = CreatureService.create_creature(
        name=data["name"],
        max_hp=data["max_hp"],
        atm_hp=data.get("atm_hp", 0),
        additional_info=data.get("additional_info", "")
    )

    return jsonify({
        "id": creature.id,
        "name": creature.name,
        "max_hp": creature.max_HP,
        "atm_hp": creature.atm_HP,
        "additional_info": creature.additional_info
    }), 201


@creature_bp.route("/<int:creature_id>", methods=["PUT"])
def update_creature(creature_id):
    data = request.get_json()

    creature = CreatureService.update_creature(
        creature_id,
        max_hp=data.get("max_hp"),
        atm_hp=data.get("atm_hp"),
        additional_info=data.get("additional_info")
    )

    if not creature:
        return jsonify({"error": "Creature not found"}), 404

    return jsonify({"message": "Creature updated"}), 200


@creature_bp.route("/<int:creature_id>", methods=["DELETE"])
def delete_creature(creature_id):
    success = CreatureService.delete_creature(creature_id)

    if not success:
        return jsonify({"error": "Creature not found"}), 404

    return jsonify({"message": "Creature deleted"}), 200


@creature_bp.route("/", methods=["GET"])
def get_creatures():
    creatures = CreatureService.get_all_creatures()

    result = []
    for c in creatures:
        result.append({
            "id": c.id,
            "name": c.name,
            "max_hp": c.max_HP,
            "atm_hp": c.atm_HP,
            "additional_info": c.additional_info
        })

    return jsonify(result), 200
