import pokepy
from variables import CACHE_PATCH

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
    # for id1 in ids:
    # print(f'ID: {id1}')
    # print(f"Pokemon sad-- {client_disk_cache.get_pokemon('sawsbuck').id}")
    # print(f'Pokemon -- {client_disk_cache.get_pokemon(id1).name}')
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
    """
    CACHE_PATH is stored in a separate file (not pushed to git).
    cache_location should point to the absolute path of the local cache directory.
    """
    client_disk_cache = pokepy.V2Client(cache='in_disk', cache_location=CACHE_PATCH)

    print(f'Global Cache Location: {client_disk_cache.cache_location()}')
    # Print out cache location
    print(f'Cache (get_pokemon): {client_disk_cache.get_pokemon.cache_location()}')

    # See how many items cache has at beginning of execution
    print(f'Default Cache: {client_disk_cache.get_pokemon.cache_info()}')

    # Init generation ranges (Add 1 to each range)
    gen1_range = 152
    gen2_range = 252
    gen3_range = 387
    gen4_range = 494
    gen5_range = 650
    gen6_range = 722
    gen7_range = 810
    gen8_range = 899

    # Init type_count to hold 0 for all types
    type_count = resetTypes()

    # Create generation 1
    gen1 = createGeneration(1, gen1_range)

    # Check to make sure we are hitting the cache
    print(f'Cache Info (After Gen1 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Create generation 2
    gen2 = createGeneration(gen1_range, gen2_range)

    # Check to make sure we are hitting the cache
    print(f'Cache Info (After Gen2 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Create generation 3
    gen3 = createGeneration(gen2_range, gen3_range)

    # Check to make sure we are hitting the cache
    print(f'Cache Info (After Gen3 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Create generation 4
    gen4 = createGeneration(gen3_range, gen4_range)

    # Check to make sure we are hitting the cache
    print(f'Cache Info (After Gen4 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Create generation 5
    gen5 = createGeneration(gen4_range, gen5_range)

    # Check to make sure we are hitting the cache
    print(f'Cache Info (After Gen5 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Create generation 6
    gen6 = createGeneration(gen5_range, gen6_range)

    # Check to make sure we are hitting the cache
    print(f'Cache Info (After Gen6 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Create generation 7
    gen7 = createGeneration(gen6_range, gen7_range)

    # Check to make sure we are hitting the cache
    print(f'Cache Info (After Gen7 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Create generation 8
    gen8 = createGeneration(gen7_range, gen8_range)

    # Check to make sure we are hitting the cache
    print(f'Cache Info (After Gen8 Creation): {client_disk_cache.get_pokemon.cache_info()}')

    # Leaving in for now in case I need it later
    # print(f"Example of grabbing specific types from pokemon name (Bulbasaur) : {getPokemonTypes(gen1_complete, 'bulbasaur')}")

    # Create types for Gen 1
    gen1_complete = createTypes(gen1, 1, gen1_range)

    # Create types for Gen 2
    gen2_complete = createTypes(gen2, gen1_range, gen2_range)

    # Create types for Gen 3
    gen3_complete = createTypes(gen3, gen2_range, gen3_range)

    # Create types for Gen 4
    gen4_complete = createTypes(gen4, gen3_range, gen4_range)

    # Create types for Gen 5
    gen5_complete = createTypes(gen5, gen4_range, gen5_range)

    # Create types for Gen 6
    gen6_complete = createTypes(gen6, gen5_range, gen6_range)

    # Create types for Gen 7
    gen7_complete = createTypes(gen7, gen6_range, gen7_range)

    # Create types for Gen 7
    gen8_complete = createTypes(gen8, gen7_range, gen8_range)

    # Count Types for Gen 1
    print(f'Gen 1 Types: {countTypes(gen1_complete)}')

    # Reset type_count
    type_count = resetTypes()

    # Count Types for Gen 2
    print(f'Gen 2 Types: {countTypes(gen2_complete)}')

    # Reset type_count
    type_count = resetTypes()

    # Count types for Gen 3
    print(f'Gen 3 Types: {countTypes(gen3_complete)}')

    # Reset type_count
    type_count = resetTypes()

    # Count types for Gen 4
    print(f'Gen 4 Types: {countTypes(gen4_complete)}')

    # Reset type_count
    type_count = resetTypes()

    # Count types for Gen 5
    print(f'Gen 5 Types: {countTypes(gen5_complete)}')

    # Reset type_count
    type_count = resetTypes()

    # Count types for Gen 6
    print(f'Gen 6 Types: {countTypes(gen6_complete)}')

    # Reset type_count
    type_count = resetTypes()

    # Count types for Gen 7
    print(f'Gen 7 Types: {countTypes(gen7_complete)}')

    # Reset type_count
    type_count = resetTypes()

    # Count types for Gen 8
    print(f'Gen 8 Types: {countTypes(gen8_complete)}')

    # Reset type_count
    type_count = resetTypes()