
reStructuredText 语法
#######################

CHAPTERS 1 章
***************

节 
==============

小节
----------

小小节
^^^^^^^

段落
++++++

cd

表格
======

+-------+--------+-----------+
|  姓名 |   部门  |   工号   |
+=======+========+===========+
|haobo  |   zzdc |  H2410518 |
+-------+--------+-----------+




表格 table_formatter
----------------------

+
|实列| a |
+=
|示例| b|
+-


+--------+-----------+
| haobo  | haobo.gao |
+========+===========+
| yanfei | yanfie.li |
+--------+-----------+


简表格 table_formatter
------------------------


-a        ba
-b       sd



=
a . b
-
A  B C D
= = = =
ad ba ac cd 
==


===  ===  ===  ===
 a    .    b
---  ---  ---  ---
 A    B    C    D
===  ===  ===  ===
ad   ba   ac   cd
===  ===  ===  ===


代码片段
=========

.. code-block:: ruby
   :linenos:

   Some more Ruby code.


.. code-block:: c
   :linenos:

    void main(void)
    {
        printf("hello word");
    }



脚注
============

If [#note]_ is the first footnote reference, it will show up as
"[1]".  We can refer to it again as [#note]_ and again see
"[1]".  We can also refer to it as note_ (an ordinary internal
hyperlink reference).

.. [#note] This is the footnote labeled "note".


撒旦佛i文件恢复合并为佛七武海可萨佛全部
.. [1] Body elements go here.



section
========

subsection 
------------

subsubsection
^^^^^^^^^^^^^^

paragraph1
+++++++++++


paragraph
''''''''''





- This is the first bullet list item.  The blank line above the
  first list item is required; blank lines between list items
  (such as below this paragraph) are optional.

- This is the first paragraph in the second item in the list.

  This is the second paragraph in the second item in the list.
  The blank line above this paragraph is required.  The left edge
  of this paragraph lines up with the paragraph above, both
  indented relative to the bullet.

  - This is a sublist.  The bullet lines up with the left edge of
    the text blocks above.  A sublist is a new list so requires a
    blank line above and below.

- This is the third item of the main list.

This paragraph is not part of the list.


1. Item 1 initial text.

   a) Item 1a.
   b) Item 1b.

2. a) Item 2a.
   b) Item 2b.





term 1
    Definition 1.

term 2
    Definition 2, paragraph 1.

    Definition 2, paragraph 2.

term 3 : classifier
    Definition 3.

term 4 : classifier one : classifier two
    Definition 4.




:Date: 2001-08-16
:Version: 1
:Authors: - Me
          - Myself
          - I
:Indentation: Since the field marker may be quite long, the second
   and subsequent lines of the field body do not have to line up
   with the first line, but they must be indented relative to the
   field name marker, and they must line up with each other.
:Parameter i: integer



-a         Output all.
-b         Output both (this description is
           quite long).
-c arg     Output just arg.
--long     Output all day long.

-p         This option has two paragraphs in the description.
           This is the first.

           This is the second.  Blank lines may be omitted between
           options (as above) or left in (as here and below).

--very-long-option  A VMS-style option.  Note the adjustment for
                    the required two spaces.

--an-even-longer-option
           The description can also start on the next line.

-2, --two  This option has two variants.

-f FILE, --file=FILE  These two options are synonyms; both have
                      arguments.

/V         A VMS/DOS-style option.