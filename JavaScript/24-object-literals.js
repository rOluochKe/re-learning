// Objects are a way to store key-value pairs.
// They allow us to group together stat and behavior that's highly related.
// The benefit is we can make our code cohesive and organized.

// Encapsulation involves grouping together data and the methods that
// manipulate that data into a single unit.
// While hiding or abstracting away the internal details from outside interference or misuse.

const dog = {
  name: "Max",
  breed: "Dachshund",
  age: 5,
  weightInPounds: 12,
  eat: function () {
    console.log("Chomp!");
  },
  bark() {
    console.log("Woof!");
  },
};

// In programming languages such as C or C++,
// when you create an object you have to explicitly allocate and deallocate memory.
// But in programming languages such as JavaScript, C#, Java, or Python
// the languages have garbage collection to manage memory for us.
