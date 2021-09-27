import pytest

from tasks.hard.game import Warrior, Arena


def test_create_warrior():
    warrior = Warrior("war_name")

    assert warrior.name == "war_name"
    assert warrior.health_points == 100


def test_hit_warrior():
    attacker = Warrior("attacker")
    assert hasattr(attacker, "hit")

    defender = Warrior("defender")
    assert defender.health_points == 100
    attacker.hit(defender)
    assert defender.health_points == 80

    defender.health_points = 0
    with pytest.raises(ValueError):
        attacker.hit(defender)


def test_create_arena():
    empty_arena = Arena()

    assert isinstance(empty_arena.warriors, list)
    assert len(empty_arena.warriors) == 0

    warrior = Warrior("Warrior")
    arena_with_warriors = Arena([warrior])

    assert isinstance(arena_with_warriors.warriors, list)
    assert len(arena_with_warriors.warriors) == 1
    assert warrior in arena_with_warriors.warriors


def test_add_warrior_to_arena():
    arena = Arena()
    warrior = Warrior("Warrior")

    arena.add_warrior(warrior)
    assert len(arena.warriors) == 1
    assert warrior in arena.warriors

    with pytest.raises(ValueError):
        arena.add_warrior(warrior)


def test_choose_warrior():
    arena = Arena()
    warrior = Warrior("Warrior")
    arena.warriors.append(warrior)

    assert warrior is arena.choose_warrior()


def test_battle():
    arena = Arena()
    with pytest.raises(ValueError):
        arena.battle()
    arena.warriors.append(Warrior("Warrior"))
    with pytest.raises(ValueError):
        arena.battle()

    for _ in range(5):
        arena.warriors.append(Warrior("Warrior"))

    winner = arena.battle()

    assert winner in arena.warriors
    assert len(arena.warriors) == 1