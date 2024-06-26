Tips and Tricks
===============

Setting NBT, metadata and quantity
----------------------------------
| All LootTweaker methods that take an ``IItemStack`` will attempt to preserve the metadata, NBT tag, and stacksize of the passed ``IItemStack``. 
| This is done by automatically generating *set_damage*, *set_data* and *set_count* functions. 
| A function will not be auto-generated for a loot entry if the entry already has a function of the same type. 
| This means that 
| ``pool.addItemEntry(<minecraft:apple> * 2, 1);``
| is equivalent to 
| ``pool.addItemEntryHelper(<minecraft:apple>, 1, 1, [Functions.setCount(2, 2)], []);``
