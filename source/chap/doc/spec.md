# recommonmark对markdown的支持特性


|  1  |  2  |  3  |
| --- | --- | --- |
| 1   | 1   | 1   |
| 1   | 2   | 1   |



```eval_rst

.. graphviz::

   digraph foo {
      "bar" -> "baz";
   }

```

```eval_rst

.. uml::

   Alice -> Bob: Hi!
   Alice <- Bob: How are you?

```

```eval_rst
.. autoclass:: recommonmark.transform.AutoStructify
    :show-inheritance:
```

``` important:: Its a note! in markdown!
```




``` sidebar:: Line numbers and highlights

     emphasis-lines:
       highlights the lines.
     linenos:
       shows the line numbers as well.
     caption:
       shown at the top of the code block.
     name:
       may be referenced with `:ref:` later.
```

``` code-block:: c
     :linenos:
     :emphasize-lines: 3,5
     :caption: An example code-block with everything turned on.
     :name: Full code-block example

     # Comment line
     import System
     System.run_emphasis_line
     # Long lines in code blocks create a auto horizontal scrollbar
     System.exit!
```