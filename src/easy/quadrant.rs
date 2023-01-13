fn main() {
    let mut line1 = String::new();
    std::io::stdin().read_line(&mut line1).unwrap();
    let x: i32 = line1.trim().parse().unwrap();

    let mut line2 = String::new();
    std::io::stdin().read_line(&mut line2).unwrap();
    let y: i32 = line2.trim().parse().unwrap();

    if x > 0 {
        if y > 0 {
            println!("1");
        } else {
            println!("4");
        }
    } else {
        if y > 0 {
            println!("2");
        } else {
            println!("3");
        }
    }
}
