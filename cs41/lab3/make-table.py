#!/usr/bin/env python3 -tt

def make_table(key_justify='left', value_justify='right', **kwargs):
    if not kwargs:
        return
    key_column_length = max([len(x) for x in kwargs])
    value_column_length = max([len(x) for x in kwargs.values()])
    table_length = key_column_length + value_column_length + 7
    alignment_symbols = {
        'left': '<', 
        'center': '^',
        'right' : '>'
    }
    print("="*table_length)
    for key, value in kwargs.items():
        print("| {:{key_align}{key_len}} | {:{val_align}{val_len}} |".format(
            key,
            value,
            key_align=alignment_symbols[key_justify],
            key_len=key_column_length,
            val_align=alignment_symbols[value_justify],
            val_len=value_column_length))
    print("=" * table_length)

make_table(
    first_name="Sam",
    last_name="Redmond",
    shirt_color="pink"
)

make_table(
    key_justify="right",
    value_justify="center",
    song="Style",
    artist_fullname="Taylor $wift",
    album="1989"
)