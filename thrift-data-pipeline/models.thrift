namespace py models

struct Product{
    1: string title,
    2: double price
    3: bool in_stock
}

struct HTML{
    1: string url,
    2: string html
}

service ParserService{
    void ping(),
    Product parse(1: HTML html)
}