create table products (
    id  integer primary key autoincrement not null,
    title   text,
    price   real,
    out_of_stock    boolean,
    url text
    )
