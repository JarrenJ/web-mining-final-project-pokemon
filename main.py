import pokepy
# import pokebase as pb
# from pokebase import cache

if __name__ == "__main__":
    # cache.API_CACHE = None
    # print(f'Cache: {cache.API_CACHE}')
    # print(f'Default Cache: {cache.get_default_cache()}')
    # client = pokepy.V2Client()
    client_mem_cache = pokepy.V2Client(cache='in_memory')
    print(f'Default Cache: {client_mem_cache.get_pokemon.cache_info()}')
    gen1_range = 152
    gen1_ids = [i for i in range(1, gen1_range)]
    gen1_names = [client_mem_cache.get_pokemon(i) for i in range(1, gen1_range)]
    zipped = zip(gen1_ids, gen1_names)
    gen1 = dict(zipped)
    for poke in gen1:
        print(f'Poke: {gen1.get(poke).name}')
        for type_slot in gen1.get(poke).types:
            print('{} - {}: {}'.format(gen1.get(poke).name, type_slot.slot, type_slot.type.name.title()))
    print(f'Cache Info: {client_mem_cache.get_pokemon.cache_info()}')

    # CACHED
    print('BEGIN CACHED')
    # gen1_range = 152
    # gen1_ids = [i for i in range(1, gen1_range)]
    gen1_names = [client_mem_cache.get_pokemon(i) for i in range(1, gen1_range)]
    zipped = zip(gen1_ids, gen1_names)
    gen1 = dict(zipped)
    for poke in gen1:
        print(f'Poke: {gen1.get(poke).name}')
        for type_slot in gen1.get(poke).types:
            print('{} - {}: {}'.format(gen1.get(poke).name, type_slot.slot, type_slot.type.name.title()))

    print(f'Cache Info: {client_mem_cache.get_pokemon.cache_info()}')

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



