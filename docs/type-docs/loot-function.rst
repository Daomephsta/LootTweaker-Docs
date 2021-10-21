LootFunction
============

:full name: ``loottweaker.vanilla.loot.LootFunction``

Condition and function formatting
---------------------------------
Conditions and functions should be supplied to methods as arrays of `DataMaps <https://docs.blamejared.com/1.12/en/Vanilla/Data/DataMap/>`_
or :doc:`conditions`/:doc:`functions`. Do not supply the conditions as part of a parent tag.
When using `DataMap`_ to supply conditions or functions,
it is recommended that you surround the keys with double quotes("), as otherwise any keys which are zenscript keywords(e.g function) will cause issues.

Recommended

.. code-block:: json

    [
       {
        "count":
        {
        "min": 0.0,
        "max": 2.0
        },
        "function": "minecraft:set_count"
       }
    ]

Not Recommended

.. code-block:: none

    [
       {
        count:
        {
        min: 0.0,
        max: 2.0
        },
        function: "minecraft:set_count"
       }
    ]

Methods
-------

LootFunction addConditionsJson(DataMap[] conditions)
++++++++++++++++++++++++++++++++++++++++++++++++++++

    Adds conditions to this loot function

    :parameters: 

    * conditions - an array of instances of `DataMap`_, each a LootCondition in JSON form. It is recommended that the keys are enclosed in quotes to avoid conflicts between JSON key names and ZenScript keywords.
  
    :errors: if any of the elements of ``conditions`` do not parse successfully.

    :returns: the loot function this method was called on

LootFunction addConditionsHelper(LootCondition[] conditions)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    Adds conditions to this loot function

    :parameters:

    * conditions - an array of instances of :doc:`LootCondition <conditions>`

    :returns: the loot function this method was called on

.. _DataMap: https://docs.blamejared.com/1.12/en/Vanilla/Data/DataMap/