// Define a struct for a Person
struct Person {
    name: String,
    age: u32,
}

// Define an enum for different commands
enum Command {
    SayHello,
    SayGoodbye,
    CheckAge,
}

// Function to process a command for a person
fn process_command(person: &Person, command: Command) {
    match command {
        Command::SayHello => {
            println!("Hello, {}!", person.name);
        }
        Command::SayGoodbye => {
            println!("Goodbye, {}!", person.name);
        }
        Command::CheckAge => {
            if person.age >= 18 {
                println!("{} is an adult.", person.name);
            } else {
                println!("{} is a minor.", person.name);
            }
        }
    }
}

fn main() {
    // Create a new person
    let person = Person {
        name: String::from("Alice"),
        age: 25,
    };

    // Create a list of commands
    let commands = vec![
        Command::SayHello,
        Command::CheckAge,
        Command::SayGoodbye,
    ];

    // Process each command
    for command in commands {
        process_command(&person, command);
    }
}
