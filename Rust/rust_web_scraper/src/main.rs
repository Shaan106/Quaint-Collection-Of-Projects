// cargo add scraper reqwest --features "reqwest/blocking"
// for web scraping

//cargo add csv
//for exporting data

//data struct to store product info
struct Product {
    url: Option<String>,
    image: Option<String>,
    name: Option<String>,
    price: Option<String>,
}

fn main() {
    println!("Hello, world!");

    // going to a website and getting its html
    let response = reqwest::blocking::get("https://www.scrapingcourse.com/ecommerce/");

    //unwrap html
    let html_content = response.unwrap().text().unwrap();
    //print the html (for testing)
    println!("{html_content}"); // works :)


    // parse html, returns an HTML tree object
    let document = scraper::Html::parse_document(&html_content);


    //li.product is the unique identifier for the product list
    let html_product_selector = scraper::Selector::parse("li.product").unwrap();
    let html_products = document.select(&html_product_selector);

    //mutable (dynamic) array to store products
    // of type vector of Products
    let mut products: Vec<Product> = Vec::new();

    //loop over each product
    for html_product in html_products {

        let url = html_product
            .select(&scraper::Selector::parse("a").unwrap())
            .next()
            .and_then(|a| a.value().attr("href"))
            .map(str::to_owned);

        let image = html_product
            .select(&scraper::Selector::parse("img").unwrap())
            .next()
            .and_then(|img| img.value().attr("src"))

            .map(str::to_owned);
        let name = html_product
            .select(&scraper::Selector::parse("h2").unwrap())
            .next()
            .map(|h2| h2.text().collect::<String>());

        let price = html_product
            .select(&scraper::Selector::parse(".price").unwrap())
            .next()
            .map(|price| price.text().collect::<String>());


        //adding to data struct
        let product = Product {
            url,
            image,
            name,
            price,
        };

        //pushing to products array
        products.push(product);
    }

    // exporting to csv
    // create the CSV output file
    let path = std::path::Path::new("products.csv");
    let mut writer = csv::Writer::from_path(path).unwrap();

    // append the header to the CSV
    writer
        .write_record(&["url", "image", "name", "price"])
        .unwrap();
    // populate the output file
    for product in products {
        let url = product.url.unwrap();
        let image = product.image.unwrap();
        let name = product.name.unwrap();
        let price = product.price.unwrap();
        writer.write_record(&[url, image, name, price]).unwrap();
    }

    // free up the resources
    writer.flush().unwrap();


}
