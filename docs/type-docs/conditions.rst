Conditions
==========
.. zenscript:type:: loottweaker.Conditions

JSON can be verbose and difficult to write. This type can help.
It provides methods for creating simple loot conditions, but if you wish to use complex loot conditions you still have to write them in JSON.
``minecraft:entity_properties`` and ``minecraft:entity_scores`` do not have helper methods as they are too complex.

All methods on this page, except ``parse()`` create a vanilla loot condition, so their parameters are equivalent to the parameters of the equivalent loot condition.
All vanilla loot conditions are listed and documented `here <https://minecraft.gamepedia.com/Loot_table?oldid=1192000#Conditions>`_.

The corresponding type for loot functions is :doc:`functions`.

Methods
-------

See :doc:`here <method-documentation-format>` for an explanation of the method documentation format used on this page.


.. zenscript:function:: static LootCondition randomChance(float chance)

    :equivalent to: ``minecraft:random_chance``

    .. code-block:: java

        import loottweaker.Conditions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0, [], // Arbitrary values for example purposes
            [
                Conditions.randomChance(0.5) // 50% chance
            ]
        );

.. zenscript:function:: static LootCondition randomChanceWithLooting(float chance, float lootingMult)

    :equivalent to: ``minecraft:random_chance_with_looting``

    .. code-block:: java

        import loottweaker.Conditions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0, [], // Arbitrary values for example purposes
            [
                // 50% + looting level x 1% chance
                Conditions.randomChanceWithLooting(0.5, 0.01)
            ]
        );

.. zenscript:function:: static LootCondition killedByPlayer()

    :equivalent to: ``minecraft:killed_by_player``

    .. code-block:: java

        import loottweaker.Conditions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0, [], // Arbitrary values for example purposes
            [
                Conditions.killedByPlayer()
            ]
        );

.. zenscript:function:: static LootCondition killedByNonPlayer()

    :equivalent to: ``minecraft:killed_by_player`` with the ``inverse`` tag set to true

    .. code-block:: java

        import loottweaker.Conditions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0, [], // Arbitrary values for example purposes
            [
                Conditions.killedByNonPlayer()
            ]
        );

.. zenscript:function:: static LootCondition parse(DataMap json)

    .. deprecated:: 0.3.0
       ``LootPool.addItemEntry``, ``LootPool.addLootTableEntry``, and ``LootPool.addEmptyEntry`` are capable of automatically parsing Maps into LootConditions.

    Parses a `DataMap <https://docs.blamejared.com/1.12/en/Vanilla/Data/DataMap/>`_ into a ``LootCondition``.

    :parameters:
        * json - an instance of ``DataMap`` representing a LootCondition in JSON form. It is recommended that the keys are enclosed in quotes to avoid conflicts between JSON key names and ZenScript keywords.
    :returns: ``json`` as a LootCondition
    :errors: if ``json`` does not parse successfully.

.. zenscript:function:: static LootCondition zenscript(loottweaker.CustomLootCondition zenFunction)

    Adapts ``zenFunction`` into a ``LootCondition``.

    :parameters:
        * zenFunction - a `ZenScript function <https://docs.blamejared.com/1.12/en/AdvancedFunctions/Custom_Functions>`_
          with parameters ``(IRandom, LootContext)`` and return type ``boolean``.
    :returns: a loot condition which passes if ``zenFunction`` returns true.
    :see:
        * `IRandom <https://docs.blamejared.com/1.12/en/Vanilla/Utils/IRandom/>`_
        * :doc:`LootContext <loot-context>`

    .. code-block:: java

        import crafttweaker.util.IRandom;
        import loottweaker.LootContext;
        import loottweaker.Conditions;

        // somePool is a LootPool created elsewhere
        somePool.addItemEntry(
            <minecraft:potato>, 1, 0, [], // Arbitrary values for example purposes
            [
                Conditions.zenscript(function(rng as IRandom, context as LootContext) as boolean
                {
                    return context.world().isRaining();
                })
            ]
        );

.. zenscript:type:: loottweaker.CustomLootCondition

    A `ZenScript function <https://docs.blamejared.com/1.12/en/AdvancedFunctions/Custom_Functions>`_
    with parameters ``(IRandom, LootContext)`` and return type ``boolean``