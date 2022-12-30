LootFunction
============
.. zenscript:type:: loottweaker.vanilla.loot.LootFunction

Represents a loot function. Either created using a method of the :doc:`functions` class,
or automatically converted from a :ref:`JSON format map <json-format-maps>`
by LootTweaker.

Methods
-------

.. zenscript:function:: LootFunction addConditions(LootCondition[] conditions)

    Adds conditions to this loot function

    :parameters:

    * conditions - an array of instances of :doc:`LootCondition <conditions>` to add.
      Maps are :ref:`automatically converted <autoconverted>`.

    :returns: the loot function this method was called on

    .. code-block:: java

      import loottweaker.vanilla.loot.Conditions;

      // someLootFunction is a LootFunction created elsewhere
      someLootFunction.addConditions([
        {"condition": "killed_by_player"},
        Conditions.randomChance(0.5)
      ]);
