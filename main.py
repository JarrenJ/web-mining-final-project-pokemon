import pokepy
import numpy as np
import matplotlib.pyplot as plt
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


def generateTypeGraph(type, marker, marker_color, marker_size, line_color, line_width, label):
    return plt.plot(['Gen 1', 'Gen 2', 'Gen 3', 'Gen 4', 'Gen 5', 'Gen 6', 'Gen 7', 'Gen 8'],
                    [gen1_types[type], gen2_types[type], gen3_types[type], gen4_types[type],
                     gen5_types[type], gen6_types[type], gen7_types[type], gen8_types[type]],
                    marker=marker, markerfacecolor=marker_color, markersize=marker_size, color=line_color,
                    linewidth=line_width, label=label)


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

    # Store Gen 1 types with count
    gen1_types = countTypes(gen1_complete)
    type_count = resetTypes()
    # Store Gen 1 types with count
    gen2_types = countTypes(gen2_complete)
    type_count = resetTypes()
    # Store Gen 1 types with count
    gen3_types = countTypes(gen3_complete)
    type_count = resetTypes()
    # Store Gen 1 types with count
    gen4_types = countTypes(gen4_complete)
    type_count = resetTypes()
    # Store Gen 1 types with count
    gen5_types = countTypes(gen5_complete)
    type_count = resetTypes()
    # Store Gen 1 types with count
    gen6_types = countTypes(gen6_complete)
    type_count = resetTypes()
    # Store Gen 1 types with count
    gen7_types = countTypes(gen7_complete)
    type_count = resetTypes()
    # Store Gen 1 types with count
    gen8_types = countTypes(gen8_complete)
    type_count = resetTypes()
    # print([poke_type for poke_type in type_count])

    plt_grass = generateTypeGraph('Grass', 'o', 'green', '8', 'green', '2', 'Grass')
    plt_fire = generateTypeGraph('Fire', 'o', 'orange', '8', 'red', '2', 'Fire')
    plt_water = generateTypeGraph('Water', 'o', 'blue', '8', 'skyblue', '2', 'Water')
    plt_poison = generateTypeGraph('Poison', 'o', 'purple', '8', 'pink', '2', 'Poison')
    plt_flying = generateTypeGraph('Flying', 'o', 'grey', '8', 'grey', '2', 'Flying')
    plt_bug = generateTypeGraph('Bug', 'o', 'yellow', '8', 'green', '2', 'Bug')
    plt_normal = generateTypeGraph('Normal', 'o', 'white', '8', 'grey', '2', 'Normal')
    plt_ground = generateTypeGraph('Ground', 'o', 'brown', '8', 'brown', '2', 'Ground')
    plt_electric = generateTypeGraph('Electric', 'o', 'yellow', '8', 'yellow', '2', 'Electric')
    plt_dragon = generateTypeGraph('Dragon', 'o', 'blue', '8', 'grey', '2', 'Dragon')
    plt_ice = generateTypeGraph('Ice', 'o', 'skyblue', '8', 'blue', '2', 'Ice')
    plt_fairy = generateTypeGraph('Fairy', 'o', 'pink', '8', 'pink', '2', 'Fairy')
    plt_fighting = generateTypeGraph('Fighting', 'o', 'brown', '8', 'black', '2', 'Fighting')
    plt_steel = generateTypeGraph('Steel', 'o', 'grey', '8', 'grey', '2', 'Steel')
    plt_psychic = generateTypeGraph('Psychic', 'o', 'pink', '8', 'purple', '2', 'Psychic')
    plt_rock = generateTypeGraph('Rock', 'o', 'black', '8', 'brown', '2', 'Rock')
    plt_ghost = generateTypeGraph('Ghost', 'o', 'white', '8', 'grey', '2', 'Ghost')
    plt_dark = generateTypeGraph('Dark', 'o', 'black', '8', 'black', '2', 'Dark')

    # plt_gen_1 = plt.plot(['Gen 1', 'Gen 2', 'Gen 3', 'Gen 4', 'Gen 5', 'Gen 6', 'Gen 7', 'Gen 8'], [gen1_types['Grass'], gen2_types['Grass'], gen3_types['Grass'], gen4_types['Grass'], gen5_types['Grass'], gen6_types['Grass'], gen7_types['Grass'], gen8_types['Grass']],
    #                      marker='o', markerfacecolor='green', markersize=8, color='green', linewidth=2, label='Grass')

    # plt_gen_1 = plt.plot([poke_type for poke_type in gen1_types], [gen1_types[count] for count in gen1_types],
    #                      marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=2, label='Gen 1')
    # plt_gen_2 = plt.plot([poke_type for poke_type in gen2_types], [gen2_types[count] for count in gen2_types],
    #                      marker='o', markerfacecolor='red', markersize=8, color='red', linewidth=2, label='Gen 2')
    # plt_gen_3 = plt.plot([poke_type for poke_type in gen3_types], [gen3_types[count] for count in gen3_types],
    #                      marker='o', markerfacecolor='black', markersize=8, color='black', linewidth=2, label='Gen 3')
    # plt_gen_4 = plt.plot([poke_type for poke_type in gen4_types], [gen4_types[count] for count in gen4_types],
    #                      marker='o', markerfacecolor='yellow', markersize=8, color='yellow', linewidth=2, label='Gen 4')
    # plt_gen_5 = plt.plot([poke_type for poke_type in gen5_types], [gen5_types[count] for count in gen5_types],
    #                      marker='o', markerfacecolor='green', markersize=8, color='green', linewidth=2, label='Gen 5')
    # plt_gen_6 = plt.plot([poke_type for poke_type in gen6_types], [gen6_types[count] for count in gen6_types],
    #                      marker='o', markerfacecolor='pink', markersize=8, color='purple', linewidth=2, label='Gen 6')
    # plt_gen_7 = plt.plot([poke_type for poke_type in gen7_types], [gen7_types[count] for count in gen7_types],
    #                      marker='o', markerfacecolor='purple', markersize=8, color='pink', linewidth=2, label='Gen 7')
    # plt_gen_8 = plt.plot([poke_type for poke_type in gen8_types], [gen8_types[count] for count in gen8_types],
    #                      marker='o', markerfacecolor='orange', markersize=8, color='yellow', linewidth=2, label='Gen 8')
    plt.title('Types (Gen1 - Gen8)')
    plt.xlabel('Types')
    plt.ylabel('Pokemon of Type')
    plt.tick_params(axis='x', which='major', labelsize=5)
    plt.legend(loc="upper right")
    plt.savefig('graphs/test5.png')

    # 'Grass': 0,
    # 'Fire': 0,
    # 'Water': 0,
    # 'Poison': 0,
    # 'Flying': 0,
    # 'Bug': 0,
    # 'Normal': 0,
    # 'Ground': 0,
    # 'Electric': 0,
    # 'Dragon': 0,
    # 'Ice': 0,
    # 'Fairy': 0,
    # 'Fighting': 0,
    # 'Steel': 0,
    # 'Psychic': 0,
    # 'Rock': 0,
    # 'Ghost': 0,
    # 'Dark': 0,

    # Pie chart labels
    labels = ['Grass', 'Fire', 'Water', 'Poison', 'Flying', 'Bug', 'Normal', 'Ground', 'Electric', 'Dragon', 'Ice',
              'Fairy', 'Fighting', 'Steel', 'Psychic', 'Rock', 'Ghost', 'Dark']


    def generatePie(gen):
        return [gen['Grass'], gen['Fire'], gen['Water'], gen['Poison'], gen['Flying'],
                gen['Bug'], gen['Normal'], gen['Ground'], gen['Electric'],
                gen['Dragon'], gen['Ice'], gen['Fairy'], gen['Fighting'], gen['Steel'],
                gen['Psychic'], gen['Rock'], gen['Ghost'], gen['Dark']]

    sizes = generatePie(gen8_types)

    # sizes = [gen1_types['Grass'], gen1_types['Fire'], gen1_types['Water'], gen1_types['Poison'], gen1_types['Flying'],
    #          gen1_types['Bug'], gen1_types['Normal'], gen1_types['Ground'], gen1_types['Electric'],
    #          gen1_types['Dragon'], gen1_types['Ice'], gen1_types['Fairy'], gen1_types['Fighting'], gen1_types['Steel'],
    #          gen1_types['Psychic'], gen1_types['Rock'], gen1_types['Ghost']]
    explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)

    # Colors (hexadecimals for types of pokemon in same order as labels above)
    colors = ['#7AC74C', '#EE8130', '#6390F0', '#A33EA1', '#A98FF3', '#A6B91A', '#A8A77A', '#E2BF65', '#F7D02C',
              '#6F35FC', '#96D9D6', '#D685AD', '#C22E28', '#B7B7CE', '#F95587', '#B6A136', '#735797', '#705746']

    fig1, ax1 = plt.subplots()

    # Insetad of using a %, show actual number in pie chart
    total = sum(sizes) / 100.0
    autopct = lambda x: "%d" % round(x * total)

    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct=autopct, startangle=90, pctdistance=0.85)

    # draw circle to mimic donut shaped pie chart
    circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(circle)

    plt.title('Gen 8 Types')
    ax1.axis('equal')  # Pie is drawn as a circle.
    plt.tight_layout()
    plt.savefig('graphs/gen8Types.png')

    # plt_gen_2 = plt.plot(['Gen 1', 'Gen 2', 'Gen 3', 'Gen 4', 'Gen 5', 'Gen 6', 'Gen 7', 'Gen 8'],
    #                      [gen1_types['Fire'], gen2_types['Fire'], gen3_types['Fire'], gen4_types['Fire'],
    #                       gen5_types['Fire'], gen6_types['Fire'], gen7_types['Fire'], gen8_types['Fire']],
    #                      marker='o', markerfacecolor='orange', markersize=8, color='red', linewidth=2, label='Fire')
    # plt.title('Types (Gen1 - Gen8)')
    # plt.xlabel('Types')
    # plt.ylabel('Pokemon of Type')
    # plt.tick_params(axis='x', which='major', labelsize=5)
    # plt.legend(loc="upper right")
    # plt.savefig('test2.png')
