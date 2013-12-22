# Converting ``.tex`` to ``.rst``

To convert a TeX or LaTeX source into a restructured test file (``rst``) I use a combination of the tool ``pandoc``, some regular expression magic in my text editor, and some hand editing.

## Using pandoc

1. Make sure ``pandoc`` is installed. On OSX you can do ``brew install pandoc``. On Ubuntu you can do ``sudo apt-get install pandoc``. To verify that it is properly installed open up a new terminal window or tab and enter ``which pandoc``. If something ending in ``/pandoc`` appears, you are good to go.
1. Prepare the ``.tex`` source. Really this is just a matter of extracting the portion of the source file that you would like to translate and moving it to its own file in the directory where you want the ``.rst`` file to end up.
1. ``cd`` to the directory where you put your new ``.tex`` file and run pandoc. The main command syntax is ``pandoc -s source_file_name.tex -o output_file_name.rst``. The ``-s`` flag tells pandoc that the next thing you enter the source file name and the ``-o`` flag allows you to specify the output file name. (*Note* if you didn't give the new source file a ``.tex`` extension, pandoc will probably not work properly).

After those steps, most of your work should be done for you.

## Cleaning up the Translated Document

The output of pandoc is pretty good, but definitely not perfect. Here is a list of things that it **does not** do very well (I will list them here and then show shortcuts for how to fix them after the list):

* Handle equation labels.

### Fixing Equation Labels and References

#### Equation Labels

I have to do quite a bit of clean up here. Let's work with an example. Suppose you had the following LaTeX source:

```latex
\begin{equation} \label{eq:HHObj}
  \max \sum_{t = 0}^{\infty} \beta^t u \left( c_t \right)
\end{equation}
```

The correct corresponding restructured text should be:

```rst
.. math::
    \max \sum_{t = 0}^{\infty} \beta^t u \left( c_t \right)
    :label: HHObj
```

However, pandoc gives this:

```rst
.. math::

   \label{eq:HHObj}
     \max \sum_{t = 0}^{\infty} \beta^t u \left( c_t \right)
```

The first thing we need to do is change ``\label{eq:HHObj}`` to ``:label: HHObj``. To do this I use the following regular expression to find and replace. I'll give instructions for how to do this in Sublime Text. I give the keyboard shortcuts for Ubuntu and then the ones for OSX are in parenthesis:

1. Open the find and replace dialog: ``ctrl+h`` (``super+alt+f``)
1. Make sure the box with a ``*`` is not grayed out. It is the one on the top left of this new box. This enables regular expression searching
1. Enter ``\\label\{(.+?)\}`` into the "Find What" box. I'll break down what each piece does:
    * ``\\label`` searches for the ``\label`` LaTeX command. We need two ``\``'s  because `\\`` is a special symbol in regular expressions (regex) so we need to "escape" it (tell the regular expression parser to treat it as a single ``\`` character)
    * ``\{``  searches for the opening curly brace. ``{`` is also a special regex symbol, so we need to escape it also
    * ``(.+?)`` This uses 4 special regex things. The ``.`` matches anything except a new line character. The ``+`` says we want 1 or more of what preceeded it, so in this case we want 1 or more of any character on the current line. The ``?`` says that the "more" from the ``+`` should be "non-greedy" -- which means it should match as few characters as possible (if we didn't do this and there happened to be another ``}`` on the same line, it would match everything up to that ``}``. Putting the ``?`` here ensures we don't leave the ``\label{}`` command) . Finally, this is enclosed in ``()`` because we want to "capture" what is inside the parenthesis -- in this case the actual name of our label.
    * ``\}`` This just escapes the closing curly brace from the ``\label{}`` command.
1. Enter ``:label: \1`` in the "Replace with" box. This is another regular expression. Everything is very normal and exactly what you would think up to the ``\1``. This is special syntax for using the first (hence the ``1``) item we captured in our find regex (remember we "capture" things using ``()``). We captured the actual label name so it goes here.
1. Press the "Replace All" button or use the keyboard shortcut ``ctrl+alt+enter`` (``ctrl+alt+enter``). This will scan the entire document and convert every instance of ``\label{name}`` to ``:label: name``.

Now that we have the correct rst command, we need to reorganize things. To continue with our example we should have the following:

```rst
.. math::

   :label: eq:HHObj
     \max \sum_{t = 0}^{\infty} \beta^t u \left( c_t \right)
```

We need do three things: (1) move actual body of the equation indented one time just under the ``.. math:`` directive, move the ``:label:`` just below that, and (3) make sure each of those lines is indented one (and only one) time under the ``.. math:`` directive. I will explain how I do each step using sublime keyboard shortcuts:

(1) Put the cursor on the line with the equation and press ``shift+ctrl+up`` (``super+ctrl+up``) to have it swap places with the ``:label:``. I then press it one more time to put this just below the directive. It should now look like this:

```rst
.. math::
     \max \sum_{t = 0}^{\infty} \beta^t u \left( c_t \right)

   :label: eq:HHObj
```

(2) Do the same trick to get the label just beneath the equation content. It should now look like this:

```rst
.. math::
     \max \sum_{t = 0}^{\infty} \beta^t u \left( c_t \right)
   :label: eq:HHObj
```

(3) I then press ``shift+up`` (``shift+up``) to select a portion of the line with the ``:label:`` and a part of the equation's line. Then use ``ctrl+[`` (``super+[``) however many times is necessary for both of those lines to have now whitespace in front of them. Then hit ``ctrl+]`` (``super+]``) one time to indent them once under the directive. The finished product should look like this:

```rst
.. math::
    \max \sum_{t = 0}^{\infty} \beta^t u \left( c_t \right)
    :label: eq:HHObj
```

#### Equation References

For some reason, pandoc completely ignores calls to ``\eqref{}`` and doesn't properly handle ``\ref{}`` for equations. However, this is pretty simple to fix. Consider the following LaTeX source:

```tex
The household's problem is to maximize \ref{eq:HHObj} subject to \eqref{eq:HHBC},
where $\beta \in (0, 1)$ is a discount factor.
```

Pandoc would give rst that looks like

```rst
The household’s problem is to maximize [eq:HHObj] subject to ,
where :math:`\beta \in (0, 1)` is a discount factor.
```

where the correct rst is

```rst
The household's problem is to maximize :eq:`eq:HHObj` subject to :eq:`eq:HHBC`,
where :math:`\beta \in (0, 1)` is a discount factor.
```

Notice that it treated the call ``\ref{eq:HHObj}`` as a normal cross reference (like the ones we use to reference another section or subsection) and completely ignored the use of ``\eqref``. The fastest way I have found to fix this is to just copy and paste the original LaTeX source and then use a regular expression to convert it to the correct rst command.

So I would copy and paste the part of the code that calls ``ref`` and ``eqref`` so that my rst looks like:

```rst
The household’s problem is to maximize \ref{eq:HHObj} subject to \eqref{eq:HHBC},
where :math:`\beta \in (0, 1)` is a discount factor.
```

I then use the following regular expression in the "Find What" box: ``\\(eq)?ref\{(.+?)\}``. I'll break it down piece by piece again:

* ``\\``: Again we escape the ``\`` so the regex parser treats it like a real backslash.
* ``(eq)?ref``: We are using the capture syntax on the characters ``eq``, but not so we can keep track of it for later. In this case the ``?`` after the closing parenthesis says we would like to find 0 or 1 of the group proceeding the ``?``, which in this case needed to be two characters, not just one. Because we needed to match cases of ``ref`` and ``eqref`` we need to match when we find 0 or 1 of the two letter sequence ``eq`` followed by the sequence ``ref``.
* ``\{(.+?)\}`` This is the same sequence we met above. It escapes the opening ``{`` [``\{``], does a non-greedy capturing match on 1 or more of anything [``(.+?)``], and escapes the closing ``}`` [``\}``]

I then enter the following regular expression into the "Replace With" box: ``:eq:`\2` `` This is similar to the replace with box from above, but we need to add the backtick characters and use capture number 2 from the find box because we don't want to use the condition match of the sequence ``eq`` we would have gotten from ``(eq)?``. We then use Replace All ``ctrl+alt+enter`` (``ctrl+alt+enter``) and get the correct rst:

```rst
The household’s problem is to maximize :eq:`eq:HHObj` subject to :eq:`eq:HHBC`,
where :math:`\beta \in (0, 1)` is a discount factor.
```

### Many Short Lines -> Few Long Lines

This is more personal preference, but pandoc will write out lines that are no longer than 80 characters. This means longer paragraphs are broken into many lines of rst source, even if the LaTeX source had the whole paragraph on a single line. This is a pretty quick fix for sublime. What I do is open the find dialog using ``ctrl+f`` (``super+f``) -- the find and replace dialog we have been using by ``ctrl+h`` (``super+alt+f``) would work too -- and enter the following regex into the Find box: ``.+\n^[\w:]``. I'll break it down again:

* ``.+``: find one or more of anything... Not very useful
* ``\n``: find a new-line character
* ``^``:anchors the search to the beginning of a line. This is important because it will only allow us to match if the expression following the ``^`` is the very first character on a line. This will ensure we don't mess up any indented code in some kind of directive.
* ``[\w:]``: The ``\w`` says that we should match any character that is commonly used in words (letters, numbers, and the underscore) **or** the ``:`` character.

The net effect of this regex is to match all sets of more than one line where the second line begins with a word or a colon. The colon is important because it will allow us to match even if we are in the middle of an inline directive like ``:math:``. This is probably not a bullet proof way to find all paragraphs that were split across lines, but I haven't run into any errors using it.

After entering the regex I hit find all ``alt+enter`` (``alt+enter``), which will insert an active cursor everywhere where the regular expression matched. I then move to the beginning of each line using ``home`` (``super+left``) and then hit backspace once followed by the space bar. This will take the paragraph that was split across many lines and put them on a single line.

### Citations

Sphinx (and therefore rst) does not properly handle citations. There are a few things we need to do to get this tor work properly. Consider the LaTeX source

```tex
This is the approach taken in \citet{GreatPaper:2016}
```

pandoc would convert this to

```rst
This is the approach taken in
```

There is a sphinx extension that allows you to use the a LaTeX ``.bib`` file to handle citations. You will need to install this into your python distribution using ``conda install sphinxcontrib-bibtex`` (or if you aren't using anaconda ``pip install sphinxcontrib-bibtex``). This will download and install the bibtex sphinx extension for you. **NOTE**: you only need to do this once. After this is installed you can then use ``:cite:`ref` ``, where ``ref`` is what would go into a ``\cite{}`` command in LaTeX.

To fix the issue with the missing citation I would simply copy and paste the LaTeX source that calls a member of the ``\cite`` family and call the following regex find and replace. The find half is ``\\cite[tp]?\{(.+?)\}?`` and the replace half is ``:cite:`\1` ``. The find regex searches for ``\cite``, ``\citep``, or ``\citet``, then captures the actual reference to be inserted by our replace regex. If you use other ``cite`` commands in LaTeX you can add them to the find regex.

To actually include the bibliography on the page then scroll to the bottom of the .rst file and paste the following:

```rst
.. rubric:: Bibliography

.. bibliography:: file_name.bib
  :enumtype: upperroman
```

where ``file_name.bib`` is the name of the ``.bib`` file that is in the same directory as the ``.rst`` file calling it. This will insert a bold heading called ``Bibliography`` and print out the bib entries that were cited in the body of the rst file.

### Section labels

Pandoc doesn't use the Sphinx system for referencing sections. This is somewhat tedious to correct, I have mostly had to do it purely by hand. Luckily, the references to different sections of a book or paper are not extremely common, so it isn't too bad to fix manually. Consider the LaTeX source:

```tex
\section{New Section} \label{sec:new_section}

This is my new section

\section{Other Section} \label{sec:other_section}

This is another section. It comes after \ref{sec:new_section}.
```

Pandoc translates this to:

```rst
New Section
===========

[sec:new:sub:`s`\ ection]

This is my new section

Other Section
=============

[sec:other:sub:`s`\ ection]

This is another section. It comes after [sec:new:sub:`s`\ ection].
```

To make this work properly we need the following rst output:

```rst
.. _sec:new_section:

New Section
===========

This is my new section

.. _sec:other_section:

Other Section
=============

This is another section. It comes after :ref:`sec:new_section`.
```

I have just had to correct these by hand. Notice two important things. First, when defining the section label we need to start the line with ``.. _name:``. The underscore before the name and the colon after the name are important. Second, no other text can appear in lines between ``.. _name:`` and the section heading.

### Figures

TODO: write this up better.

We have to do most of the work by hand with figures. If the pages to be generated are in html format, it is optimal to use figures stored in ``png`` format.

Consider the following LaTeX source:

```tex
\begin{figure}
\begin{center}
\includegraphics[width=0.75\textwidth]{ES_plot_1.eps}
\end{center}
\caption{\small{Ramsey plan and Ramsey outcome.  From upper left to right, first panel: $Q_t$; second panel, $\tau_t$,
third panel $u_t = Q_{t+1} - Q_t$.}}%
\label{fig:ES_plot_1}%
\end{figure}
```

To get something similar we would use the following rst:

```rst
.. _fig:ES_plot_1:

.. figure:: images/ES_plot_1.png
  :align: center
  :figclass: align-center

  Figure 1

  Ramsey plan and Ramsey outcome. From upper left to right, first panel: :math:`Q_t`; second panel, :math:`\tau_t`, third panel :math:`u_t = Q_{t+1} - Q_t`.
```

### Other Common Issues

Here is a list of other things that pandoc does not do properly:

* Handle custom commands. If I had the line ``\newcommand{\bmat}{\begin{matrix}}`` in the LaTeX source and then used it using ``$\bmat$``, pandoc would simply insert ``:math:`\bmat` `` without ever defining what ``\bmat`` is. I just over come this using the regex tools we have been building up. In this case the Find What box would be ``\\bmat`` and the Replace With box would be ``\\begin\{matrix\}``
* If in the LaTeX source we end an environment like ``equation`` or ``align`` and then start the next line of text with a space, pandoc will put that space in the rst. This is bad because the end of an environment is usually associated with the ``.. math:`` directive and the space in front of the next paragraph would cause it to be included in the directive. There really isn't anything fancy to fix this, I just move the cursor onto the line and press ``ctrl+[`` (``super+[``) and dedent to remove leading whitespace.
