Commands
========

LootTweaker adds a single command, /ct loottables.

Subcommands
-----------
.. option:: all

    | Dumps all built-in loot tables.
    | Example:
    | ``/ct loottables all``

.. option:: byName <tableID>

    | Dumps the loot table with the specified ID.
    | Example:
    | ``/ct loottables byName minecraft:chests/simple_dungeon``

.. option:: generate chest

    | Generates a chest that uses the specified loot table at the position the player is looking at.
    | Example:
    | ``/ct loottables generate chest minecraft:chests/simple_dungeon``

.. option:: generate entity

    | Summons an entity that uses the specified loot table at the position the player is looking at.
    | Chest minecarts and similar will generate the loot into their inventory. Other entities will drop the loot on death.
    | Example:
    | ``/ct loottables generate entity minecraft:chests/simple_dungeon minecraft:creeper``

.. option:: list

    | Lists all built-in loot tables.
    | Example:
    | ``/ct loottables list``

.. option:: target

    | Dumps the loot table associated with the object the player is looking at.
    | Example:
    | ``/ct loottables target``

    .. note::

        Some entities don't have a loot table (e.g The Wither).

Dump location
-------------
Dumped loot tables can be found at *minecraftRootFolder*/dumps. The folder structure is the same one used in resourcepacks, so the loot table ``minecraft:chests/simple_dungeon`` would be found at *minecraftRootFolder*/dumps/minecraft/chests/simple_dungeon.json.
