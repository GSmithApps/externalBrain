# External Brain

## Mental Model

Think of this like **Obsidian**, or a folder full
of markdown files. The only differences are:

- Instead of every file
  having a unique file name, it has a unique
  set of tags. For example, instead of
  `butterscotch cookies.md`, you would have
  `{butterscotch, cookies}`.
- Instead of a folder full of files, it's
  a python dictionary full of tag sets mapped
  to strings, like this:
  ```python
  {
    {'cookies', 'oatmeal'}: 'very tasty',
    {'cookies', 'butterscotch'}: 'very very tasty'
  }
  ```
- In obsidian, you have an open file, and in
  this, you have an active location/dictionary
  element. 

You can also think of it like **working at a terminal**
and navigating through a folder structure of text
files.  The differences are:

- Instead of having a current working directory,
  you have a current working set of tags. For example,
  instead of `c:\users\...`, you have `{'cookies', 'oatmeal'}`.
- Instead of navigating the folder hierarchy by going
  in and out of folders with `cd ..`, you add
  and remove tags from
  your working tag set. For example, if you were
  at `{'cookies', 'oatmeal'}`, and then removed
  `'oatmeal'` by running `go_back('oatmeal')`,
  you'd be at `{'cookies'}`.

These changes are small, but they're awesome.
What they allow you to do is do relative nodes.
For example, if you were in `{'cookies'}`, and
you wanted to reference the note about butterscotch
cookies, all you'd have to do is a relative tag
reference, instead of writing out the full tag
set. Like this:

```python
{
  {'cookies'}:'I like ^^ butterscotch ^^ ones'
  {'cookies', 'butterscotch'}: 'I like butterscotch cookies'
}
```



## todo

- figure out how to do relative tags (or tags in general) in docs
- fuzzy search
- print tdon
  - especially with a tag filter criteria
- simpler method calls with args and kwargs

## UI

`difference_tf_with_tsot`

`union_tf_with_tsot`

`_return_tf_as_a_set`

## Tags inside the documents

you can put a relative tag inside a document with
the following `+{},{}-`

## Glossary

| abbreviation | word                 |
| ------------ | -------------------- |
| tsot         | the set of tags      |
| tdon         | the dict of nodes    |
| tcp          | the current position |
| tf           | the following        |

