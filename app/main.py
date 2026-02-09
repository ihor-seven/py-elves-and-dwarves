from app.players import (
    ElfRanger,
    Druid,
    DwarfWarrior,
    Player,
    Elf,
    Dwarf,
)


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger("Nardual Chaekian", "flute", 7)
    warrior = DwarfWarrior("Thiddeal", "French Fries", 7)

    ranger.play_elf_song()
    warrior.eat_favourite_dish()

    team = [
        Druid("Druid", "flute", "ABC"),
        ElfRanger("Ranger", "trumpet", 33),
    ]
    print(calculate_team_total_rating(team))  # 102
