LootTweaker
===========
.. zenscript:type:: loottweaker.LootTweaker

Table names
-----------
Table names use the format ``namespace:path``.
Namespaces can use:

* numbers (0123456789)
* lowercase letters (abcdefghijklmnopqrstuvwxyz)
* underscores (_)
* hyphens (-)
* periods (.)

Paths can use:

* numbers (0123456789)
* lowercase letters (abcdefghijklmnopqrstuvwxyz)
* underscores (_)
* hyphens (-)
* periods (.)
* forward slashes (/)

Methods
-------

See :doc:`here <method-documentation-format>` for an explanation of the method documentation format used on this page.

.. zenscript:function:: static LootTable getTable(String tableName)

    Gets a loot table by name.

    :parameters:
        * *tableName* - the unique name of the table.
    :errors: if no loot table exists with the specified name.
    :returns: the table with the specified name.

    .. code-block:: java

        // Get the dungeon loot table and store it for later
        val simple_dungeon = loottweaker.LootTweaker.getTable("minecraft:chests/simple_dungeon");

.. zenscript:function:: static LootTable newTable(String tableName)

    Creates a new table with a given name. LootTweaker created tables behave exactly like mod created tables, with one
    exception. They cannot be dumped by ``/ct loottables byName`` or ``/ct loottables all`` at this time.
    To view the JSON form, load a save, then check its data/loot_tables folder.

    :parameters:
        * tableName - the unique name of the table. It should be similar to your pack name.
          Avoid using *minecraft* or *loottweaker* as namespaces for tables your pack creates.
    :warns: if the table name implicitly or explicitly uses the minecraft namespace.
     This warning can be disabled in LootTweaker's config.
    :errors: if a loot table with the specified name already exists.
    :returns: an empty table with the specified name.

    .. code-block:: java

        // Create a new loot table and store it for later
        val simple_dungeon = loottweaker.LootTweaker.createTable("examplepack:dave");