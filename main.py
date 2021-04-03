import pokepy
# import pokebase as pb
# from pokebase import cache

def createPokemonTypeDict(names, pokemon, types):
    """Append multiple values to a key in the given dictionary"""
    if pokemon not in names:
        names[pokemon] = list()
    names[pokemon].extend(types)
    return names


def getPokemonTypes(generation, name):
    return generation[name]


def createGeneration(baseRange, maxRange):
    ids = [i for i in range(baseRange, maxRange)]
    names = [client_disk_cache.get_pokemon(i) for i in range(baseRange, maxRange)]
    generation = zip(ids, names)
    return dict(generation)


def createTypes(generation, baseRange, maxRange):
    empty_types = [[] for i in range(baseRange, maxRange)]
    names = [client_disk_cache.get_pokemon(i).name for i in range(baseRange, maxRange)]
    generation_empty_types = zip(names, empty_types)
    generation_names = dict(generation_empty_types)
    for pokemon in generation:
        name = generation.get(pokemon).name
        types = []
        for type_slot in generation.get(pokemon).types:
            types.append(type_slot.type.name.title())
        generation_complete = createPokemonTypeDict(generation_names, name, types)
    return generation_complete


def resetTypes():
    return {
        'Grass': 0,
        'Fire': 0,
        'Water': 0,
        'Poison': 0,
        'Flying': 0,
        'Bug': 0,
        'Normal': 0,
        'Ground': 0,
        'Electric': 0,
        'Dragon': 0,
        'Ice': 0,
        'Fairy': 0,
        'Fighting': 0,
        'Steel': 0,
        'Psychic': 0,
        'Rock': 0,
        'Ghost': 0,
        'Dark': 0,
    }


def countTypes(generation):
    for pokemon in generation:
        type_count[generation[pokemon][0]] += 1
        if len(generation[pokemon]) > 1:
            type_count[generation[pokemon][1]] += 1
    return type_count


if __name__ == "__main__":
    # cache.API_CACHE = None
    # print(f'Cache: {cache.API_CACHE}')
    # print(f'Default Cache: {cache.get_default_cache()}')
    # client = pokepy.V2Client()
    # client_mem_cache = pokepy.V2Client(cache='in_memory')
    # for poke in gen1:
    #     print(f'Poke: {gen1.get(poke).name}')
    #     for type_slot in gen1.get(poke).types:
    #         print('{} - {}: {}'.format(gen1.get(poke).name, type_slot.slot, type_slot.type.name.title()))
    # print(f'Cache Info: {client_disk_cache.get_pokemon.cache_info()}')

    # CACHED
    # print('BEGIN CACHED')
    # gen1_names = [client_disk_cache.get_pokemon(i) for i in range(1, gen1_range)]
    # zipped = zip(gen1_ids, gen1_names)
    # gen1 = dict(zipped)
    # for poke in gen1:
    #     print(f'Pokemon: {gen1.get(poke).name}')
    #     for type_slot in gen1.get(poke).types:
    #         print('{} - {}: {}'.format(gen1.get(poke).name, type_slot.slot, type_slot.type.name.title()))
    # print(f'Cache Info: {client_disk_cache.get_pokemon.cache_info()}')

    client_disk_cache = pokepy.V2Client(cache='in_disk')
    print(f'Disk Cache: {client_disk_cache.get_pokemon.cache_location()}')
    print(f'Default Cache: {client_disk_cache.get_pokemon.cache_info()}')
    gen1_range = 152
    gen2_range = 252
    gen3_range = 387
    type_count = resetTypes()

    # Create generation 1
    # gen1_ids = [i for i in range(1, gen1_range)]
    # gen1_names = [client_disk_cache.get_pokemon(i) for i in range(1, gen1_range)]
    # zipped = zip(gen1_ids, gen1_names)
    # gen1Old = dict(zipped)
    gen1 = createGeneration(1, gen1_range)
    # print('-----')
    # print(gen1Old)
    print(f'Cache Info (After Gen1 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Create generation 2
    # gen2_ids = [i for i in range(gen1_range, gen2_range)]
    # gen2_names = [client_disk_cache.get_pokemon(i) for i in range(gen1_range, gen2_range)]
    # zipped = zip(gen2_ids, gen2_names)
    # gen2 = dict(zipped)
    gen2 = createGeneration(gen1_range, gen2_range)
    print(f'Cache Info (After Gen2 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Create generation 3
    # gen3_ids = [i for i in range(gen2_range, gen3_range)]
    # gen3_names = [client_disk_cache.get_pokemon(i) for i in range(gen2_range, gen3_range)]
    # zipped = zip(gen3_ids, gen3_names)
    # gen3 = dict(zipped)
    gen3 = createGeneration(gen2_range, gen3_range)
    print(f'Cache Info (After Gen3 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Types for Gen 1
    # gen1_types = [[] for i in range(1, gen1_range)]
    # gen1_names = [client_disk_cache.get_pokemon(i).name for i in range(1, gen1_range)]
    # gen1_empty_types = zip(gen1_names, gen1_types)
    # generation1_names = dict(gen1_empty_types)
    # # print(f'Gen 1 Dict: {generation1_names}')
    # for poke in gen1:
    #     name = gen1.get(poke).name
    #     types = []
    #     for type_slot in gen1.get(poke).types:
    #         types.append(type_slot.type.name.title())
    #     gen1_complete = createPokemonTypeDict(generation1_names, name, types)
    gen1_complete = createTypes(gen1, 1, gen1_range)
    # print(f'Gen1 + Types: {gen1_complete}')
    # for pokemon in gen1_complete:
    #     print(f'Entry: {pokemon} - {gen1_complete[pokemon]}')
    # print(f"Example of grabbing specific types from pokemon name (Bulbasaur) : {getPokemonTypes(gen1_complete, 'bulbasaur')}")
    # Types for Gen 2
    gen2_complete = createTypes(gen2, gen1_range, gen2_range)
    # gen2_types = [[] for i in range(gen1_range, gen2_range)]
    # gen2_names = [client_disk_cache.get_pokemon(i).name for i in range(gen1_range, gen2_range)]
    # gen2_empty_types = zip(gen2_names, gen2_types)
    # generation2_names = dict(gen2_empty_types)
    # # print(f'Gen 1 Dict: {generation1_names}')
    # for pokemon in gen2:
    #     name = gen2.get(pokemon).name
    #     types = []
    #     for type_slot in gen2.get(pokemon).types:
    #         types.append(type_slot.type.name.title())
    #     gen2_complete = createPokemonTypeDict(generation2_names, name, types)

    # Types for Gen 3
    gen3_complete = createTypes(gen3, gen2_range, gen3_range)
    # gen3_types = [[] for i in range(gen2_range, gen3_range)]
    # gen3_names = [client_disk_cache.get_pokemon(i).name for i in range(gen2_range, gen3_range)]
    # gen3_empty_types = zip(gen3_names, gen3_types)
    # generation3_names = dict(gen3_empty_types)
    # # print(f'Gen 1 Dict: {generation1_names}')
    # for pokemon in gen3:
    #     name = gen3.get(pokemon).name
    #     types = []
    #     for type_slot in gen3.get(pokemon).types:
    #         types.append(type_slot.type.name.title())
    #     gen3_complete = createPokemonTypeDict(generation3_names, name, types)

    # Count Types for Gen 1

    print(f'Gen 1 Types: {countTypes(gen1_complete)}')
    type_count = resetTypes()

    # for pokemon in gen1_complete:
    #     # print(gen1_complete[pokemon][0])
    #     type_count[gen1_complete[pokemon][0]] += 1
    #     if len(gen1_complete[pokemon]) > 1:
    #         # print(gen1_complete[pokemon][1])
    #         type_count[gen1_complete[pokemon][1]] += 1
    # print(f'Gen 1 Types: {type_count}')

    # Reset Type Counts
    print(f'Gen 2 Types: {countTypes(gen2_complete)}')
    type_count = resetTypes()
    # print(f'Types reset: {type_count}')

    # Count Types for Gen 2

    # for pokemon in gen2_complete:
    #     # print(gen1_complete[pokemon][0])
    #     type_count[gen2_complete[pokemon][0]] += 1
    #     if len(gen2_complete[pokemon]) > 1:
    #         # print(gen1_complete[pokemon][1])
    #         type_count[gen2_complete[pokemon][1]] += 1
    # print(f'Gen 2 Types: {type_count}')
    # # Reset Type Counts
    # type_count = resetTypes()

    # Count Types for Gen 3
    print(f'Gen 3 Types: {countTypes(gen3_complete)}')
    type_count = resetTypes()
    # for pokemon in gen3_complete:
    #     # print(gen1_complete[pokemon][0])
    #     type_count[gen3_complete[pokemon][0]] += 1
    #     if len(gen3_complete[pokemon]) > 1:
    #         # print(gen1_complete[pokemon][1])
    #         type_count[gen3_complete[pokemon][1]] += 1
    # print(f'Gen 3 Types: {type_count}')
    # # Reset Type Counts
    # type_count = resetTypes()

    # for poke in gen1:
    #     name = gen1.get(poke).name
    #     types = []
    #     for type_slot in gen1.get(poke).types:
    #         types.append(type_slot.type.name.title())
    #     test = createPokemonTypeDict(generation1_names, name, types)
    #     print(f'IDK? : {test}')
    # generation1 = client_disk_cache.get_generation(1).pokemon_species
    # print('----------')
    # print(f'List of Gen 1: {generation1}')
    # for i in range(len(generation1)):
    #     print(f'{generation1[i].name}')
    # for type_slot in generation1[i].types:
    #     print('{} - {}: {}'.format(generation1[i].name, type_slot.slot, type_slot.type.name.title()))
    # client_mem_cache.get_pokemon.cache_clear()
    # print(f'Pokemon : {client_mem_cache.get_pokemon(14)}')
    # print(f'Pokemon : {client_mem_cache.get_pokemon(14)}')
    # gen1_range = 152
    # gen1_ids = [i for i in range(1, 4)]
    # gen1_names = [pb.pokemon(i) for i in range(1, 4)]
    # zipped = zip(gen1_ids, gen1_names)
    # gen1 = dict(zipped)
    # print(f'Poke Base: {gen1}')
    # for poke in gen1:
    #     print(f'Poke: {gen1.get(poke)}')
    #     for type_slot in gen1.get(poke).types:
    #         print('{} - {}: {}'.format(gen1.get(poke), type_slot.slot, type_slot.type.name.title()))
    # cache.save(data=gen1, endpoint='https://pokeapi.co/api/v2/pokemon')
    # print(f'{cache}')
