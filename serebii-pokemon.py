import os
import json
import requests
from bs4 import BeautifulSoup
from bs4 import ResultSet, Tag
from dataclasses import dataclass


@dataclass
class Pokemon:
    id: str
    name: str
    type: list[str]
    abilities: list[str]
    bs_hp: str
    bs_att: str
    bs_def: str
    bs_s_att: str
    bs_s_def: str
    bs_spd: str

    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


def get_html(url):
    r = requests.get(url)
    return r.text


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup


def parse_pokemon_type(pokemon_data: Tag):
    links: ResultSet[Tag] = pokemon_data.find_all("a")
    # split by / and return the last as the type for all links
    return [link["href"].split("/")[-1].capitalize() for link in links]


def parse_pokemon_info(pokemon_data):
    return Pokemon(
        id=pokemon_data[0].text.strip(),
        name=pokemon_data[2].text.strip(),
        type=parse_pokemon_type(pokemon_data[3]),
        abilities=pokemon_data[4].text.strip().split(" "),
        bs_hp=pokemon_data[5].text.strip(),
        bs_att=pokemon_data[6].text.strip(),
        bs_def=pokemon_data[7].text.strip(),
        bs_s_att=pokemon_data[8].text.strip(),
        bs_s_def=pokemon_data[9].text.strip(),
        bs_spd=pokemon_data[10].text.strip(),
    )


def save_on_json(pokemons: [Pokemon]):
    with open("pokemons.json", "w", encoding="utf-8") as file:
        raw_data = "[\n"
        for pokemon in pokemons:
            raw_data += pokemon.json() + ",\n"
        raw_data = raw_data[:-2] + "\n]"
        file.write(raw_data)


def save_on_text(pokemons: list[Pokemon]):
    if not os.path.exists("./pokemons"):
        os.mkdir("./pokemons")

    for pokemon in pokemons:
        with open(f"./pokemons/{pokemon.id}.txt", "w", encoding="utf-8") as file:
            raw_data = f"""
ID: {pokemon.id}
Name: {pokemon.name}
Type: {', '.join(pokemon.type)}
Abilities: {', '.join(pokemon.abilities)}

Base Stats:
\tHP: {pokemon.bs_hp}
\tAttack: {pokemon.bs_att}
\tDefense: {pokemon.bs_def}
\tSpecial Attack: {pokemon.bs_s_att}
\tSpecial Defense: {pokemon.bs_s_def}
\tSpeed: {pokemon.bs_spd}
"""
            file.write(raw_data)


def main():
    html = get_html("https://www.serebii.net/pokemon/nationalpokedex.shtml")
    dom = parse_html(html)

    raw_pokemons = dom.select("tr")

    pokemons = []
    for pokemon in raw_pokemons:
        pokemon_data = pokemon.select(".fooinfo")
        if not pokemon_data:
            continue

        pokemons.append(parse_pokemon_info(pokemon_data))

    save_on_json(pokemons)
    save_on_text(pokemons)


if __name__ == "__main__":
    main()
