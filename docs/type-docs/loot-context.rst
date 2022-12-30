LootContext
===========
.. zenscript:type:: loottweaker.LootContext

Context object for loot generation

Methods
----------

See :doc:`here <method-documentation-format>` for an explanation of the method documentation format used on this page.

.. zenscript:function:: IEntity lootedEntity()
    :external-type: IEntity https://docs.blamejared.com/1.12/en/Vanilla/Entities/IEntity/

    :returns: the entity generating loot, may be null_.

.. zenscript:function:: IPlayer killerPlayer()
    :external-type: IPlayer https://docs.blamejared.com/1.12/en/Vanilla/Players/IPlayer/

    :returns: the player who triggered loot generation, may be null_.

.. zenscript:function:: IEntity killer()
    :external-type: IEntity https://docs.blamejared.com/1.12/en/Vanilla/Entities/IEntity/

    :returns: the entity that triggered loot generation, may be null_.

.. zenscript:function:: float luck()

    :returns: the luck_ level of this loot generation

.. zenscript:function:: IWorld world()
    :external-type: IWorld https://docs.blamejared.com/1.12/en/Vanilla/World/IWorld/

    :returns: the world loot is being generated in

.. zenscript:function:: int lootingModifier()

    :returns: the Looting enchantment level of this loot generation

.. _luck: https://minecraft.fandom.com/wiki/Luck
.. _null: https://docs.blamejared.com/1.12/en/Vanilla/Global_Functions/#isnull