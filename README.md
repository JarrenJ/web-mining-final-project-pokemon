# final-project-JarrenJ


Demonstrating Cache
---

Upon initial run, my cache will start like this:
- Default Cache: CacheInfo(hits=0, misses=0, size=0)
    - This an empty cache.
- After I run it, my cache will look like this:
    - Cache Info: CacheInfo(hits=0, misses=151, size=151)
        - This shows that my cache now has 151 items in it (in this case all 151 pokemon of generation 1). The `misses=151` means that I didn't use any cached data, which is expected as I was grabbing the resources for the first time.
- After running the same code a second time, my cache looks like this:
    - Cache Info: CacheInfo(hits=151, misses=151, size=151)
        - This shows that I used all 151 item in my cache, `hits=151`. The size didnt get any bigger because I was not calling an new remote resources, but rather using my locally cached resources.
    
Milestone 4
---
An example of how I am manipulating my data:

I start by grabbing all Pokémon in a generation based on their respective ID's and then dril down into the `type` object associated with the pokemon from the api and create a dictrionary with the following structure.
```python
{
    'bulbasaur': ['Grass', 'Poison'], 
    'ivysaur': ['Grass', 'Poison'], 
    'venusaur': ['Grass', 'Poison'] 
 }
```
Using this, structure I can grab the types and count them all up, and create a new dictionary with the following structure.

**Gen 1**
```python
{'Grass': 14, 'Fire': 12, 'Water': 32, 'Poison': 33, 'Flying': 19, 'Bug': 12, 'Normal': 22, 'Ground': 14, 'Electric': 9, 'Dragon': 3, 'Ice': 5, 'Fairy': 5, 'Fighting': 8, 'Steel': 2, 'Psychic': 14, 'Rock': 11, 'Ghost': 3, 'Dark': 0}
```