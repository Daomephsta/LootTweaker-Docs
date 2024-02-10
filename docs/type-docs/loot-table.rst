LootTable
=========
.. zenscript:type:: loottweaker.vanilla.loot.LootTable

Methods
-------

See :doc:`here <method-documentation-format>` for an explanation of the method documentation format used on this page.

.. zenscript:function:: clear()

    Removes all pools from this table. This includes any loot added by a script before this method was run.

    .. code-block:: java

        // someTable is a LootTable created elsewhere
        someTable.clear();

.. zenscript:function:: LootPool addPool(String poolName, float minRolls, float maxRolls, float minBonusRolls, float maxBonusRolls)

    Adds a new pool to this table, and returns it.

    :parameters:

    * poolName - a name for the table. Must be unique within the table.
    * minRolls - the minimum rolls of the new pool.
    * maxRolls - the maximum rolls of the new pool.
    * minBonusRolls-  the minimum bonus rolls of the new pool.
    * maxBonusRolls - the maximum bonus rolls of the new pool.

    :errors: if a pool with the same name already exists in the table
    :returns: the new pool

    .. code-block:: java

        // someTable is a LootTable created elsewhere
        val somePool = someTable.addPool("somePool", 1, 1, 0, 0);

.. zenscript:function:: removePool(String poolName)

    Removes the pool with the name `poolName` from this table.

    :parameters:

    * poolName - the table-unique name of the pool

    :errors: if no loot pool with the specified name exists.

    .. code-block:: java

        // someTable is a LootTable created elsewhere
        someTable.removePool("somePool");

.. zenscript:function:: LootPool getPool(String poolName)

    Gets a LootPool by name.

    :parameters:

    * poolName - the table-unique name of the pool

    :errors: if no loot pool with the specified name exists.
    :returns: the loot pool with the specified name.

    .. code-block:: java

        // someTable is a LootTable created elsewhere
        val somePool = someTable.getPool("somePool");

Pool Names
----------
Pools you add have whatever name you give them.
The first default pool in a table is named main. Successive pools are named in the format poolN,
where N is a number that starts at 1 and increments for each pool.