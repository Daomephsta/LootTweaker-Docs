:orphan:

.. |2^31| replace:: 2\ :sup:`31`\

Method Documentation Format
===========================

.. code-block:: java

    ReturnType methodName(Parameter1Type parameter1, Parameter2Type parameter2)
    // or
    static ReturnType methodName(Parameter1Type parameter1, Parameter2Type parameter2)

``ReturnType`` is the ZenScript type the method returns instances of.

``methodName`` is the name to use when calling the method. There may be multiple
methods with the same name, but different parameters.

After the method name is the parameter list, which is enclosed in (). There
may be any number of parameters, including none.
Each parameter has a type and a name. The parameter type is the type of value to
pass as that parameter when calling the method.

``static`` means the method must be called on the ZenScript type itself;
i.e. if the type is called ``Foo`` and the method is documented as
``static staticMethod()``, a call would be ``Foo.staticMethod()``.

Otherwise the method must be called on an instance of the ZenScript type; i.e.
if the type is called ``Foo`` and the method is documented as
``instanceMethod()``,  a call would be ``someFoo.instanceMethod``,
where ``someFoo`` is an instance of ``Foo``.
Ways to get an instance vary depending on the type.

Example 1
---------
:Type:

.. zenscript:type:: loottweaker.LootTweaker
   :noindex:

:Method:

.. zenscript:function:: static LootTable getTable(String tableName)
   :noindex:

:Call:

.. code-block:: java

   import loottweaker.LootTweaker;
   var someTable = LootTweaker.getTable("example:someTable");

Example 2
---------
:Type:

.. zenscript:type:: loottweaker.vanilla.loot.LootTable
   :noindex:

:Method:

.. zenscript:function:: LootPool getPool(String poolName)
   :noindex:

:Call:

.. code-block:: java

   // someTable is a var containing a LootTable, but it's not shown here
   var somePool = someTable.getPool("somePool");

Example 3
---------
:Type:

.. zenscript:type:: loottweaker.vanilla.loot.LootPool
   :noindex:

:Method:

.. zenscript:function:: addItemEntry(IItemStack stack, int weightIn, @Optional String name)
   :noindex:

:Call:

.. code-block:: java

   // somePool is a var containing a LootPool, but it's not shown here
   // No optional name argument, LootTweaker will generate one
   somePool.addItemEntry(<minecraft:apple>, 3);
   // Usage of optional name argument
   somePool.addItemEntry(<minecraft:apple>, 3, "apple");

Common Types
------------

.. zenscript:type:: boolean

    A value that is either `true` or `false`

.. zenscript:type:: int

    A whole number from -|2^31| to |2^31| - 1.

    :examples: * ``1``
               * ``-52``

.. zenscript:type:: float

    A floating point number from -|2^31| to |2^31| - 1.

    :examples: * ``3.141``
               * ``-2.05``

.. zenscript:type:: String

    A sequence of characters.

    :examples: * ``"Alice"``
               * ``"cat@example.com"``
               * ``"minecraft:chests/simple_dungeon"``
               * ``"123ABCxyz789"``

.. zenscript:type:: crafttweaker.data.DataMap

    A representation of key-value formats, such as JSON and NBT.
    `More info <https://docs.blamejared.com/1.12/en/Vanilla/Data/DataMap/#datamap>`__

    :examples: * ``{"function": "minecraft:set_count", "count": {"min": 1.0, "max": 3.0}}``
               * ``{"condition": "killed_by_player"}``

.. zenscript:type:: crafttweaker.item.IItemStack

    An item stack with metadata, size & NBT data.
    `More info <https://docs.blamejared.com/1.12/en/Vanilla/Items/IItemStack>`__

    :examples: * ``<minecraft:apple>``
               * ``<minecraft:potato> * 3``
               * ``<minecraft:dye:3>``

.. _Array Types:

Array Types
-----------
Arrays hold multiple objects of the same type. An array type name is the name of the type it holds followed by '[]', so the type name of an array of Strings would be 'String[]'.
Arrays are created by surrounding the elements in square brackets and separating them with commas, like so::

    ["Alice", "Bob", "Charlie"]
    [1, 2, 3, 4, 5]

More info `here <https://crafttweaker.readthedocs.io/en/latest/#AdvancedFunctions/Arrays_and_Loops/#arrays>`__.

Optional arguments
------------------
If an argument has @Optional before the type (e.g @Optional String name), it's optional. If you do not specify a value, LootTweaker will generate one.
For example, ``LootPool#addItemEntry(IItemStack stack, int weightIn, @Optional String name)`` can be called in 2 ways::

    pool.addItemEntry(<minecraft:apple>, 5, "not_an_orange");

or ::

    pool.addItemEntry(<minecraft:apple>, 5);

The second call will make LootTweaker pick an appropriate value for the ``name`` parameter.
