# final-project-JarrenJ


Demonstrating Cache
---
Current saving to RAM

Upon initial run, my cache will start like this:
- Default Cache: CacheInfo(hits=0, misses=0, size=0)
    - This an empty cache.
- After I run it, my cache will look like this:
    - Cache Info: CacheInfo(hits=0, misses=151, size=151)
        - This shows that my cache now has 151 items in it (in this case all 151 pokemon of generation 1). The `misses=151` means that I didn't use any cached data, which is expected as I was grabbing the resources for the first time.
- After running the same code a second time, my cache looks like this:
    - Cache Info: CacheInfo(hits=151, misses=151, size=151)
        - This shows that I used all 151 item in my cache, `hits=151`. The size didnt get any bigger because I was not calling an new remote resources, but rather using my locally cached resources.