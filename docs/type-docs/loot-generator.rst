LootGenerator
=============
.. zenscript:type:: loottweaker.LootGenerator

A reusable object for generating loot from the tables of a specific world with a configured loot context (luck, looted entity, player, etc.). Generation does not reset the context.

You'll need to be familiar with the vanilla loot system and its loot contexts to make use of the full capabilities of this class.

Call `LootTweaker.createLootGenerator </type-docs/loottweaker.html#zenfunction-createLootGenerator(IWorld)>`__ to create a loot generator.

.. zenscript:function:: LootGenerator luck(float luck)

    Configures the luck value of the loot generator's context.

    :returns: the same loot generator, to allow method chaining

    .. code-block:: java

        import loottweaker.LootTweaker;

        LootTweaker.createLootGenerator(world)
            .luck(42.0)
            .generate("minecraft:entities/cow");

.. zenscript:function:: LootGenerator lootedEntity(IEntity entity)

    Configures the looted entity of the loot generator's context.

    :returns: the same loot generator, to allow method chaining

    .. code-block:: java

        import loottweaker.LootTweaker;

        LootTweaker.createLootGenerator(world)
            .lootedEntity(someEntity)
            .generate("minecraft:entities/cow");

.. zenscript:function:: LootGenerator player(IPlayer player)

    Configures the looting player of the loot generator's context.

    :returns: the same loot generator, to allow method chaining

    .. code-block:: java

        import loottweaker.LootTweaker;

        LootTweaker.createLootGenerator(world)
            .player(somePlayer)
            .generate("minecraft:entities/cow");

.. zenscript:function:: LootGenerator damageSource(IDamageSource damageSource)

    Configures the killing damage source of the loot generator's context.

    :returns: the same loot generator, to allow method chaining

    .. code-block:: java

        import loottweaker.LootTweaker;
        import crafttweaker.damage.IDamageSource;

        LootTweaker.createLootGenerator(world)
            .damageSource(IDamageSource.MAGIC())
            .generate("minecraft:entities/cow");

.. zenscript:function:: IItemStack[] generate(String tableId)

    Generates loot with the previously configured context. The configured loot context is retained after calling.

    :parameters:

    * tableId - the id of the loot table to generate loot from

    :errors: if no loot table exists with the specified name.
    :returns: an array of item stacks generated from the loot table with the loot generator's configured context.


.. zenscript:function:: generateInto(String tableId, IEntity iEntity, @Optional String face, @Optional String overflow)

    Convenience method for generating loot into an inventory of a entity. The configured loot context is retained after calling.

    :parameters:

    * tableId - the id of the loot table to generate loot from
    * iEntity - the entity 
    * face - (Optional) Which "side" of the entity to access. Some entities provide access to different entities from different sides. If you're not sure, use ``"NONE"``. Valid values are ``"NONE"`` (default), ``"TOP"``, ``"BOTTOM"``, ``"NORTH"``, ``"EAST"``, ``"SOUTH"``, or ``"WEST"``.
    * overflow - (Optional) Determines what is done with loot that doesn't fit in the inventory. Valid values are ``"VOID"`` (default) to destroy excess loot, or ``"DROP"`` to drop excess loot at the entity's position.

    :errors: 
    
    * if the entity provides no inventory for the specified ``face``
    * if no loot table exists with the specified name.

.. zenscript:function:: generateInto(String tableId, IBlockPos inventoryPos, @Optional String face, @Optional String overflow)

    Convenience method for generating loot into an inventory of a block. The configured loot context is retained after calling.

    :parameters:
    
    * tableId - the id of the loot table to generate loot from
    * inventoryPos - the position of the block
    * face - (Optional) Which "side" of the block to access. Some blocks provide access to different entities from different sides. If you're not sure, use ``"NONE"``. Valid values are ``"NONE"`` (default), ``"TOP"``, ``"BOTTOM"``, ``"NORTH"``, ``"EAST"``, ``"SOUTH"``, or ``"WEST"``.
    * overflow - (Optional) Determines what is done with loot that doesn't fit in the inventory. Valid values are ``"VOID"`` (default) to destroy excess loot, or ``"DROP"`` to drop excess loot above ``inventoryPos``.

    :errors:

    * if there is no tile entity at ``inventoryPos``
    * if the tile entity provides no inventory for the specified ``face``
    * if no loot table exists with the specified name.

.. code-block:: java

    // A simple example focusing on the most important code
    // world is an IWorld val/var defined and set elsewhere
    if (!world.remote)
    {
        val cowItems = LootTweaker.createLootGenerator(world)
            .generate("minecraft:entities/cow");
        for item in cowItems {
            print(item);
        }
    }

.. code-block:: java

    import loottweaker.LootTweaker;
    import crafttweaker.event.EntityLivingJumpEvent;
    import crafttweaker.player.IPlayer;
    import crafttweaker.damage.IDamageSource;

    events.onEntityLivingJump(function(event as EntityLivingJumpEvent) {
    	val world = event.entity.world;
    	if (world.remote || !(event.entity instanceof IPlayer))
    	{
            return;
    	}
    	val player as IPlayer = event.entity;
    	val lootGenerator = LootTweaker.createLootGenerator(world)
            .luck(42.0)
            .lootedEntity(event.entity)
            .player(player)
            .damageSource(IDamageSource.MAGIC());
    	for item in lootGenerator.generate("minecraft:entities/cow") {
            player.dropItem(item);
    	}
    });
