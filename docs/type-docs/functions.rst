Functions
=========
.. zenscript:type:: loottweaker.vanilla.loot.Functions

JSON can be verbose and difficult to write. This type can help.
It provides methods for creating simple loot functions, but if you wish to use complex loot functions you still have to write them in JSON.
``minecraft:set_attributes`` does not have a helper method as it is too complex.

All methods on this page, except ``parse()`` create a vanilla loot function, so their parameters are equivalent to the parameters of the equivalent loot function.
All vanilla loot functions are listed and documented `here <https://minecraft.gamepedia.com/Loot_table#Functions>`_.

The corresponding type for loot conditions is :doc:`conditions`.

Methods
-------

See :doc:`here <method-documentation-format>` for an explanation of the method documentation format used on this page.

.. zenscript:function:: static LootFunction enchantRandomly(String[] enchantIDList)

    :equivalent to: ``minecraft:enchant_randomly``
    :errors: if any enchantment ID does not resolve to an enchantment

    .. code-block:: java

        import loottweaker.vanilla.loot.Functions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0,
            [
                Functions.enchantRandomly(["minecraft:looting"])
            ],
            [] // Arbitrary value for example purposes
        );

.. zenscript:function:: static LootFunction enchantWithLevels(int min, int max, boolean isTreasure)

    :equivalent to: ``minecraft:enchant_with_levels``

    .. code-block:: java

        import loottweaker.vanilla.loot.Functions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0,
            [
                // Enchant with a level from 5 to 10, allowing treasure-only enchantments
                Functions.enchantWithLevels(5, 10, true)
            ],
            [] // Arbitrary value for example purposes
        );

.. zenscript:function:: static LootFunction lootingEnchantBonus(int min, int max, int limit)

    :equivalent to: ``minecraft:looting_enchant``

    .. code-block:: java

        import loottweaker.vanilla.loot.Functions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0,
            [
                // 1 to 3 extra items per level of looting, maximum of 5 in total
                Functions.lootingEnchantBonus(1, 3, 5)
            ],
            [] // Arbitrary value for example purposes
        );

.. zenscript:function:: static LootFunction setCount(int min, int max)

    :equivalent to: ``minecraft:set_count``

    .. code-block:: java

        import loottweaker.vanilla.loot.Functions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0,
            [
                // Stack size of 1 to 3
                Functions.setCount(1, 3)
            ],
            [] // Arbitrary value for example purposes
        );

.. zenscript:function:: static LootFunction setDamage(float min, float max)

    :equivalent to: ``minecraft:set_damage``
    :errors: if ``max`` is greater than 1.0

    .. code-block:: java

        import loottweaker.vanilla.loot.Functions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0,
            [
                // 75% to 90% durability remaining (10% to 25% damage)
                Functions.setDamage(0.75, 0.90)
            ],
            [] // Arbitrary value for example purposes
        );

.. zenscript:function:: static LootFunction setMetadata(int min, int max)

    :equivalent to: ``minecraft:set_data``

    .. code-block:: java

        import loottweaker.vanilla.loot.Functions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0,
            [
                // Metadata of 1 to 3
                Functions.setMetadata(1, 3)
            ],
            [] // Arbitrary value for example purposes
        );

.. zenscript:function:: static LootFunction setNBT(DataMap nbtData)

    :equivalent to: ``minecraft:set_nbt``
    :errors: if ``nbtData`` is not a compound tag

    .. code-block:: java

        import loottweaker.vanilla.loot.Functions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0,
            [
                // Makes item unbreakable via NBT
                Functions.setNBT({"Unbreakable": true})
            ],
            [] // Arbitrary value for example purposes
        );

.. zenscript:function:: static LootFunction smelt()

    :equivalent to: ``minecraft:furnace_smelt``

    .. code-block:: java

        import loottweaker.vanilla.loot.Functions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0,
            [
                Functions.smelt()
            ],
            [] // Arbitrary value for example purposes
        );

.. zenscript:function:: static LootFunction parse(DataMap json)

    Deprecated. 0.3.0 introduced entry addition methods capable of automatically parsing Maps into LootConditions.
    Parses a `DataMap <https://docs.blamejared.com/1.12/en/Vanilla/Data/DataMap/>`_ into a ``LootFunction``.

    :parameters:
        * json - an instance of ``DataMap`` representing a LootCondition in JSON form. It is recommended that the keys are enclosed in quotes to avoid conflicts between JSON key names and ZenScript keywords.
    :returns: ``json`` as a LootFunction.
    :errors: if ``json`` does not parse successfully.

.. zenscript:function:: static LootFunction zenscript(loottweaker.CustomLootFunction zenFunction)

    Adapts ``zenFunction`` into a ``LootFunction``.

    :parameters:
        * zenFunction - a `ZenScript function <https://docs.blamejared.com/1.12/en/AdvancedFunctions/Custom_Functions>`
          with parameters ``(IItemStack, IRandom, LootContext)`` and return type ``IItemStack``.
    :returns: a loot condition which changes the generated item using ``zenFunction``.
    :see:
        * `IItemStack <https://docs.blamejared.com/1.12/en/Vanilla/Items/IItemStack/>`_
        * `IRandom <https://docs.blamejared.com/1.12/en/Vanilla/Utils/IRandom/>`_
        * :doc:`LootContext <loot-context>`

    .. code-block:: java

        import crafttweaker.item.IItemStack;
        import crafttweaker.util.IRandom;
        import loottweaker.LootContext;
        import loottweaker.vanilla.loot.Functions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0,
            [
                Functions.zenscript(function(input as IItemStack, rng as IRandom, context as LootContext) as IItemStack
                {
                    return input.withDisplayName("Super Potato");
                })
            ],
            [] // Arbitrary value for example purposes
        );

.. zenscript:type:: loottweaker.CustomLootFunction

    A `ZenScript function <https://docs.blamejared.com/1.12/en/AdvancedFunctions/Custom_Functions>`
    with parameters ``(IItemStack, IRandom, LootContext)`` and return type ``IItemStack``.