from model.creature import Maturity, Creature, Kind, Health, Satiety, Toilet, cat_kind
import pytest


@pytest.mark.parametrize('kind, name', [(cat_kind, "Ovca"), (cat_kind, "1234")])
def test_creature_init(kind, name):
    creature = Creature(kind, name)
    assert creature.name == name
    assert creature.mature == Maturity.CUB
    assert creature.params[Health].value == 10
    assert creature.params[Satiety].value == 5


@pytest.mark.parametrize('health, hunger', [(9.5, 4.0)])
def test_creature_update(health, hunger):
    creature = Creature(cat_kind, "Ovca")
    creature.update()
    assert creature.params[Health].value == health
    assert creature.params[Satiety].value == hunger


@pytest.mark.parametrize('maturity, health, hunger', [(Maturity.YOUNG, (0, 50), (0, 30)),
                                                      (Maturity.ADULT, (0, 45), (0, 25)),
                                                      (Maturity.OLD, (0, 35), (0, 20))])
def test_creature_grow_up(maturity, health, hunger):
    creature = Creature(cat_kind, "Ovca")
    creature._grow_up(maturity)
    assert creature.params[Health].range == health
    assert creature.params[Satiety].range == hunger


@pytest.mark.parametrize('value, min_, max_, expected', [(5, 0, 25, 4.0),
                                                         (0, 0, 30, 0),
                                                         (0, 0, 25, 0),
                                                         (0, 0, 20, 0)])
def test_hunger_update(value, min_, max_, expected):
    creature = Creature(cat_kind, "Ovca")
    hunger = Satiety(value, min_, max_, creature)
    hunger.update()
    assert hunger.value == expected


@pytest.mark.parametrize('value, min_, max_, expected', [(10, 0, 20, 9.5),
                                                         (0, 0, 50, 0),
                                                         (0, 0, 45, 0),
                                                         (0, 0, 35, 0)])
def test_health_update(value, min_, max_, expected):
    creature = Creature(cat_kind, "Ovca")
    health = Health(value, min_, max_, creature)
    health.update()
    assert health.value == expected


@pytest.mark.parametrize('value, min_, max_, expected', [(5, 0, 15, 6),
                                                         (0, 0, 20, 1),
                                                         (0, 0, 25, 1),
                                                         (0, 0, 15, 1)])
def test_toilet_update(value, min_, max_, expected):
    creature = Creature(cat_kind, 'Ovca')
    toilet = Toilet(value, min_, max_, creature)
    toilet.update()
    assert toilet.value == expected
