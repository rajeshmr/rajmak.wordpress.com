namespace py models

struct Product{
    1: string title,
    2: double price
}

service ParserService{
    void ping(),
    Product parse(1: string body)
}